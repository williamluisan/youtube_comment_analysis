# global variables
keywords_positive = [
    'langgeng', 'semangat', 'mantul', 'gemesin', 'natural',
    'kepo', 'lucu', 'romantis', 'perfect', 'congrats',
    'finally', 'terharu', 'merinding', 'sabar', 'smart',
    'salut', 'santuy', 'mirip', 'bijak', 'ikhlas'
]
keywords_negative = [
    'goblok', 'anjing', 'bodoh', 'bacot', 'kontol',
    'sampah', 'lonte', 'munafik', 'anjir', 'hujat',
    'ngentot', 'murahan', 'bangsat', 'coli', 'jelek',
    'jijik', 'tolol', 'blok', 'toket', 'pamer',
    'fitnah', 'hina', 'gila', 'bego', 'seksi', 
    'hot', 'drama', 'lol'
]

class Keywords:
    def load(self, type):
        if type == 'positive':
            return keywords_positive
        else:
            return keywords_negative