Expense Tracker API + Analytics Dashboard

A full-stack expense tracking application built with Flask and SQLite, featuring a RESTful API and an interactive analytics dashboard powered by Chart.js.
Deployed live on Render.
Live Demo
Production URL:
https://expense-tracker-yscz.onrender.com

Features
• Full REST API with complete CRUD functionality
• SQLite database with automated schema creation
• Category-based analytics using SQL aggregation queries
• Interactive Chart.js dashboard for real-time visualisation
• Deployed using Gunicorn on Render
• GitHub-integrated CI-based deployment

Tech Stack
  Backend
  Python
  Flask
  SQLite
  Gunicorn
  Frontend
  HTML
  CSS
  Chart.js

Deployment
  Render

API Endpoints
  Get all expenses
  GET /expenses

  Create expense
  POST /expenses
  
  Update expense
  PUT /expenses/<id>
  
  Delete expense
  DELETE /expenses/<id>
  
  Get category summary
  GET /summary
  
  Get total spending
  GET /total

  Dashboard UI
  GET /dashboard

Local Setup

  Clone the repository:
  
  git clone https://github.com/mustafe10-1/expense-tracker.git
  cd expense-tracker
  
  
  Create virtual environment:
  
  python -m venv venv
  source venv/bin/activate   # Mac/Linux
  venv\Scripts\activate      # Windows
  
  
  Install dependencies:
  
  pip install -r requirements.txt
  
  
  Run the app:
  
  python app.py
  
  
  Visit:
  http://127.0.0.1:5000

Project Structure
expense-tracker/
│
├── app.py
├── expenses.db
├── requirements.txt
├── templates/
│   └── dashboard.html
└── Procfile

Design Decisions

• SQLite chosen for lightweight, file-based persistence
• RESTful architecture for scalability and frontend flexibility
• SQL aggregation used for efficient category summaries
• Chart.js selected for lightweight interactive visualisation
• Gunicorn used in production for WSGI server reliability

Future Improvements

• User authentication and multi-user support
• PostgreSQL migration for production scaling
• Docker containerisation
• Automated testing with pytest
• Pagination for large datasets
