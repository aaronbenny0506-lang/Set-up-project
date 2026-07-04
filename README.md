# Basic Flask App

A minimal Flask web application created as a starter project for setting up
a well-structured GitHub repository.

## 🗂️ Project Structure

```
├── app.py               # Main Flask application (routes)
├── requirements.txt      # Python dependencies
├── templates/
│   ├── index.html        # Homepage
│   └── about.html        # About page
├── static/
│   └── style.css         # Stylesheet
└── README.md              # This file
```

## 🚀 Setup & Run Locally

1. **Install Python** (3.8+) if you don't already have it.

2. **Clone or download this repository**, then open a terminal in the
   project folder.

3. **(Optional but recommended) create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the app:**
   ```bash
   python app.py
   ```

6. Open your browser and go to `http://127.0.0.1:5000`

## ✨ Features

- Two routes: Home (`/`) and About (`/about`)
- Uses Flask's Jinja2 templating to render dynamic content (e.g. current year)
- Basic CSS styling served from the `static/` folder
