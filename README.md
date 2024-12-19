# Fake Data Generator with Streamlit

## Overview
The Fake Data Generator is a Streamlit-based application that allows users to generate realistic fake data for various domains. The generated data can be previewed, downloaded as a CSV file, and used for testing, prototyping, or learning purposes. The tool provides several data domains to choose from, ensuring flexibility and ease of use.

---

## Features
- **Data Domains**: Generate fake data for multiple domains:
  1. Financial Data
  2. Real-Estate Data
  3. Amazon Sales Data
  4. Healthcare Data
  5. Educational Data
  6. E-commerce Reviews Data

- **Customization**:
  - Select the domain of data.
  - Specify the number of rows to generate (minimum 1000 rows).

- **Data Export**:
  - Preview a sample of the generated data in the Streamlit UI.
  - Download the complete dataset as a CSV file.

---

## Requirements

### Python Packages
Install the required dependencies using pip:

```bash
pip install streamlit faker pandas
```

### Additional Tools
- **Python 3.7 or higher**
- **A Web Browser** to run and view the Streamlit app.

---

## Installation and Setup

1. Clone or download the repository:
   ```bash
   git clone https://github.com/your-repository/fakedata-generator.git
   cd fakedata-generator
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open the URL displayed in the terminal (default is `http://localhost:8501`) in your web browser.

---

## How to Use

1. Launch the application by running `streamlit run app.py`.
2. Select the type of data to generate from the dropdown menu.
3. Specify the number of rows to generate (minimum of 1000 rows).
4. Click the "Generate Data" button.
5. Preview the sample data displayed below.
6. Use the "Download Data as CSV" button to download the full dataset.

---

## Data Domains

### 1. Financial Data
- **Fields**: Account Number, Account Type, Transaction Date, Transaction Type, Amount, Currency, Description, Sender Name, Receiver Name.
- **Examples**:
  - Description: "Payment for strategic initiatives to John Doe."

### 2. Real-Estate Data
- **Fields**: Property ID, Property Type, Price, Address, Owner Name, Listed Date, Description.
- **Examples**:
  - Description: "A spacious 3-bedroom apartment located in a prime area."

### 3. Amazon Sales Data
- **Fields**: Order ID, Product Name, Category, Price, Quantity Sold, Total Revenue, Order Date.
- **Examples**:
  - Product Names: "Smartphone, Laptop, Refrigerator, LED TV."

### 4. Healthcare Data
- **Fields**: Patient ID, Patient Name, Age, Gender, Diagnosis, Admission Date, Discharge Date, Bill Amount.
- **Examples**:
  - Diagnosis: "Diabetes, Hypertension, Flu."

### 5. Educational Data
- **Fields**: Student ID, Name, Grade, Subject, Exam Date, Marks Scored, Attendance Percentage.
- **Examples**:
  - Subject: "Mathematics, Physics, Chemistry."

### 6. E-commerce Reviews Data
- **Fields**: Review ID, Product Name, User Name, Rating, Review Date, Review Text.
- **Examples**:
  - Review Text: "The product is excellent and met my expectations."

---

## Customization
You can extend or modify the script to include additional domains or customize existing ones. To add a new domain:
1. Create a new function (e.g., `generate_custom_data(rows)`).
2. Define the fields and logic for generating the data.
3. Add the function to the `generate_data` function switch case.

---

## Contribution
Contributions to enhance this project are welcome! Feel free to submit pull requests or report issues in the repository.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- **Faker Library**: For providing extensive fake data generation capabilities.
- **Streamlit**: For the seamless UI framework.

---


