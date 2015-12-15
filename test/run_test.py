import subprocess
import sys
import time

def run_cuda(p, s):
    f = open("result_cuda.txt", "w")
    subprocess.call(["../cuda/cuda_wave", p, s], stdout=f)

def run_serial(p, s):
    f = open("result_serial.txt", "w")
    subprocess.call(["../serial/serial_wave", p, s], stdout=f)

def run(p, s):
    start_time1 = time.time()
    run_serial(p, s)
    end_time1 = time.time()

    start_time2 = time.time()
    run_cuda(p, s)
    end_time2 = time.time()

    print "serial output diff with cuda output"
    run_diff()
    print "serial wave equation program run %s seconds" % (end_time1 - start_time1)
    print "cuda wave equation program run %s seconds" % (end_time2 - start_time2)

def run_diff():
    subprocess.call(["diff", "result_cuda.txt", "result_serial.txt"])
    

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Usage:\n\t python run_test.py points steps"
	sys.exit()

    run(sys.argv[1], sys.argv[2])
