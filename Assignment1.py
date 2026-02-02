import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

text = "The quick, BROWN foxes...they are JUMPING over 10 lazy dogs!"


text = text.lower()


text = re.sub(r'[^a-z\s]', '', text)


tokens = word_tokenize(text)


stop_words = set(stopwords.words('english'))
tokens = [w for w in tokens if w not in stop_words]


ps = PorterStemmer()
tokens = [ps.stem(w) for w in tokens]

print(tokens)
