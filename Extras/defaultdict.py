# defaultdict(int) — Safe Frequency Counting
# In a regular Python dictionary d = {}, trying to do d['apple'] += 1 when 'apple' isn't in the dictionary yet throws a KeyError and crashes your code. defaultdict(int) automatically assigns a default value of 0 to any new key you access.

from collections import defaultdict

nums = [10, 20, 10, 30, 10]
freq = defaultdict(int)  # Every new key defaults to 0

for num in nums:
    freq[num] += 1       # No KeyError!

print(freq[10])          # Output: 3
print(freq[99])          # Output: 0 (doesn't crash even though 99 wasn't in nums)


# When to use it: Whenever you are counting occurrences, building adjacency lists for graphs (defaultdict(list)), or grouping items together.