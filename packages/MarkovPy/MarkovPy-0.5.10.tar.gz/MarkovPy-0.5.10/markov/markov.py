import random
import re
from collections import Counter, namedtuple

re_smiley = re.compile(r'[8;:=%][-oc*^]?[)(D\/\\]')
re_smiley_reversed = re.compile(r'[)(D\/\\][-oc*^]?[8;:=%]')
re_smiley_asian = re.compile(r'\^[o_.]?\^')
extra_smileys = ['<3', '\o', '\o/', 'o/']
re_smileys = [re_smiley, re_smiley_reversed, re_smiley_asian]
re_url = re.compile(r'(?:(?:https?|ftp):\/\/.*)')

Word = namedtuple('Word', ['word', 'score'])


def is_smiley(word):
    '''
    check if ``word`` is a smiley

    :param word: word to check
    :type word: str

    :return: result of check
    :rtype: bool
    '''
    if word in extra_smileys:
        return True
    for re_smiley in re_smileys:
        if re_smiley.match(word):
            return True
    return False


def prepare_line(line):
    '''
    split words to line, lower words, add newlines and remove invalid chars

    :param line: line to prepare
    :type line: str
    :return: prepared line
    :rtype: list
    '''
    words_ = line.split()
    words = []
    for word_ in words_:
        word = None
        # prevent smileys and urls from getting lower'd
        if is_smiley(word_) or re_url.match(word_):
            word = word_
        else:
            word = word_.lower()
        if len(word) >= 1:
            words.append(word)
    words.append('\n')
    return words


class MarkovPy:

    def __init__(self, store):
        '''
        :param store: a compatible markov-store
        :type store: class
        '''
        self.store = store

    def _best_known_word(self, words):
        '''
        Find the best known word out of `words`

        :param words: list of words
        :type words: list

        :returns: best known word
        :rtype: str
        '''
        # build word_relations-list (word, relation-count)
        word_relations = [
            Word(word, score=self.store.relation_count(word))
            for word in words if word in self.store
        ]
        # no known words => None
        if not word_relations:
            return None
        # only one word in the list => return
        if len(word_relations) == 1:
            return word_relations[0].word
        else:
            # sort words by relation-count
            sorted_word_relations = sorted(
                word_relations, key=lambda x: x.score, reverse=True
            )
            highest_num = sorted_word_relations[0].score
            # add word with most relations to the best_known_words-list
            best_known_words = [sorted_word_relations[0].word]
            for word, num in word_relations:
                # check if word has the same (highest) relation-count
                if num == highest_num:
                    # => add it to the best_known_words-list
                    best_known_words.append(word)
                else:
                    break
            # choose a random word from that list
            if len(best_known_words) == 1:
                return best_known_words[0]
            else:
                return random.choice(best_known_words)

    def learn(self, line, prepared=False):
        '''
        learn from ``line``

        :param line: line to add
        :param prepared: line was already split to words
        :type line: str
        :type prepared: bool
        '''
        if prepared:
            words = line
        else:
            words = prepare_line(line)
        for i in range(0, len(words)):
            curr_word = words[i]
            if len(words) <= i + 1:
                break
            next_word = words[i + 1]
            self.store.insert(curr_word, next_word)

    def reply(self, start, min_length=5, max_length=10, prepared=False):
        '''
        generated a reply to ``start``

        :param min_length: minimal length of reply
        :param max_length: max length of reply
        :param prepared: line was already split to words
        :type min_length: int
        :type max_length: int
        :type prepared: bool
        :return: response
        :rtype: str
        '''
        if prepared:
            start_words = start
        else:
            start_words = prepare_line(start)
        # gen answer
        start_word = self._best_known_word(start_words)
        if not start_word:
            return None
        if min_length > max_length:
            max_length = min_length + 1
        length = random.randint(min_length, max_length)
        answer = [start_word]
        while len(answer) < length:
            # key doesn't exist => no possible next words
            if answer[-1] not in self.store:
                break
            possible_words = self.store.next_words(answer[-1])
            if len(possible_words) == 1:
                word = list(possible_words)[0][0]
            else:
                # sort random word but weight
                word = random.choice(
                    list(Counter(dict(possible_words)).elements())
                )
            # choosen word == line-end => break
            if word == '\n':
                break
            # add to answer
            answer.append(word)
        if len(answer) < min_length:
            # dont return too short answers
            return None
        return ' '.join(answer)

    def process(self, line, learn=True, reply=True):
        '''
        process ``line``

        :param line: line to process
        :param learn: learn from line
        :param reply: reply to line (and return answer)
        :type line: str
        :type learn: bool
        :type reply: bool
        :return: answer if ``reply``
        :rtype: str
        '''
        prepared_line = prepare_line(line)
        if learn:
            self.learn(prepared_line, prepared=True)
        if reply:
            return self.reply(prepared_line, prepared=True)

    def __len__(self):
        return len(self.store)
