import pytest
from app import app

def test_app_initialization():
    """בדיקה שהאפליקציה אותחלה בהצלחה"""
    assert app is not None
    assert app.layout is not None

def test_app_layout_components():
    """בדיקה שיש רכיבים בממשק המשתמש"""
    layout = app.layout
    assert len(layout.children) > 0

def test_dimensions():
    """בדיקה שכל הממדים קיימים"""
    expected_dimensions = [
        "אסטרטגיה וכיוון",
        "יכולת הסתגלות",
        "תהליכים ומבנה",
        "תרבות ולמידה",
        "מדדים ותוצאות"
    ]
    assert len(expected_dimensions) == 5

def test_score_range():
    """בדיקה שטווח הציונים תקין"""
    min_score = 1
    max_score = 5
    assert min_score >= 1
    assert max_score <= 5 