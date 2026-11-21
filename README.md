
# 🎬 Netflix Movies and TV Shows – Data Cleaning & Analytics

## 📌 Project Overview

This project focuses on cleaning, analyzing, and visualizing the Netflix Movies and TV Shows dataset using Python.

The project uses Pandas and NumPy for data cleaning and preprocessing, Jupyter Notebook for data exploration, and Streamlit with Plotly to build an interactive analytics dashboard.

The main objective is to understand real-world messy data, handle missing values, fix inconsistent data types, and extract meaningful insights from Netflix content data.

---

## 🎯 Problem Statement

Real-world datasets often contain missing values, duplicate records, inconsistent formats, and incorrect data types.

The Netflix dataset contains these challenges, making it useful for learning practical data cleaning and exploratory data analysis.

This project addresses these problems by cleaning and transforming the original dataset and presenting the results through an interactive dashboard.

---

## 🎯 Project Objectives

- Explore the Netflix dataset using Pandas.
- Identify missing values column by column.
- Handle missing values using appropriate methods.
- Detect and remove duplicate records.
- Clean mixed-type duration columns.
- Convert date columns into datetime format.
- Perform Exploratory Data Analysis (EDA).
- Generate meaningful insights.
- Build an interactive Netflix analytics dashboard.
- Export the cleaned dataset into a CSV file.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| Jupyter Notebook | Data exploration and analysis |
| Streamlit | Interactive dashboard |
| Plotly | Interactive visualizations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| VS Code | Development environment |
| Git & GitHub | Version control |

---

## 📂 Dataset Information

Dataset: Netflix Movies and TV Shows

Source: Kaggle

Dataset Link:
https://www.kaggle.com/datasets/shivamb/netflix-shows

The dataset contains information about Netflix movies and TV shows, including:

- Show ID
- Type
- Title
- Director
- Cast
- Country
- Date Added
- Release Year
- Rating
- Duration
- Listed In
- Description

Note: Download the original CSV file from Kaggle and place it inside the dataset folder.

---

## 📁 Project Structure

Netflix-Data-Analytics/
│
├── dataset/
│   └── netflix_titles.csv
│
├── notebooks/
│   └── Netflix_Data_Cleaning.ipynb
│
├── output/
│   └── netflix_cleaned.csv
│
├── app.py
│
├── utils.py
│
├── requirements.txt
│
└── README.md

---

## 🧹 Data Cleaning Process

The following data cleaning operations are performed:

### 1. Data Exploration
- Display first and last five records.
- Check dataset shape.
- Inspect column names and data types.
- Generate statistical summaries.

### 2. Missing Value Analysis
- Identify missing values.
- Calculate missing-value percentages.
- Handle missing categorical information.
- Preserve unknown information instead of inventing values.

### 3. Duplicate Handling
- Identify duplicate records.
- Remove exact duplicate rows.

### 4. Duration Cleaning
- Extract movie duration in minutes.
- Extract TV show duration in seasons.
- Create separate numerical columns.

### 5. Date Conversion
- Convert date_added into datetime format.
- Extract year and month.

### 6. Data Validation
- Verify data types.
- Check remaining missing values.
- Compare original and cleaned datasets.

### 7. Export
- Save the cleaned dataset as netflix_cleaned.csv.

---

## 📊 Dashboard Features

The interactive dashboard includes:

- Total Netflix Shows
- Total Directors
- Total Countries
- Total Genres
- Total Ratings
- Movies vs TV Shows distribution
- Top 10 genres
- Content distribution by release year
- Ratings distribution
- Top 10 content-producing countries

### Interactive Filters

- Content type selection
- Release year range selection

---

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open Project Folder

```bash
cd Netflix-Data-Analytics
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
venv\Scripts\activate.bat
```

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 6: Download Dataset

Download the Netflix dataset from Kaggle and place:

```text
dataset/netflix_titles.csv
```

### Step 7: Run Data Cleaning Notebook

Open the notebook:

```text
notebooks/Netflix_Data_Cleaning.ipynb
```

Select your Python environment and execute all cells in order.

The cleaned dataset will be generated inside the output folder.

### Step 8: Run Streamlit Dashboard

```bash
streamlit run app.py
```

Open the browser:

http://localhost:8501

---

## 📸 Dashboard Preview

Add your project screenshots here after running the application.

Example:

![Netflix Dashboard](screenshots/dashboard.png)

---

## 🚀 Future Improvements

- Add more interactive filters.
- Perform advanced exploratory data analysis.
- Add country-wise geographical visualizations.
- Develop additional content recommendation insights.
- Deploy the dashboard online.
- Add more data-driven visualizations.

---

## 📚 Learning Outcomes

Through this project, I learned:

- Python programming for Data Analytics.
- Pandas DataFrame operations.
- Handling missing values.
- Data type conversion.
- Data cleaning and preprocessing.
- Exploratory Data Analysis.
- Interactive dashboard development.
- Data visualization.
- Git and GitHub project management.

---

## 👩‍💻 Author

**Your Name**

Aspiring Data Analyst

Skills: Python | Pandas | NumPy | SQL | Data Analytics

GitHub: YOUR_GITHUB_PROFILE_URL

---

## ⭐ Acknowledgements

Thanks to Kaggle for providing the Netflix Movies and TV Shows dataset for learning and analysis.

Dataset credit:
https://www.kaggle.com/datasets/shivamb/netflix-shows
