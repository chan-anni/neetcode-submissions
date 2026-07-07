class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''.join(ch.lower() for ch in s if ch.isalnum())
        # removes the '' and joins the letter if the letter/num is only letter or num

        print(st)
        i = 0
        k = len(st)-1

        while (i < k):
            if (st[i] != st[k]):
                 return False
            i += 1
            k -= 1
        return True