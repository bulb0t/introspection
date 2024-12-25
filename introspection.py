from pprint import pprint

from inspect import getmodule

def introspection_info(obj):
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    return f'type: {type(obj).__name__}, attributes: {attributes}, methods: {methods}, module: {getmodule(obj).__name__ if getmodule(obj) else "__main__"}'

pprint(introspection_info(5))

