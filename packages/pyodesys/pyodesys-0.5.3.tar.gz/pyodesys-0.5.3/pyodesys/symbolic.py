# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from itertools import chain, repeat
import os

import numpy as np

from .core import OdeSys
from .util import (
    banded_jacobian, transform_exprs_dep,
    transform_exprs_indep, _ensure_4args
)


def _lambdify(backend=None):
    backend = os.environ.get('PYODESYS_SYM_BACKEND', 'sympy')
    if backend == 'sympy':
        import sympy as sp

        def lambdify(*args, **kwargs):
            if 'modules' not in kwargs:
                kwargs['modules'] = [{'ImmutableMatrix': np.array}, 'numpy']
            return sp.lambdify(*args, **kwargs)
        return lambdify
    elif backend == 'pysym':
        import pysym as ps
        return ps.Lambdify
    else:
        raise NotImplementedError('Unknown symbolic package: %s' %
                                  backend)


def _lambdify_unpack(backend=None):
    backend = os.environ.get('PYODESYS_SYM_BACKEND', 'sympy')
    if backend == 'sympy':
        return True
    elif backend == 'pysym':
        return False
    else:
        raise NotImplementedError('Unknown symbolic package: %s' %
                                  backend)


def _Matrix(backend=None):
    backend = os.environ.get('PYODESYS_SYM_BACKEND', 'sympy')
    if backend == 'sympy':
        import sympy as sp
        return sp.Matrix
    elif backend == 'pysym':
        import pysym as ps
        return ps.Matrix
    else:
        raise NotImplementedError('Unknown symbolic package: %s' %
                                  backend)


def _Symbol(backend=None):
    backend = os.environ.get('PYODESYS_SYM_BACKEND', 'sympy')
    if backend == 'sympy':
        import sympy as sp

        def Symbol(*args, **kwargs):
            if 'real' not in kwargs:
                kwargs['real'] = True
            return sp.Symbol(*args, **kwargs)
        return Symbol
    elif backend == 'pysym':
        import pysym as ps
        return ps.Symbol
    else:
        raise NotImplementedError('Unknown symbolic package: %s' %
                                  backend)


def _Dummy(backend=None):
    backend = os.environ.get('PYODESYS_SYM_BACKEND', 'sympy')
    if backend == 'sympy':
        import sympy as sp
        return sp.Dummy
    elif backend == 'pysym':
        import pysym as ps
        return ps.Dummy
    else:
        raise NotImplementedError('Unknown symbolic package: %s' %
                                  backend)


def _symarray(backend=None):
    backend = os.environ.get('PYODESYS_SYM_BACKEND', 'sympy')
    if backend == 'sympy':
        import sympy as sp

        def symarray(prefix, shape, Symbol=None, real=True):
            """ Creates an nd-array of symbols

            Parameters
            ----------
            prefix : str
            shape : tuple
            Symbol : callable
                (defualt :func:`Symbol`)
            """
            # see https://github.com/sympy/sympy/pull/9939
            # when released: return sp.symarray(key, n, real=True)
            arr = np.empty(shape, dtype=object)
            for index in np.ndindex(shape):
                arr[index] = (
                    Symbol or (lambda name: sp.Symbol(name, real=real))
                )('%s_%s' % (prefix, '_'.join(map(str, index))))
            return arr
        return symarray
    elif backend == 'pysym':
        import pysym as ps
        return ps.symarray
    else:
        raise NotImplementedError('Unknown symbolic package: %s' %
                                  backend)


