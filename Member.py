# 建立建構子(__init__/constructor)"姓名、屬性陣列、分數陣列、權重陣列"
# self:習慣用法，理論上也可以用其他名詞
# member = Member() member是物件(object)，Member是類別(class)，
# 類別下的方法(method)下的括號是參數(parameter)
class Member:
    def __init__(self, name, attributeArray, scoreArray, weightArray):
        self.name = name
        self.attributeArray = attributeArray
        self.scoreArray = scoreArray
        self.weightArray = weightArray
#定義"計算權重"方法
    def evaluate(self):
        score = 0.0;
        for i in range(len(self.scoreArray)):
            score += (self.scoreArray[i] * self.weightArray[i])
        return score
    
        #return:回傳給呼叫evaluate方法的人，我是evaluate(member.evaluate)
        # return同時有結束的意思
    # 等號左邊都是變數

    # scoreArray=[[]]
    # for i in range(num_attributes):
    #     scoreArray.append([])
    #     for j in range(num_scores):
    #         scoreArray[i].append(float(data[i][j]))
   
# class member"負責"計算權重
        
## class A:
##     pass
## class B:
##     pass

## def method():
##     print(1+1)