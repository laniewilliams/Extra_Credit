from dataclasses import dataclass
from pathlib import Path
import matplotlib.pyplot as plt
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

text = open("facebook_comments.txt",'r')
lines = text.readlines()
positive_count = 0
negative_count = 0
for line in lines:
    blob=TextBlob(line)
    print(blob.sentiment)
    if blob.sentiment.polarity > 0:
        positive_count += 1
    if blob.sentiment.polarity < 0:
        negative_count += 1


data = [positive_count,negative_count]
labels= ['Postive','Negative']



plt.bar(labels,data)
plt.title('Sentiment of Facebook Comments')
plt.xlabel('Polarity')
plt.ylabel('Number of Comments')
plt.show()
