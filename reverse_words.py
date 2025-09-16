# Problem: Reverse the words in a given string.

class Solution:
    def reverse_words(self, s: str) -> str:
        # Two-pointer approach (in-place reversal of words)
        words = s.split()
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        return ' '.join(words)

if __name__ == "__main__":
    s = Solution()
    data = "Mohan Babu University"
    print(f"Original string: {data}")
    print(f"Reversed words string: {s.reverse_words(data)}")