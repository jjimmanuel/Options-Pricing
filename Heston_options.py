import QuantLib as ql
from QuantLib import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


today = Date(7, 1, 2014)
Settings_instance().evaluationDate = today

exercise = EuropeanExercise(Date(7, 6, 2014))
option = EuropeanOption(PlainVanillaPayoff(Option.Call, 105), exercise)

underly = SimpleQuote(105.00)
rate = SimpleQuote(0.01)
sigma = SimpleQuote(0.2)
date = Actual360()
dividend = 0.0

rf_curve = FlatForward(0, TARGET(), QuoteHandle(rate), date)
rf_curveHandle = YieldTermStructureHandle(rf_curve)

dividend_curve = FlatForward(0, TARGET(), dividend, date)
dividend_curveHandle = YieldTermStructureHandle(dividend_curve)

heston = HestonModel(HestonProcess(rf_curveHandle, dividend_curveHandle, QuoteHandle(underly), 0.04, 0.1, 0.01, 0.05, -0.75))

engine = AnalyticHestonEngine(heston)
option.setPricingEngine(engine)

print(option.NPV())







