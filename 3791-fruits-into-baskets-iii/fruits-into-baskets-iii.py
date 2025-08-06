import bisect
class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
       
        n = len(baskets)
        segment_tree = [0]*(4*n)

        def build(ind, l, r):
            if l==r:
                segment_tree[ind] = baskets[l]
                return
            m = (l+r)//2
            build(2*ind+1, l, m)
            build(2*ind+2, m+1, r)
            segment_tree[ind] = max(segment_tree[2*ind+1], segment_tree[2*ind+2])

        def query(ind, l, r, val):
            if segment_tree[ind] < val:
                return (float('-inf'), -1)
            if l==r:
                return (segment_tree[ind], ind)
            m = (l+r)//2
            left = query(2*ind+1, l, m,val)
            if left[0]>=val:
                return left
            right = query(2*ind+2, m+1, r, val)
            if right[0] >= val:
                return right
            return (float('-inf'), -1)

        def update(ind):
            if ind<0:
                return
            lc = segment_tree[2*ind + 1]
            rc = segment_tree[2*ind + 2]
            segment_tree[ind] = max(lc, rc)
            update((ind - 1)//2)
        build(0, 0, n-1)
        unplaced = 0
        for f in fruits:
            ind = query(0, 0, n-1, f)[1]
            if ind != -1:
                segment_tree[ind] = -1
                update((ind - 1)//2)
            else:
                unplaced += 1
        return unplaced