from automan.api import Problem, Automator
import numpy as np
from object import R,M,G
import matplotlib.pyplot as plt
from math import sqrt


class Orbit2(Problem):
    def get_name(self):
        return 'Orbit2'
    
    def get_commands(self):
        
        p1 = [2*R,0 ,0]
        velocities = [
                [0,sqrt(G*M*0.5/R),0],
                [0,sqrt(0.75*G*M/R),0],
                [0,sqrt(G*M/R),0]
              ]
        cmd_list = []
        python_path ="/usr/bin/python3"
        for i,v in enumerate(velocities):
            out = self.input_path('velocity_'+str(i),'data')
            cmd_list.append(
                (
                 'velocity_'+str(i), python_path+' driver_2.py'+
                 ' -posvec1 '+ str(p1[0]) + " " + str(p1[1])+ " "+ str(p1[2])+
                 ' -velocity1 '+ str(v[0])+" "+str(v[1])+" "+str(v[2])+
                 ' -proc numba'+
                 ' -o '+ out,
                 None   
                )
            )
        return cmd_list
    
    def run(self):
       self.make_output_dir()
class Orbit(Problem):

    def get_name(self):
        return 'Orbit'
    
    def get_commands(self):
        N = 3
        posvec1 = [0 , 0 , 0]
        velocity1 = np.zeros((N,3))
        posvec2 = [1 , 1,  1]
        velocity2 = np.ones((N,3))

        cmd_list = []
        python_path ='/usr/bin/python3'
        

        cmd_list2 =[]
        procedure = ["pure","numpy","numba"]
        dts = [60, 40, 30, 20,10,5]
        p1 = [0 , 0 , 0]
        v1 = np.zeros((N,3))
        p2 = [1 , 1,  1]
        v2 = [0,0,0]
        for proc in procedure:
            for dt in dts:
                out = self.input_path(proc +"_"+ str(dt),'data')
                cmd_list2.append(
                    (proc +"_"+ str(dt),
                     python_path+' driver_2.py'+
                     ' -proc '+proc+
                     ' -dt '+ str(dt)+
                     ' -o '+ out,
                     None
                    
                    )
                )
                

        p3 = [R,2*R,3*R]
        cmd_list3 = [("sample","/usr/bin/python3 driver_2.py -procedure numba  -dt 60 -M1 1 -posvec1"+" "+ str(p3[0])+" "+str(p3[1])+" "+str(p3[2]), None)]

        return cmd_list2
    
    def run(self):
        procedure = ["pure","numpy","numba"]
        y = [[],[],[]]
        dts = [60, 40, 30, 20,10,5]
        self.make_output_dir()
        for i,proc in enumerate(procedure):
            for dt in dts:
                stdout = self.input_path(proc +"_"+ str(dt), 'stdout.txt')
                with open(stdout) as f:
                    data = float(f.read().split()[0])
                    y[i].append(data)

                    #print(proc,dt,f.read().split()[0])
        
        plt.plot(dts,y[0],label="pure")
        plt.plot(dts,y[1],label="numpy")
        plt.plot(dts,y[2],label="numba")
        plt.title("Time taken vs dt ")
        plt.xlabel("dt in sec (1 frame per dt interval)")
        plt.ylabel("Time taken")
        plt.legend(['pure','numpy','numba'])
        plt.savefig(self.output_path('perfomance_compare.png'))
        plt.close()

class Orbit3(Problem):

    def get_name(self):
        return 'Orbit3'
    
    def get_commands(self):
        
        dt = 60
        N = [1,2,4,8,16]
        cmd_list = []
        procedure =['numpy','pure']
        python_path = '/usr/bin/python3'
        for proc in procedure:
            for n in N:
                out = self.input_path(proc+"_"+str(n),'data')
                
                cmd_list.append((
                    proc+"_"+str(n),
                    python_path+' driver_3.py'+
                    ' -N '+str(n)+
                    ' -proc '+proc+
                    ' -dt '+str(dt)+
                    ' -o '+out,
                    None

                ))
        return cmd_list
            

    def run(self):
        self.make_output_dir()
        dt = 200
        N = [1,2,4,8,16]
        cmd_list = []
        procedure =['numpy','pure']
        python_path = '/usr/bin/python3'
        y = [[],[]]

        for i,proc in enumerate(procedure):
            for n in N:
                stdout = self.input_path(proc+"_"+str(n),'stdout.txt')
                with open(stdout) as f:
                    data = float(f.read().split()[0])
                    y[i].append(data)
        
        plt.plot(N,y[0],label="numpy")
        plt.plot(N,y[1],label="pure")
        plt.title("Time taken vs No of  objects")
        plt.xlabel("No of objects")
        plt.ylabel("time taken")
        plt.legend(["numpy","pure"])
        plt.savefig(self.output_path('perfomance_compare_2.png'))
        plt.close()




if __name__ == '__main__':

    automator = Automator(
        simulation_dir = 'outputs',
        output_dir = 'manuscript/figures',
        all_problems = [Orbit3,Orbit2,Orbit]
    )
    automator.run()


