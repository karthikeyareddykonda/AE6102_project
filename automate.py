from automan.api import Problem, Automator
import numpy as np
from object import R,M
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
        for i in range(N):
            v2 = [str(velocity2[i][0]), str(velocity2[i][1]), str(velocity2[i][2])]
            out = self.input_path('velocity_'+str(i),'data')
            cmd_list.append(
                ('velocity_'+str(i), python_path+' driver_2.py'+
                  ' -velocity2 '+ v2[0]+' '+v2[1]+' '+ v2[2]+
                  ' -proc other'+
                   ' -o '+ out,
                   None)
            )

        cmd_list2 =[]
        procedure = ["pure","numpy","numba"]
        dts = [60, 40, 30, 20, 10]
        for proc in procedure:
            for dt in dts:
                dt

        p3 = [R,2*R,3*R]
        cmd_list3 = [("sample","/usr/bin/python3 driver_2.py -procedure numba  -dt 60 -M1 1 -posvec1"+" "+ str(p3[0])+" "+str(p3[1])+" "+str(p3[2]), None)]

        return cmd_list3
    
    def run(self):
        self.make_output_dir()

if __name__ == '__main__':

    automator = Automator(
        simulation_dir = 'outputs',
        output_dir = 'manuscript/figures',
        all_problems = [Orbit]
    )
    automator.run()