class SymbolicSys(OdeSys):
    """ ODE System from symbolic expressions

    Creates a :class:`OdeSys` instance
    from symbolic expressions. Jacboian and second derivatives
    are derived when needed.

    Parameters
    ----------
    dep_exprs : iterable of (symbol, expression)-pairs
    indep : symbol
        Independent variable (default: None => autonomous system).
    params : iterable of symbols
        parameters
    jac : ImmutableMatrix or bool (default: True)
        if True:
            calculate jacobian from exprs
        if False:
            do not compute jacobian (use explicit steppers)
        if instance of ImmutableMatrix:
            user provided expressions for the jacobian
    roots : iterable of expressions
        Equations to look for root's for during integration
        (currently available through cvode).
    lambdify : callback
        default: :py:func:`sympy.lambdify`.
    lambdify_unpack : bool (default: True)
        Whether or not unpacking of args needed when calling lambdify callback.
    Matrix : class
        default: :py:class:`sympy.Matrix`.
    Symbol : class
        default: :py:class:`sympy.Symbol`.
    Dummy : class
        default: :py:class:`sympy.Dummy`.
    symarray : callback
        default: :py:class:`sympy.symarray`.
    \*\*kwargs:
        See :py:class:`OdeSys`

    Attributes
    ----------
    dep : iterable of symbols
        dependent variables
    indep : symbol
        independent variable
    params : iterable of symbols
        parameters

    Notes
    -----
    Works for a moderate number of unknowns, :py:func:`sympy.lambdify` has
    an upper limit on number of arguments.

    """

    def __init__(self, dep_exprs, indep=None, params=(), jac=True, dfdx=True,
                 roots=None, lambdify=None, lambdify_unpack=None, Matrix=None,
                 Symbol=None, Dummy=None, symarray=None, **kwargs):
        self.dep, self.exprs = zip(*dep_exprs)
        self.indep = indep
        self.params = params
        self._jac = jac
        self._dfdx = dfdx
        self.roots = roots
        self.lambdify = lambdify or _lambdify()
        self.lambdify_unpack = (_lambdify_unpack() if lambdify_unpack is None
                                else lambdify_unpack)
        self.Matrix = Matrix or _Matrix()
        self.Symbol = Symbol or _Symbol()
        self.Dummy = Dummy or _Dummy()
        self.symarray = symarray or _symarray()
        # we need self.band before super().__init__
        self.band = kwargs.get('band', None)
        if kwargs.get('names', None) is True:
            kwargs['names'] = [y.name for y in self.dep]
        super(SymbolicSys, self).__init__(
            self.get_f_ty_callback(),
            self.get_j_ty_callback(),
            self.get_dfdx_callback(),
            self.get_roots_callback(),
            nroots=None if roots is None else len(roots),
            **kwargs)

    @classmethod
    def from_callback(cls, cb, ny, nparams=0, backend=None, **kwargs):
        """ Create an instance from a callback.

        Parameters
        ----------
        cb : callbable
            Signature rhs(x, y[:], p[:]) -> f[:]
        ny : int
            length of y
        nparams : int (default: 0)
            length of p
        backend : module (optional)
            default: sympy
        \*\*kwargs :
            keyword arguments passed onto :class:`SymbolicSys`

        Returns
        -------
        An instance of :class:`SymbolicSys`.
        """
        if backend is None:
            import sympy as backend
        x = kwargs.get('Symbol', _Symbol())('x')
        y = kwargs.get('symarray', _symarray())('y', ny)
        p = kwargs.get('symarray', _symarray())('p', nparams)
        try:
            exprs = cb(x, y, p, backend)
        except TypeError:
            exprs = _ensure_4args(cb)(x, y, p, backend)
        return cls(zip(y, exprs), x, p, **kwargs)

    @classmethod
    def from_other(cls, ori, **kwargs):  # provisional
        new_kw = kwargs.copy()
        if ori.roots is not None:
            raise NotImplementedError('roots currently unsupported')
        if 'params' not in new_kw:
            new_kw['params'] = ori.params

        if len(ori.pre_processors) > 0:
            if 'pre_processors' not in new_kw:
                new_kw['pre_processors'] = []
            new_kw['pre_processors'] = ori.pre_processors + new_kw[
                'pre_processors']

        if len(ori.post_processors) > 0:
            if 'post_processors' not in new_kw:
                new_kw['post_processors'] = []
            new_kw['post_processors'] = ori.post_processors + new_kw[
                'post_processors']

        return cls(zip(ori.dep, ori.exprs), ori.indep, **new_kw)

    @property
    def ny(self):
        """ Number of dependent variables in the system. """
        return len(self.exprs)

    def _args(self, x=None, y=None, params=()):
        if x is None:
            x = self.indep
        if y is None:
            y = self.dep
        args = tuple(y)
        if self.indep is not None:
            args = (x,) + args
        return args + tuple(params)

    def get_jac(self):
        """ Derives the jacobian from ``self.exprs`` and ``self.dep``. """
        if self._jac is True:
            if self.band is None:
                f = self.Matrix(1, self.ny, lambda _, q: self.exprs[q])
                self._jac = f.jacobian(self.dep)
            else:
                # Banded
                self._jac = self.Matrix(banded_jacobian(
                    self.exprs, self.dep, *self.band))
        elif self._jac is False:
            return False

        return self._jac

    def get_dfdx(self):
        """ Calculates 2nd derivatives of ``self.exprs`` """
        if self._dfdx is True:
            if self.indep is None:
                self._dfdx = [0]*self.ny
            else:
                self._dfdx = [expr.diff(self.indep) for expr in self.exprs]
        elif self._dfdx is False:
            return False
        return self._dfdx

    def get_f_ty_callback(self):
        """ Generates a callback for evaluating ``self.exprs``. """
        cb = self.lambdify(list(chain(self._args(), self.params)), self.exprs)

        def f(x, y, params=()):
            if self.lambdify_unpack:
                return np.asarray(cb(*self._args(x, y, params)))
            else:
                return np.asarray(cb(self._args(x, y, params)))
        return f

    def get_j_ty_callback(self):
        """ Generates a callback for evaluating the jacobian. """
        j_exprs = self.get_jac()
        if j_exprs is False:
            return None
        cb = self.lambdify(list(chain(self._args(), self.params)), j_exprs)

        def j(x, y, params=()):
            if self.lambdify_unpack:
                return np.asarray(cb(*self._args(x, y, params)))
            else:
                return np.asarray(cb(self._args(x, y, params)))
        return j

    def get_dfdx_callback(self):
        """ Generate a callback for evaluating derivative of ``self.exprs`` """
        dfdx_exprs = self.get_dfdx()
        if dfdx_exprs is False:
            return None
        cb = self.lambdify(list(chain(self._args(), self.params)), dfdx_exprs)

        def dfdx(x, y, params=()):
            if self.lambdify_unpack:
                return np.asarray(cb(*self._args(x, y, params)))
            else:
                return np.asarray(cb(self._args(x, y, params)))
        return dfdx

    def get_roots_callback(self):
        """ Generate a callback for evaluating ``self.roots`` """
        if self.roots is None:
            return None
        cb = self.lambdify(list(chain(self._args(), self.params)), self.roots)

        def roots(x, y, params=()):
            if self.lambdify_unpack:
                return np.asarray(cb(*self._args(x, y, params)))
            else:
                return np.asarray(cb(self._args(x, y, params)))
        return roots

    # Not working yet:
    def _integrate_mpmath(self, xout, y0, params=()):
        """ Not working at the moment, need to fix
        (low priority - taylor series is a poor method)"""
        raise NotImplementedError
        xout, y0, self.internal_params = self.pre_process(xout, y0, params)
        from mpmath import odefun

        def rhs(x, y):
            rhs.ncall += 1
            return [
                e.subs(
                    ([(self.indep, x)] if self.indep is not None else []) +
                    list(zip(self.dep, y))
                ) for e in self.exprs
            ]
        rhs.ncall = 0

        cb = odefun(rhs, xout[0], y0)
        yout = []
        for x in xout:
            yout.append(cb(x))
        info = {'nrhs': rhs.ncall}
        return self.post_process(
            xout, yout, self.internal_params)[:2] + (info,)

    def _get_analytic_stiffness_cb(self):
        J = self.get_jac()
        eig_vals = list(J.eigenvals().keys())
        cb = self.lambdify(list(chain(self._args(), self.params)), eig_vals)

        def eigen_values(x, y, params):
            if self.lambdify_unpack:
                return np.asarray(cb(*self._args(x, y, params)))
            else:
                return np.asarray(cb(self._args(x, y, params)))
        return eigen_values

    def analytic_stiffness(self, xyp=None):
        """ Running stiffness ratio from last integration.

        Calculate sittness ratio, i.e. the ratio between the largest and
        smallest absolute eigenvalue of the (analytic) jacobian matrix.

        See :meth:`OdeSys.stiffness` for more info.
        """
        return self.stiffness(xyp, self._get_analytic_stiffness_cb())


