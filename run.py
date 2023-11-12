import Grouping
from Grouping import *

# sorts input member data
inputFile = 'data.txt'
(memberArray, avoidedCombinationArray) = Grouping.sortInputs(inputFile)

# prints the sorted member data
print('All members (sorted by their total scores):')
Grouping.printMembers(memberArray)

# prints the combination of members to be avoided
print('Combination of members to be avoided:')
for i in range(len(avoidedCombinationArray)):
    print(i+1, avoidedCombinationArray[i][0], avoidedCombinationArray[i][1])
print()

# selects and prints the best group (with 3 members)
bestGroup = Grouping.returnBestGroup(memberArray, 3, avoidedCombinationArray)
print('The best group (with 3 members):')
Grouping.printMembers(bestGroup)

# arranges the members into 3 groups and prints the 3 groups
groupArray = Grouping.groupMembers(memberArray, 3, avoidedCombinationArray)
print('Evenly arranged 3 groups:')
for i in range(3):
    Grouping.printMembers(groupArray[i])

