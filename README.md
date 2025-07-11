# 🧠 Sentiment Analysis Web App

A Flask web app that uses TextBlob to analyze user-submitted text and determine sentiment.

---

## 📌 Features

- Analyze sentiment: Positive / Negative / Neutral
- Displays:
  - Sentiment
  - Polarity (from -1 to +1)
  - Subjectivity (from 0 to 1)
  - Word count
  - Confidence level (based on subjectivity)
- Clean, modern UI with responsive layout
- History saved during browser session

---

## 📃 License

This project is licensed under the MIT License.


## 🚀 Installation

Clone the repo and install requirements:

```bash
git clone https://github.com/neemabhandari18/Sentiment-Analysis-App.git
cd Sentiment-Analysis-App
pip install -r requirements.txt


python -m textblob.download_corpora
