import nltk
from nltk.corpus import stopwords
from collections import Counter
nltk.download("punkt")


# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')

# Read the contents of the file
# random_paragraphs.txt
with open(r"D:\cloud_ass\cloud_ass\random_paragraphs.txt") as file:
    text = file.read()
# Tokenize the text into words
words = nltk.word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Display word frequency count
for word, freq in word_freq.items():
    print(f'{word}: {freq}')
