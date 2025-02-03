import pandas as pd

# Load the dataset
df = pd.read_csv('newfile.csv')

# 1. Distribution of Ratings
rating_distribution = df['score'].value_counts()
print("Distribution of Ratings:")
print(rating_distribution)

# 2. Total Number of Upvotes
total_upvotes = df['thumbsUpCount'].sum()
print("\nTotal Number of Upvotes:", total_upvotes)

# 3. Male-to-Female Distribution (Not directly possible without gender data)
print("\nMale-to-Female Distribution: Cannot be determined from the dataset.")

# 4. Longest Review
longest_review = df.loc[df['content'].str.len().idxmax()]
print("\nLongest Review:")
print("User:", longest_review['userName'])
print("Review:", longest_review['content'])

# 5. Frequency of Reviews
df['at'] = pd.to_datetime(df['at'])
df['date'] = df['at'].dt.date
review_frequency = df['date'].value_counts().sort_index()
print("\nFrequency of Reviews:")
print(review_frequency)

# 6. Most Common Time for Reviews
df['hour'] = df['at'].dt.hour
common_review_time = df['hour'].value_counts().idxmax()
print("\nMost Common Time for Reviews (Hour of the Day):", common_review_time)

# 7. Overall Sentiment
positive_reviews = df[df['score'] == 5]
negative_reviews = df[df['score'] < 5]
print("\nOverall Sentiment:")
print("Positive Reviews:", len(positive_reviews))