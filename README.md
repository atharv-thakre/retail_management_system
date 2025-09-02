# 🏬 Retail Management System (Python + Tkinter + SQLite3)

A **Retail Management System (RMS)** built with **Python Tkinter GUI** and **SQLite3 database**.  
This system works completely **offline & locally**, providing an easy-to-use solution for managing retail operations such as employees, inventory, and billing.

---

## 📂 Project Structure

retail_management_system/ <br>
├── main.py # Entry point (choose Admin / Employee)<br>
├── admin.py # Admin panel (manage inventory, employees, merchants)<br>
├── employee.py # Employee panel (billing system, sales records)<br>
├── support.py # Helper functions and utilities<br>
├── images/ # 24 PNG icons & UI images<br>
├── database/<br>
│ ├── account.db # SQLite3 database (employees, products, merchants, bills)<br>
│ └── raw_inventory.csv # Initial inventory data<br>
└── fonts/ # Custom fonts used in GUI<br>

---

## ✨ Features
✔️ **Admin & Employee login system** (direct login options)  
✔️ **Employee Management** → Add, Remove, Edit employee details  
✔️ **Inventory Management** → Add, Edit, Delete products & update stock  
✔️ **Merchant Management** → Add & manage product suppliers  
✔️ **Billing System** → Generate bills & record transactions  
✔️ **Previous Bills Record** → Access and view past bills  
✔️ **GUI Interface** → User-friendly design with icons, buttons & images  
✔️ **Local Database** → Uses SQLite3 (no external setup needed)  

---


## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
   ```bash
   git clone https://github.com/atharv-thakre/retail_management_system.git
   cd retail_management_system
   ```

### 2️⃣ Create virtual environment (optional but recommended)
- windows
```bash
python -m venv venv
venv\Scripts\activate
```

- mac / linux
```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Run the app
```bash
python -m uvicorn app.main:app --reload
```

---

## 🖥️ Screenshots 
> You can add some screenshots of your GUI here (main menu, billing, admin panel, etc.)

---
   
