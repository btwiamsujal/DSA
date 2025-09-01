class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        max_heap = []

        def calculate_gain(p, t):
            return float(t - p) / (t * (t + 1))

        for p, t in classes:
            gain = calculate_gain(p, t)
            heapq.heappush(max_heap, (-gain, p, t))

        for _ in range(extraStudents):
            neg_gain, p, t = heapq.heappop(max_heap)

            p_new = p + 1
            t_new = t + 1

            new_gain = calculate_gain(p_new, t_new)

            heapq.heappush(max_heap, (-new_gain, p_new, t_new))

        total_ratio_sum = 0
        for neg_gain, p, t in max_heap:
            total_ratio_sum += float(p) / t

        return total_ratio_sum / len(classes)