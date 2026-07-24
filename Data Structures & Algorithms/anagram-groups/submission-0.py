class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Group ={}
        for word in strs:
            key="".join(sorted(word))
            if key not in Group:
                Group[key] = []
            Group[key].append(word)
        return list(Group.values()) 
        