
spam_words = ["win", "cash", "free"]


msg = input("Enter message: ").lower()


found = [word for word in spam_words if word in msg]


if found:
    print(True)
    print("Spam words found:", found)
else:
    print(False)
    print("Spam words found:", [])
