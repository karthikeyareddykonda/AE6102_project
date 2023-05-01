import argparse
from object import object,R,M,nobject,Multi_object
import numpy as np
import time


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="AE project",
        description="Basic driver for N body system"
    )

    parser.add_argument('-N', type=int,required=False,default=2,help="No of satellites")
    parser.add_argument('-d',type=float,required=False,default=2*R,help="Initial spher boundary")



    parser.add_argument('-procedure',type=str, required=False,default="pure",choices=["pure","numpy"])
    
    



    parser.add_argument('-T', type=int,required=False,default= 50*24*3600,help="No of seconds to simulate")
    parser.add_argument('-dt', type=int, required=False,default=60,help="dt time unit")

    parser.add_argument('-o',type=str, help="file path to save output of all frames")

    args = parser.parse_args()
    Nobj = args.N 
    d = args.d 
    proc = args.procedure
    T = args.T
    dt = args.dt 
    out_file = args.o

    N = int(T/dt) # the no of frames to generate
    ob_all ,ob2 = None, None
    
    ob2 = object(m= M)
    ob_all = Multi_object(Nobj=Nobj,d=d)

    time_taken = None
    if(proc == "pure"):
        t1 = time.perf_counter()

        frames = ob_all.get_frames_pure(obj2=ob2,dt=dt,N=N)
        t2 = time.perf_counter()
        time_taken = t2-t1

    if(proc == "numpy"):
        t1 = time.perf_counter()
        frames = ob_all.get_frames_numpy(obj2=ob2,dt=dt,N=N)
        t2 = time.perf_counter()
        time_taken = t2-t1
    
    print(time_taken)
    if(out_file is not None):
        np.save(out_file,frames)

