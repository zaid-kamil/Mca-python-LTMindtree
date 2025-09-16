# Problem: Check if a given string is a palindrome.
class Solution:
    def is_palindrome(self, s: str) -> bool:
        # Two-pointer approach to check for palindrome
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
if __name__ == "__main__":
    s = Solution()
    data = "racecar"
    print(f"Original string: {data}")
    print(f"Is palindrome: {s.is_palindrome(data)}")

    data2 = "hello"
    print(f"Original string: {data2}")
    print(f"Is palindrome: {s.is_palindrome(data2)}")