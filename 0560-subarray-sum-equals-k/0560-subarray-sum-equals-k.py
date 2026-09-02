class Solution(object):
    def subarraySum(self, nums, k):
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range (n):
            prefix[i+1] = prefix[i] + nums[i]

        prefix_count = {0:1}
        count = 0
        for current_sum in prefix[1:]:
            needed = current_sum - k
            if needed in prefix_count:
                count+= prefix_count[needed]
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
        return count                