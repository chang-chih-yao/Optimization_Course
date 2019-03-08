import numpy as np

# readme -> https://hackmd.io/s/HJgboGyAz

x = np.array([1, 1.6, 3, 4.1, 5.2, 5.9, 6.8, 8.1, 8.7, 9.2, 9.9])
y = np.array([27, 32.5, 30, 37.3, 36.4, 32.4, 28.5, 30, 34.1, 39, 36])
print("x:",x)
print("y:",y)

from scipy import optimize

def func(t, a, b, c, d, e, f, g):
    return a * np.cos(b * (t)) + c * t**2 + d * t + e + f * t**3 + g * t**4

def rsq_poly(p):
    yfit = np.polyval(p, x)
    yresid = y - yfit
    SSresid = sum(pow(yresid,2))
    SStotal = len(y) * np.var(y)
    rsq = 1 - SSresid/SStotal
    rsq = round(rsq, 5)
    return str(rsq)

def rsq_other(p):
    yfit = func(x, p[0], p[1], p[2], p[3], p[4], p[5], p[6])
    print(yfit)
    print(y)
    yresid = y - yfit
    SSresid = sum(pow(yresid,2))
    SStotal = len(y) * np.var(y)
    rsq = 1 - SSresid/SStotal
    rsq = round(rsq, 5)
    return str(rsq)


p1 = np.polyfit(x,y,1)
p2 = np.polyfit(x,y,2)
p3 = np.polyfit(x,y,3)
p4 = np.polyfit(x,y,4)
p5 = np.polyfit(x,y,5)
p6 = np.polyfit(x,y,6)
p7 = np.polyfit(x,y,7)
p8 = np.polyfit(x,y,8)
print("coefficients of linear regresstion equation :",p1)
print("coefficients of quadratic regresstion equation :",p2)

par, par_convariance = optimize.curve_fit(func, x, y)
print("func params:", par)

import matplotlib.pyplot as plt
plt.figure(1)
plt.title("Polynomial regression")
plt.plot(x,y,'o')
xp = np.linspace(0.5, 10, 500)  # to let the graph smoother
plt.plot(xp,np.polyval(p1,xp), label='Order:1'+', rsq:'+rsq_poly(p1))
plt.plot(xp,np.polyval(p2,xp), label='Order:2'+', rsq:'+rsq_poly(p2))
plt.plot(xp,np.polyval(p3,xp), label='Order:3'+', rsq:'+rsq_poly(p3))
plt.plot(xp,np.polyval(p4,xp), label='Order:4'+', rsq:'+rsq_poly(p4))
plt.plot(xp,np.polyval(p5,xp), label='Order:5'+', rsq:'+rsq_poly(p5))
plt.plot(xp,np.polyval(p6,xp), label='Order:6'+', rsq:'+rsq_poly(p6))
plt.plot(xp,np.polyval(p7,xp), label='Order:7'+', rsq:'+rsq_poly(p7))
plt.plot(xp,np.polyval(p8,xp), label='Order:8'+', rsq:'+rsq_poly(p8))
plt.plot(xp,func(xp, par[0], par[1], par[2], par[3], par[4], par[5], par[6]), 'c-', label='Cos(x)+poly'+', rsq:'+rsq_other(par))
plt.legend()
plt.show()



