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

# alternative method of fetching 100 schedule decisions ahead
result_alt = sched.get_next(100)

unique_set = Set(result_alt)
for res in unique_set:
    print "%s: %s counts"%(res, result_alt.count(res))
