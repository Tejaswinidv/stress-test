import sys
import os
lst = []
lst.append(3.65434)
lst.append(2.98547)
lst.append(3.34344)
print ("average is ",sum(lst)/len(lst))
avg = sum(lst)/len(lst)
CHECK_FOLDER = os.path.isdir("event")
if not CHECK_FOLDER:
    os.makedirs("event")
#os.mkdir("event")
python_file = open("event/metric_value.txt", "a")
python_file.write("3.65434")
python_file.write('\n')
python_file.write("2.98547")
python_file.write('\n')
python_file.write(str(avg))
os.system('cat event/metric_value.txt')
python_file.close()
