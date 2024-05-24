#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install Flask plotly
from flask import Flask, render_template
import plotly.graph_objs as go

app = Flask(__name__)


social_media_platforms = ['Facebook', 'Twitter', 'Instagram']
followers = [5000, 3000, 8000]

@app.route('/')
def index():
    
    data = [
        go.Bar(
            x=social_media_platforms,
            y=followers,
            marker=dict(color='rgb(26, 118, 255)')
        )
    ]

    layout = go.Layout(
        title='Social Media Followers',
        xaxis=dict(title='Social Media Platform'),
        yaxis=dict(title='Followers Count')
    )

    chart = go.Figure(data=data, layout=layout)

    
    chart_json = chart.to_json()

    return render_template('index.html', chart_json=chart_json)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)


# In[ ]:




