import sys, re, pprint, time
import nltk
import nltk.sentiment.sentiment_analyzer
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

from Keywords import Keywords
from Bigrams import Bigrams

# membuat stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# membuat object keywords
keywords = Keywords()
bigrams  = Bigrams()

# load komentar dari file
file = open('20190806_comment_HLkZNGl101k.txt', 'r', encoding="utf8")

def main():
    regex        = re.compile("[^a-zA-Z0-9\s]")    
    ind_stops    = set(stopwords.words('indonesian'))
    keywords_pos = keywords.load('positive')
    keywords_neg = keywords.load('negative')
    bigrams_pos  = bigrams.load('positive')
    bigrams_neg  = bigrams.load('negative')

    comments_positive = 0
    comments_negative = 0
    comments_uncategorized = 0

    # mengambil komentar per line
    no = 0
    for line in file:
        # cek jika line tidak berisi komentar        
        if line.isspace() != True:
            # pre-processing data
            line = regex.sub(' ', line)     # mengganti karakter yang tidak diinginkan dengan spasi
            line = line.lower()             # membuat semua kata menjadi huruf kecil
            line = nltk.word_tokenize(line) # memisahkan kata per kata di dalam kalimat (tokenization)
            line = ' '.join([word for word in line if word not in ind_stops]) # menghilangkan stopword
            line = stemmer.stem(line)       # stemming
            
            # hitung positif dan negatif
            analysis_keyword_pos = nltk.sentiment.util.extract_unigram_feats(line.split(), keywords_pos)
            analysis_keyword_neg = nltk.sentiment.util.extract_unigram_feats(line.split(), keywords_neg)
            count_keyword_pos    = sum(map((1).__eq__, analysis_keyword_pos.values()))
            count_keyword_neg    = sum(map((1).__eq__, analysis_keyword_neg.values()))

            analysis_bigram_pos  = nltk.sentiment.util.extract_bigram_feats(line.split(), bigrams_pos) 
            analysis_bigram_neg  = nltk.sentiment.util.extract_bigram_feats(line.split(), bigrams_neg) 
            count_bigram_pos     = sum(map((1).__eq__, analysis_bigram_pos.values()))
            count_bigram_neg     = sum(map((1).__eq__, analysis_bigram_neg.values()))
            
            # lakukan perhitungan total
            total_pos   = count_keyword_pos + count_bigram_pos
            total_neg   = count_keyword_neg + count_bigram_neg

            if (total_pos > total_neg):
                comments_positive += 1

            if (total_pos < total_neg):
                comments_negative += 1

            if (total_pos == 0 and total_neg == 0):
                comments_uncategorized += 1
            if (total_pos != 0 and total_neg != 0 and total_pos == total_neg):
                comments_uncategorized +=1

            # -------------------------------------------
            # | Debugging area
            # -------------------------------------------
            no += 1
            print(str(no)+". "+line)

            # keywords debugging
            
            #pprint.pprint(analysis_keyword_pos)
            #pprint.pprint(analysis_keyword_neg)
            print("Keyword positif: ", count_keyword_pos)
            print("Keyword negatif: ", count_keyword_neg)
            

            # bigram debugging
            
            #pprint.pprint(analysis_bigram_pos)
            #pprint.pprint(analysis_bigram_neg)
            print("Bigram positif: ", count_bigram_pos)
            print("Bigram negatif: ", count_bigram_neg, "\n")            
            

            if no == 1000:
                break

            # -------------------------------------------
            # | // Debugging area
            # -------------------------------------------
    
    # results
    print("Total komentar positif: ", comments_positive)
    print("Total komentar negatif: ", comments_negative)
    print("Total komentar tidak terkategorikan: ", comments_uncategorized)

if __name__ == "__main__":
    start_time = time.time()
    main() 
    print("--- %s seconds ---" % (time.time() - start_time))