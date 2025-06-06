# 🧮 Insurance Cost Analysis – Python Portfolio Project

This project reads and analyzes data from a CSV file (`insurance.csv`) containing medical insurance information. It calculates average costs, explores relationships between variables such as smoking status, BMI, age, region, and number of children, and helps understand the factors affecting insurance pricing.

---

## 📂 Dataset

The project uses a CSV file with the following columns:
- `age`
- `sex`
- `bmi`
- `children`
- `smoker`
- `region`
- `charges` (i.e. insurance cost)

Make sure the file `insurance.csv` is in the same directory as the script.

---

## 🔍 Features & Analysis Performed

- ✅ Read and parse data using `csv.DictReader`
- ✅ Store and structure data using Python lists
- ✅ Calculate:
  - Average insurance cost
  - Average BMI
  - Age statistics (min, max, average)
  - Male vs Female participant ratio
- ✅ Analyze:
  - Cost difference between smokers and non-smokers
  - Average cost by region
  - Insurance cost vs number of children
  - Insurance cost vs BMI
  - Insurance cost vs Age
  - Insurance cost vs Gender

## 🧠 Insurance Cost Formula (Used for Simulations)

```python
insurance_cost = 250*age - 128*sex + 370*bmi + 425*children + 24000*smoker - 12500
Note: sex is treated as 0 for female and 1 for male; smoker is 1 for smoker, 0 otherwise.

📊 Output Examples
Average cost if smokers quit
Region with highest average cost
BMI and Age segments with highest cost
Male/Female cost comparisons


🚀 How to Run
Make sure Python 3 is installed.
python main.py
Ensure that the insurance.csv file is in the same directory.

Requirements
Python 3.x
No external libraries required (only built-in csv module used)


---
