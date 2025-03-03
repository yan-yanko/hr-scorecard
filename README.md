# דוח מודל ADAPT לארגונים

אפליקציית Dash להצגת וניתוח ציונים לפי מודל ADAPT לארגונים.

## תכונות

- הצגת ציונים בגרף רדאר (Spider Chart)
- ממשק משתמש אינטואיטיבי בעברית
- אפשרות לעדכון ציונים בזמן אמת
- תצוגה ויזואלית של 5 ממדי המודל:
  - אסטרטגיה וכיוון
  - יכולת הסתגלות
  - תהליכים ומבנה
  - תרבות ולמידה
  - מדדים ותוצאות

## התקנה

1. התקן את התלויות הנדרשות:
```bash
pip install -r requirements.txt
```

2. הפעל את האפליקציה:
```bash
python app.py
```

3. פתח את הדפדפן בכתובת: `http://127.0.0.1:8050`

## פיתוח

### הגדרת סביבת פיתוח

1. צור סביבה וירטואלית:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

2. התקן את התלויות:
```bash
pip install -r requirements.txt
```

### הרצת בדיקות

```bash
pytest tests/
```

## תרומה לפרויקט

1. Fork את המאגר
2. צור ענף חדש (`git checkout -b feature/amazing-feature`)
3. Commit את השינויים (`git commit -m 'הוספת תכונה מדהימה'`)
4. Push לענף (`git push origin feature/amazing-feature`)
5. פתח Pull Request

## רישיון

פרויקט זה מופץ תחת רישיון MIT. ראה קובץ [LICENSE](LICENSE) לפרטים נוספים.

## יצירת קשר

Yan Yanko - [@yan_yanko](https://github.com/yan-yanko)

קישור לפרויקט: [https://github.com/yan-yanko/hr-scorecard](https://github.com/yan-yanko/hr-scorecard) 