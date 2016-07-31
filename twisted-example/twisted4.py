#ref: http://twistedmatrix.com/documents/current/core/howto/defer.html

from twisted.internet import defer, reactor

def printResult(result):
    print 9
    print(result)

def addTen(result):
    print 7
    return result + " ten"

# Deferred gets callback before DeferredList is created
print 1
deferred1 = defer.Deferred()
print 2
deferred2 = defer.Deferred()
print 3
deferred1.addCallback(addTen)
print 4
dl = defer.DeferredList([deferred1, deferred2])
print 5
dl.addCallback(printResult)
print 6
deferred1.callback("one") # fires addTen, checks DeferredList, stores "one ten"
print 8
deferred2.callback("two")
print 10
# At this point, dl will fire its callback, printing:
#     [(1, 'one ten'), (1, 'two')]

# Deferred gets callback after DeferredList is created
print 11
deferred1 = defer.Deferred()
print 12
deferred2 = defer.Deferred()
print 13
dl = defer.DeferredList([deferred1, deferred2])
print 14
deferred1.addCallback(addTen) # will run *after* DeferredList gets its value
print 15
dl.addCallback(printResult)
print 16
deferred1.callback("one") # checks DeferredList, stores "one", fires addTen
print 17
deferred2.callback("two")
print 18
# At this point, dl will fire its callback, printing:
#     [(1, 'one), (1, 'two')]