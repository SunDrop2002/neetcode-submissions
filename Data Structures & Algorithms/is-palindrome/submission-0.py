import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        translator = str.maketrans('', '', string.punctuation)
        clean_text = s.translate(translator).replace(" ", "")
        return clean_text.lower() == clean_text[::-1].lower()
        






        