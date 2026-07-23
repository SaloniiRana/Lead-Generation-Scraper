# Public Data Scraper for Lead Generation

A modular, scalable Python application built to extract public business data, website references, and social loops from target web structures. Developed as part of a college internship project.

## 🚀 Features
- **Modular Architecture:** Separates processing layers (`scraper.py`) from execution layers (`main.py`).
- **Target Tracking:** Filters layout structures to locate core company websites.
- **Social Media Scopes:** Auto-identifies public profile structures (e.g., Instagram loops).
- **Data Structuring:** Converts collected leads seamlessly into an active `.csv` sheet for Excel.

## 🛠️ Tech Stack
- **Language:** Python 3
- **Libraries:** Beautiful Soup 4, Requests, Pandas

## 📋 Setup & Usage Instructions
1. Clone or download this repository.
2. Open your terminal inside the folder and run:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```
3. Execute the pipeline:
   ```bash
   python main.py
   ```
4. Find your generated leads exported directly into `generated_leads.csv`.
