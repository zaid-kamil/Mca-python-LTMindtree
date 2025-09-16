# Problem: Reverse a given string.
class Solution:
    def reverse_string(self, s: str) -> str:
        # Two-pointer approach (in-place reversal)
        left, right = 0, len(s) - 1
        s_list = list(s) 
        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return ''.join(s_list)
    
if __name__ == "__main__":
    s = Solution()
    data = "Mohan Babu University"
    print(f"Original string: {data}")
    print(f"Reversed string: {s.reverse_string(data)}")