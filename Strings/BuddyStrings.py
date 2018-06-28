
class Solution(object):
    def buddyStrings(self, A, B):
        # If the lengths are not equal, then its not possible.
        if len(A) != len(B):
            return False
        # If the both are equal, then we need to swap the same characters.
        # Also A=ab ; B=ab will fail, so we need additional conditional to check repetitions. (Running out of space !)
        if A == B and len(set(A)) < len(A):
            print(A, B)
            return True
        # Compare each character with every other character and count tuples that don't match.
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        # True if the len of count of such tuples is 2 and a is reverse of b.
        return len(dif) == 2 and dif[0] == dif[1][::-1]

