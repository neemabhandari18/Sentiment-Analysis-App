

#  Sentiment-Analysis-App

This is a simple and clean web application built using **Flask** and **TextBlob** that performs **sentiment analysis** on user-input text. It analyzes the text and returns the **sentiment** (Positive/Negative/Neutral), **polarity**, **subjectivity**, and **confidence level** based on subjectivity.

---

## 📌 Features

- Analyze sentiment from user input
- Displays:
  - Sentiment (Positive / Negative / Neutral)
  - Polarity (scale -1 to 1)
  - Subjectivity (scale 0 to 1)
  - Word Count
  - Confidence level (High/Medium/Low)
- Auto-centers input form and results
- Session-based history tracking (in memory)
- Responsive and modern UI

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.x installed
- Install required packages:

```bash
pip install flask textblob
python -m textblob.download_corpora

