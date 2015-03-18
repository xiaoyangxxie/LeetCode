__author__ = 'xyang'
class number:
    def bitCount(self,n):
        c = 0              #count
        while n > 0:
            n &= n - 1     #remove the low-order bit
            c += 1
        return c

if __name__ == "__main__":
    n = input("n : ")  #input
    f = number()
    result = f.bitCount(n)
    print "the count of one is ", result

