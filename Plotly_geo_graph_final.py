#######################
#     NEW VERSION     #
#######################

#better and improved, now with animation

import plotly.express as px
import pandas as pd

#Read the CSV file
df = pd.read_csv('./final_data.csv')
df.head()

#Create a new field in the dataframe with the value raise to the power of .7 to reduce the range of value,
#thus making the small bubble visible
df['value_display'] = df['value']**0.7

#Create the scatter geo object
fig = px.scatter_geo(df,
                     locations='iso_alpha',
                     hover_name='country',
                     hover_data={
                         'country':False,
                         'iso_alpha':False,
                         'year':False,
                         'value':True,
                         'value_display':False
                     },
                     size='value_display',
                     animation_frame='year',
                     color='value',
                     color_continuous_scale=px.colors.sequential.Viridis,
                     )

#Customize the scatter geo object layout
fig.update_layout(
        title_text = 'Number of work-related death in European Union country per year (2011-2018)',
        geo = dict(
            scope = 'europe',
            landcolor = 'rgb(217, 217, 217)',
            showland = True,
        )
    )


#Show the scatter object in the browser
fig.show()