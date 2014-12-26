class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        # Tee-hee
        return bin(int(a, 2) + int(b, 2))[2:]
