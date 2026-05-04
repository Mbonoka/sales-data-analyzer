# Sales Data Analyzer

## 📌 Problem
Businesses often have messy sales data that is hard to analyze.

## ✅ Solution
This project cleans raw sales data and generates insights such as total revenue and top-performing products.

## 🛠 Tech Stack
- Python
- Pandas
- Matplotlib

## ▶️ How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run:
   python src/analyze.py

## 🌐 Dashboard
This project includes an interactive dashboard built with Streamlit.

Run:
streamlit run app.py

## 📊 Results
- Total revenue calculated
- Revenue by product visualized
- Chart saved in `outputs/`

## 🔥 Bonus Improvements
To enhance functionality and real-world usability:

### ✅ Export Results
The project can export summarized insights to a CSV file:
```python
revenue_by_product.to_csv("outputs/revenue_summary.csv")