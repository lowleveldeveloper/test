li=[4,12,15,16,22,11]
lii=[12,27,42,57,72,87]

x=0
for i in range(0,len(li)):
    x = x+li[i]*(lii[i]-55.7)**2
print(x)


"""
71.4, 71.5, 72.8, 73.1

75.1, 75.2, 75.2, [75.9], 77.4, 77.8

78.7, (79.1, 79.2), 81.6, 81.8

82.5, 82.9, 83.1, 83.2, 83.4, 83.7, 83.8, [83.9], 85.6, 85.9

86.0, (86.2, 88.0), 88.2

90.8
"""
"""
22, 25,
34, 35,
41, 41, 46, 46, 46, 47, 49,
54, 54, 59,
60


8,
13, 14, 16, 16,
23, 28,
33, 39,
61
"""
"""
60,
64, 64,
68,
71,
73,
76, 76, 76,
80, 80,
84, 84,
88, 88, 88,
92, 92, 92,
96
"""

