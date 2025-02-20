from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # 方法一 sotrted :T O(N log N), S O(1)
        # ana_dict = defaultdict(list)

        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     ana_dict[sorted_word].append(word)

        # return list(ana_dict.values())
    #    ana_dict變成這樣
    #     {
    #     'aet': ['eat', 'tea', 'ate'],
    #     'ant': ['tan', 'nat'],
    #     'abt': ['bat']
    # }
        
        # 方法二 counter :T O(1), S O(1)
        ana_dict = defaultdict(list)
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char) - ord('a')] += 1
            count = tuple(count)   #（list）无法作为字典的键，因为它是可变的
            ana_dict[count].append(word) #append 任何類型可以添加到list, exted只能延長list

        return list(ana_dict.values())
