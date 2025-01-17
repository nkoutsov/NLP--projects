#!/usr/bin/env python
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn import preprocessing
import pandas as pd
import matplotlib.pyplot as plt

from os import path
from wordcloud import WordCloud

currdir = path.dirname(__file__)

train_data = pd.read_csv('./datasets/train_set.csv', sep="\t")

categories = set(train_data["Category"])
for cat in categories:
	text=train_data[train_data["Category"]==cat]
	text=text["Content"]
	text=text.to_string()

	wc = WordCloud(stopwords=ENGLISH_STOP_WORDS)
	wdcd = wc.generate(text)

	wc.to_file(path.join(currdir, cat + ".png"))

    # Display the generated image:
    # the matplotlib way:

	plt.imshow(wdcd, interpolation='bilinear')
	plt.axis("off")
	plt.show()
