from scipy.optimize import minimize
from gurobipy import*

# readme : https://hackmd.io/s/ryhmC_Zy7

def F1(r):
    return -(12*r - pow(r, 3)) * 3.1415


res = minimize(F1, 0, method='powell')
print("1.")
print(res)
print("r =", res.x)
print("h =", (12-res.x*res.x)/res.x)


print("----------------------------------")


print("2.")
m=Model('2.')
f1=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='f1')
f2=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='f2')
f3=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='f3')
f4=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='f4')
f5=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='f5')
f6=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='f6')
f7=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='f7')
f8=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='f8')
f9=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='f9')
m.update()

m.setObjective((f1/11.5)*(f1/11.5) + (f2/92.5)*(f2/92.5) + (f3/44.3)*(f3/44.3) + (f4/98.1)*(f4/98.1) + (f5/20.1)*(f5/20.1) + (f6/6.1)*(f6/6.1) + (f7/45.5)*(f7/45.5) + (f8/31.0)*(f8/31.0) + (f9/44.3)*(f9/44.3) ,GRB.MINIMIZE)
m.addConstr((0.0298*f1 - 0.044*f2 - 0.044*f3 - 4)==0,'c0')
m.addConstr((-0.0138*f3 + 0.0329*f4 + 0.00329*f5 - 0.025*f6 - 0.025*f7 - 33)==0,'c1')
m.addConstr((0.0279*f5 - 0.0619*f7 + 0.0317*f8 - 0.0368*f9 - 31)==0,'c2')
m.optimize()

print('obj:%d'%m.objVal)
for v in m.getVars():
    print('%s:%d'%(v.varName,v.x))


print("----------------------------------")

print("3.")
m=Model('3.')
x1=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='x1')
x2=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='x2')
x3=m.addVar(lb=0,vtype=GRB.CONTINUOUS,name='x3')
m.update()

m.setObjective(5*x1 + 4*x2 -x3 ,GRB.MINIMIZE)
m.addConstr((x1 + 2*x2 -x3)>=1,'cc0')
m.addConstr((2*x1 + x2 + x3)>=4,'cc1')
m.optimize()

print('obj:%d'%m.objVal)
for v in m.getVars():
    print('%s:%d'%(v.varName,v.x))