# from google_play_scraper import Sort, reviews
# import pandas as pd
# result, continuation_token = reviews(
#     'com.instagram.android',
#     lang='en', # defaults to 'en'
#     country='us', # defaults to 'us'
#     sort=Sort.NEWEST, # defaults to Sort.NEWEST
#     count=100, # defaults to 100
#     filter_score_with=5 # defaults to None(means all score)
# )

# df=pd.DataFrame(result)

# df.to_csv(f"newfile.csv", index=False, encoding='utf-8-sig')
# print(df)


from google_play_scraper import Sort, reviews
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
from datetime import datetime

# Scrape Google Play reviews
result, continuation_token = reviews(
    'com.instagram.android',
    lang='en',
    country='us',
    sort=Sort.NEWEST,
    count=100,
    filter_score_with=5
)

# Convert to DataFrame
df = pd.DataFrame(result)

# Save to CSV
df.to_csv("newfile.csv", index=False, encoding='utf-8-sig')

# Convert 'at' column to datetime
df['at'] = pd.to_datetime(df['at'])

# 1. Distribution of ratings
rating_distribution = df['score'].value_counts().sort_index()

# 2. Total number of upvotes
total_upvotes = df['thumbsUpCount'].sum()

# 3. Male-to-Female distribution cannot be determined from the dataset

# 4. Longest review
longest_review = df.loc[df['content'].str.len().idxmax(), 'content']

# 5. Frequency of reviews (daily count)
review_frequency = df['at'].dt.date.value_counts().sort_index()

# 6. Most common review submission times (hourly distribution)
df['hour'] = df['at'].dt.hour
common_review_time = df['hour'].value_counts().sort_index()

# 7. Overall sentiment (average rating)
average_rating = df['score'].mean()

# Plot rating distribution
plt.figure(figsize=(8, 5))
sns.barplot(x=rating_distribution.index, y=rating_distribution.values, palette="viridis")
plt.xlabel("Ratings")
plt.ylabel("Count")
plt.title("Distribution of Ratings")
plt.show()

# Plot review submission frequency
plt.figure(figsize=(12, 5))
review_frequency.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel("Date")
plt.ylabel("Number of Reviews")
plt.title("Daily Review Frequency")
plt.xticks(rotation=45)
plt.show()

# Plot common review submission times
plt.figure(figsize=(8, 5))
sns.barplot(x=common_review_time.index, y=common_review_time.values, palette="coolwarm")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Reviews")
plt.title("Most Common Review Submission Times")
plt.show()

# Print results
print("Rating Distribution:")
print(rating_distribution)
print("\nTotal Upvotes:", total_upvotes)
print("\nLongest Review:", longest_review)
print("\nReview Frequency:")
print(review_frequency.head())
print("\nMost Common Review Submission Times:")
print(common_review_time.head())
print("\nOverall Average Rating:", average_rating)


