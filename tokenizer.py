data = ""

with open("clean_data.txt", "r") as f:
    data = f.read().split()

with open("tokens.txt", "w") as f:
    tokenList = []
    for rawToken in data:
        if(rawToken != "|||" or "###"):
            token = rawToken.lower()
            tokenList.append(token)
    out = "\n".join(set(tokenList))
    f.write(out)

print("Wrote " + str(len(set(tokenList))) + " tokens out of " + str(len(data)) + " words.")