class Member:
    def __init__(self, name, attributeArray, scoreArray, weightArray):
        self.name = name
        self.attributeArray = attributeArray
        self.scoreArray = scoreArray
        self.weightArray = weightArray

    def evaluate(self):
        score = 0.0;
        for i in range(len(self.scoreArray)):
            score += (self.scoreArray[i] * self.weightArray[i])
        return score
        
        