class TransformedSys(SymbolicSys):
    """ SymbolicSys with abstracted variable transformations.

    Parameters
    ----------
    dep_exprs : iterable of pairs
        see :class:`SymbolicSys`
    indep : Symbol
        see :class:`SymbolicSys`
    dep_transf : iterable of (expression, expression) pairs
        pairs of (forward, backward) transformations for the dependents
        variables
    indep_transf : pair of expressions
        forward and backward transformation of the independent variable
    params :
        see :class:`SymbolicSys`
    exprs_process_cb : callbable
        signatrue f(exprs) -> exprs
        post processing of the expressions for the derivatives of the
        dependent variables after transformation have been applied.
    \*\*kwargs :
        keyword arguments passed onto :class:`SymbolicSys`
    """

    def __init__(self, dep_exprs, indep=None, dep_transf=None,
                 indep_transf=None, params=(), exprs_process_cb=None,
                 **kwargs):
        dep, exprs = zip(*dep_exprs)
        if dep_transf is not None:
            self.dep_fw, self.dep_bw = zip(*dep_transf)
            exprs = transform_exprs_dep(self.dep_fw, self.dep_bw,
                                        list(zip(dep, exprs)))

        else:
            self.dep_fw, self.dep_bw = None, None

        if indep_transf is not None:
            self.indep_fw, self.indep_bw = indep_transf
            exprs = transform_exprs_indep(self.indep_fw, self.indep_bw,
                                          list(zip(dep, exprs)), indep)
        else:
            self.indep_fw, self.indep_bw = None, None

        if exprs_process_cb is not None:
            exprs = exprs_process_cb(exprs)

        pre_processors = kwargs.pop('pre_processors', [])
        post_processors = kwargs.pop('post_processors', [])
        super(TransformedSys, self).__init__(
            zip(dep, exprs), indep, params,
            pre_processors=pre_processors + [self._forward_transform_xy],
            post_processors=[self._back_transform_out] + post_processors,
            **kwargs)
        # the pre- and post-processors need callbacks:
        args = self._args(indep, dep, params)
        self.f_dep = self.lambdify(args, self.dep_fw)
        self.b_dep = self.lambdify(args, self.dep_bw)
        if (self.indep_fw, self.indep_bw) != (None, None):
            self.f_indep = self.lambdify(args, self.indep_fw)
            self.b_indep = self.lambdify(args, self.indep_bw)
        else:
            self.f_indep = None
            self.b_indep = None

    @classmethod
    def from_callback(cls, cb, ny, nparams=0, dep_transf_cbs=None,
                      indep_transf_cbs=None, **kwargs):
        """
        Create an instance from a callback.

        Analogous to :func:`SymbolicSys.from_callback`.

        Parameters
        ----------
        cb : callable
            Signature rhs(x, y[:], p[:]) -> f[:]
        ny : int
            length of y
        nparams : int
            length of p
        dep_transf_cbs : iterable of pairs callables
            callables should have the signature f(yi) -> expression in yi
        indep_transf_cbs : pair of callbacks
            callables should have the signature f(x) -> expression in x
        \*\*kwargs :
            keyword arguments passed onto :class:`TransformedSys`
        """
        x = kwargs.get('Symbol', _Symbol())('x')
        y = kwargs.get('symarray', _symarray())('y', ny)
        p = kwargs.get('symarray', _symarray())('p', nparams)
        exprs = _ensure_4args(cb)(x, y, p)
        if dep_transf_cbs is not None:
            dep_transf = [(fw(yi), bw(yi)) for (fw, bw), yi
                          in zip(dep_transf_cbs, y)]
        else:
            dep_transf = None

        if indep_transf_cbs is not None:
            indep_transf = indep_transf_cbs[0](x), indep_transf_cbs[1](x)
        else:
            indep_transf = None

        return cls(list(zip(y, exprs)), x, dep_transf,
                   indep_transf, p, **kwargs)

    def _back_transform_out(self, xout, yout, params):
        args = self._args(xout, yout.T, params)
        if self.lambdify_unpack:
            return (xout if self.b_indep is None else self.b_indep(*args),
                    np.array(self.b_dep(*args)).T, params)
        else:
            return (xout if self.b_indep is None else self.b_indep(args),
                    np.array(self.b_dep(args)).T, params)

    def _forward_transform_xy(self, x, y, p):
        args = self._args(x, y, p)
        if self.lambdify_unpack:
            return (x if self.f_indep is None else self.f_indep(*args),
                    self.f_dep(*args), p)
        else:
            return (x if self.f_indep is None else self.f_indep(args),
                    self.f_dep(args), p)


