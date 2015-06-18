import types

def issubclass_recursive(child, parent):
    if not child or not parent:
        return False

    child_class = child if isinstance(child,
                                      types.ClassType) else child.__class__
    parent_class = parent if isinstance(parent,
                                        types.ClassType) else parent.__class__

    if issubclass(child_class, parent_class):
        return True

    for base in child_class.__bases__:
        if issubclass_recursive(base, parent):
            return True

    return False


def coalesce(*args):
    if args:
        for arg in args:
            if arg is not None:
                return arg

    return None
