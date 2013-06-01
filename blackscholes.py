import math

# The cumulative normal distribution function
def cnd(x):
  A1 =  0.31938153
  A2 = -0.356563782
  A3 =  1.781477937
  A4 = -1.821255978
  A5 =  1.330274429

  l = abs(x)
  k = 1 / (1 + 0.2316419 * l)
  cnd = 1 - 1 / math.sqrt(2 * math.pi) * math.exp(-l ** 2 / 2) * (A1 * k + A2 * k ** 2 + A3 * k ** 3 + A4 * k ** 4 + A5 * k ** 5)
  
  if x < 0:
    cnd = 1 - cnd

  return cnd

def BlackScholes(CallPutFlag, S, x, T, r, v):
  d1 = (math.log(S / x) + (r - v ** 2 / 2) * T) / (v * math.sqrt(T))
  d2 = d1 - v * math.sqrt(T)

  if CallPutFlag == "c":
     return S * cnd(d1) - x * math.exp(-r * T) * cnd(d2)
  elif CallPutFlag == "p":
     return x * math.exp(-r * T) * cnd(-d2) - S * cnd(-d1)
    
#print BlackScholes('c', 2.8, 2.9, 0.83333333, 0.01, 0.2)

