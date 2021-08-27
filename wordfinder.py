"""Word Finder: finds random words from a dictionary."""

from random import randint

class WordFinder:
    '''finds random words from a dictionary

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    '''

    def __init__(self, file_path):
        '''initialize instance of word finder to find random words from a file'''
        self.file_path = file_path
        self.word_lst = []
        self.word_list()
        print(f'{len(self.word_lst)} words read')

    def __repr__(self):
        '''string description about this instance of the WordFinder class'''
        return f'<WordFinder filepath = {file_path}>'


    def word_list(self):
        '''open file, read file, and return a list of all words included in the file'''
        file = open(self.file_path, 'r')
        lines = file.readlines()
        self.word_lst = [line.strip() for line in lines]
        file.close()


    def random(self):
        '''picks a random word from the previously generated word list'''
        rand_index = randint(0, len(self.word_lst)-1)
        return self.word_lst[rand_index]







class SpecialWordFinder(WordFinder):
    '''extends class WordFinder to handle blank lines and comment characters
    
    >>> swf = SpecialWordFinder("otherwords.txt")
    4 words read

    >>> swf.random() in ["apple", "parsnips", "kale", "mango"]
    True

    >>> swf.random() in ["apple", "parsnips", "kale", "mango"]
    True

    >>> swf.random() in ["apple", "parsnips", "kale", "mango"]
    True
    
    '''

    def __init__(self, file_path):
        '''initialize instance of Special Word Finder Class to find words in more complicated files'''
        super().__init__(file_path)

    def word_list(self):
        '''open file, read file, handle comments or non-word lines, return list of valid words'''
        file = open(self.file_path, 'r')
        lines = file.readlines()
        for line in lines:
            if line[0] == '#':
                continue
            elif not line.strip():
                continue
            else:
                self.word_lst.append(line.strip())
        file.close()

