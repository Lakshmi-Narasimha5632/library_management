# Library Management System

A Django library management system with a dashboard, book catalogue, book profiles, and complete book CRUD actions.

## Run locally

```powershell
"C:/Program Files/Python313/python.exe" -m pip install -r requirements.txt
"C:/Program Files/Python313/python.exe" manage.py migrate
"C:/Program Files/Python313/python.exe" manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser.

## Features

- Dashboard with catalogue stats and recently added books
- Add, edit, view, and delete books
- Optional cover-image upload with local media storage
- SQLite database through Django migrations
- Responsive Django template UI with no external frontend dependency
