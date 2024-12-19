import streamlit as st
import pandas as pd
from faker import Faker
import random
from io import BytesIO

# Initialize Faker
fake = Faker()

# Function to generate financial data
def generate_financial_data(rows):
    data = []
    for _ in range(rows):
        data.append({
            "Account Number": fake.iban(),
            "Account Type": random.choice(["Savings", "Current", "Business"]),
            "Transaction Date": fake.date_this_year(),
            "Transaction Type": random.choice(["Credit", "Debit"]),
            "Amount": round(random.uniform(10, 5000), 2),
            "Currency": random.choice(["USD", "EUR", "INR", "GBP"]),
            "Description": f"Payment for {fake.bs()} to {fake.name()}",
            "Sender Name": fake.name(),
            "Receiver Name": fake.name(),
        })
    return pd.DataFrame(data)

# Function to generate real-estate data
def generate_real_estate_data(rows):
    data = []
    for _ in range(rows):
        data.append({
            "Property ID": fake.uuid4(),
            "Property Type": random.choice(["Apartment", "Villa", "Commercial", "Land"]),
            "Price": round(random.uniform(50000, 1000000), 2),
            "Address": fake.address(),
            "Owner Name": fake.name(),
            "Listed Date": fake.date_this_year(),
            "Description": f"A {random.choice(['spacious', 'modern', 'well-maintained', 'luxurious'])} {random.choice(['3-bedroom', '2-bedroom', 'studio', '4-bedroom'])} {random.choice(['apartment', 'villa', 'office space'])} located in a prime area."
        })
    return pd.DataFrame(data)

# Function to generate Amazon sales data
def generate_amazon_sales_data(rows):
    data = []
    product_names = ["Smartphone", "Laptop", "Headphones", "Washing Machine", "Refrigerator", "LED TV", "Microwave Oven", "Air Conditioner", "Vacuum Cleaner", "Smartwatch", "Playstation", "Computer Chipset"]
    for _ in range(rows):
        data.append({
            "Order ID": fake.uuid4(),
            "Product Name": random.choice(product_names),
            "Category": random.choice(["Electronics", "Clothing", "Books", "Home Appliances"]),
            "Price": round(random.uniform(5, 500), 2),
            "Quantity Sold": random.randint(1, 100),
            "Total Revenue": round(random.uniform(10, 10000), 2),
            "Order Date": fake.date_this_year(),
        })
    return pd.DataFrame(data)

# Function to generate healthcare data
def generate_healthcare_data(rows):
    data = []
    for _ in range(rows):
        data.append({
            "Patient ID": fake.uuid4(),
            "Patient Name": fake.name(),
            "Age": random.randint(1, 100),
            "Gender": random.choice(["Male", "Female", "Other"]),
            "Diagnosis": random.choice(["Diabetes", "Hypertension", "Flu", "COVID-19", "Migraine"]),
            "Admission Date": fake.date_this_year(),
            "Discharge Date": fake.date_this_year(),
            "Bill Amount": round(random.uniform(500, 10000), 2)
        })
    return pd.DataFrame(data)

# Function to generate education data
def generate_education_data(rows):
    data = []
    for _ in range(rows):
        data.append({
            "Student ID": fake.uuid4(),
            "Student Name": fake.name(),
            "Age": random.randint(18, 30),
            "Course": random.choice(["Computer Science", "Mechanical Engineering", "Business Administration", "Psychology"]),
            "Enrollment Date": fake.date_this_year(),
            "Graduation Date": fake.date_this_decade(),
            "GPA": round(random.uniform(2.0, 4.0), 2)
        })
    return pd.DataFrame(data)

# Function to generate e-commerce reviews data
def generate_reviews_data(rows):
    data = []
    for _ in range(rows):
        data.append({
            "Review ID": fake.uuid4(),
            "Product Name": random.choice(["Smartphone", "Laptop", "Headphones", "Washing Machine", "Refrigerator", "LED TV", "Microwave Oven", "Air Conditioner", "Vacuum Cleaner", "Smartwatch", "Playstation", "Computer Chipset"]),
            "Reviewer Name": fake.name(),
            "Rating": random.randint(1, 5),
            "Review Date": fake.date_this_year(),
            "Review Text": fake.sentence(nb_words=15)
        })
    return pd.DataFrame(data)

# Function to generate selected data
def generate_data(data_type, rows):
    if data_type == "Financial Data":
        return generate_financial_data(rows)
    elif data_type == "Real-Estate Data":
        return generate_real_estate_data(rows)
    elif data_type == "Amazon Sales Data":
        return generate_amazon_sales_data(rows)
    elif data_type == "Healthcare Data":
        return generate_healthcare_data(rows)
    elif data_type == "Education Data":
        return generate_education_data(rows)
    elif data_type == "E-Commerce Reviews Data":
        return generate_reviews_data(rows)

# Streamlit UI
st.title("Fake Data Generator")

# Data type selection
data_type = st.selectbox("Select the type of data to generate:", ["Financial Data", "Real-Estate Data", "Amazon Sales Data", "Healthcare Data", "Education Data", "E-Commerce Reviews Data"])

# Number of rows input
rows = st.number_input("Enter the number of rows to generate:", min_value=1000, step=100)

# Generate button
if st.button("Generate Data"):
    df = generate_data(data_type, rows)
    st.write("### Sample Data:")
    st.dataframe(df.head(10))

    # Download button
    buffer = BytesIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)
    st.download_button(
        label="Download Data as CSV",
        data=buffer,
        file_name=f"{data_type.replace(' ', '_')}_fake_data.csv",
        mime="text/csv"
    )
