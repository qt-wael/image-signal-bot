# Telegram Signal Bot from Chart Images 📊🤖

هذا البوت يقوم بتحليل صور الشموع والمؤشرات الفنية (RSI و Stochastic) تلقائيًا، ويرسل توصية شراء أو بيع مباشرة على تيليجرام.

## ✅ الميزات
- استخراج RSI و Stochastic من الصور.
- تحليل تلقائي وإرسال التوصية.
- سهل التشغيل على Render أو محليًا.

---

## 📦 الملفات المرفقة
- `main.py`: كود البوت.
- `requirements.txt`: المكتبات المطلوبة.
- `README.md`: هذا الملف.

---

## 🚀 خطوات النشر على [Render](https://render.com)

1. **اذهب إلى** [https://render.com](https://render.com) وسجّل دخولك.
2. اضغط على **New Web Service** ثم اختر **Deploy from GitHub**.
3. اربط حسابك GitHub واختر الريبو الذي يحتوي هذا الكود.
4. أدخل الإعدادات التالية:

### إعدادات Render:

- **Name**: `signal-bot`
- **Runtime**: Python 3
- **Build Command**:
  ```bash
  pip install -r requirements.txt
  ```
- **Start Command**:
  ```bash
  python main.py
  ```

---

## ⚠️ ملاحظة
تأكد من أن `pytesseract` و `tesseract-ocr` مثبتين على السيرفر. للأسف Render لا يدعمها مباشرة، لذلك يفضل استخدام [Railway](https://railway.app) أو استضافة محلية.

---

## 🧪 التشغيل محليًا

```bash
git clone https://github.com/USERNAME/image-signal-bot.git
cd image-signal-bot
pip install -r requirements.txt
python main.py
```

---

## 🤖 إعداد التوكن

قم باستبدال هذا السطر في `main.py`:

```python
BOT_TOKEN = "YOUR_TOKEN_HERE"
```

بـ:

```python
BOT_TOKEN = "توكن البوت الخاص بك من BotFather"
```

---

## 📸 تجربة
أرسل صورة فيها مؤشر RSI و Stochastic إلى البوت، وسيقوم بالرد مباشرة بالتحليل.

---

## 🔧 المتطلبات
- Python 3.8+
- Tesseract OCR
- Telegram Bot API Token

