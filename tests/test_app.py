import pytest
from dash.testing.application_runners import import_app
from dash.testing.composite import DashComposite

def test_app_initialization():
    app = import_app("app")
    assert app is not None
    assert app.layout is not None

def test_app_layout_components():
    app = import_app("app")
    layout = app.layout
    assert len(layout.children) > 0
    assert any(isinstance(child, dict) for child in layout.children) 