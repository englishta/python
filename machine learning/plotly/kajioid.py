import plotly.graph_objs as go
import plotly.offline as offline
from math import pi, cos, sin, tan

import numpy as np

xx = []
yy = []

def deg(kaku):
    return kaku*(pi/180)


def kansuy(t):
    a = 3
    t = deg(t)
    rety = a*(1+cos(t))*sin(t) 
    return rety

def kansux(t):
    a = 3
    t = deg(t)
    ret = a*(1+cos(t))*cos(t)
    return ret

for i in range(0, 361):
    xx.append(kansux(i))
    yy.append(kansuy(i))

trace = go.Scatter(
    x = xx,
    y = yy,
    mode = 'markers'
)

data = [trace]
offline.plot(data, filename='DAta', auto_open=True)