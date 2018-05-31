# Jack and Daniel are friends. They want to encrypt their conversations so that they can save themselves from interception by a detective agency so they invent a new cipher.

# Every message is encoded to its binary representation. Then it is written down times, shifted by bits. Each of the columns is XORed together to get the final encoded string.

# If and it looks like so:

# 1001011     shift 0
# 01001011    shift 1
# 001001011   shift 2
# 0001001011  shift 3
# ----------
# 1110101001  <- XORed/encoded string s

# Now we have to decode the message. We know that . The first digit in so our output string is going to start with . The next two digits are also , so they must have been XORed with . We know the first digit of our shifted string is a as well. Since the digit of is , we XOR that with our and now know there is a in the position of the original string. Continue with that logic until the end.

# Then the encoded message and the key are sent to Daniel.

# Jack is using this encoding algorithm and asks Daniel to implement a decoding algorithm.
# Can you help Daniel implement this?

# Input Format

# The first line contains two integers and , the length of the original decoded string and the number of shifts.
# The second line contains the encoded string consisting of ones and zeros.

# Constraints




# It is guaranteed that is valid.

# Output Format

# Return the decoded message of length , consisting of ones and zeros.

# Sample Input 0

# 7 4
# 1110100110

# Sample Output 0

# 1001010

# Explanation 0

# 1001010
#  1001010
#   1001010
#    1001010
# ----------
# 1110100110

# Sample Input 1

# 6 2
# 1110001

# Sample Output 1

# 101111

# Explanation 1

# 101111
#  101111
# -------
# 1110001

def cipher(k, s):
    n = len(s) - (k - 1)
    res = ""
    others = [0] * (k - 1)
    index = 0
    for x in s:
        s = reduce(lambda x,y: x ^ y, others)
        current = s ^ int(x)
        others[index] = current
        index = (index + 1) % (k - 1)
        res += str(current)
        if len(res) == n:
            break
    return res
