# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

# Each LED represents a zero or one, with the least significant bit on the right.

# For example, the above binary watch reads "3:25".

# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

# Example:

# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

# Note:

#     The order of output does not matter.
#     The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
#     The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        solutions = []
        settings = [("", num)]

        def conv_minutes(minutes):
            m = int(minutes, 2)
            if m < 10:
                return "0" + str(m)
            return str(m)

        def conv_hours(hours):
            return str(int(hours, 2))

        def convert(bits):
            minutes = bits[:6]
            hours = bits[6:]
            return conv_hours(hours) + ":" + conv_minutes(minutes)



        while settings:
            bits, to_set = settings.pop()
            if to_set == 0:
                solutions.append("0" * (10 - len(bits)) + bits)
            if 10 - len(bits) >= to_set and len(bits) < 11 and to_set > 0:
                if (len(bits) != 3 or bits[0] != "1") and (len(bits) != 9 or bits[:3] != "111"):
                    settings.append(("1" + bits, to_set - 1))
                settings.append(("0" + bits, to_set))
        return [convert(x) for x in solutions]