def symmetricsys(dep_tr=None, indep_tr=None, **kwargs):
    """
    A factory function for creating symmetrically transformed systems.

    Parameters
    ----------
    dep_tr : pair of callables (default: None)
        Forward and backward transformation to be applied to the
        dependent variables
    indep_tr : pair of callables (default: None)
        Forward and backward transformation to be applied to the
        independent variable
    \*\*kwargs :
        default keyword arguments for the TransformedSys subclass

    Returns
    -------
    Subclass of TransformedSys

    Examples
    --------
    >>> import sympy
    >>> logexp = (sympy.log, sympy.exp)
    >>> LogLogSys = symmetricsys(
    ...     logexp, logexp, exprs_process_cb=lambda exprs: [
    ...         sympy.powsimp(expr.expand(), force=True) for expr in exprs])

    """
    if dep_tr is not None:
        if not callable(dep_tr[0]) or not callable(dep_tr[1]):
            raise ValueError("Exceptected dep_tr to be a pair of callables")
    if indep_tr is not None:
        if not callable(indep_tr[0]) or not callable(indep_tr[1]):
            raise ValueError("Exceptected indep_tr to be a pair of callables")

    class _Sys(TransformedSys):
        def __init__(self, dep_exprs, indep=None, **inner_kwargs):
            new_kwargs = kwargs.copy()
            new_kwargs.update(inner_kwargs)
            dep, exprs = zip(*dep_exprs)
            super(_Sys, self).__init__(
                zip(dep, exprs), indep,
                dep_transf=list(zip(
                    list(map(dep_tr[0], dep)),
                    list(map(dep_tr[1], dep))
                )) if dep_tr is not None else None,
                indep_transf=((indep_tr[0](indep), indep_tr[1](indep))
                              if indep_tr is not None else None),
                **new_kwargs)

        @classmethod
        def from_callback(cls, cb, ny, nparams=0, **inner_kwargs):
            new_kwargs = kwargs.copy()
            new_kwargs.update(inner_kwargs)
            return TransformedSys.from_callback(
                cb, ny, nparams,
                dep_transf_cbs=repeat(dep_tr) if dep_tr is not None else None,
                indep_transf_cbs=indep_tr,
                **new_kwargs)
    return _Sys


