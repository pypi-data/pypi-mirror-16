import builtins
import typing
import numbers
from collections import ChainMap
from typing import Optional, Union, Any, TypeVar, Tuple


class EnahncedTypeVar:
    """
    Utility wrapper for adding extra properties to default TypeVars
    Allows TypeVars to be bivariant
    Can be constructed as any other TypeVar or from existing TypeVars
    """
    
    def __init__(self,
                 name: str,
                 *constraints: Any,
                 bound: Optional[type]=None,
                 covariant: Optional[bool]=False,
                 contravariant: Optional[bool]=False,
                 type_var: Optional[TypeVar]=None):
        if type_var:
            self.type_var = type_var
            self.__name__ = type_var.__name__
            self.__bound__ = type_var.__bound__
            self.__covariant__ = type_var.__covariant__
            self.__contravariant__ = type_var.__contravariant__
            self.__constraints__ = type_var.__constraints__
        else:
            self.type_var = TypeVar(name, *constraints, bound=bound)
            self.__name__ = name
            self.__bound__ = bound
            self.__covariant__ = covariant
            self.__contravariant__ = contravariant
            self.__constraints__ = constraints

    def __repr__(self):
        """
        Further enhances TypeVar representation through addition of bi-variant symbol
        """
        if self.__covariant__ and self.__contravariant__:
            prefix = '*'
        elif self.__covariant__:
            prefix = '+'
        elif self.__contravariant__:
            prefix = '-'
        else:
            prefix = '~'
        return prefix + self.__name__


# According to https://docs.python.org/3/reference/datamodel.html,
# there are two types of integers - int and bool, but the 'PEP 3141 -- A Type Hierarchy for Numbers'
# (https://www.python.org/dev/peps/pep-3141/)
# makes no such distinction.
# As I could not find required base classes to differentiate between two types of integers,
# I decided to add my own classes.
# If I am wrong, please let me know


class Integer(numbers.Integral):
    """
    Integer stub class
    """
    pass


class Boolean(numbers.Integral):
    """
    Boolean stub class
    """
    pass


TYPE_ALIASES = {
    tuple: Tuple,
    int: Integer,
    bool: Boolean,
    float: numbers.Real,
    complex: numbers.Complex,
    dict: typing.Dict,
    list: typing.List,
    None: type(None)
}


def is_type_of_type(data: Union[type, str, None],
                    data_type: Union[type, str, TypeVar, EnahncedTypeVar, None],
                    covariant: bool=False,
                    contravariant: bool=False,
                    local_variables: Optional[dict] = None,
                    global_variables: Optional[dict] = None
                    ) -> bool:
    """
    Returns if the type or type like object is of the same type as constrained
    Support co-variance, contra-variance and TypeVar-s
    Also, can extract type from the scope if only its name was given
    """
    # Calling scope should be passed implicitly
    # Otherwise, it is assumed to be empty
    if local_variables is None:
        local_variables = {}

    if global_variables is None:
        global_variables = {}

    calling_scope = ChainMap(local_variables, global_variables, vars(typing), vars(builtins))

    # If a variable is string, then it should look it up in the scope of a calling function
    if isinstance(data_type, str):
        data_type = calling_scope[data_type]

    if isinstance(data, str):
        data = calling_scope[data]

    is_type_var = data_type.__class__ is TypeVar or data_type.__class__ is EnahncedTypeVar

    # Checks if the type is in the list of type aliases
    # And replaces it (if found) with a base form
    data = TYPE_ALIASES.get(data, data)
    data_type = TYPE_ALIASES.get(data_type, data_type)

    if is_type_var:
        if data_type.__bound__:
            constraints = [data_type.__bound__]
        else:
            constraints = data_type.__constraints__
        covariant = data_type.__covariant__
        contravariant = data_type.__contravariant__
    else:
        constraints = [data_type]

    if not constraints:
        constraints = [Any]

    constraints = [TYPE_ALIASES.get(constraint, constraint) for constraint in constraints]
    
    if Any in constraints:
        return True
    elif covariant and contravariant:
        return any((d in data.__mro__) or (data in d.__mro__) for d in constraints)
    elif covariant:
        return any(d in data.__mro__ for d in constraints)
    elif contravariant:
        return any(data in d.__mro__ for d in constraints)
    else:
        return any(data is d for d in constraints)
