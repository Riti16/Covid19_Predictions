
# coding: utf-8

# In[1]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import send_file
import dash_table as dat 
import pandas as pd
import plotly.graph_objs as go
import datetime as dt
import io
import numpy as np

print("Executing code")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(external_stylesheets=external_stylesheets)
server = app.server

app.config['suppress_callback_exceptions']=True


# In[2]:


filepath = r'total_cases_data.csv'
st = pd.read_csv(filepath)


# In[3]:


st=st.loc[:, 'Date':'human_date']
st


# In[4]:


filepath = r'predicted_data.csv'
st2 = pd.read_csv(filepath)


# In[5]:


st2


# In[6]:


import plotly.graph_objects as go
import numpy as np
import plotly.express as px

random_x = st['human_date']
random_y = st['Total'] 

random_x2 = st2['human_date']
random_y2 = st2['Total'] 

fig = go.Figure()

fig.add_trace(go.Scatter(x=random_x, y=random_y, marker_color='rgb(118,002,025)',
                    mode='lines+markers',name='actual'))

fig.add_trace(go.Bar(x=random_x2, y=random_y2,name='predicted', marker_color='rgb(88,202,325)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6))

#fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
#                  marker_line_width=1.5, opacity=0.6)
fig.update_layout(title_text='Covid-19 India Predictions', height=400, width=1000, title_font=dict(size=32),hoverlabel_align = 'left')

#fig = px.bar(st2, x='Date', y='Total')

#fig.add_trace(go.Scatter(x=random_x2, y=random_y2,
#                    mode='lines+markers',name='predicted',line=dict(color='firebrick', width=4,dash='dash')))

fig.show()

'''
app.layout = html.Div([
    dcc.Graph(figure=fig),
    html.H2("Accuracy of the prediction is: 99.86%"),
])
'''
app.layout = html.Div([
    html.H3("National Helpline Numbers: +91-11-23978046 | 1800112545 | 1075", style={'color': 'blue', 'fontSize': 14}),
    dcc.Graph(figure=fig),
    html.H2("Accuracy of the prediction is: 99.6%", style={'fontSize': 24}), #change here - paste from accuracy_final
    html.P("* 3 initial cases in Kerala recovered; the above chart shows actual covid numbers from the resumption of cases on March 2nd and predicted covid numbers from March 26th."),
    html.P("* Actual Covid Numbers are taken from Ministry Of Health And Family Welfare Covid Website : https://covidindia.org/"),
    html.P("* The above Coronavirus spread numbers are predicted using log transformations, Exponential Growth and linear regression. The Linear Model is only the best estimate of the Exponential Growth function."),
    html.P("* Possibilities of going further:"),
    html.Ol([
        html.Li([
                  "The Exponential Growth will only fit the epidemic at the beginning. Due to measures such as social distancing and lockdown, the growth might not follow exponential pattern or there could be certain error margin that we could inspect in further study.",
               ] ),
        html.Li(["Also, at some point, healed people will not spread the virus anymore and when (almost) everyone is or has been infected, the growth will stop."])
    ]),
    html.P("NOTE: The exponential growth of Corona Virus outbreak is limited to the first phase of the outbreak since the big limitation of Exponential Growth is that it never stops growing. Later, we'll switch to the next step for this model as the epidemic growth is characterized by increasing growth in the beginning period (Epidemiologists have studied these types of outbreaks and it is well known that the first period of an epidemic follows Exponential Growth), but a decreasing growth at a later stage. For example in the Coronavirus case, this maximum limit would be the total number of people in the world, because when everybody is sick, the growth will necessarily diminish.", style={'color': 'DarkBlue'}),
    html.P("Thanks for visting. The source code is on Github which will be made public soon and pull requests will also be accepted in sometime. Stay tuned:)", style={'color': 'DarkGoldenRod'})
])

if __name__ == '__main__':
    app.run_server(debug=True)