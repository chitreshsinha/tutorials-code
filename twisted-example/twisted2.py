#ref: http://twistedmatrix.com/documents/current/core/howto/defer.html
from twisted.internet import reactor, defer
from datetime import datetime 

def nowTime():
    return datetime.now()

class Getter:
    def gotResults(self, x):
        print 15, nowTime()
        """
        The Deferred mechanism provides a mechanism to signal error
        conditions.  In this case, odd numbers are bad.

        This function demonstrates a more complex way of starting
        the callback chain by checking for expected results and
        choosing whether to fire the callback or errback chain
        """
        if self.d is None:
            print 16, nowTime()
            print("Nowhere to put results")
            return

        print 17, nowTime()
        d = self.d
        print 18, nowTime()
        self.d = None
        print 19, nowTime()
        if x % 2 == 0:
            print 20, nowTime()
            d.callback(x*3)
        else:
            print 21, nowTime()
            d.errback(ValueError("You used an odd number!"))
        print 22, nowTime()

    def _toHTML(self, r):
        print 23, nowTime()
        """
        This function converts r to HTML.

        It is added to the callback chain by getDummyData in
        order to demonstrate how a callback passes its own result
        to the next callback
        """
        return "Result: %s" % r

    def getDummyData(self, x):
        print 3, nowTime()

        """
        The Deferred mechanism allows for chained callbacks.
        In this example, the output of gotResults is first
        passed through _toHTML on its way to printData.

        Again this function is a dummy, simulating a delayed result
        using callLater, rather than using a real asynchronous
        setup.
        """
        self.d = defer.Deferred()
        print 4, nowTime()
        # simulate a delayed result by asking the reactor to schedule
        # gotResults in 2 seconds time
        reactor.callLater(2, self.gotResults, x)
        print 5, nowTime()
        self.d.addCallback(self._toHTML)
        print 6, nowTime()
        return self.d

def cbPrintData(result):
    print 8, nowTime()
    print(result)

def ebPrintError(failure):
    print 9, nowTime()
    import sys
    sys.stderr.write(str(failure))

# this series of callbacks and errbacks will print an error message
print 1, nowTime()
g = Getter()
print 2, nowTime()
d = g.getDummyData(3)
print 7, nowTime()
d.addCallback(cbPrintData)
print 8, nowTime()
d.addErrback(ebPrintError)
print 9, nowTime()

# this series of callbacks and errbacks will print "Result: 12"
g = Getter()
print 10, nowTime()
d = g.getDummyData(4)
print 11, nowTime()
d.addCallback(cbPrintData)
print 12, nowTime()
d.addErrback(ebPrintError)
print 13, nowTime()

reactor.callLater(4, reactor.stop)
print 14, nowTime()
reactor.run()
print 24, nowTime()