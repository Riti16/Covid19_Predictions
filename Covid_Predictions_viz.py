
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
fig.update_layout(title_text='Covid-19 India Predictions', height=650, width=1300, title_font=dict(size=32),hoverlabel_align = 'left')

#fig = px.bar(st2, x='Date', y='Total')

#fig.add_trace(go.Scatter(x=random_x2, y=random_y2,
#                    mode='lines+markers',name='predicted',line=dict(color='firebrick', width=4,dash='dash')))

fig.show()


# In[ ]:


app.layout = html.Div([
    dcc.Graph(figure=fig),
    html.H2("Accuracy of the prediction is: 99.86%"),
])

if __name__ == '__main__':
    app.run_server(debug=True)