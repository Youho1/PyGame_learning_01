# sample_sorted2.py

temp1 = sorted([(0,1), (5,3), (2,4)])
temp2 = sorted([(0,1), (5,3), (2,4)], key = lambda x: x[1])
print(temp1)
print(temp2)