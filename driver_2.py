# this file implements the basic driver with argparser.. To be used in automan
import argparse
from object import object,R,M,nobject
import numpy as np
import time



if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="AE project",
        description="Basic driver for 2 body system"
    )

    parser.add_argument('-M1', type=float,  required=False,default="1",help= "Mass of object")
    parser.add_argument('-R1', type=float, required=False,default="1" ,help="Radius of obj1")
    parser.add_argument('-posvec1', type=float,nargs=3,required=False,default=[0,0,0], help="position vector in x y z")
    parser.add_argument('-velocity1', type=float,nargs=3,required=False,default=[0,0,0], help="velocity vector in x y z")

    parser.add_argument('-procedure',type=str, required=False,default="other",choices=["pure","numpy","numba"])
    
    


    parser.add_argument('-M2', type=float,  required=False,default="1",help= "Mass of object")
    parser.add_argument('-R2', type=float, required=False,default="1" ,help="Radius of obj1")
    parser.add_argument('-posvec2', type=float,nargs=3,required=False,default=[1,1.5,1], help="position vector in x y z")
    parser.add_argument('-velocity2', type=float,nargs=3,required=False,default=[0,0,0], help="velocity vector in x y z")
    

    parser.add_argument('-T', type=int,required=False,default= 365*24*3600,help="No of seconds to simulate")
    parser.add_argument('-dt', type=int, required=False,default=60,help="dt time unit")

    parser.add_argument('-o',type=str, help="file path to save output of all frames")
    args = parser.parse_args()
    v = []
    M1,R1,P1,V1 =None, None, None, None
    M2,R2,P2,V2 =None, None, None, None
    
    proc = args.procedure
    M1 = args.M1
    M2 = args.M2

    R1= args.R1
    R2 =args.R2

    P1= args.posvec1
    P2= args.posvec2

    V1 = args.velocity1
    V2 = args.velocity2
    T = args.T
    dt = args.dt
    out_file =args.o

    N = int(T/dt)

    ob1, ob2 = None, None


    #print(V1)
    if(proc == "pure" or proc == "numba" ):
        ob1 = object(m= M1,x= P1[0],y= P1[1], z= P1[2], vx=V1[0],vy=V1[1],vz=V1[2] )
        ob2 = object(m= M2,x= P2[0],y= P2[1], z= P2[2], vx=V2[0],vy=V2[1],vz=V2[2] )
    else:
        ob1 = nobject(m = M1,position=np.array(P1),velocity=np.array(V1))
        ob2 = nobject(m = M2,position=np.array(P2),velocity=np.array(V2))


    frames = np.zeros((N,6))
    time_taken = 0
    
    if(proc =="pure"):
        t1 = time.perf_counter()
        for i in range(N):
            
        # print(i)
            ob1.update_due_ob(dt,ob2)
            ob2.update_due_ob(dt,ob1)

                #Not a good approximation
            frames[i,:3] = ob1.give_pos()
            frames[i,3:] = ob2.give_pos()
        t2 = time.perf_counter()
        time_taken = t2-t1
    
    elif(proc == "numpy"):
        t1 = time.perf_counter()

        frames = ob1.get_frames(ob=ob2,N=N,dt=dt)
        
        t2 = time.perf_counter()
        time_taken = t2-t1
    else:
        t1 = time.perf_counter()

        frames = ob1.get_frames(ob=ob2,N=N,dt=dt)
        
        t2 = time.perf_counter()
        time_taken = t2-t1


    

    print("Time taken by ",proc, time_taken)
    if out_file is not None:
        np.savez(out_file,frames)
    







