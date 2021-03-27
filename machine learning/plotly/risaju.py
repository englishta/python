import plotly.graph_objs as go
import plotly.offline as offline
from math import pi, cos, sin, tan, e

import numpy as np

xx = []
yy = []
A = 1
B = 1
a = 3
b = 4
gu = 0

def deg(kaku):
    return kaku*(pi/180)


def kansuy(t):
    k = deg(t)
    rety = B*sin(b*k)
    return rety

def kansux(t):
    k = deg(t)
    retx = A*sin(a*k+gu)
    return retx

for i in range(0, 361*18):
    shi = i/2
    xx.append(kansux(shi))
    yy.append(kansuy(shi))

trace = go.Scatter(
    x = xx,
    y = yy,
    mode = 'markers'
)

data = [trace]
offline.plot(data, filename='DAta', auto_open=True)
