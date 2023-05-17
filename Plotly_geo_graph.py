import math
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('./data2.csv')
df.head()

def getNumberRangeColor(val):
    for i in range (len(limits)):
        if limits[i][0] <= val <= limits[i][1]:
            return i
    return -1



limits = [(0,10000),(10000,100000),(100000,3000000)]
state = ['Belgium','Bulgaria','Czechia','Denmark','Germany','Estonia','Ireland','Greece','Spain','France','Croatia','Italy','Cyprus','Latvia','Lithuania','Luxembourg','Hungary','Malta','Netherlands','Austria','Poland','Portugal','Romania','Slovenia','Slovakia','Finland','Sweden','Iceland','Norway','Switzerland','United Kingdom']
colors = ["rgba(44, 255, 45, 0.25)","rgba(255, 234, 0, 0.25)","rgba(255, 29, 30, 0.25)"]
cities = []
scale = 250

fig = go.Figure()

for i in range(len(state)):
    fig.add_trace(go.Scattergeo(
        locations = [state[i]],
        locationmode = 'country names',
        text = str(df['2011'][state.index(state[i])]),
        marker = dict(
            size = math.log(df['2011'][state.index(state[i])]/scale, math.e)*5,
            color = colors[getNumberRangeColor(df['2011'][state.index(state[i])])],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = state[i]))



fig.update_layout(
        title_text = 'Number of death on work in 2011',
        showlegend = True,
        geo = dict(
            scope = 'europe',
            landcolor = 'rgb(217, 217, 217)',
        )
    )

fig.show()