# 📌 Data Processing Assignment

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![JSON](https://img.shields.io/badge/JSON-Data%20Parsing-orange?style=flat-square&logo=json)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green?style=flat-square&logo=fastapi)

---

## 📖 Project Overview
This project processes and analyzes location-based data using Python. The script:

✔ **Loads & Parses** JSON files 📂  
✔ **Merges Data** based on `id` 🔗  
✔ **Counts Valid Points** per type 🏨 ☕ 🍽️  
✔ **Calculates Average Ratings** ⭐  
✔ **Finds Highest Reviews Location** 📍  
✔ **Detects Incomplete Data Locations** (*Bonus Point*) ❗

---

## 🏗️ Folder Structure
```
data-processing-assignment/
│── data/
│   ├── locations.json
│   ├── metadata.json
│── src/
│   ├── main.py
│── README.md
```

---

## 🛠️ Technologies Used
- 🐍 **Python** (v3.8+)
- 📜 **JSON** (Data Handling)
- 🔢 **Collections** (Defaultdict)

---

## 🚀 Installation & Setup
1️⃣ Clone this repository:
```sh
git clone https://github.com/yourusername/data-processing-assignment.git
cd data-processing-assignment
```
2️⃣ Install dependencies (if any):
```sh
pip install -r requirements.txt
```
3️⃣ Run the script:
```sh
python src/main.py
```

---

## 📊 Sample Output
```sh
Valid points per type: {'restaurant': 3, 'hotel': 3, 'cafe': 2}
Average rating per type: {'restaurant': 4.1, 'hotel': 3.4, 'cafe': 4.6}
Location with highest reviews: {'id': 'loc_07', 'latitude': 64.0522, 'longitude': -108.233, 'type': 'hotel', 'rating': 2.0, 'reviews': 900}
Incomplete data locations: []
```

---
