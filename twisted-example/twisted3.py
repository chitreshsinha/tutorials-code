# A callback that unpacks and prints the results of a DeferredList

from twisted.internet import defer, reactor

def printResult(result):
    print 9, result
    for (success, value) in result:
        print 10
        if success:
            print 11
            print('Success:', value)
        else:
            print 12
            print('Failure:', value.getErrorMessage())

# Create three deferreds.
print 1
deferred1 = defer.Deferred()
print 2
deferred2 = defer.Deferred()
print 3
deferred3 = defer.Deferred()

# Pack them into a DeferredList
print 4
dl = defer.DeferredList([deferred1, deferred2, deferred3], consumeErrors=True)

# Add our callback
print 5
dl.addCallback(printResult)

# Fire our three deferreds with various values.
print 6
deferred1.callback('one')
print 7
deferred2.errback(Exception('bang!'))
print 8
deferred3.callback('three')

# At this point, dl will fire its callback, printing:
#    Success: one
#    Failure: bang!
#    Success: three
# (note that defer.SUCCESS == True, and defer.FAILURE == False)