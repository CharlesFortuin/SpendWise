# SpendWise

SpendWise is a personal finance web application built with **Python**, **Flask**, and **SQLite** that helps users manage their income, expenses, and budgets through an intuitive web interface.

The application allows users to record transactions, categorize income and expenses, track budgets, and visualize their financial data, making it easier to understand spending habits and manage personal finances.

---

## Screenshots

### Dashboard

![Dashboard](screenshots/home-chart-table.png)

### Add Transaction

![Add Transaction](screenshots/add-transaction.png)

### Budget Tracking

![Budget Tracking](screenshots/budget-view.png)

### Spending Chart

![Spending Chart](screenshots/home-chart.png)

## Features

### Dashboard
- View current balance, income, expenses, and transactions
- Visualize spending by category with charts
- Track budgets and spending progress

### Transactions
- Add new transactions
- Edit existing transactions
- Delete transactions
- Search transactions by title
- Filter transactions by type

### Budget Management
- Set a budget for each expense category
- Automatically track spending by category
- View remaining budget in real time
- Visual progress bars with colour indicators
- Receive visual feedback when a budget is exceeded

### User Experience
- Navigation between pages
- Active page highlighting
- Flash messages for successful actions
- Clean and responsive interface

---

## Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- Jinja2
- Chart.js
- Git
- GitHub

---

## Project Structure

```text
SpendWise/
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│
├── utils/
│   └── database.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/CharlesFortuin/SpendWise.git
```

Navigate to the project directory:

```bash
cd SpendWise
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Upcoming Features

- Monthly financial reports
- Improved dashboard analytics
- Responsive mobile layout
- User authentication

---

## What I Learned

This project helped me gain practical experience with:

- Building a full-stack web application using Flask
- Designing and querying SQLite databases
- Implementing CRUD operations
- Creating dynamic pages with Jinja templates
- Developing responsive interfaces with HTML, CSS, and JavaScript
- Visualizing data using Chart.js
- Implementing budget tracking and progress calculations
- Organizing development using Git and feature branches

---

## Author

**Charles Fortuin**

GitHub: https://github.com/CharlesFortuin

LinkedIn: https://www.linkedin.com/in/charles-fortuin-470a20415/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BrcymNyXrSMe2cc6cFLD5yg%3D%3D