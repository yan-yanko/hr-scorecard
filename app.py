import dash
from dash import dcc, html, Input, Output, State, callback
import plotly.graph_objects as go
import json
from pathlib import Path
import os

# יצירת אפליקציה
app = dash.Dash(__name__)
server = app.server  # נדרש עבור Heroku

# יצירת תיקיית data אם לא קיימת
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# נתוני דוגמה לציונים של ארגון
dimensions = ["אסטרטגיה וכיוון", "יכולת הסתגלות", "תהליכים ומבנה", "תרבות ולמידה", "מדדים ותוצאות"]
default_scores = [4, 3, 5, 2, 4]

def create_radar_chart(scores, org_name="הארגון שלי"):
    """יצירת גרף רדאר"""
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=scores + [scores[0]],
        theta=dimensions + [dimensions[0]],
        fill='toself',
        name=org_name
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 5])
        ),
        showlegend=True,
        title=f"ניתוח מודל ADAPT - {org_name}"
    )
    return fig

def save_scores(org_name, scores):
    """שמירת ציונים לקובץ"""
    filename = data_dir / f"{org_name}.json"
    data = {
        "org_name": org_name,
        "scores": scores,
        "dimensions": dimensions
    }
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_scores(org_name):
    """טעינת ציונים מקובץ"""
    filename = data_dir / f"{org_name}.json"
    if filename.exists():
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data["scores"]
    return default_scores

# ממשק המשתמש
app.layout = html.Div([
    html.H1("דוח מודל ADAPT לארגונים", style={'textAlign': 'center', 'direction': 'rtl'}),
    
    # טופס הזנת פרטים
    html.Div([
        html.Label("שם הארגון:", style={'direction': 'rtl'}),
        dcc.Input(id='org-name', type='text', placeholder='הכנס שם ארגון...', style={'margin': '10px', 'direction': 'rtl'}),
        html.Button('טען נתונים', id='load-btn', style={'margin': '10px'}),
    ], style={'textAlign': 'center', 'margin': '20px'}),
    
    # גרף
    dcc.Graph(id='radar-chart'),
    
    # טופס הזנת ציונים
    html.Div([
        html.H3("עדכון ציונים", style={'textAlign': 'center', 'direction': 'rtl'}),
        html.P("מלא את הציונים לכל ממד (1-5):", style={'textAlign': 'center', 'direction': 'rtl'}),
        *[
            html.Div([
                html.Label(dim, style={'direction': 'rtl'}),
                dcc.Input(
                    id=f"input-{i}",
                    type="number",
                    min=1,
                    max=5,
                    step=1,
                    value=default_scores[i],
                    style={'margin': '10px'}
                )
            ], style={'margin': '10px', 'textAlign': 'center'}) 
            for i, dim in enumerate(dimensions)
        ],
        html.Button("שמור ועדכן", id="save-btn", style={'margin': '20px'})
    ], style={'border': '1px solid #ddd', 'padding': '20px', 'margin': '20px', 'borderRadius': '5px'}),
    
    # הודעות למשתמש
    html.Div(id='message-area', style={'textAlign': 'center', 'margin': '20px', 'direction': 'rtl'})
])

@callback(
    [Output('radar-chart', 'figure'),
     Output('message-area', 'children')],
    [Input('save-btn', 'n_clicks'),
     Input('load-btn', 'n_clicks')],
    [State('org-name', 'value')] +
    [State(f'input-{i}', 'value') for i in range(len(dimensions))],
    prevent_initial_call=True
)
def update_chart(save_clicks, load_clicks, org_name, *scores):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if not org_name:
        return dash.no_update, "נא להזין שם ארגון"
    
    if button_id == 'save-btn':
        if any(score is None for score in scores):
            return dash.no_update, "נא להזין ציונים תקינים (1-5)"
        scores_list = list(scores)
        save_scores(org_name, scores_list)
        return create_radar_chart(scores_list, org_name), "הנתונים נשמרו בהצלחה"
    
    elif button_id == 'load-btn':
        try:
            loaded_scores = load_scores(org_name)
            return create_radar_chart(loaded_scores, org_name), "הנתונים נטענו בהצלחה"
        except:
            return dash.no_update, "לא נמצאו נתונים לארגון זה"

if __name__ == '__main__':
    app.run_server(debug=True) 