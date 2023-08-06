import pickle
from os.path import exists

from markov.markov import Word
from markov.stores import Store


class Pickle(Store):
    def __init__(self, path='markov.pickle'):
        self.path = path
        self.store = {}
        if exists(self.path):
            try:
                self.store = pickle.load(open(self.path, 'br'))
            except EOFError:
                print('Couldn\'t find data in', self.path)

    def commit(self):
        pickle.dump(self.store, open(self.path, 'bw+'))

    def insert(self, word, next_word):
        if word in self.store:
            if next_word in self.store[word]:
                self.store[word][next_word] += 1
            else:
                self.store[word][next_word] = 1
        else:
            self.store[word] = {next_word: 1}
        self.commit()

    def relation_count(self, word):
        return len(self.store.get(word, {}))

    def next_words(self, target_word):
        return [
            Word(word, score)
            for word, score in self.store.get(target_word, {}).items()
        ]

    def clear(self):
        self.store = {}
        self.commit()

    def __contains__(self, word):
        return word in self.store

    def __len__(self):
        return len(self.store)
