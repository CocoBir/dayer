# -*- coding: utf-8 -*-

"""

    python string formater: r vs s
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    difference between string formater r and s

    :Created: 2016-8-1
    :Copyright: (c) 2016<chenbo@nsfocus.com>

"""


from datetime import datetime


if __name__ == '__main__':

    now = datetime.now()

    print (
            "when you use %s to format string, you "
            "use str() function to convert the object "
            "to string, but %r use repr() to format object."
        )

    print "use s as formater: %s" % now
    print "use r as formater: %r" % now

