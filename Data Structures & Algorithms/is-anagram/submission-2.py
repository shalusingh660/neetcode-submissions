class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s.lower())!=len(t.lower()):
            return False
        Anagram ={}
        for ch in s:
            if ch in Anagram:
                Anagram[ch]+=1
            else:
                Anagram[ch] = 1
        for ch in t:
            if ch not in Anagram:
                return False
            else:
                Anagram[ch]-=1
            if Anagram[ch]<0:
                return False
        return True



            
        