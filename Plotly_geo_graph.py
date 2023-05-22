import math
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('./data.csv')
df.head()

def getNumberRangeColor(val):
    for i in range (len(limits)):
        if limits[i][0] <= val <= limits[i][1]:
            return i
    return -1

def legend_click_callback(event_data):
    # Codice da eseguire quando viene premuta la legenda
    # Puoi accedere alle informazioni sull'evento tramite l'oggetto event_data
    
    # Esempio: Stampa il nome dell'elemento della legenda premuto
    print(event_data)


#Range dei colori e colori dei marker
limits = [(0,10000),(10000,100000),(100000,3000000)]
colors = ["rgba(44, 255, 45, 0.25)","rgba(255, 234, 0, 0.25)","rgba(255, 29, 30, 0.25)"]

#Lista degli stati presenti nel CSV
state = df['country'].to_list()

#Lista degli anni delle rilevazioni presenti nel CSV (.pop(0) elimina il primo campo [country])
years = df.columns.to_list()
years.pop(0)

#Scala usata per ridurre le dimensioni dei marker
scale = 250

#Creo la figura
fig = go.Figure()

for y in range(len(years)):
    year = years[y]
    for i in range(len(state)):
        #inserisco un marker per ogni stato per ogni anno
        fig.add_trace(go.Scattergeo(
            locations = [state[i]],
            locationmode = 'country names',
            text = str(df[year][state.index(state[i])]),
            marker = dict(
                size = math.log(df[year][state.index(state[i])]/scale, math.e)*5,
                color = colors[getNumberRangeColor(df[year][state.index(state[i])])],
                line_color = 'rgb(40,40,40)',
                line_width = 0.5,
                sizemode = 'area'
            ),
            #mostro un solo marker per ogni anno (solo il primo inserito)
            showlegend = True if i == 0 else False,

            #Inserisco il marker nel legend group
            name = year,
            legendgroup = year,
            visible = True if y == 0 else "legendonly"
            ))



#Aggoirno il layout per inserire il titolo, land color e scope della mappa
fig.update_layout(
        title_text = 'Number of work-related death in European Union country per year (2011-2018)',
        geo = dict(
            scope = 'europe',
            landcolor = 'rgb(217, 217, 217)',
            showland = True,
        )
)

# Imposta il clickmode della figura su 'event+select'
fig.update_layout(clickmode="event+select")

# Associa la funzione di callback all'evento 'plotly_legendclick'
#fig.data[0].on_click(print('ok'))

fig.show()