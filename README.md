# 🧠 Text2SQL using Google Gemini Pro API

Convert **natural language questions** into **SQL queries** automatically using **Google Gemini Pro LLM** and retrieve data from an SQLite database — all through an interactive **Streamlit** web app. 🚀

---

## 🌟 Project Overview

This project demonstrates how to:
1. 💬 Take user input in plain English.
2. ⚙️ Convert it into a valid SQL query using **Google Gemini Pro API**.
3. 🗃️ Execute the SQL query on a local **SQLite database**.
4. 📊 Display the database results interactively using **Streamlit**.

---

## 🧩 Tools & Technologies Used

| Tool | Purpose |
|------|----------|
| 🧮 **SQLite 3** | Lightweight local database for storing student records |
| 🎨 **Streamlit** | To create an interactive web UI |
| 🤖 **Google Gemini Pro (gemini-2.5-flash)** | Converts English questions to SQL queries |
| 🔐 **dotenv** | For securely loading API keys from `.env` file |

---

## 🧱 Project Architecture


```
     ┌─────────────────────────────┐
     │     Streamlit Frontend      │
     │ (User inputs English query) │
     └──────────────┬──────────────┘
                    │
                    ▼
         ┌────────────────────┐
         │ Google Gemini Pro  │
         │ (Text → SQL Query) │
         └────────┬───────────┘
                  │
                  ▼
       ┌──────────────────────┐
       │     SQLite DB        │
       │ (Executes SQL query) │
       └─────────┬────────────┘
                 │
                 ▼
     ┌────────────────────────────┐
     │   Streamlit Output View    │
     │ (Displays query & results) │
     └────────────────────────────┘
```

---

## 📂 Project Structure

```

📁 text2sql-gemini
│
├── 📄 app.py                 # Streamlit app for the UI and Gemini integration
├── 📄 sql.py                 # Creates the database, tables, and inserts data
├── 📄 requirements.txt       # Python dependencies
├── 📄 .env                   # Stores API key securely
├── 📄 README.md              # Project documentation
└── 📁 student.db             # Auto-generated SQLite database (after running sql.py)

````

---

## ⚙️ Setup Instructions

Follow these steps to set up and run the project on your local machine.

### 1️⃣ Create a Virtual Environment
```bash
python3 -m venv venv
````

Activate the environment:

**Windows PowerShell**

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

```bash
venv\Scripts\Activate.ps1
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**📦 requirements.txt**

```
streamlit
google-generativeai
python-dotenv
```

---

### 3️⃣ Set Up Environment Variables

Create a file named `.env` in your project root and add:

```
GEMINI_API_KEY='your_api_key_here'
```

🔑 Get your API key from:
👉 [https://aistudio.google.com/app/api-keys](https://aistudio.google.com/app/api-keys)

---

### 4️⃣ Create Database and Sample Data

Run the following to create the `student.db` file and populate it with data:

```bash
python sql.py
```

✅ You should see `student.db` created in your project folder.
It contains a table named **students** with sample student records.

---

### 5️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

🌐 Open your browser and visit:
👉 [http://localhost:8501](http://localhost:8501)

You’ll see the **Text-to-SQL Query App** interface.

---

## 💬 Example Usage

Try these questions in the Streamlit input box:

| Example Question                             | Expected SQL Query                                              |
| -------------------------------------------- | --------------------------------------------------------------- |
| "Which students scored above 90 marks?"      | `SELECT NAME FROM STUDENTS WHERE MARKS > 90;`                   |
| "What is the average score for each class?"  | `SELECT CLASS, AVG(MARKS) FROM STUDENTS GROUP BY CLASS;`        |
| "Who are the top 5 students based on marks?" | `SELECT NAME, MARKS FROM STUDENTS ORDER BY MARKS DESC LIMIT 5;` |

---

## 🧠 Sample Output Snapshots

<img width="528" height="960" alt="image" src="https://github.com/user-attachments/assets/5d05246f-f93f-4341-a7e2-ecb7ad176144" />

<img width="581" height="996" alt="image" src="https://github.com/user-attachments/assets/0330ecdd-64d5-45d8-a030-ff38d8aacf0c" />

---

## 🧰 Deactivate Virtual Environment

When done, deactivate your environment:

```bash
deactivate
```

---

## 🧩 How It Works (Step-by-Step)

1. **User Input**: You type a question in natural language.
2. **Gemini Processing**: The model (`gemini-2.5-flash`) converts your text into a valid SQL query.
3. **SQLite Execution**: The query runs against `student.db`.
4. **Streamlit Output**: The SQL and its results are displayed on the page.

---

## 🧠 Prompt Used for Gemini Model

```text
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENTS and has the following columns - NAME, CLASS, SECTION and MARKS.
Then display the output results clearly, without any parentheses, commas, or tuple formatting.
```

---

## 🧩 Future Enhancements

* Add support for multiple database schemas.
* Implement query validation and error handling.
* Visualize query results (charts, tables).
* Add authentication for API key security.

---
