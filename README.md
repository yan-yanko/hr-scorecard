# דוח מודל ADAPT לארגונים

מערכת web להערכה וניתוח ארגוני לפי מודל ADAPT. המערכת מאפשרת לארגונים ליצור ולשמור דוחות הערכה ולעקוב אחר התקדמותם.

## גישה למערכת

האפליקציה זמינה בכתובת: [https://hr-scorecard.onrender.com](https://hr-scorecard.onrender.com)

## תכונות

- הצגת ציונים בגרף רדאר (Spider Chart)
- ממשק משתמש אינטואיטיבי בעברית
- שמירת נתונים לכל ארגון
- אפשרות לטעינת נתונים קיימים
- תצוגה ויזואלית של 5 ממדי המודל:
  - אסטרטגיה וכיוון
  - יכולת הסתגלות
  - תהליכים ומבנה
  - תרבות ולמידה
  - מדדים ותוצאות

## שימוש במערכת

1. היכנס למערכת בכתובת: [https://hr-scorecard.onrender.com](https://hr-scorecard.onrender.com)
2. הזן את שם הארגון שלך
3. מלא את הציונים לכל אחד מהממדים (בסולם 1-5)
4. לחץ על "שמור ועדכן" כדי לשמור את הנתונים
5. בביקור הבא, הזן את שם הארגון ולחץ על "טען נתונים" כדי לראות את הדוח הקודם

## פיתוח מקומי

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

3. הפעל את השרת המקומי:
```bash
python app.py
```

4. פתח את הדפדפן בכתובת: `http://127.0.0.1:8050`

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