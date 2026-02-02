import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is a simple example showing stopword removal in NLTK."

stop_words = set(stopwords.words("english"))
words = word_tokenize(text)

filtered = [w for w in words if w.lower() not in stop_words]

print("Filtered Words:", filtered)
