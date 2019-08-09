# global variables
bigrams_positive = [
    ('friend', 'goals'), ('baik', 'banget'),
    ('so', 'beautiful'), ('panutan', 'aku'),
    ('fav','couple'), ('keep', 'enjoy'),
    ('sehat', 'selalu'), ('the', 'best'),
    ('sehat', 'terus'), ('ikut', 'seneng'),
    ('realita', 'kehidupan'), ('sharing','positif')
]
bigrams_negative = [
    ('bodo', 'amat'), ('hapus', 'aja'),
    ('main', 'game'), ('report', 'aja'),
    ('mampus', 'lu'), ('bacot', 'anjing'),
    ('sabar', 'aja')
]

class Bigrams:
    def load(self, type):
        if type == 'positive':
            return bigrams_positive
        else:
            return bigrams_negative