import numpy as np
from matplotlib import pyplot as plt

def traj_planner(p0,pf,v,sample_time=0.002):  
    trajx=[]
    trajy=[]
    trajz=[]
    L=np.sqrt(np.square((pf[0]-p0[0]))+np.square((pf[1]-p0[1]))+np.square((pf[2]-p0[2])))
    Lx = pf[0]-p0[0]
    t_toal=L/v
    N = int(np.floor(t_toal/sample_time))
    dx=(pf[0]-p0[0])/N
    dy=(pf[1]-p0[1])/N
    dz=(pf[2]-p0[2])/N
    x=np.zeros(N+1)
    y=np.zeros(N+1)
    z=np.zeros(N+1)
    x[0]=p0[0]
    y[0]=p0[1]
    z[0]=p0[2]
    for i in range(N):
        x[i+1]=x[i]+dx
        y[i+1]=y[i]+dy
        z[i+1]= 0.05* np.sin((i/N*Lx)*25) #步长25cm，5步走1米
        # print(t_toal)
        # print(z[i+1])

        trajx.append(x[i+1])
        trajy.append(y[i+1])
        trajz.append(z[i+1])

        traj = [trajx,trajy,trajz]
    return traj  #traj[0][1]  0:x轴  0:第一个时刻点


if __name__ =="__main__":
    p0=[0,0,0.2]
    pf=[2,0,0.2]
    v=1
    sample_time=0.002
    traj =  traj_planner(p0,pf,v,sample_time=sample_time)

    # print(traj)

    fig = plt.figure(figsize=(6,4))
    # plt.plot(np.transpose(traj[0][:]),np.transpose(traj[2][:]),label='sin')
    # print(np.size(np.transpose(traj[0][:])))
    # print(np.size(np.transpose(traj[2][:])))
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('z')
    plt.plot(range(len(np.transpose(traj[0][:]))),np.transpose(traj[0][:]),label='x_traj')
    plt.show()
    filename = 'sin.png'
    plt.savefig(filename)
    plt.clf()