# MediCare — Pharmacy Management System

A full-stack pharmacy management web application built to simplify and organize common pharmacy operations such as medicine inventory management, customer management, sales processing, billing, authentication, and transaction history.

MediCare combines a responsive frontend with a Flask backend, SQLAlchemy ORM, and SQLite database to provide an end-to-end workflow for managing pharmacy data and transactions.

---

## 📌 Overview

Managing medicines, customers, inventory, and sales manually can become difficult as the amount of data increases.

**MediCare** was built as a practical full-stack application to bring these operations together in a single system.

The application allows users to:

* Manage medicine inventory
* Add and manage customers
* Process medicine sales
* Automatically calculate transaction totals
* Update medicine stock after a sale
* Generate bills
* Generate QR codes for transactions
* View sales history
* Monitor inventory and dashboard statistics
* Authenticate users and protect application access

The main objective of the project was not only to build the user interface, but also to understand how the **frontend, backend, database, authentication, and business logic work together in a complete web application**.

---

## ✨ Features

### 💊 Medicine & Inventory Management

* Add new medicines
* Store medicine name, category, price, stock, and expiry information
* View available medicines in an organized inventory table
* Monitor current stock
* Identify low-stock medicines
* Update inventory information

### 👥 Customer Management

* Add and manage customer information
* Associate customers with sales transactions
* Retrieve customer information during the billing process

### 🛒 Sales Management

* Create new sales transactions
* Select customers and medicines
* Enter required quantities
* Calculate transaction totals
* Store completed transactions
* Automatically update medicine stock after a sale

### 🧾 Billing

* Generate transaction bills dynamically
* Display customer and purchase details
* Display total transaction amount
* Generate bill information for completed sales
* Support print/download workflow depending on the application interface

### 📱 QR Code Generation

* Generate a QR code for completed bills
* Include important transaction information inside the QR code
* Display the generated QR code on the bill

### 📊 Dashboard

* Display important pharmacy statistics
* Show total medicines
* Show total customers
* Provide low-stock information
* Give a quick overview of the current system state

### 📜 Sales History

* Store completed transactions
* View previous sales
* Review transaction information

### 🔐 Authentication

* User login system
* Session-based authentication
* Protected application sections
* Authentication handled using Flask-Login

---

## 🛠️ Tech Stack

### Backend

* **Python**
* **Flask**
* **Flask-SQLAlchemy**
* **Flask-Login**

### Database

* **SQLite**
* **SQLAlchemy ORM**

### Frontend

* **HTML5**
* **CSS3**
* **JavaScript**
* **Bootstrap**
* **Jinja2 Templates**

### Additional Libraries

* **QRCode** — QR code generation
* **Pillow** — image processing used by the QR generation workflow
* **Werkzeug** — utilities used by Flask for web application functionality and security-related operations

---

## 🏗️ Application Architecture

The basic application architecture follows this flow:

```text
┌──────────────────────────────┐
│         Frontend             │
│ HTML + CSS + Bootstrap       │
│ JavaScript + Jinja2          │
└──────────────┬───────────────┘
               │
               │ HTTP Request
               ▼
┌──────────────────────────────┐
│       Flask Backend          │
│ Routes + Business Logic      │
│ Authentication + Processing  │
└──────────────┬───────────────┘
               │
               │ SQLAlchemy ORM
               ▼
┌──────────────────────────────┐
│       SQLite Database        │
│ Users                        │
│ Medicines                    │
│ Customers                    │
│ Sales                        │
│ Sale Items                   │
└──────────────┬───────────────┘
               │
               │ Query Result
               ▼
┌──────────────────────────────┐
│        Flask Backend         │
└──────────────┬───────────────┘
               │
               │ Rendered Response
               ▼
┌──────────────────────────────┐
│          Frontend            │
│ Updated data shown to user   │
└──────────────────────────────┘
```

---

## 🔄 Example: Sales Workflow

One of the main workflows in MediCare is processing a sale.

```text
User selects customer
        ↓
User selects medicine
        ↓
User enters quantity
        ↓
Flask receives the request
        ↓
Backend validates and processes the data
        ↓
Transaction total is calculated
        ↓
Sale is stored in database
        ↓
Sale items are stored
        ↓
Medicine stock is updated
        ↓
Bill is generated
        ↓
QR code is generated
        ↓
Updated result is displayed to user
```

This demonstrates how the different layers of the application interact rather than operating as isolated pages.

---

## 🗄️ Database Design

The application uses **SQLite** as the database and **SQLAlchemy** as the ORM.

The main entities include:

