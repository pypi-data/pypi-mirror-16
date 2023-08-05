# --------------------------------------------------------------------------
# Source file provided under Apache License, Version 2.0, January 2004,
# http://www.apache.org/licenses/
# (c) Copyright IBM Corp. 2015, 2016
# --------------------------------------------------------------------------
from enum import Enum

from docplex.mp.compat23 import StringIO
from docplex.mp.utils import is_number, is_string, str_holo


class ModelingObjectBase(object):

    __array_priority__ = 100

    """ModelingObjectBase()

    Parent class for all modeling objects (variables and constraints).

    This class is not intended to be instantiated directly.
    """
    __slots__ = ("_name", "_model", "_has_automatic_name")


    def __init__(self, model, name=None, has_automatic_name=False):
        self._name = name
        self._model = model
        self._has_automatic_name = has_automatic_name

    def get_name(self):
        """ This property is used to get or set the name of the modeling object.

        """
        return self._name

    def set_name(self, name):
        self.check_name(name)
        self._name = name
        if name:
            self._has_automatic_name = False

    def check_name(self, new_name):
        # INTERNAL: basic method for checking names.
        pass  # pragma: no cover

    name = property(get_name, set_name)

    def has_name(self):
        """ Checks whether the object has a name.

        Returns:
            True if the object has a name.

        """
        return self._name is not None

    def has_automatic_name(self):
        return self._has_automatic_name

    def has_user_name(self):
        """ Checks whether the object has a valid name given by the user.

        Returns:
            True if the object has a valid name given by the user.

        """
        return self.has_name() and not self._has_automatic_name

    def _set_automatic_name(self, auto_name):
        # INTERNAL
        self._name = auto_name  # no check here
        self._has_automatic_name = True

    @property
    def model(self):
        """
        This property returns the :class:`docplex.mp.model.Model` to which the object belongs.
        """
        return self._model

    def _get_model(self):
        return self._model

    def is_in_model(self, model):
        return model and self._model is model

    def _check_model_has_solution(self):
        self.model.check_has_solution()

    def fatal(self, msg, *args):
        self.error_handler.fatal(msg, args)

    def error(self, msg, *args):
        self.error_handler.error(msg, args)

    def warning(self, msg, *args):
        self.error_handler.warning(msg, args)

    def trace(self, msg, *args):
        self.error_handler.trace(msg, args)

    @property
    def error_handler(self):
        return self._model.error_handler

    def truncated_str(self):
        return str_holo(self, maxlen=self._model._max_repr_len)

    def zero_expr(self):
        # INTERNAL
        return self._model._get_zero_expr()

    def _unsupported_binary_operation(self, lhs, op, rhs):
        self.fatal("Unsupported operation: {0!s} {1:s} {2!s}", lhs, op, rhs)

    def is_quad_expr(self):
        return False


class ModelingObject(ModelingObjectBase):

    __slots__ = ("_index", "_origin", "_container")

    def is_valid_index(self, idx):
        # INTERNAL: This is where the valid index check is performed
        return idx >= 0

    # @profile
    def __init__(self, model, name=None, index=-1, is_automatic_name=False, container=None):
        ModelingObjectBase.__init__(self, model, name, has_automatic_name=is_automatic_name)
        self._index = index
        self._origin = None
        self._container = container

    def is_generated(self):
        """ Checks whether this object has been generated by another modeling object.

        If so, the origin object is stored in the ``_origin`` attribute.

        Returns:
            True if the objects has been generated.
        """
        return self._origin is not None

    def notify_origin(self, origin):
        if origin is not None:
            self._origin = origin
            # generated objects have generated names too
            self._has_automatic_name = True

    def origin(self):
        return self._origin

    def __hash__(self):
        return id(self)

    @property
    def unchecked_index(self):
        return self._index

    def get_index(self):
        return self._index

    def set_index(self, idx):
        self._index = idx

    def has_valid_index(self):
        return self._index >= 0

    def _get_index_or_raise(self):
        ''' Returns the index if valid, otherwise raises an exception.'''
        if not self.has_valid_index():
            self.fatal("Modeling object {0!s} has invalid index: {1:d}", self, self._index)  # pragma: no cover
        return self._index

    index = property(get_index, set_index)
    safe_index = property(_get_index_or_raise)

    def get_container(self):
        # INTERNAL
        return self._container


