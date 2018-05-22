#  Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

# According to the example above:

# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        ratios = {}
        for (a, b), ratio in zip(equations, values):
            ratios[(a, b)] = ratio
            ratios[(b, a)] = 1 / ratio
            ratios[(a, a)] = 1.0
            ratios[(b, b)] = 1.0

        not_done = True
        while not_done:
            not_done = False
            to_add = []
            for x in ratios:
                for y in ratios:
                    if x[1] == y[0] and (x[0], y[1]) not in ratios:
                        to_add.append([(x[0], y[1]), ratios[y] * ratios[x]])
                        not_done = True
            for x,y in to_add:
                ratios[x] = y

        results = []
        for a, b in queries:
            if (a, b) in ratios:
                results.append(ratios[a, b])
            else:
                results.append(-1.0)
        return results
