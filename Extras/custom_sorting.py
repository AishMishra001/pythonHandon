# arr.sort(key=lambda x: x[1]) — Custom Sorting
# By default, if you sort a list of pairs/tuples [[1, 5], [2, 3], [4, 1]], Python sorts by the first element (x[0]). Using key=lambda x: x[1] tells Python: "For each item x, look at index 1 (the second element) to decide the sort order."

intervals = [[1, 5], [2, 3], [4, 1]]

# Sort by the SECOND element (index 1) in ascending order
intervals.sort(key=lambda x: x[1])

print(intervals)         # Output: [[4, 1], [2, 3], [1, 5]]

# When to use it: Greedy and interval problems (like Merge Intervals or Minimum Platforms in your Phase 1 list) where you need to sort by end time, weight, or value instead of the first element. (Tip: Use -x[1] if you want descending order).