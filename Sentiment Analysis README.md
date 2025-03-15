REQUIREMENTS
[pandas
textblob
matplotlib
wordcloud]

- Ensure your CSV file is named **`Reviews.csv`**  
- Place it in the same directory as **`Sentiment_Analysis_TextBlob.py`**  
- If your dataset has a different name, either rename it to `Reviews.csv` or update the following line in the script:  
  ```python
  df = pd.read_csv("your_filename.csv")

# ai-sentiment-analysis-Textblob
A sentiment analysis project using NLP to classify Amazon reviews for AMAZON FINE FOODS as Positive, Negative, or Neutral.

# AI Sentiment Analysis using TextBlob

## 📌 Project Overview
This project performs sentiment analysis on Amazon Fine Food Reviews using TextBlob, a simple NLP tool for processing textual data. It analyzes customer reviews and classifies them into Positive, Negative, or Neutral sentiments. 

## 🚀 Features
- **Loads Amazon Fine Food Reviews dataset** (CSV format)
- **Applies sentiment analysis** using TextBlob
- **Visualizes results** with sentiment distribution bar charts
- **Generates word clouds** for negative reviews
- **Exports analyzed results** into a CSV file

## 🛠️ Technologies Used
- Python
- Pandas
- TextBlob
- Matplotlib
- WordCloud

## 🔧 Installation & Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/Quoe102/ai-sentiment-analysis-Textblob.git
   cd ai-sentiment-analysis-Textblob
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the sentiment analysis script:
   ```bash
   python Sentiment_Analysis_TextBlob.py
   ```
4. View the output in `sentiment_results.csv`.

## 📊 Sample Output
The script classifies each review and generates an output like:

| Review Text | Sentiment |
|-------------|-----------|
| "The product is amazing!" | Positive |
| "Not worth the money." | Negative |
| "It's okay, but could be better." | Neutral |

## 📂 Data
- **Dataset**: Due to file size constraints, the original dataset is not included.
- **Sample Data**: You can manually upload a small CSV file (optional) for testing.

## 📜 License
This project is open-source and available under the MIT License.

---

🚀 **Inspired by AI automation!** Have suggestions? Feel free to contribute or reach out!
