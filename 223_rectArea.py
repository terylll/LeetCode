class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        x = [A, E, C, G]
        y = [B, D, F, H]

        x.sort()
        y.sort()

        x_min = min(A, E, C, G)
        x_max = max(A, E, C, G)

        y_min = min(B, D, F, H)
        y_max = min(B, D, F, H)

        res = (y_max - y_min) * (x_max - x_min)

        res -= (x[1] - x_min) * (y[1] - y_min)
        res -= (x_max - x[2]) * (y_max - y[2])

        return res

