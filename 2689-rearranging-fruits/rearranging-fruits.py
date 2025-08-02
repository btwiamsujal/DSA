class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        freq = Counter(basket1)
        freq.subtract(Counter(basket2))
        to_swap = []
        for fruit_cost, count in freq.items():
            if count % 2:
                return -1
            for _ in range(abs(count) // 2):
                to_swap.append(fruit_cost)
        to_swap.sort()

        min_overall_fruit = min(basket1 + basket2)
        cost = 0
        for i in range(len(to_swap) // 2):

            direct_swap_cost = to_swap[i]
            indirect_swap_cost = 2 * min_overall_fruit

            cost += min(direct_swap_cost, indirect_swap_cost)
        return cost