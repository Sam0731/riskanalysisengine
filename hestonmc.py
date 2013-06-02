import math
import random
import ltqnorm

def HestonMC(S0, K, r, days_to_maturity, V0, rho, kappa, theta, vol, numPaths):
  dt = 1.0 / 365.0
  path = 0.0

  for i in range(0, numPaths):
    lnSt = math.log(S0)
    lnVt = math.log(V0)
    currentS = S0
    currentV = V0

    for step in range(1, days_to_maturity+1):
      rand1 = 0.0
      while rand1 == 0.0:
        rand1 = random.random()

      rand2 = 0.0
      while rand2 == 0.0:
        rand2 = random.random()

      epsilon = ltqnorm.ltqnorm(rand1)
      epsilons = ltqnorm.ltqnorm(rand2)
      epsilonv = rho * epsilons + math.sqrt(1 - rho**2) * epsilons
      lnSt = lnSt + (r - 0.5 * currentV) * dt + math.sqrt(currentV) * math.sqrt(dt) * epsilons
      currentS = math.exp(lnSt)
      lnVt = lnVt + ((kappa * (theta - currentV) - 0.5 * vol ** 2) * (1 / currentV)) * dt + (vol * (1 / math.sqrt(currentV)) * math.sqrt(dt) * epsilonv)
      currentV = math.exp(lnVt)

    path = path + math.exp(-r * days_to_maturity/365.0) * max(currentS - K, 0)

  return path/numPaths
