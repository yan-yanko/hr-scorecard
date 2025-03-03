import dash
from dash import dcc, html
import plotly.graph_objects as go

# יצירת אפליקציה
app = dash.Dash(__name__)

# נתוני דוגמה לציונים של ארגון
dimensions = ["אסטרטגיה וכיוון", "יכולת הסתגלות", "תהליכים ומבנה", "תרבות ולמידה", "מדדים ותוצאות"]
scores = [4, 3, 5, 2, 4]  # ציונים לדוגמה

# גרף רדאר (Spider Chart)
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=scores + [scores[0]],  # סוגרים את המעגל
    theta=dimensions + [dimensions[0]],  # סוגרים את המעגל
    fill='toself',
    name='מצב הארגון'
))
fig.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 5])
    ),
    showlegend=False,
    title="ניתוח מודל ADAPT"
)

# ממשק המשתמש
app.layout = html.Div([
    html.H1("דוח מודל ADAPT לארגונים"),
    dcc.Graph(figure=fig),
    html.P("מלא את הציונים לכל ממד (1-5):"),
    *[
        html.Div([
            html.Label(dim),
            dcc.Input(id=f"input-{dim}", type="number", min=1, max=5, step=1, value=scores[i])
        ]) for i, dim in enumerate(dimensions)
    ],
    html.Button("עדכן", id="update-button"),
])

if __name__ == '__main__':
    app.run_server(debug=True) 