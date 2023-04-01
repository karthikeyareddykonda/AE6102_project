from object import object, R, M
import numpy as np
import time
if __name__ == "__main__":

    '''
    options
    Display while simulation being run ? ---- can show the difference 
    in simulation speeds of differetn optimizations
    Display after simulation done for limited time.. Can Either do it in 
    a fixed simulation time, or real time

    scale ?   
    No of objects ?
    Size of interval simulations ?

    What to simulate ? Simulate the questions for which answers are solved by 
    simulations... :) 


    '''
    x, y, z = 2*R, 2*R, 2*R
    vx, vy, vz = 0, 0, 0

    ob = object(x=x, y=y, z=z, vx=vx, vy=vy, vz=vz)
    earth = object(m=M)

    T = 365*24*3600    # The time to simulate in seconds ?
    N = int(T/60)       # No of frames

    dt = T/N

    frames = np.zeros((N, 3))

    t1 = time.perf_counter()

    for i in range(N):

        ob.update_due_ob(dt, earth)
        frames[i, :] = ob.give_pos()

    t2 = time.perf_counter()

    print("Time taken to compute: ", t2-t1)
