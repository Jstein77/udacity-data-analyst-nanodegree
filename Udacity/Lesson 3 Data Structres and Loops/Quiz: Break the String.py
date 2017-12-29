headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs

for headline in headlines:
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break
    news_ticker += headline + " "
    print("debug: the sting is {} chars long.".format(len(news_ticker)))

print(news_ticker)
