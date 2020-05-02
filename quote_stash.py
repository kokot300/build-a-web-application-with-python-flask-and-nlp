#!/usr/bin/python3

import pandas as pd
import numpy as np
from random import randrange
import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# declare global variable
quotes = None
sid = SentimentIntensityAnalyzer()



def prepare_sentiment_quote_stash(quote_stash_path):
    global quotes

    # load the quote stash
    quotes = pd.read_csv(quote_stash_path)

    sid = SentimentIntensityAnalyzer()

    all_compounds = []
    for sentence in quotes['quote']:
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            if k == 'compound':
                all_compounds.append(ss[k])

    # add sentiment to the data
    quotes['sentiment_score'] = all_compounds

    # create ladder index
    quotes = quotes.sort_values('sentiment_score')
    quotes['index'] = [ix for ix in range(0, len(quotes))]

    return quotes


print(prepare_sentiment_quote_stash('cytaty.csv'))
quotes.head()

print(quotes.shape)
quotes.head()

for sentence in quotes['quote']:
    print(sentence)
    break

all_compounds = []
for sentence in quotes['quote']:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
        print()

        if k == 'compound':
            all_compounds.append(ss[k])


import matplotlib
import matplotlib.pyplot as plt
plt.plot(sorted(all_compounds))
plt.title('Overall sentiment in quote stash')
plt.grid()

quotes['sentiment_score'] = all_compounds
quotes.head()

import numpy as np

# the most negative
print(np.min(quotes['sentiment_score']))
# the most positive
np.max(quotes['sentiment_score'])


