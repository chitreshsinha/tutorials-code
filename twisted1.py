from twisted.internet import reactor, defer
from datetime import datetime 

def nowTime():
    return datetime.now()

def getDummyData(inputData):
    print 2, nowTime()
    """
    This function is a dummy which simulates a delayed result and
    returns a Deferred which will fire with that result. Don't try too
    hard to understand this.
    """
    print 3, nowTime()
    #creates a deferred object to attach a callback to it
    deferred = defer.Deferred()
    print 4, nowTime()
    # simulate a delayed result by asking the reactor to fire the
    # Deferred in 2 seconds time with the result inputData * 3
    reactor.callLater(2, deferred.callback, inputData * 3)
    print 5, nowTime()
    return deferred

def cbPrintData(result):
    print 10, nowTime()
    """
    Data handling function to be added as a callback: handles the
    data by printing the result
    """
    print('Result received: {}'.format(result))
    print 11, nowTime()


print "Print Start From Here"
print 1, nowTime()
deferred = getDummyData(3)
print 6, nowTime()
#appends cbPrintData to getDummyData's deferred object. It will be called once getDummyData's deferred object has result
deferred.addCallback(cbPrintData)
print 7, nowTime()
# manually set up the end of the process by asking the reactor to
# stop itself in 4 seconds time
reactor.callLater(4, reactor.stop)
print 8, nowTime()
# start up the Twisted reactor (event loop handler) manually
print('Starting the reactor')
print 9, nowTime()
reactor.run()
print 12, nowTime()