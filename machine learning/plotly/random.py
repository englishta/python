import plotly.graph_objs as go
import numpy as np
import plotly.offline as offline

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]
offline.plot(data, filename='data', auto_open=True)



