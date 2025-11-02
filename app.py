from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

import streamlit as st
import sqlite3
import google.generativeai as genai

# Configure Google Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
DATABASE_URL = os.getenv("DATABASE_URL")

# Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-2.5-flash')
    response=model.generate_content([prompt[0],question])
    return response.text

# Function To retrieve query from the database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENTS and has the following columns - NAME, CLASS, SECTION and MARKS 
    Then display the output results clearly, **without any parentheses, commas, or tuple formatting**.
    \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENTS ;
    \nExample 2 - Tell me all the students studying in 10th Grade?, 
    the SQL command will be something like this SELECT * FROM STUDENTS
    where CLASS="10th Grade"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    st.header("The SQL Query is")
    st.subheader(response)
    response=read_sql_query(response,"student.db")
    st.header("The Response is")
    for row in response:
        print(row)
        st.subheader(row)