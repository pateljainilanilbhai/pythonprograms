import re
from textblob import TextBlob
x=input("enter a text to analyse")
analysis = TextBlob(x)


if analysis.sentiment.polarity > 0:
    print( 'positive')
elif analysis.sentiment.polarity == 0:
    print( 'neutral')
else:
    print('negative')