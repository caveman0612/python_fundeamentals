with open("words.txt", "r") as words:
    print(type(words))
    words = words.read()
    print(type(words))
    words = words[:50]
    words = words.split("\n")
    words = " | ".join(words)
    print(words)
    with open("words1.txt", "a") as word1:
        word1.write("\n" + words)