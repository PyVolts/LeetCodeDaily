def firstUniqChar(self, s):
        counts = collections.Counter(s)
        
        unique = [letter for letter, occurence in counts.items() if occurence == 1]
        
        if not len(unique) > 0:
            return -1
        
        index = len(s)
        
        for letter in unique:
            if s.index(letter) < index:
                index = s.index(letter)
        
      
        return index