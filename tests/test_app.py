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
    from app import dimensions
    assert dimensions == expected_dimensions

def test_scores_range():
    """בדיקה שהציונים בטווח תקין"""
    from app import scores
    assert all(1 <= score <= 5 for score in scores) 