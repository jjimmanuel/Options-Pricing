
import QuantLib as ql
from QuantLib import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


today = Date(7, 1, 2014)
Settings_instance().evaluationDate = today

# The Option

exercise = EuropeanExercise(Date(7, 6, 2014))
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


# Try Changing the Underlying Value

x = [80.0, 90.0, 100.0, 110.0, 120.0]
y = []
for i in x:
    underly.setValue(i)
    y.append(option.NPV())


plt.xlabel("Underlying Price of Security")
plt.ylabel("Option Price")
plt.title("Option Price as a Function of Underlying Security")
plt.plot(x, y, label = "curve 1")



Settings_instance().evaluationDate = Date(7, 2, 2014)
option.NPV()
x = [80.0, 90.0, 100.0, 110.0, 120.0]
y = []
for i in x:
    underly.setValue(i)
    y.append(option.NPV())
plt.plot(x, y, label = "curve 2")

Settings_instance().evaluationDate = Date(7, 3, 2014)
option.NPV()
x = [80.0, 90.0, 100.0, 110.0, 120.0]
y = []
for i in x:
    underly.setValue(i)
    y.append(option.NPV())
plt.plot(x, y, label = "curve 3")

Settings_instance().evaluationDate = Date(7, 4, 2014)
option.NPV()
x = [80.0, 90.0, 100.0, 110.0, 120.0]
y = []
for i in x:
    underly.setValue(i)
    y.append(option.NPV())
plt.plot(x, y, label = "curve 4")

Settings_instance().evaluationDate = Date(7, 5, 2014)
option.NPV()
x = [80.0, 90.0, 100.0, 110.0, 120.0]
y = []
for i in x:
    underly.setValue(i)
    y.append(option.NPV())
plt.plot(x, y, label = "curve 5")

plt.legend()
plt.show()








