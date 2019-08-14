import sys
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from resources import keywords
from resources import bigrams

class Train:        
    def word_feats(self, words):
        return dict([(word, True) for word in words])

    def main(self):
        keywords_positive   = keywords.keywords_positive
        keywords_negative   = keywords.keywords_negative
        
        positive_feature    = [(self.word_feats(pos), 'pos') for pos in keywords_positive] 
        negative_feature    = [(self.word_feats(neg), 'neg') for neg in keywords_negative]

        train_set   = positive_feature + negative_feature
        classifier  = NaiveBayesClassifier.train(train_set)
        
        return classifier

Train().main()