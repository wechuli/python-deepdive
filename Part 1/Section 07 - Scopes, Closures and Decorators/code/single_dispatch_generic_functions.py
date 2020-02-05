from html import escape
from decimal import Decimal
from fractions import Fraction


def singledispatch(fn):
    registry = {

    }
    registry[object] = fn

    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)

    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner

    # write a function to access the registry to get the dispatch associated with a fucntion
    def dispatch(type_):
        return registry.get(type(type_), registry[object])

    decorated.register = register
    decorated.dispatch = dispatch

    return decorated


@singledispatch
def htmlize(arg):
    return escape(str(arg))


def html_escape(arg):
    return escape(str(arg))


@htmlize.register(int)
def html_int(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))


@htmlize.register(float)
def html_real(a):
    return '{0:.2f}'.format(round(a, 2))


@htmlize.register(str)
def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')

# You can stack the decorators


@htmlize.register(list)
@htmlize.register(tuple)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(htmlize(item)) for item in l)

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


@htmlize.register(dict)
def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(html_escape(k), htmlize(v))
             for k, v in d.items())

    return '<ul>\n' + '\n'.join(items) + '\n<ul>'


@htmlize.register(set)
def html_set(arg):
    return html_list(arg)


print(htmlize('1 < 100'))
print(htmlize(100))
print(htmlize((1, 2, 3)))

print(htmlize.dispatch(int))
