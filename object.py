import numpy as np
import numba
G = 6.67*1e-11
R = 6.378e6
M = 5.97e24

def gravity(m1, m2, x1, y1, z1, x2, y2, z2):

    #  resolved gravity ?

    r = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
    C = G*m1*m2/(r**3)
    fx = C*(x1-x2)
    fy = C*(y1-y2)
    fz = C*(z1-z2)

    return -fx, -fy, -fz


def gen_framesp(m1,m2,x1,y1,z1,x2,y2,z2,vx,vy,vz,dt,N,frames):
    
    const = G*m2
    
    for i in range(N):
        r = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
        C = G*m2/(r**3)
        fx = -C*(x1-x2)
        fy = -C*(y1-y2)
        fz = -C*(z1-z2)

        vx += fx*dt
        vy += fy*dt
        vz += fz*dt
        x1 += vx*dt
        y1 += vy*dt
        z1 += vz*dt

       

        frames[i][0] = x1
        frames[i][1] = y1
        frames[i][2] = z1




class object:

    x, y, z, vx, vy, vz = 0, 0, 0, 0, 0, 0
    m = 0
    nfunc = None
    def __init__(self, m=1.0, x=0.0, y=0.0, z=0.0, vx=0.0, vy=0.0, vz=0.0):

        self.m = m
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.nfunc = numba.njit(gen_framesp)
        dummy = np.zeros((10,3))
        self.nfunc(m,1,1,1,1,0,0,0,1,1,1,1,10,dummy)
       # gen_framesp(self.m,ob.m,[self.x,self.y,self.z],[ob.x,ob.y,ob.z],[self.vx,self.vy,self.vz],dt,N,frames)

    def update(self, dt, ax, ay, az):

        self.vx = self.vx + ax*dt
        self.vy = self.vy + ay*dt
        self.vz = self.vz + az*dt

        # Can use complex methods
        # ut + (1/2)a t*t
        #
        self.x = self.x + self.vx*dt
        self.y = self.y + self.vy*dt
        self.z = self.z + self.vz*dt

    def acc(self, ob):

        # calculate acceleration of Ob on the current object

        fx,fy,fz = gravity(self.m, ob.m,self.x, self.y, self.z, ob.x, ob.y, ob.z)

        return (fx/self.m,fy/self.m,fz/self.m)
    
    def update_due_ob(self,dt,ob):

        ax,ay,az = self.acc(ob)
        self.update(dt,ax,ay,az)

    def get_frames(self,ob,N,dt,opt="pure"):
        frames = np.zeros((N,3))
        

        if(opt == "pure"):

            gen_framesp(self.m,ob.m,self.x,self.y,self.z,ob.x,ob.y,ob.z,self.vx,self.vy,self.vz,dt,N,frames)
        else:
            
            self.nfunc(self.m,ob.m,self.x,self.y,self.z,ob.x,ob.y,ob.z,self.vx,self.vy,self.vz,dt,N,frames)
        return frames

    def give_pos(self):

        return (self.x,self.y,self.z)

def gen_frames(m1,m2,p1,p2,v1,dt,N,frames):
    
    const = G*m2
    print("called")
    for i in range(N):
        rel_pos = p2-p1
        acc = (const/(rel_pos@rel_pos.T)**1.5)*rel_pos
        v1 = v1 + acc*dt
        p1 = p1 + v1*dt
        frames[i,:] = p1.T


class nobject:
    pos = np.zeros((3,1))
    vel = np.zeros((3,1))
    m = 1

    def __init__(self,m, position, velocity):

        if(position is not None):
            self.pos = position

        if(velocity is not None):
            self.vel = velocity

        self.m = m 
        ngen_frames = numba.njit()
        #print("From constructor")
        #print("Pos",self.pos)
        #print("vel",self.vel)

    def get_frames(self,ob,N,dt):
        
        frames = np.zeros((N,3))
        gen_frames(self.m,ob.m,self.pos,ob.pos,self.vel,dt,N,frames)
        return frames

    
    def update(self,dt ,acc ):

        self.vel = self.vel + acc*dt
        self.pos = self.pos + self.vel*dt

    def acc(self,ob):
        

        rel_pos = ob.pos-self.pos
        #if(np.sum(rel_pos**2) == 0):
        #    print("division by zero", self.pos, ob.pos)
        #const = (G*ob.m)/((np.sum(rel_pos**2))**1.5)
        const = 1
        return const*rel_pos*0

    def update_due_ob(self,dt,ob):

        #accel = self.acc(ob)
        #self.update(dt=dt,acc=0)
        rel_pos = ob.pos - self.pos

        self.pos = self.pos
       # return None 

    def give_pos(self):

        return self.pos.T
