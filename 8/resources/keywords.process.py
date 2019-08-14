from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# list stowords
ind_stops    = set(stopwords.words('indonesian'))

# membuat stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# membuat keyword sendiri
madein_keywords_positive = [
    'langgeng', 'semangat', 'mantul', 'gemesin', 'natural',
    'kepo', 'lucu', 'romantis', 'perfect', 'congrats',
    'finally', 'terharu', 'merinding', 'sabar', 'smart',
    'salut', 'santuy', 'mirip', 'bijak', 'ikhlas',
    'hebat', 'cakep', 'kasihan', 'sopan', 'insaf', 'tobat', 'aman', 'introspeksi', 
    'respect', 'relax', 'suka', 'like', 'berkarya', 'hargai', 'hikmah', 'bahagia',
    'like', 'proses', 'gg', 'sukses', 'sirik', 'pray', 'barbar', 'luv', 'benar',
    'penyanyi', 'positif', 'cobaan', 'seru', 'inspring', 'cocok', 'nyimak', 'strong', 'nice', 'sayang', 
    'cantik', 'support', 'suka', 'dukung', 'perfect', 'idaman', 'setuju', 'pintar', 'baik', 'aman', 'tabah', 'bagus', 
    'sukses', 'percaya', 'selamat', 'sabar', 'imut', 'impian', 'terbaik', 'bangga', 'seru', 'love', 'setuju', 'senang',
    'mantap', 'cinta', 'sweet', 'hebat', 'wonder', 'good', 'keren', 'kuat', 'gift', 'pro', 'semangat', 'beautiful', 'pretty',
    'asik', 'adem', 'nyaman', 'mantap', 'gemesin', 'netral', 'best', 'pemersatu', 'mantul'
]
madein_keywords_negative = [
    'goblok', 'anjing', 'bodoh', 'bacot', 'kontol',
    'sampah', 'lonte', 'munafik', 'anjir', 'hujat',
    'ngentot', 'murahan', 'bangsat', 'coli', 'jelek',
    'jijik', 'tolol', 'blok', 'toket', 'pamer',
    'fitnah', 'hina', 'gila', 'bego', 'seksi', 
    'hot', 'drama', 'lol', 'mampus', 'musang', 'montok', 'ngotot',
    'preketek', 'telanjang', 'babi', 'kampungan', 'peang',
    'sombong', 'glodok', 'bohong', 'menipu', 'maniac', 'gajelas', 'bego', 
    'bacol', 'senonoh', 'gaje', 'dajjal', 'apes', 'hancur, ganggu', 'cengeng', 
    'buaya', 'basi', 'gundek', 'kapok', 'sesat', 'aneh', 'tolah', 'mesum', 'pantek', 
    'cupu', 'ceurik', 'halu', 'sinetron', 'ngeyel', 'coeg', 'colmek', 'lebay',
    'karma', 'sokor', 'deportasi', 'miris', 'creeper', 'pascol', 'adult', 'bangke',
    'lebok', 'comberan', 'pea', 'report', 'dungu', 'jancok', 'oon', 'victim', 
    'heran', 'birahi', 'parah', 'nasib', 'aurat', 'tuntut', 'panas', 'paradoks', 'puki',
    'sokong', 'cobaan', 'gandul', 'kejam', 'cebong', 'bangkek', 'goyang'
]

# mengambil dari library di https://github.com/masdevid/ID-OpinionWords
extra_keywords_positive = []
extra_keywords_negative = []

with open('resources/positive.txt', 'r', encoding="utf8") as pos_dict:
    positive_words = pos_dict.readlines()
    positive_words = [w.replace('\n', '').lower() for w in positive_words]
    positive_words = positive_words + madein_keywords_positive
    for w_pos in positive_words:
        w_len = w_pos.split(' ')
        if (len(w_len) == 1):
            if w_pos not in ind_stops:
                w_pos = stemmer.stem(w_pos)
                extra_keywords_positive.append(w_pos)

with open('resources/negative.txt', 'r', encoding="utf8") as neg_dict:
    negative_words = neg_dict.readlines()
    negative_words = [w.replace('\n', '').lower() for w in negative_words]
    negative_words = negative_words + madein_keywords_negative
    for w_neg in negative_words:
        w_len = w_neg.split(' ')
        if len(w_len) == 1:
            if w_neg not in ind_stops:
                w_neg = stemmer.stem(w_neg)
                extra_keywords_negative.append(w_neg)
            
keywords_positive = extra_keywords_positive
keywords_negative = extra_keywords_negative


