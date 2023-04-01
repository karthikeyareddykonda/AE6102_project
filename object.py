
G = 6.67*1e-11
def gravity(m1,m2,x1,y1,z1,x2,y2,z2):

    #  resolved gravity ?
    
    r = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
    C = G*m1*m2/(r**3)
    fx = C*(x1-x2)
    fy = C*(y1-y2)
    fz = C*(z1-z2)

    return fx,fy,fz



class object:

    x,y,z,vx,vy,vz = 0,0,0,0,0,0
    m = 0

    def __init__(self,m =1 ,x=0, y=0, z=0,vx=0,vy=0,vz=0) :
        
        self.m = m
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz


    def update(dt,ax,ay,az):

        vx = vx + ax*dt
        vy = vy + ay*dt
        vz = vz + az*dt
        
        # Can use complex methods
        # ut + (1/2)a t*t
        # 
        x = x + vx*dt
        y = y + vy*dt
        z = z + vz*dt



