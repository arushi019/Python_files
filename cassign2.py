class Point3:
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.x=0.0
        self.y=0.0
        self.z=0.0
p=Point3(1.0,2.0,3.0)
p.x=1.0
p.y=2.0
p.z=3.0
print(p.x,p.z)
def rot_y(q):
    temp=q.x
    q.x=q.z
    q.z=temp
    print(p.x,q.x)
    print(p.z,q.z)
rot_y(p)
