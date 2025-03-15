# Import Required Libraries ---
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud

#Load Dataset ---
df = pd.read_csv("Reviews.csv")

# Check dataset loaded properly
print("🛍️  AMAZON:AMAZON FINE FOODS CUSTOMER SENTIMENT ANALYSIS")
print("✅ Data Loaded Successfully")
print("Columns in consideration")
print(df.columns)  # Check available columns
print("\n📝 First 5 reviews (for validation):")
print(df["Text"].head())  # Show first 5 reviews

# Ensure "Text" Column is Not Empty --- Sanity Check
if df["Text"].isnull().sum() > 0:
    print("⚠️ Warning: Some reviews are missing. Dropping null values...")
    df = df.dropna(subset=["Text"])

# --- Step 4: Define Sentiment Analysis Function ---
def get_sentiment(text):
    try:
        polarity = TextBlob(str(text)).sentiment.polarity
        return "Positive" if polarity > 0.2 else "Negative" if polarity < -0.2 else "Neutral"
    except:
        return "Error"



# --- Step 5: Apply Sentiment Analysis ---
print("⏳ Starting sentiment analysis...")  # Debugging print...Sanity Check
df["Sentiment"] = df["Text"].apply(get_sentiment)  # Process all reviews
print("✅ Sentiment Analysis Completed (Full Dataset)") #Sanity Check
df.to_csv("sentiment_results.csv", index=False)
print("💾 Results saved to sentiment_results.csv")



# --- Step 6: Check If Sentiment Column Was Created ---
print("✅ Sentiment Analysis Completed (100 Reviews)")
print(df[["Text", "Sentiment"]].head())  # Show first 5 rows

# --- Step 7: Check Sentiment Distribution ---
print(df["Sentiment"].value_counts())
print(get_sentiment(df["Text"].iloc[0]))  # Test sentiment for first review


# --- Step 8: Visualize Sentiment Distribution ---
plt.figure(figsize=(8, 5))
plt.bar(df["Sentiment"].value_counts().index, df["Sentiment"].value_counts().values, color=["green", "gray", "red"])
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.title("Sentiment Distribution of Amazon Reviews")
from wordcloud import WordCloud

# Generate Word Cloud for Negative Reviews
negative_reviews = " ".join(df[df["Sentiment"] == "Negative"]["Text"])
wordcloud = WordCloud(width=800, height=400, background_color="black").generate(negative_reviews)
print("\n📊 Sentiment Distribution Chart...")
print("\n☁️ Generating Word Cloud for Negative Reviews...")

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Common Words in Negative Reviews")
plt.show()

print("\n🎯 Analysis Complete! Ready for Presentation.")