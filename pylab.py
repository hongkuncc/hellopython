from matplotlib import pylab
pylab.figure(1)
pylab.plot([1,2,3,4],[3,7,1,9])
pylab.figure(2)
pylab.plot([1,4,2,3],[5,6,7,8])
pylab.savefig('Figure-Addie')
pylab.figure(1)
pylab.plot([5,6,10,3])
pylab.savefig('Figure-Jane')
pylab.show()