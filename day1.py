from collections import defaultdict

list1 = []
list2 = []
count2 = defaultdict(int)

#parsing
with open('input.txt', 'r') as file:
    for line in file:
        fields = line.strip().split('   ')
    
        list1.append(int(fields[0]))
        list2.append(int(fields[1]))
        count2[int(fields[1])] += 1

#a
list1.sort()
list2.sort()

sum = 0

for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

print(sum) 

#b
simScore = 0
for i in range(len(list1)):
    simScore += list1[i] * count2[list1[i]]

print(simScore)
        