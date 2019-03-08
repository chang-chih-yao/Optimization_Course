import math
import numpy as np 
import matplotlib.pyplot as plt

# readme -> https://hackmd.io/s/Sy6A8YX2z

tau=0.382

def F(x):
    return math.pow(x,4)*math.exp(-x)

def G(x,y):
    return math.pow(x,4)+4*math.pow(y,2)-math.pow(x,2)-4*x*y

def G_local_min(l, u, e, label_str):
    k=0       # steps
    x1 = (1-tau)*l+tau*u
    x2 = tau*l+(1-tau)*u
    print("Golden section:")
    print("Interval : [%lf, %lf]" % (l, u))
    
    t = np.array([])
    s = np.array([])
    while((u-l)>e):
        if(F(x1)>F(x2)):
            l=x1
            x1=x2
            x2=tau*l+(1-tau)*u
        else:
            u=x2
            x2=x1
            x1=(1-tau)*l+tau*u
        k+=1
        #print("%d  %lf %lf %lf" % (k,x1,x2,(u-l)) )
        
        t = np.append(t,k)
        s = np.append(s,F(x1))
    plt.plot(t,s,label=label_str)
    
    print("local min:%lf, when x = %lf\n" % (F(x1), x1))
    return x1

def G_local_max(l, u, e, label_str):
    k=0
    x1 = (1-tau)*l+tau*u
    x2 = tau*l+(1-tau)*u
    print("Golden section:")
    print("Interval : [%lf, %lf]" % (l, u))

    t = np.array([])
    s = np.array([])

    while((u-l)>e):
        if(F(x1)>F(x2)):
            u=x2
            x2=x1
            x1=(1-tau)*l+tau*u
        else:
            l=x1
            x1=x2
            x2=tau*l+(1-tau)*u
            
        k+=1
        #print("%d  %lf %lf %lf" % (k,x1,x2,(u-l)) )

        t = np.append(t,k)
        s = np.append(s,F(x1))
    plt.plot(t,s,label=label_str)
    
    print("local max:%lf, when x = %lf\n" % (F(x1), x1))
    return x1

def D_local_min(l, u, e, t, label_str):
    k=0
    x1=(l+u)/2-t
    x2=(l+u)/2+t
    print("Dichotomous:")
    print("Interval : [%lf, %lf]" % (l, u))

    tt = np.array([])
    s = np.array([])

    while((u-l)>e):
        if(F(x1)>F(x2)):
            l=x1
            x1=(l+u)/2-t
            x2=(l+u)/2+t
        else:
            u=x2
            x1=(l+u)/2-t
            x2=(l+u)/2+t
        k+=1

        tt = np.append(tt,k)
        s = np.append(s,F(x1))
    plt.plot(tt,s,label=label_str)
    
    print("local min:%lf, when x = %lf\n" % (F(x1), x1))
    return x1


def D_local_max(l, u, e, t, label_str):
    k=0
    x1=(l+u)/2-t
    x2=(l+u)/2+t
    print("Dichotomous:")
    print("Interval : [%lf, %lf]" % (l, u))

    tt = np.array([])
    s = np.array([])

    while((u-l)>e):
        if(F(x1)>F(x2)):
            u=x2
            x1=(l+u)/2-t
            x2=(l+u)/2+t
        else:
            l=x1
            x1=(l+u)/2-t
            x2=(l+u)/2+t
        k+=1

        tt = np.append(tt,k)
        s = np.append(s,F(x1))
    plt.plot(tt,s,label=label_str)
    
    print("local max:%lf, when x = %lf\n" % (F(x1), x1))
    return x1


def G_local_min_univariate_x(l, u, e, y):
    k=0
    x1 = (1-tau)*l+tau*u
    x2 = tau*l+(1-tau)*u

    while((u-l)>e):
        if(G(x1, y)>G(x2, y)):
            l=x1
            x1=x2
            x2=tau*l+(1-tau)*u
        else:
            u=x2
            x2=x1
            x1=(1-tau)*l+tau*u
        k+=1
    return x1


def G_local_min_univariate_y(l, u, e, x):
    k=0
    x1 = (1-tau)*l+tau*u
    x2 = tau*l+(1-tau)*u

    while((u-l)>e):
        if(G(x, x1)>G(x, x2)):
            l=x1
            x1=x2
            x2=tau*l+(1-tau)*u
        else:
            u=x2
            x2=x1
            x1=(1-tau)*l+tau*u
        k+=1
    return x1


def Univariate(l_x, u_x, l_y, u_y, x, y, e, label_str):
    r=0
    limit=0                     # stop condition
    print("Univariate method:")
    print("Interval : x[%lf, %lf], y[%lf, %lf]"% (l_x, u_x, l_y, u_y))
    print("begin: x=%lf, y=%lf"% (x, y))

    t = np.array([x])
    s = np.array([y])

    while(True):
        r = G_local_min_univariate_x(l_x, u_x, 0.0001, y)
        x=r
        t = np.append(t,x)
        s = np.append(s,y)
        r = G_local_min_univariate_y(l_y, u_y, 0.0001, x)
        limit = r-y
        y=r
        t = np.append(t,x)
        s = np.append(s,y)
        print("x=%lf, y=%lf"% (x, y))
        if(math.fabs(limit)<e):
            print("\nwhen (x:%lf, y:%lf)"%(x,y))
            break
        
    plt.plot(t,s,label=label_str)
    return G(x,y)


