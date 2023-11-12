import Member
from Member import *
import fileinput
import random

class Grouping: 
    ### method for soting input member data ###
    def sortInputs(inputFile):
        # creates a file input stream
        inputFileObj = fileinput.input(inputFile)
        # gets attributes 
        attributeArray = inputFileObj.readline().split()
        # gets weights
        weightArray = []
        data = inputFileObj.readline().split()
        for i in range(len(data)):
            weightArray.append(float(data[i]))
        # initializes the member array
        memberArray = []
        # initializes the avioded combination array
        avoidedCombinationArray = []
        # creates Memeber objects and puts them in an array (memberArray)
        while(True):   
            data = inputFileObj.readline().split()
            # checks if it is the end of the member list (followed by the avoided combinations)
            if (data[0].strip() == 'avoid'):
                # puts the avoided combinations in an array (avoidedCombinationArray)
                while(True):
                    data = inputFileObj.readline().split()
                    # checks if it is the end of the file (break if it is)
                    if (len(data) == 0):
                        inputFileObj.close()
                        break
                    avoidedCombinationArray.append(data)
                break
            name = data[0]
            scoreArray = []
            for i in range(1,len(data)):
                scoreArray.append(float(data[i]))
            member = Member(name, attributeArray, scoreArray, weightArray)
            memberArray.append(member)        
        # sorts memberArray by members' total scores (largest to smallest)   
        memberArray = sorted(memberArray, key = lambda member: member.evaluate(), reverse = True)
        # returns memberArray & avoidedCombinationArray
        return memberArray, avoidedCombinationArray

    ### method for selecting the best group ###
    def returnBestGroup(memberArray, groupSize, avoidCombinationArray):
        # selects the members of the best group by their total scores
        bestGroup = []
        for i in range(groupSize):
            bestGroup.append(memberArray[i])
        # considers the combinations of memebers to be avoided and replaces them with other members
        offset = 0
        i = 0
        while(i < len(avoidCombinationArray)):
            # considers each combination to be avoided
            indexA = Grouping.contain(bestGroup, avoidCombinationArray[i][0])
            indexB = Grouping.contain(bestGroup, avoidCombinationArray[i][1])
            i = i + 1
            if ((indexA >= 0) and (indexB >= 0) and ((groupSize+offset) < len(memberArray))):
                if indexA < indexB:
                    bestGroup[indexB] = memberArray[groupSize+offset]
                else:
                    bestGroup[indexA] = memberArray[groupSize+offset]
                offset = offset + 1
                i = 0 # since the group members are altered, all combinations will be check again
            bestGroup = sorted(bestGroup, key = lambda member: member.evaluate(), reverse = True)
        return bestGroup

    ### method for evenly grouping members ###
    def groupMembers(memberArray, numberOfGroups, avoidedCombinationArray):
        # initilizes the group array
        groupArray = []
        for i in range(numberOfGroups):
            group = []
            groupArray.append(group)
        # arrange the memebers evenly into groups
        for i in range(len(memberArray)):
            groupArray[i%numberOfGroups].append(memberArray[i])
        # considers the combinations of memebers to be avoided and make exchanges between groups
        i = 0
        count = 0
        while (i < numberOfGroups):
            j = 0
            while(j < len(avoidedCombinationArray)):
                # considers each combination to be avoided
                indexA = Grouping.contain(groupArray[i], avoidedCombinationArray[j][0])
                indexB = Grouping.contain(groupArray[i], avoidedCombinationArray[j][1])
                j = j + 1
                if ((indexA >= 0) and (indexB >= 0)):
                    if (i+1)<len(groupArray):
                        if random.random() > 0.5:
                            Grouping.exchange(groupArray[i], indexA, groupArray[i+1], indexA)
                        else:
                            Grouping.exchange(groupArray[i], indexB, groupArray[i+1], indexB)
                    else:
                        if random.random() > 0.5:
                            Grouping.exchange(groupArray[i], indexA, groupArray[i-1], indexA)
                        else:
                            Grouping.exchange(groupArray[i], indexB, groupArray[i-1], indexB)
                    i = 0
                    j = 0
                    count = count+1
            i = i + 1
            # set a threshold to break in case some combinations can not be avoided. 
            if (count > len(memberArray)*40):
                break
        return groupArray

    ### method for checking if a member exists in a group ###
    def contain(group, memberName):
        for i in range(len(group)):
            if group[i].name == memberName:
                return i
        return -1

    ### Method for exchange members bewteen groups ###
    def exchange(groupA, memberRankA, groupB, memberRankB):
        t = groupA[memberRankA]
        groupA[memberRankA] = groupB[memberRankB]
        groupB[memberRankB] = t
        
    ### method for printing an array of persons' data ###
    def printMembers(memberArray):
        for i in range(len(memberArray)):
            print(i+1, memberArray[i].name, memberArray[i].scoreArray, memberArray[i].evaluate())
        print()





    