class ScaledSys(TransformedSys):
    """ Transformed system where the variables have been scaled linearly.

    Parameters
    ----------
    dep_exprs:
        see :class:`SymbolicSys`
    indep:
        see :class:`SymbolicSys`
    dep_scaling: number (>0) or iterable of numbers
        scaling of the dependent variables (default: 1)
    indep_scaling: number (>0)
        scaling of the independent variable (default: 1)
    params:
        see :class:`SymbolicSys`
    \*\*kwargs:
        keyword arguments passed onto TransformedSys

    Examples
    --------
    >>> from sympy import Symbol
    >>> x = Symbol('x')
    >>> scaled = ScaledSys([(x, x*x)], dep_scaling=1000)
    >>> scaled.exprs
    (x**2/1000,)

    """

    @staticmethod
    def _scale_fw_bw(scaling):
        return (lambda x: scaling*x, lambda x: x/scaling)

    def __init__(self, dep_exprs, indep=None, dep_scaling=1, indep_scaling=1,
                 params=(), **kwargs):
        dep, exprs = list(zip(*dep_exprs))
        try:
            n = len(dep_scaling)
        except TypeError:
            n = len(dep_exprs)
            dep_scaling = [dep_scaling]*n
        transf_dep_cbs = [self._scale_fw_bw(s) for s in dep_scaling]
        transf_indep_cbs = self._scale_fw_bw(indep_scaling)
        super(ScaledSys, self).__init__(
            dep_exprs, indep,
            dep_transf=[(transf_cb[0](depi),
                         transf_cb[1](depi)) for transf_cb, depi
                        in zip(transf_dep_cbs, dep)],
            indep_transf=(transf_indep_cbs[0](indep),
                          transf_indep_cbs[0](indep)) if indep is not None else
            None, **kwargs)

    @classmethod
    def from_callback(cls, cb, ny, nparams=0, dep_scaling=1, indep_scaling=1,
                      **kwargs):
        """
        Create an instance from a callback.

        Analogous to :func:`SymbolicSys.from_callback`.

        Parameters
        ----------
        cb: callable
            Signature rhs(x, y[:], p[:]) -> f[:]
        ny: int
            length of y
        nparams: int
            length of p
        dep_scaling: number (>0) or iterable of numbers
            scaling of the dependent variables (default: 1)
        indep_scaling: number (>0)
            scaling of the independent variable (default: 1)
        \*\*kwargs:
            keyword arguments passed onto :class:`ScaledSys`

        Examples
        --------
        >>> def f(x, y, p):
        ...     return [p[0]*y[0]**2]
        >>> odesys = ScaledSys.from_callback(f, 1, 1, dep_scaling=10)
        >>> odesys.exprs
        (p_0*y_0**2/10,)

        """
        return TransformedSys.from_callback(
            cb, ny, nparams,
            dep_transf_cbs=repeat(cls._scale_fw_bw(dep_scaling)),
            indep_transf_cbs=cls._scale_fw_bw(indep_scaling),
            **kwargs
        )


