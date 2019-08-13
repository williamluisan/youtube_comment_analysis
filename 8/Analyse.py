import sys, re, pprint, time, os
import nltk
import nltk.sentiment.sentiment_analyzer
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from config import config
from resources import keywords
from resources import bigrams
from Visualize import Visualize
from Train import Train

# file yang akan dianalisa
FILE_TO_ANALYSE = config.FILE_TO_ANALYSE
tot_comments_available = config.TOT_COMMENTS_AVAILABLE

# membuat stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# load komentar dari file
file = open('data/' + FILE_TO_ANALYSE, 'r', encoding="utf8")

# file untuk menyimpan komentar sesuai kategori
os.remove('data/comments_pos.txt')
os.remove('data/comments_neg.txt')
os.remove('data/comments_uncat.txt')
file_comment_pos    = open("data/comments_pos.txt", 'a', encoding="utf8")
file_comment_neg    = open("data/comments_neg.txt", 'a', encoding="utf8")
file_comment_uncat  = open("data/comments_uncat.txt", 'a', encoding="utf8")

class Analyse:
    def main(self):
        # waktu dimulai eksekusi fungsi main
        start_time  = time.time()

        # melakukan training feature
        trainer = Train()
        classifier = trainer.main()

        tot_comments_to_analyze = int(input('Total komentar yang akan dianalisa (0 = semua, 1 .. ' + str(tot_comments_available) + ') : '))

        regex        = re.compile("[^a-zA-Z0-9\s]")    
        ind_stops    = set(stopwords.words('indonesian'))
        keywords_pos = keywords.keywords_positive
        keywords_neg = keywords.keywords_negative
        bigrams_pos  = bigrams.bigrams_positive
        bigrams_neg  = bigrams.bigrams_negative

        comments_positive = comments_negative = comments_uncategorized = 0
        keyword_pos_match_total = keyword_neg_match_total = bigram_pos_match_total = bigram_neg_match_total = 0
        pos = neg = 0

        # membuat object untuk visualisasi
        visualize = Visualize()

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
                line_split = nltk.word_tokenize(line) # memecahkan kembali menjadi kata per kata
                
                # melakukan prediksi
                for word in line_split:
                    classifyingResult = classifier.classify(trainer.word_feats(word))
                    if classifyingResult == 'neg':
                        neg = neg + 1
                    if classifyingResult == 'pos':
                        pos = pos + 1
                
                positive_value = float(pos)/len(line_split)
                negative_value = float(neg)/len(line_split)

                if positive_value > negative_value:
                    comments_positive += 1
                    file_comment_pos.write(line + '\n\n')
                
                if positive_value < negative_value:
                    comments_negative += 1
                    file_comment_neg.write(line + '\n\n')
                
                # kembalikan ke state awal = 0
                pos = neg = 0

                """
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
                    file_comment_pos.write(line + '\n\n')

                if (total_pos < total_neg):
                    comments_negative += 1
                    file_comment_neg.write(line + '\n\n')

                if (total_pos == 0 and total_neg == 0):
                    comments_uncategorized += 1
                    file_comment_uncat.write(line + '\n\n')

                if (total_pos != 0 and total_neg != 0 and total_pos == total_neg):
                    comments_uncategorized +=1
                    file_comment_uncat.write(line + '\n')

                # perhitungan total keywords dan bigram
                keyword_pos_match_total += count_keyword_pos
                keyword_neg_match_total += count_keyword_neg
                bigram_pos_match_total  += count_bigram_pos
                bigram_neg_match_total  += count_bigram_neg
                """

                # -------------------------------------------
                # | Debugging area
                # -------------------------------------------
                no += 1
                print(str(no)+". "+line)

                # keywords debugging
                #pprint.pprint(analysis_keyword_pos)
                #pprint.pprint(analysis_keyword_neg)
                #print("Keyword positif: ", count_keyword_pos)
                #print("Keyword negatif: ", count_keyword_neg)
                print("Positive prediction: ", positive_value)
                print("Negative prediction: ", negative_value, "\n")

                # bigram debugging            
                #pprint.pprint(analysis_bigram_pos)
                #pprint.pprint(analysis_bigram_neg)
                #print("Bigram positif: ", count_bigram_pos)
                #print("Bigram negatif: ", count_bigram_neg, "\n")            

                # -------------------------------------------
                # | // Debugging area
                # -------------------------------------------

                # batasan komentar untuk dianalisa
                if tot_comments_to_analyze != 0:
                    if no == tot_comments_to_analyze:
                        break
        
        # close all files
        file_comment_pos.close()
        file_comment_neg.close()
        file_comment_uncat.close()

        # results
        comments_total      = comments_positive + comments_negative + comments_uncategorized    # total komentar
        comments_analyzed   = comments_positive + comments_negative                             # total komentar yang dianalisa
        comments_analyzed_percentage = (comments_analyzed * 100) / comments_total               # presentasi komentar yang berhasil dianalisa

        print("------------------------------ RESULT ------------------------------")
        print("Total komentar positif: ", comments_positive)
        print("Total komentar negatif: ", comments_negative)
        print("Total komentar tidak terkategorikan: ", comments_uncategorized, "\n")
        print(
            "Total komentar dianalisa = {} ({:.2f}%) dari {} komentar" 
            . format(comments_analyzed, comments_analyzed_percentage, comments_total)
        )
        print("Keyword positif (match) = {}" . format(keyword_pos_match_total))
        print("Keyword negatif (match) = {}" . format(keyword_neg_match_total))
        print("Bigram positif (match) = {}" . format(bigram_pos_match_total))
        print("Bigram negatif (match) = {}" . format(bigram_neg_match_total))
        print("--------------------------------------------------------------------")

        # mengitung waktu eksekusi
        stop_time   = time.time()
        seconds_executed = stop_time - start_time
        minutes_executed = (stop_time - start_time) / 60
        print("\nexecution time: {:.2f} seconds / {:.2f} minutes" . format(seconds_executed, minutes_executed))

        # generate grafik
        visualize.main(
            [comments_uncategorized, comments_positive, comments_negative], 
            [keyword_pos_match_total, keyword_neg_match_total, bigram_pos_match_total, bigram_neg_match_total], 
            comments_total,
            tot_comments_available
        )

if __name__ == "__main__":
    Analyse().main()