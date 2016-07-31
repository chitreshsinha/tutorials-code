from twisted.internet import defer, reactor
from twisted.web.client import getPage
from datetime import datetime 

def nowTime():
    return datetime.now()

def listCallback(results):
    print '9--------------listCallback', nowTime()
    print 'len(results)', len(results)
    print 'len(r1)', len(results[0][1])
    print 'len(r2)', len(results[1][1])

def finish(ign):
    print '10--------------finish', nowTime()
    #print 'ign', ign
    reactor.stop()

def test():
    print'2------------test', nowTime()
    d1 = getPage('http://www.google.com')
    print '3-------------getPage - google', nowTime()
    d2 = getPage('http://yahoo.com')
    print '4-------------getPage - yahoo', nowTime()
    dl = defer.DeferredList([d1, d2])
    print '5--------------dl', nowTime()
    dl.addCallback(listCallback)
    print '6----------------', nowTime()
    dl.addCallback(finish)
    print '7---------------------', nowTime()

print '1----------------------', nowTime()
test()
print '8--------------------', nowTime()
reactor.run()
print '11----------------------', nowTime()