
word_counts = {"I": 3, "love": 2, "NLP": 1}


N = sum(word_counts.values())
V = len(word_counts)


def laplace_smoothing(word):
    return (word_counts.get(word, 0) + 1) / (N + V)

def add_k_smoothing(word, k=0.5):
    return (word_counts.get(word, 0) + k) / (N + k * V)


words = ["love", "Python"]  

for w in words:
    print(f"Word: {w}")
    print("Laplace:", laplace_smoothing(w))
    print("Add-K:", add_k_smoothing(w))
    print()
