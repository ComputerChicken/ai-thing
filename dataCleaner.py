total = ""

with open("reddit_file.txt", "r", encoding="utf-8") as f:
    total = f.read().split(" ")

newTotal = []

for word in total:
    if(word != "|||" and word != "###"):
        newWord = ""
        for letter in word:
            if(letter.isalpha()):
                newWord += letter
        newTotal.append(newWord)
    else:
        newTotal.append(word)

with open("clean_data.txt","w") as f:
    f.write(" ".join(newTotal))