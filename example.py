import pywrr
from sets import Set

# test data to schedule
data = [ ("A", 6), 
        ("B", 5), 
        ("C", 4), 
        ("D", 3), 
        ("E", 2),
        ("F", 1),
      ]

# initialize scheduler
sched = pywrr.WRRScheduler(data)

result = []
for i in range(0, 100):
    choose = sched.get_next()
    print "Choose is : %s"%choose[0]
    result.append(choose[0])


unique_set = Set(result)
for res in unique_set:
    print "%s: %s counts"%(res, result.count(res))
 
