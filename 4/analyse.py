import sys, re, pprint
import nltk
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.corpus import stopwords

# membuat stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# load komentar dari file
file = open('20190806_comment_HLkZNGl101k.txt', 'r')

def main():
    regex     = re.compile("[^a-zA-Z0-9\s]")    
    ind_stops = set(stopwords.words('indonesian'))

    # mengambil komentar per line
    for idx, line in enumerate(file):
        # cek jika line tidak berisi komentar        
        if line.isspace() != True:
            # pre-processing data
            line = regex.sub(' ', line)     # mengganti karakter yang tidak diinginkan dengan spasi
            line = line.lower()             # membuat semua kata menjadi huruf kecil
            line = nltk.word_tokenize(line) # memisahkan kata per kata di dalam kalimat (tokenization)
            line = ' '.join([word for word in line if word not in ind_stops]) # menghilangkan stopword
            line = stemmer.stem(line)       # pake stemmer, depe preprocessing jadi lalod. Apa taruh pas di mo ba simpang jo?

            print(line, "\n")
            
            if idx == 10:
                sys.exit('exit: looping sampe beberapa komentar dulu')

if __name__ == "__main__":
    main() 