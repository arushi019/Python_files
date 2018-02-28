import random
finish=[]
start=[0,0]
fires=[]
walls=[]
env=[]
def init_env():
    for i in range(102):
        env.append([])
        for j in range(102):
            env[i].append(0)
def init_finish():
    x=random.randint(1,101)
    y=random.randint(1,101)
    finish.append(x)
    finish.append(y)
    env[x][y]=1
def init_fires():
    num=random.randint(1,20)
    for i in range(num):
        x=random.randint(1,101)
        y=random.randint(1,101)
        while x==finish[0] and y==finish[1]:
            x=random.randint(1,101)
            y=random.randint(1,101)
        fires.append([x,y])
        env[x][y]=-1
def init_walls():
    num=random.randint(1,20)
    for i in range(num):
        x=random.randint(1,101)
        y=random.randint(1,101)
        while env[x][y]!=0:
            x=random.randint(1,101)
            y=random.randint(1,101)
        walls.append([x,y])
        env[x][y]=-2
init_env()
init_finish()
init_fires()
init_walls()
for i in range(101):
    print(env[i])