def _skip(indices, iterable):
    return np.asarray([elem for idx, elem in enumerate(
        iterable) if idx not in indices])


def _append(arr, *iterables):
    if isinstance(arr, np.ndarray):
        return np.concatenate((arr,) + iterables)
    arr = arr[:]
    for iterable in iterables:
        arr += type(arr)(iterable)
    return arr


def _concat(*args):
    return np.concatenate(list(map(np.atleast_1d, args)))


class PartiallySolvedSystem(SymbolicSys):
    """ Use analytic expressions for some dependent variables

    Parameters
    ----------
    original_system: SymbolicSys
    analytic_factory: callable
        signature: solved(x0, y0, p0) -> dict, where dict maps
        independent variables as analytic expressions in remaining variables
    Dummy: callable (default: None)
        if None use self.Dummy

    Examples
    --------
    >>> import sympy as sp
    >>> odesys = SymbolicSys.from_callback(
    ...     lambda x, y, p: [
    ...         -p[0]*y[0],
    ...         p[0]*y[0] - p[1]*y[1]
    ...     ], 2, 2)
    >>> dep0 = odesys.dep[0]
    >>> partsys = PartiallySolvedSystem(odesys, lambda x0, y0, p0: {
    ...         dep0: y0[0]*sp.exp(-p0[0]*(odesys.indep-x0))
    ...     })
    >>> print(partsys.exprs)  # doctest: +SKIP
    (_Dummy_29*p_0*exp(-p_0*(-_Dummy_28 + x)) - p_1*y_1,)
    >>> y0, k = [3, 2], [3.5, 2.5]
    >>> xout, yout, info = partsys.integrate([0, 1], y0, k, integrator='scipy')
    >>> info['success'], yout.shape[1]
    (True, 2)

    """

    def __init__(self, original_system, analytic_factory, Dummy=None,
                 **kwargs):
        self.original_system = original_system
        self.analytic_factory = analytic_factory
        if original_system.roots is not None:
            raise NotImplementedError('roots currently unsupported')
        Dummy = Dummy or _Dummy()
        self.init_indep = Dummy()
        self.init_dep = [Dummy() for _ in range(original_system.ny)]

        if 'pre_processors' in kwargs or 'post_processors' in kwargs:
            raise NotImplementedError("Cannot override pre-/postprocessors")
        analytic = self.analytic_factory(self.init_indep, self.init_dep,
                                         original_system.params)
        new_dep = [dep for dep in original_system.dep if dep not in analytic]
        new_params = _append(original_system.params, (self.init_indep,),
                             self.init_dep)
        self.analytic_cb = self._get_analytic_cb(
            original_system, list(analytic.values()), new_dep, new_params)
        analytic_ids = [original_system.dep.index(dep) for dep in analytic]
        nanalytic = len(analytic_ids)
        new_exprs = [expr.subs(analytic) for idx, expr in enumerate(
            original_system.exprs) if idx not in analytic_ids]
        new_kw = kwargs.copy()
        if 'name' not in new_kw and original_system.names is not None:
            new_kw['names'] = original_system.names
        if 'band' not in new_kw and original_system.band is not None:
            new_kw['band'] = original_system.band

        def pre_processor(x, y, p):
            return (x, _skip(analytic_ids, y), _append(
                p, [x[0]], y))

        def post_processor(x, y, p):
            new_y = np.empty(y.shape[:-1] + (y.shape[-1]+nanalytic,))
            analyt_y = self.analytic_cb(x, y, p)
            analyt_idx = 0
            intern_idx = 0
            for idx in range(original_system.ny):
                if idx in analytic_ids:
                    new_y[..., idx] = analyt_y[analyt_idx]
                    analyt_idx += 1
                else:
                    new_y[..., idx] = y[..., intern_idx]
                    intern_idx += 1
            return x, new_y, p[:-(1+original_system.ny)]

        def _wrap_procs(procs):
            return

        new_kw['pre_processors'] = original_system.pre_processors + [
            pre_processor]
        new_kw['post_processors'] = [
            post_processor] + original_system.post_processors

        super(PartiallySolvedSystem, self).__init__(
            zip(new_dep, new_exprs), original_system.indep, new_params,
            lambdify=original_system.lambdify,
            lambdify_unpack=original_system.lambdify_unpack,
            Matrix=original_system.Matrix,
            Symbol=original_system.Symbol,
            Dummy=original_system.Dummy,
            **new_kw)

    def _get_analytic_cb(self, ori_sys, analytic_exprs, new_dep, new_params):
        cb = ori_sys.lambdify(_concat(ori_sys.indep, new_dep, new_params),
                              analytic_exprs)

        def analytic(x, y, params):
            args = np.empty((len(x), 1+self.ny+len(params)))
            args[:, 0] = x
            args[:, 1:self.ny+1] = y
            args[:, self.ny+1:] = params
            if ori_sys.lambdify_unpack:
                return np.asarray(cb(*(args.T)))
            else:
                return np.asarray(cb(args.T))
        return analytic
