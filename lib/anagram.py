# your code goes here!

class Anagram:
    def __init__(self,word):
        self.word = word
    
    @property
    def word(self):
        return self.__word 
    
    @word.setter
    def word(self,word):
        self._word = word
        
    def match(self, arr):
        word_arr = sorted(self._word.lower())
        anagrams = [word for word in arr if sorted(word.lower()) == word_arr and word.lower() != self._word.lower()]
        return anagrams
    
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))