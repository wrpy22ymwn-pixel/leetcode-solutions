#Задача: найти самый длинный общий префикс строк в массиве
#Идея: идем по позициям слева направо,пока символ совпадает во всех строках
#длина строк<=200,поэтому r<200
class Solution(object):
    def longestCommonPrefix(self, strs):
        r=0
        if len(strs[0])==0:
            return ''
        if len(strs)==1 and len(strs[0])!=0:
            return strs[0]
        while r<200:
            if all(len(strs[i])>r for i in range(len(strs))) and all(strs[i][r]==strs[i+1][r] for i in range(len(strs)-1))==1:
                r+=1
            else:
                if r==0:
                    return ''
                return(strs[0][:r]) 
            return strs[0]#Если все строки длиной 200
