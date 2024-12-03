leftList = []
rightList = []

# load the data
with open('input.txt') as f:
    for line in f:
        data = line.split('   ')
        leftList.append(int(data[0]))
        rightList.append(int(data[1]))

# sort lists into ascending order
leftList.sort()
rightList.sort()

# sum the differences between the two lists
sum = 0
for i in range(len(leftList)):
    sum += abs(leftList[i] - rightList[i])

print('Sum', sum)

# calculate the simularity score
score = 0
for i in range(len(leftList)):
    occurs = rightList.count(leftList[i])
    score += occurs * leftList[i]

print('Score', score)