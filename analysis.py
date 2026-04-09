import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_data.csv")

print("Preview:")
print(df.head())

# -----------------------
# DATA CLEANING
# -----------------------
df = df.dropna(subset=['country', 'rating'])

# -----------------------
# ANALYSIS 1: Movies vs TV Shows
# -----------------------
type_counts = df['type'].value_counts()

type_counts.plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.savefig("content_type.png")
plt.clf()

# -----------------------
# ANALYSIS 2: Top Countries
# -----------------------
top_countries = df['country'].value_counts().head(5)

top_countries.plot(kind='bar')
plt.title("Top 5 Countries Producing Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.savefig("top_countries.png")
plt.clf()

# -----------------------
# ANALYSIS 3: Ratings Distribution
# -----------------------
ratings = df['rating'].value_counts()

ratings.plot(kind='bar')
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.savefig("ratings_chart.png")
plt.clf()

# -----------------------
# INSIGHTS
# -----------------------
print("\nINSIGHTS:")
print("Most content type:", type_counts.idxmax())
print("Top country:", top_countries.idxmax())
print("Most common rating:", ratings.idxmax())

# -----------------------
# ANALYSIS: Content over years
# -----------------------

year_counts = df['release_year'].value_counts().sort_index()

year_counts.plot()

plt.title("Content Released Over Years")
plt.xlabel("Year")
plt.ylabel("Count")

plt.savefig("year_trend.png")
plt.clf()

# Extract duration for movies
movies = df[df['type'] == 'Movie']

movies['duration'] = movies['duration'].str.replace(' min', '').astype(float)

movies['duration'].plot(kind='hist', bins=20)

plt.title("Movie Duration Distribution")
plt.xlabel("Minutes")

plt.savefig("duration_dist.png")
plt.clf()