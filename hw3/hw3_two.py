import numpy as np
from sympy import *

# readme -> https://hackmd.io/s/HJgboGyAz

x = np.array([1, 1.6, 3, 4.1, 5.2, 5.9, 6.8, 8.1, 8.7, 9.2, 9.9])
y = np.array([27, 32.5, 30, 37.3, 36.4, 32.4, 28.5, 30, 34.1, 39, 36])
print("x:",x)
print("y:",y)

tau=0.382

def F(lam, A, B, grad_S0, grad_S1):
    return sum(pow((A + lam * grad_S0) * x + (B + lam * grad_S1) - y, 2))

def G_local_min(l, u, e, A, B, grad_S0, grad_S1):
    k=0       # steps
    x1 = (1-tau)*l+tau*u
    x2 = tau*l+(1-tau)*u
    print("Golden section :")
    #print("Interval : [%lf, %lf]" % (l, u))
    
    while((u-l)>e):
        if(F(x1, A, B, grad_S0, grad_S1) > F(x2, A, B, grad_S0, grad_S1)):
            l=x1
            x1=x2
            x2=tau*l+(1-tau)*u
        else:
            u=x2
            x2=x1
            x1=(1-tau)*l+tau*u
        k+=1
        #print("%d  %lf %lf %lf" % (k,x1,x2,(u-l)) )
    
    #print("local min:%lf, when x = %lf\n" % (F(x1), x1))
    return x1




a, b = symbols('a b')
j = 1
k = 1
n = 2
a_ = np.zeros(n+2)
b_ = np.zeros(n+2)
l = np.zeros(n+2)
S0 = np.zeros(n+2)
S1 = np.zeros(n+2)

start_a = np.zeros(n+10)
start_b = np.zeros(n+10)

start_a[k] = 1
start_b[k] = 10

f = sum(pow(a * x + b - y, 2))
S = np.array([diff(f,a), diff(f,b)])
temp0 = lambdify((a, b), S[0])
temp1 = lambdify((a, b), S[1])

flag = 1

while True:
    if flag == 1:
        a_[j] = start_a[k]
        b_[j] = start_b[k]
        
        S0[j] = -temp0(a_[j], b_[j])
        S1[j] = -temp1(a_[j], b_[j])

        flag = 0

    S_len = sqrt(S0[j]**2 + S1[j]**2)
    print("len :", S_len)
    if S_len < 0.01:
        break
    print("S0 :", S0[j])
    print("S1 :", S1[j])
    l[j] = G_local_min(-9999, 9999, 0.00001, a_[j], b_[j], S0[j], S1[j])
    print("lambda :", l[j])
    a_[j+1] = a_[j] + l[j] * S0[j]
    b_[j+1] = b_[j] + l[j] * S1[j]

    print("[a, b] = [%lf, %lf]" % (a_[j+1], b_[j+1]))
    if j < n :
        trans = (pow(temp0(a_[j+1], b_[j+1]),2) + pow(temp1(a_[j+1], b_[j+1]),2)) / ( temp0(a_[j], b_[j])**2 + temp1(a_[j], b_[j])**2 )
        S0[j+1] = -temp0(a_[j+1], b_[j+1]) + trans * S0[j]
        S1[j+1] = -temp1(a_[j+1], b_[j+1]) + trans * S1[j]
        j += 1
    else:
        j = 1
        k += 1
        start_a[k] = a_[n+1]
        start_b[k] = b_[n+1]
        flag = 1
print(a_[j])
print(b_[j])
print(start_a[k])
print(start_b[k])