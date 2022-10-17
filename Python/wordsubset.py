class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        target = {}
        for targetWord in words2:
            toAdd = {}
            for letter in targetWord:
                if letter not in toAdd:
                    toAdd[letter] = 1
                else:
                    toAdd[letter] += 1
            
            for letter, occur in toAdd.items():
                if letter in target:
                    target[letter] = max(occur, target[letter])
                else:
                    target[letter] = occur
        
        ret = []
        for a in words1:
            toInclude = True
            for key in target:
                if a.count(key) < target[key]:
                    toInclude = False
                    break
            if toInclude:
                ret.append(a)
        return ret
        
        
