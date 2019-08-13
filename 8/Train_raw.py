import sys
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from resources import keywords
from resources import bigrams
  
def word_feats(words):
    return dict([(word, True) for word in words])

keywords_positive   = keywords.keywords_positive
keywords_negative   = keywords.keywords_negative

positive_feature    = [(word_feats(pos), 'pos') for pos in keywords_positive] 
negative_feature    = [(word_feats(neg), 'neg') for neg in keywords_negative]

train_set   = positive_feature + negative_feature
classifier  = NaiveBayesClassifier.train(train_set)

# Predict
neg = 0
pos = 0
sentence = "Semangat ya kak jangan sedih kita sesama perumpuan pasti hati nya Sama aku bisa ngerti kok perasan kakak sekali lagi semangat🙂"    
sentence = sentence.lower()
words = sentence.split(' ')
for word in words:
    classResult = classifier.classify( word_feats(word))
    if classResult == 'neg':
        neg = neg + 1
    if classResult == 'pos':
        pos = pos + 1

print('Positive: ' + str(float(pos)/len(words)))
print('Negative: ' + str(float(neg)/len(words)))
