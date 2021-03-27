import plotly.offline as po
import plotly.graph_objs as go
import numpy as np
from math import cos, sin, pi

grid = np.mgrid[0:10, 0:20]
grid_x = grid[0].flatten()
grid_y = grid[1].flatten()
grid_z = grid_x + grid_y
points = np.array(list(zip(grid_x, grid_y, grid_z)))


xs = []
ys = []
zs = []

for i in range(-200, 200):
    for j in range(-200, 200): 
        xs.append(i/100)
        ys.append(j/100)
        zs.append(10/((i/100)**2 + (j/100)**2 + 1))

# traceを作成
trace = go.Scatter3d(
    x=xs,
    y=ys,
    z=zs,
    mode='lines',
    marker=dict(
        color='rgb(100,200,200)',
        size=5,
        opacity=0.8
    )
)
# layoutを作成
layout = go.Layout(
    # デフォルトでは描画領域が狭いのでmarginを0に
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    ),
    # xyz軸のスケールを統一
    scene=dict(aspectmode='cube'),
)
# traceとlayoutからfigureを作成
fig = go.Figure(data=[trace], layout=layout)
# プロット
po.plot(fig, filename='sample-verts', auto_open=True)