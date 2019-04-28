import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.downloader.download('vader_lexicon')




file='book1.xlsx'

xl=pd.ExcelFile(file)
dfs=xl.parse(xl.sheet_names[0])
dfs=list(dfs['Timeline'])
print(dfs)
sid=SentimentIntensityAnalyzer()

for data in dfs:
    ss=sid.polarity_scores(data)
    print(data)
    for k in ss:
        print(k,ss[k])