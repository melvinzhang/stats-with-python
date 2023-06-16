from statistics import mean, variance, pvariance
from random import gauss

pvars = []
svars = []
for _ in range(1000):
    data = [gauss(mu=0.0, sigma=1.0) for _ in range(20)]
    pvars.append(pvariance(data))
    svars.append(variance(data))

print("Actual variance =", 1.0)
print("Mean pvariance  =", mean(pvars))
print("Mean variance   =", mean(svars))
