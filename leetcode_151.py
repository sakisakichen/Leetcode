class Solution:
    def reverseWords(self, s: str) -> str:



        # 方法一 时间复杂度O(N), 空间复杂度O(N)：单词列表new_word 占用线性大小的额外空间
        s.strip()
        new_word = s.split()
        new_word.reverse()
        return' '.join(new_word)

"""
    reverse for list, [::-1]給string
        [::-1] 是創建一個新的反轉列表，不修改原來的列表。
        reverse() 是原地反轉列表，會直接修改原列表，而不會返回新的列表
"""