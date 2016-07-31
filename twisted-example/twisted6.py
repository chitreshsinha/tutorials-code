from twisted.internet import defer, reactor
from twisted.web.client import getPage
from datetime import datetime 

def nowTime():
    return datetime.now()

def pageCallback(result):
    print '11--------------pageCallback', nowTime()
    print len(result)
    return len(result)

def listCallback(results):
    print '12--------------listCallback', nowTime()
    print results
    #for isSuccess, content in results:
    #    print "Successful? %s" % isSuccess
        #print "Content Length: %s" % len(content)

def finish(ign):
    print '13--------------finish', nowTime()
    print ign
    reactor.stop()

def test():
    print'2------------test', nowTime()
    d1 = getPage('http://www.google.com')
    print '3-------------getPage - google', nowTime()
    d1.addCallback(pageCallback)
    print '4-------------addCallback - google', nowTime()
    d2 = getPage('http://yahoo.com')
    print '5-------------getPage - yahoo', nowTime()
    d2.addCallback(pageCallback)
    print '6-------------addCallback - yahoo', nowTime()
    dl = defer.DeferredList([d1, d2])
    print '7--------------dl', nowTime()
    dl.addCallback(listCallback)
    print '8----------------', nowTime()
    dl.addCallback(finish)
    print '9---------------------', nowTime()


print '1----------------------', nowTime()
test()
print '10--------------------', nowTime()
reactor.run()
print '14----------------------', nowTime()
