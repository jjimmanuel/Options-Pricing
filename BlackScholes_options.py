
import QuantLib as ql
from QuantLib import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


today = Date(7, 3, 2014)
Settings_instance().evaluationDate = today

# The Option

exercise = EuropeanExercise(Date(7, 7, 2014))
option = EuropeanOption(PlainVanillaPayoff(Option.Call, 100), exercise)

underly = SimpleQuote(100.00)
rate = SimpleQuote(0.01)
sigma = SimpleQuote(0.2)
date = Actual360()


curve = FlatForward(0, TARGET(), QuoteHandle(rate), date)
volatility = BlackConstantVol(0, TARGET(), QuoteHandle(sigma), date)

curveHandle = YieldTermStructureHandle(curve)
volHandle = BlackVolTermStructureHandle(volatility)

process = BlackScholesProcess(QuoteHandle(underly), curveHandle, volHandle)


engine = AnalyticEuropeanEngine(process)
option.setPricingEngine(engine)

print(option.NPV())

# Try Changing the Underlying Value

x = [80.0, 90.0, 100.0, 110.0, 120.0]
y = []
for i in x:
    underly.setValue(i)
    y.append(option.NPV())

print(y)

plt.xlabel("Underlying Price of Security")
plt.ylabel("Option Price")
plt.title("Option Price as a Function of Underlying Security")
plt.plot(x, y, "bo-")
plt.show()