```text
User
 │
 └── Authentication / Application Access

Medicine
 │
 └── Stores medicine and inventory information

Customer
 │
 └── Stores customer information

Sale
 │
 ├── Customer
 └── Sale Items

SaleItem
 │
 └── Connects individual medicines with a sale
```

The database layer allows the application to persist data and retrieve it whenever required.

---

## 🧩 Project Structure

A simplified structure of the project is:

```text
medicare-pharmacy-management-system/
│
├── app.py
│
├── models.py
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── inventory.html
│   ├── customers.html
│   ├── sales.html
│   └── bill.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── screenshots/
    ├── dashboard.png
    ├── inventory.png
    ├── sales.png
    └── bill.png
```

> The exact structure may vary depending on the current version of the project.

---

## ⚙️ How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/medicare-pharmacy-management-system.git
```

Move into the project directory:

```bash
cd medicare-pharmacy-management-system
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

The application should then be available at:

```text
http://127.0.0.1:5000/
```

---

## 📦 Requirements

Example `requirements.txt`:

```text
Flask
Flask-SQLAlchemy
Flask-Login
qrcode
Pillow
Werkzeug
```

Use the exact versions from your working project environment when committing your final `requirements.txt`.

---

## 🔐 Security & Configuration

Sensitive information should not be hard-coded into the repository.

For example, do not commit:

```text
.env
secret keys
passwords
personal credentials
```

Use environment variables for secrets and add sensitive files to `.gitignore`.

Example:

```text
.env
venv/
__pycache__/
*.pyc
*.db
```

> If your SQLite database is intentionally included for demonstration purposes, remove any sensitive or real-world personal data first.

---

## 🖼️ Screenshots

Add screenshots of the main parts of the application here.

### Dashboard

![MediCare Dashboard](screenshots/dashboard.png)

### Inventory Management

![Medicine Inventory](screenshots/inventory.png)

### Sales Module

![Sales Module](screenshots/sales.png)

### Generated Bill

![Generated Bill](screenshots/bill.png)

---

## 🧠 Key Backend Concepts Implemented

This project gave me practical experience with:

* Flask routing
* Request handling
* Server-side rendering
* Jinja2 templates
* CRUD-style operations
* ORM-based database interaction
* SQLAlchemy models and relationships
* Authentication and session management
* Business logic implementation
* Inventory updates after transactions
* Dynamic bill generation
* QR code generation
* Database persistence
* Connecting frontend interactions with backend operations

---

## 💡 What I Learned

Building MediCare helped me understand how different parts of a full-stack application work together.

Some of the key concepts I practiced were:

### Backend Development

Building Flask routes and implementing the server-side logic required for different application workflows.

### Database Management

Designing models and using SQLAlchemy to communicate with SQLite instead of storing application data only on the frontend.

### Business Logic

Implementing real application rules, such as calculating transaction totals and updating medicine stock after a successful sale.

### Authentication

Implementing login and session management using Flask-Login.

### Frontend Integration

Connecting Flask backend responses to dynamic Jinja templates and creating user-facing interfaces for different modules.

### Third-Party Integration

Integrating QR-code generation into the billing workflow.

---

## 🚀 Future Improvements

Possible improvements for future versions include:

* REST API integration
* Role-based access control
* Advanced sales analytics
* Medicine expiry notifications
* Low-stock email notifications
* Search and filtering improvements
* Exporting sales reports
* PostgreSQL/MySQL support for larger deployments
* Automated testing
* Docker deployment
* Cloud deployment
* Improved responsive design

---

## 🎥 Project Demo

A complete project demonstration is available on my LinkedIn:

**LinkedIn:** [Add LinkedIn Post Link]

The demo covers:

* Application interface
* Inventory management
* Sales processing
* Billing
* QR-code generation
* Dashboard
* Sales history
* Technical implementation

---

## 👨‍💻 Author

**Sahil Desai**

B.Tech — Artificial Intelligence & Data Science

* LinkedIn: [Add LinkedIn URL]
* GitHub: [Add GitHub URL]
* LeetCode: [Add LeetCode URL]

---

## ⭐ Project Highlights

**MediCare** demonstrates an end-to-end full-stack workflow:

```text
Frontend
   ↓
Flask Backend
   ↓
Business Logic
   ↓
SQLAlchemy ORM
   ↓
SQLite Database
   ↓
Transaction Processing
   ↓
Billing + QR Generation
   ↓
Updated Frontend
```

The project was built to gain practical experience in developing a complete web application and understanding how frontend, backend, database, authentication, and business logic integrate into a single system.

---

## 📄 License

This project was created for educational and portfolio purposes.

Add a specific open-source license such as MIT only if you want others to reuse and modify the project under those terms.
