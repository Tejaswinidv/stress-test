import sys
import os
lst = []
lst.append(3.65434)
lst.append(2.98547)
lst.append(3.34344)
print ("average is ",sum(lst)/len(lst))
avg = sum(lst)/len(lst)
os.mkdir("event")
python_file = open("event/metric_value.txt", "a")
python_file.write(str(avg))
python_file.close()
