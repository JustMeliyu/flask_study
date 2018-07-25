from types import BuiltinFunctionType, BuiltinMethodType, FunctionType, MethodType, ClassType


def help(object, spacing=10, collapse=1):
    """Print methods and doc strings.
    Takes module, class, list, dictionary, or string."""

    typeList = (BuiltinFunctionType, BuiltinMethodType, FunctionType, MethodType, ClassType)

    methodList = [method for method in dir(object) if type(getattr(object, method)) in typeList]

    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)

    print "\n".join(["%s %s" %
                     (method.ljust(spacing),
                      processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])


if __name__ == "__main__":
    help(object=[])
    print help.__doc__
