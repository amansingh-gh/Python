#symmetric_difference
l = {1,2,3,4,5,6,7,8,9}
l1 = {45,87,5,1,8,475,1}
l2 = l.symmetric_difference(l1)
print(l2)

#symmetric_difference_update
l = {1,2,3,4,5,6,7,8,9}
l1 = {45,87,5,1,8,475,1}
l.symmetric_difference_update(l1)
print(l)