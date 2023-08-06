from pyfunk import combinators as _
from pyfunk.misc import T
from functools import reduce


def __map_object(obj, fn):
    def reducer(newObj, key):
        newObj[key] = fn(obj[key])
        return newObj
    return reduce(reducer, obj.keys(), {})


def __filter_object(obj, fn):
    def reducer(newObj, key):
        if fn(obj[key]):
            newObj[key] = obj[key]
        return newObj
    return reduce(reducer, obj.keys(), {})


@_.curry
def fmap(fn, arr):
    '''
    Generic function for dealing with objects and arrays.
    @sig fmap :: (a -> b) -> [a] -> [b]
    '''
    if hasattr(arr, 'keys'):
        return __map_object(arr, fn)
    else:
        return list(map(fn, arr))


@_.curry
def fslice(x, y, arr):
    '''
    Composable equivalent of [:]. Use None for the second argument
    for the equivalent [x:]
    @sig fslice :: Number -> Number -> [a] -> [a]
    '''
    return arr[x:y]


@_.curry
def freduce(fn, init, arr):
    '''
    Composable equivalent of reduce in functional tools. Pass None
    if no init exists.
    @sig freduce :: (a -> b) -> a -> [a] -> b
    '''
    return reduce(fn, arr, init) if init else reduce(fn, arr)


@_.curry
def ffilter(fn, arr):
    '''
    Composable equivalent of iterable filter function.
    @sig ffilter :: (a -> Bool) -> [a] -> [a]
    '''
    if hasattr(arr, 'keys'):
        return __filter_object(arr, fn)
    else:
        return list(filter(fn, arr))


@_.curry
def prop(string, obj):
    '''
    Property access as a function
    @sig prop :: String -> Dict -> a
    '''
    return obj.get(string)


@_.curry
def concat(c1, c2):
    '''
    Equivalent of + for concatables(string, array)
    @sig concat :: Concatable c => c a -> c a -> c a
    '''
    return c1 + c2


@_.curry
def index_of(fn, arr):
    '''
    Find the index of first element that passes given.
    @sig index_of :: (a -> Bool) -> [a] -> Number
    '''
    for i in range(len(arr)):
        if fn(arr[i]):
            return i
    return -1


@_.curry
def array_get(i, arr):
    '''
    Array access as a function.
    @sig array_get :: Number -> [a] ->  a
    '''
    try:
        return arr[i]
    except IndexError:
        return None


@_.curry
def first(fn, arr):
    '''
    Get the first element that passes the test.
    @sig first :: (a -> Bool) -> [a] -> a
    '''
    return array_get(index_of(fn, arr), arr)


head = first(T)
head.__doc__ = '''
Get the top of an array
@sig head :: [a] -> a
'''


@_.curry
def take_while(fn, arr):
    '''
    Retrieve the first set of elements that pass the given test.
    @sig take_while :: (a -> Bool) -> [a] -> [a]
    '''
    i = index_of(_.fnot(fn), arr)
    return fslice(0, 0 if i == -1 else i, arr)


@_.curry
def drop_while(fn, arr):
    '''
    Slice array starting from the element that fails the given test.
    @sig drop_while :: (a -> Bool) -> [a] -> [a]
    '''
    i = index_of(_.fnot(fn), arr)
    return fslice(len(arr) if i == -1 else i, None, arr)

def tail(ls):
    '''
    Get every element in the list except for the head
    @sig tail :: [a] -> [a]
    '''
    return ls[1:]


def body(ls):
    '''
    Get every element in the list except the last one.
    @sig body ::  [a] -> [a]
    '''
    return ls[:-1]


def last(ls):
    '''
    Get the element at the end of the list
    @sig last :: [a] -> a
    '''
    return ls[-1:].pop()


def fzip(items):
    '''
    Create a map from the list of tuples.
    @sig fzip :: [(Str, (* -> a))] -> Dict (* -> a)
    '''
    return {x: y for x, y in items}


def flatten(listoflists):
    '''
    Flattens an array of arrays one level deep
    @sig flatten :: [[a]] -> [a]
    '''
    return freduce(concat, [], listoflists)
