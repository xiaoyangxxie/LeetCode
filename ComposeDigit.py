__author__ = 'xyang'
'''
 There has 1,2,3,4 digit,how many
'''
cnt =0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i !=j and i!=k and j!=k:
                print i*100 + j*10 +k
                cnt += 1
print cnt