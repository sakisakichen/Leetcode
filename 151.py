class Solution:
    def reverseWords(self, s: str) -> str:

        s.strip()
        new_word = s.split()
        new_word.reverse()
        return' '.join(new_word)

