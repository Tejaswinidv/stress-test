#import docker
import os
import sys
import time
from multiprocessing import Pool
import multiprocessing
import timeit

def img_pkg_pull(self):
            #print(sequence);
    pid = os.getpid()
    print("\n Entered Process \n ***PROCESSS ID**** : ",pid)
    command = ('imgpkg pull -b registry-acceptance.tanzu.vmware.com/tanzu-application-platform/tap-packages:0.3.0-build.2 -o /tmp/tap/%s' % pid )
    #print ("\nPull Command is : "+command)
    original_time = time.time()
    os.system(command)
    #print(timeit.timeit(setup = os.system(command), stmt = os.system(command), number = 1))
    times_now = time.time() - original_time
    #print("Execution time is: ",times_now)
    print ("\n Finished working on PID : %s  Execution Time Taken for this pull is %s " % (pid,times_now))
    os.system('rm -rf /tmp/taptest/%s' % pid)

if __name__ == '__main__':
    try:
        #print("\n Enter Docker Login Credentials registry-acceptance.tanzu.vmware.com ")
        #os.system('docker login registry-acceptance.tanzu.vmware.com')
        #n = int(input("\n Please enter number of pulls: "))
        #if not n :
        #    print("Enter Valid Input")
        #    exit
        inputs = list(range(10))
        origin_time = time.time()
        p = multiprocessing.Pool(processes = 10)
        p.map_async(img_pkg_pull, inputs)
        p.close()
        p.join()
        time_interval = time.time() - origin_time
        print ('Total Time Taken :', time_interval)

    except:
        #print("Unexpected error occured:", sys.exc_info()[0])
        print(" \n Unexpected error occured..!!")
