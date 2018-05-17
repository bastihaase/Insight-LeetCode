#  Given a non-empty array of integers, return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note:

#     You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
#     Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        return counts.most_common(k)


import heapq

class Solution2(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        heap = [(-value, key) for key, value in freq.items()]
        heapq.heapify(heap)
        sol =[]
        for i in range(k):
            sol.append(heapq.heappop(heap)[1])
        return sol
