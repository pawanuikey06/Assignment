# Flask Application

Welcome to the **Flask Application**! This application demonstrates a simple and functional web server using Python's Flask framework. Follow the instructions below to set up and run the application.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.+**: [Download Python](https://www.python.org/downloads/)
- **Pip**: Python package manager (comes with Python)
- **Virtualenv** (optional): For creating a virtual environment
- **MySQL Server**: [Download MySQL](https://dev.mysql.com/downloads/installer/)
- **Git**: [Download Git](https://git-scm.com/downloads)

## 📦 Setup Instructions

1. **Clone the Repository**

   Clone the project to your local machine:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo


2. **Database Setup**
    You need a MySQL database for this Flask app. Follow the steps 
     below to set up the database and populate it with sample data

     *Database Schema*

      The application interacts with a MySQL database. Below is the 
      schema for the users table.

    ```bash
     CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    role VARCHAR(50) NOT NULL
     ) ;

     
    

    **Configure DataBase Connection**
    ```bash
     db_config = {
    'host': 'localhost',
    'user': 'root',  
    'password': 'password',  
    'database': 'your_database'  
     }

##  Task 2 

  **SQL Queries**

```bash
  1- INSERT INTO users (name, email, role)
    VALUES
    ('Pawan', 'xyz@gmail.com', 'Software 
      Developer'),

  2 -SELECT id, name, email, role FROM users;

  3- SELECT id, name, email, role FROM users 
    WHERE id = 1;