class Expr(ModelingObjectBase):
    """Expr()

    Parent class for all expression classes.
    """
    __slots__ = ()

    def __init__(self, model, name=None):
        ModelingObjectBase.__init__(self, model, name)

    def clone(self):
        raise NotImplementedError  # pragma: no cover

    def copy(self, target_model, var_mapping):
        # internal
        raise NotImplementedError  # pragma: no cover

    def number_of_variables(self):
        """
        Returns:
            integer: The number of variables in the expression.
        """
        return sum(1 for _ in self.iter_variables())  # pragma: no cover


    def contains_var(self, dvar):
        """ Checks whether a variable is present in the expression.

        :param: dvar (:class:`docplex.mp.linear.Var`): A decision variable.

        Returns:
            Boolean: True if the variable is present in the expression, else False.
        """
        for v in self.iter_variables():
            if dvar is v:
                return True
        else:
            return False

    def __contains__(self, dvar):
        """Overloads operator `in` for an expression and a variable.

        :param: dvar (:class:`docplex.mp.linear.Var`): A decision variable.

        Returns:
            Boolean: True if the variable is present in the expression, else False.
        """
        return self.contains_var(dvar)

    def to_string(self, nb_digits=None, prod_symbol='', use_space=False):
        oss = StringIO()
        if nb_digits is None:
            nb_digits = self.model.float_precision
        self.to_stringio(oss, nb_digits=nb_digits, prod_symbol=prod_symbol, use_space=use_space)
        return oss.getvalue()

    def to_stringio(self, oss, nb_digits, prod_symbol, use_space, var_namer=lambda v: v.name):
        raise NotImplementedError  # pragma: no cover

    def __str__(self):
        return self.to_string()

    def _num_to_stringio(self, oss, num, ndigits=None):
        # INTERNAL
        if ndigits is None:
            ndigits = self.model.float_precision
        if num == int(num):
            oss.write('%d' % num)
        else:
            # use second arg as nb digits:
            oss.write("{0:.{1}f}".format(num, ndigits))

    def __pos__(self):
        # + e is identical to e
        return self

    def is_discrete(self):
        raise NotImplementedError  # pragma : no cover

    def is_zero(self):
        return False

    def is_constant(self):
        return False

    def get_constant(self):
        return 0

    constant = property(get_constant)

    @property
    def float_precision(self):
        return 0 if self.is_discrete() else self.model.float_precision

    def _round_if_discrete(self, raw_value):
        if self.is_discrete():
            return self.model.round_nearest(raw_value)
        else:
            return raw_value

    def _get_solution_value(self):
        # INTERNAL: compute solutoion value.
        raise NotImplementedError  # pragma: no cover

    def notify_used(self, ct):
        # INTERNAL
        pass

    @property
    def solution_value(self):
        self._check_model_has_solution()
        return self._get_solution_value()

    def __ne__(self, other):
        self.model.unsupported_neq_error(self, other)

    def __pow__(self, power):
        # INTERNAL
        # power must be checke in {0, 1, 2}
        self.model.typecheck_as_power(self, power)
        if 0 == power:
            return 1
        elif 1 == power:
            return self
        else:
            return self.square()

    def square(self):
        # redefine for each class of expression
        return None  # pragma : no cover

    def __gt__(self, e):
        """ The strict > operator is not supported
        """
        self.model.unsupported_relational_operator_error(self, ">", e)

    def __lt__(self, e):
        """ The strict < operator is not supported
        """
        self.model.unsupported_relational_operator_error(self, "<", e)


# --- Priority class used for relaxation
class Priority(Enum):
    # priority values are not sequential integers
    VERY_LOW, LOW, MEDIUM, HIGH, VERY_HIGH = range(100, 6 * 100, 100)
    MANDATORY = 999999999

    @staticmethod
    def default_priority():
        return Priority.MEDIUM

    @staticmethod
    def all_sorted():
        # INTERNAL
        sorted_properties = [Priority.VERY_LOW, Priority.LOW, Priority.MEDIUM, Priority.HIGH, Priority.VERY_HIGH]
        return sorted_properties

    def get_index(self):
        return self.value / 100

    def _level(self):
        # INTERNAL: retuens an integer value for priority
        return self.value

    def print_name(self):
        priority_names = {Priority.MANDATORY: 'Mandatory',
                          Priority.HIGH: 'High',
                          Priority.VERY_HIGH: "Very High",
                          Priority.MEDIUM: 'Medium',
                          Priority.LOW: 'Low',
                          Priority.VERY_LOW: 'Very Low'}
        return priority_names.get(self, "Unexpected Priority")

    def get_geometric_preference_factor(self, base=10.0):
        # INTERNAL: returns a CPLEX preference factor as a poer of "base"
        # MEDIUM priority has always a preference factor of 1
        assert is_number(base)
        if self.is_mandatory():
            return 1e+20
        else:
            # pylint complains about no value member but is wrong!
            diff = self.get_index() - Priority.MEDIUM.get_index()
            factor = 1.0
            pdiff = diff if diff >= 0 else -diff
            for _ in range(0, int(pdiff)):
                factor *= base
            return factor if diff >= 0 else 1.0 / factor

    def less_than(self, other):
        assert isinstance(other, Priority)
        return self._level() < other._level()

    def __lt__(self, other):
        return self.less_than(other)

    def __gt__(self, other):
        return other.less_than(self)

    def is_mandatory(self):
        return self == Priority.MANDATORY


# ---


class ObjectiveSense(Enum):
    """
    This enumerated class defines the two types of objectives, `Minimize` and `Maximize`.
    """
    Minimize, Maximize = 1, 2

    # static method: which type is the default.
    @staticmethod
    def default_sense():
        return ObjectiveSense.Minimize

    def is_minimize(self):
        return self is ObjectiveSense.Minimize

    def is_maximize(self):
        return self is ObjectiveSense.Maximize

    def verb(self):
        # INTERNAL
        return "minimize" if self.is_minimize() else "maximize" if self.is_maximize() else "WHAT???"

    def action(self):
        # INTERNAL
        # minimize -> minimizing, maximize -> maximizing...
        return "%sing" % self.verb()[:-1]

    @staticmethod
    def parse(arg, logger, default_sense=None):
        if isinstance(arg, ObjectiveSense):
            return arg
        elif not arg or not is_string(arg):
            if not default_sense:
                logger.fatal("cannot convert: <{}> to oebjective sense", (arg,))
            else:
                logger.error("cannot convert: <{0!r}> to objective sense - using default: {1!s}", (arg, default_sense))
                return default_sense
        else:
            lower_text = arg.lower()
            if lower_text in {"minimize", "min"}:
                return ObjectiveSense.Minimize
            elif lower_text in {"maximize", "max"}:
                return ObjectiveSense.Maximize
            elif default_sense:
                logger.error("Text is not recognized as objective sense: {0}, expecting \"min\" or \"max\" - using default {1:s}",
                             (arg, default_sense))
                return default_sense
            else:
                logger.fatal("Text is not recognized as objective sense: {0}, expecting ""min"" or ""max", (arg,))


# noinspection PyUnusedLocal
