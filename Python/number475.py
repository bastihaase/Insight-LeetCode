# Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

# Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

# So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

# Note:

#     Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
#     Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
#     As long as a house is in the heaters' warm radius range, it can be warmed.
#     All the heaters follow your radius standard and the warm radius will the same.

import bisect

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()

        closest_heaters = [0] * len(houses)

        for i, house in enumerate(houses):
            left = bisect.bisect_left(heaters, house)
            if left >= len(heaters):
                closest_heaters[i] = abs(heaters[-1] - house)
            else:
                if heaters[left] < house:
                    closest_heaters[i] = min(abs(heaters[left] - house), abs(heaters[left + 1] - house) )
                else:
                    if left == 0:
                        closest_heaters[i] = abs(heaters[0] - house)
                    else:
                        closest_heaters[i] = min(abs(heaters[left - 1] - house), abs(heaters[left] - house) )
        return max(closest_heaters)
