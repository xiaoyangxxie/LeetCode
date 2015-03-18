__author__ = 'xyang'

class Solution:
    def singlenumber(self,astr):
        counts={}
        order=[]
        for s in astr:
            if s in counts:
                counts[s]+=1
            else:
                counts[s] =1
                order.append(s)
        for i in order:
            if counts[i] == 1:
                return i


f = Solution()
intarray = [2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
singen = f.singlenumber(intarray)
print singen