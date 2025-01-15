import inspect
import sys


class Proverka:
    flagProv = False

    def __init__(self):
        self.prov = 0

    def proverka():
        pass


def introspection_info(obj):
    slovar = {}
    attributes = []
    methods = []
    slovar["type"] = type(obj)
    for i in dir(obj):
        if callable(getattr(obj, i)):
            methods.append(i)
        else:
            attributes.append(i)
    slovar["attributes"] = attributes
    slovar["methods"] = methods
    if inspect.isfunction(obj) or inspect.isclass(obj) or inspect.ismodule(obj):
        slovar["module"] = inspect.getmodule(obj)
    else:
        slovar["module"] = __name__
    slovar["size"] = sys.getsizeof(obj)
    return slovar


int_info = introspection_info(42)
print(int_info, "\n")
float_info = introspection_info(42.5)
print(float_info, "\n")
str_info = introspection_info("str")
print(str_info, "\n")
class_info = introspection_info(Proverka)
print(class_info, "\n")
bool_info = introspection_info(Proverka.flagProv)
print(bool_info, "\n")
def_info = introspection_info(introspection_info)
print(def_info, "\n")
