# -*- coding: utf-8 -*-

"""

    wrapper use functiontools
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    test the general wrapper function and the functiontools

    :Created: 2016-8-1
    :Copyright: (c) 2016<chenbo@nsfocus.com>

"""

import functools


def greeting1(func):
    """show greeting message before each func"""
    def __wrapper__(*args, **kwargs):
        print 'Hi~, let\'s start func: %s' % func.__name__
        print 'func docs: %s' % func.__doc__
        return func(*args, **kwargs)
    return __wrapper__


def greenting2(func):
    """what's up"""
    def __wrapper__(*args, **kwargs):
        print '~Hi, let\'s start func: %s' % func.__name__
        print 'func docs: %s' % func.__doc__
        return func(*args, **kwargs)
    return functools.update_wrapper(__wrapper__, func)


def func():
    """func docs"""
    print '~execute func'


if __name__ == '__main__':

    a = greeting1(func)

    a()
    print a.__doc__

    b = greenting2(func)
    b()
    print b.__doc__