def Downhill(xmin, ymin, xmid, ymid, xmax, ymax, e, label_str):
    print("Downhill method")
    print("begin: (x1=%lf, y1=%lf), (x2=%lf, y2=%lf), (x3=%lf, y3=%lf)"% (xmin, ymin, xmid, ymid, xmax, ymax))
    
    # initial const
    a=1
    r=2
    b=0.5

    k=0    # steps

    xa=0
    ya=0
    xr=0
    yr=0
    xe=0
    ye=0
    xc=0
    yc=0
    xp=0
    yp=0

    t = np.array([])
    s = np.array([])

    while(True):
        if(pow(xmax-xmin,2)+pow(ymax-ymin,2)<e):
            break
        
        k+=1
        t = np.append(t,(xmin+xmid+xmax)/3)
        s = np.append(s,(ymin+ymid+ymax)/3)
        
        # sorted 3 points
        arr = [(G(xmin, ymin), xmin, ymin), (G(xmid, ymid), xmid, ymid), (G(xmax, ymax), xmax, ymax)]
        arr = sorted(arr, key=lambda s:s[0])
        xmin=arr[0][1]
        ymin=arr[0][2]
        xmid=arr[1][1]
        ymid=arr[1][2]
        xmax=arr[2][1]
        ymax=arr[2][2]
        # sorted 3 points

        xa=(xmid+xmin)/2
        ya=(ymid+ymin)/2

        xr=xa+a*(xa-xmax)
        yr=ya+a*(ya-ymax)

        if(G(xmin, ymin)>G(xr, yr)):
            xe=xa+r*(xr-xa)
            ye=ya+r*(yr-ya)
            if(G(xr, yr)>G(xe, ye)):
                xmax=xe
                ymax=ye
            else:
                xmax=xr
                ymax=yr
                continue
        else:
            if(G(xmid, ymid)>=G(xr, yr)):
                xmax=xr
                ymax=yr
                continue
            else:
                if(G(xr, yr)>G(xmax, ymax)):
                    xp=xmax
                    yp=ymax
                else:
                    xp=xr
                    yp=yr

                xc=xa+b*(xp-xa)
                yc=ya+b*(yp-ya)

                if(G(xc, yc)>G(xp, yp)):
                    xmax=xmax+(xmin-xmax)/2
                    xmid=xmid+(xmin-xmid)/2
                    continue
                else:
                    xmax=xc
                    ymax=yc
                    continue
    plt.plot(t,s,label=label_str)
    return G(xmin,ymin)




print("1.")
plt.figure(1)
plt.title("find min")
plt.axis([0,30,-1,5])
plt.xlabel('steps', fontsize=14)
plt.ylabel('f(x)', fontsize=14)
G_min=999999
x1 = G_local_min(-1, 2, 0.00001, "Golden[-1, 2]")
x2 = G_local_min(2, 5, 0.00001, "Golden[2, 5]")
x3 = G_local_min(5, 10, 0.00001, "Golden[5, 10]")
D_local_min(-1, 2, 0.00001, 0.000001, "D[-1, 2]")
D_local_min(2, 5, 0.00001, 0.000001, "D[2, 5]")
D_local_min(5, 10, 0.00001, 0.000001, "D[5, 10]")
plt.legend()
plt.show()

if (F(x1)<G_min):
    G_min = F(x1)
    
if (F(x2)<G_min):
    G_min = F(x2)

if (F(x3)<G_min):
    G_min = F(x3)

print("---------final local min:%lf-------------\n\n" % (G_min))
plt.figure(2)
plt.title("find max")
plt.axis([0,30,0,5])
plt.xlabel('steps', fontsize=14)
plt.ylabel('f(x)', fontsize=14)
x4 = G_local_max(-1, 10, 0.0001, "Golden[-1, 10]")
D_local_max(-1, 10, 0.00001, 0.000001, "D[-1, 10]")
plt.legend()
plt.show()

print("---------final local max:%lf-------------\n\n" % (F(x4)))

print("2.")
plt.figure(3)
plt.title("find min")
plt.axis([-4,4,-4,4])
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
print("----------local min:",Univariate(-2,2,-2,2,0,3,0.001, "Univariate_1"), "----------\n")
print("----------local min:",Univariate(-2,2,-2,2,-2,-2,0.001, "Univariate_2"), "----------\n")
plt.legend()
plt.show()

print("3.")
plt.figure(4)
plt.title("find min")
plt.axis([-4,4,-4,4])
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
print("----------local min:",Downhill(2,2,2,3,3,2,0.005, "Downhill_1"), "----------\n")
print("----------local min:",Downhill(-2,-2,-2,-3,-3,-2,0.005, "Downhill_2"), "----------\n")
plt.legend()
plt.show()