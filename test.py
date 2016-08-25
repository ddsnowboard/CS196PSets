from hw0 import *

for i, j in {missing_friends('james', 
                         '''
                         james jack jill
                         jack jill james
                         jill jack james
                         '''): 0, 

             missing_friends('james', 
                         '''
                         james jack
                         jack james jill bob
                         jill jack bob
                         bob jill jack
                         '''): 2,

             missing_friends('james', 
                         '''
                         james jack
                         jack james jill
                         jill jack
                         '''): 1
             }.iteritems():
    if  i == j:
        print "Everything is good"
    else:
        print "Something bad happened; returned %d when I wanted %d" % (i, j)
