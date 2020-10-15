# Plan for when an iterator rather than an iterable is passed as a function parameter


# check to see if it is an iterator and throw an error

def list_data(data):
    if iter(data) is data:
        raise ValueError


# convert it to an iterable