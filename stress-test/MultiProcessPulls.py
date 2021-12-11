#import docker
import os
import sys
import time
from multiprocessing import Pool
import multiprocessing
import timeit
import random 

def img_pkg_pull(self):
            #print(sequence);
    pid = os.getpid()
    print("\n Entered Process \n ***PROCESSS ID**** : ",pid)
    tap_list = ["tap-packages:0.3.0-build.2", "tap-packages:0.3.0-build.1", "tap-packages:0.4.0-build.11", "tap-packages:0.4.0-build.10", "tap-packages:0.4.0-build.9"]
    tap_pkg = random.choice(tap_list)
    command = ('imgpkg pull -b registry-acceptance.pivotal.io/tanzu-application-platform/%s -o /tmp/tap/%s' % (tap_pkg,pid) )
    #command = ('imgpkg pull -b registry-acceptance.pivotal.io/tanzu-application-platform/tap-packages:0.3.0-build.2 -o /tmp/tap/%s' % pid )
    #print ("\nPull Command is : "+command)
    original_time = time.time()
    os.system(command) 
    #print(command) 
    #print(timeit.timeit(setup = os.system(command), stmt = os.system(command), number = 1))
    times_now = time.time() - original_time
    python_file = open("event/metric_value.txt", "a+")
    python_file.write(str(times_now)+'\n') 
    python_file.close()
    #print("Execution time is: ",times_now)
    print ("\n Finished working on PID : %s  Execution Time Taken for this pull is %s " % (pid,times_now))
    os.system('rm -rf /tmp/taptest/%s' % pid)

if __name__ == '__main__':
    try:
        #print("\n Enter Docker Login Credentials registry-acceptance.tanzu.vmware.com ")
        os.system('docker login registry-acceptance.pivotal.io -u $uname -p $upassword')
        #n = int(input("\n Please enter number of pulls: "))
        #if not n :
        #    print("Enter Valid Input")
        #    exit
        CHECK_FOLDER = os.path.isdir("event")
        if not CHECK_FOLDER:
            os.makedirs("event")
        os.system('echo "$pcount" > event/count.txt') 
        with open('event/count.txt') as f:
            result = f.read().splitlines()
        count= int(result[0])
        inputs = list(range(count))
        origin_time = time.time()
        p = multiprocessing.Pool(processes = count)
        p.map_async(img_pkg_pull, inputs)
        p.close()
        p.join()
        time_interval = time.time() - origin_time
        print ('Total Time Taken :', time_interval)

    except:
        #print("Unexpected error occured:", sys.exc_info()[0])
        print(" \n Unexpected error occured..!!")
