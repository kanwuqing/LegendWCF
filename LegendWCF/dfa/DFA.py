#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:zbt
# editor:kanwuqing
# datetime:2020-03-16 11:53
# software: PyCharm
import shutil
import logging
class SensitiveFilter:
    '''敏感词检测器

    Args:
        path: 敏感词库位置
    '''
    def __init__(self, path: str = r'legendwcf\dfa\ban.txt'):
        # 读取敏感词库内容
        self.path = path
        self.load()
    
    def load(self):
        with open(self.path, 'r', encoding = 'utf-8') as f:
            self.sensitiveWordList = f.read().split('\n')
        #得到敏感词字典
        self.sensitiveWordMap = self.initSensitiveWordMap(self.sensitiveWordList)
        logging.info('敏感词检测初始化完成')
    
    def add(self, word):
        if word not in self.sensitiveWordList:
            shutil.copy(self.path, f'{self.path}.bk1')
            self.sensitiveWordList.append(word)
            with open(self.path, 'w', encoding = 'utf-8') as f:
                f.write('\n'.join(self.sensitiveWordList))
            self.load()
    
    def delete(self, word):
        if word in self.sensitiveWordList:
            shutil.copy(self.path, f'{self.path}.bk1')
            self.sensitiveWordList.remove(word)
            with open(self.path, 'w', encoding = 'utf-8') as f:
                f.write('\n'.join(self.sensitiveWordList))
            self.load()
    
    #构建敏感词库
    def initSensitiveWordMap(self,sensitiveWordList):
        sensitiveWordMap = {}
        # 读取每一行，每一个word都是一个敏感词
        for word in sensitiveWordList:
            nowMap=sensitiveWordMap
            #遍历该敏感词的每一个特定字符
            for i in range(len(word)):
                keychar=word[i]
                wordMap=nowMap.get(keychar)
                if wordMap !=None:
                    #nowMap更新为下一层
                    nowMap=wordMap
                else:
                    #不存在则构建一个map,isEnd设置为0，因为不是最后一个
                    newNextMap={}
                    newNextMap["isEnd"]=0
                    nowMap[keychar]=newNextMap
                    nowMap=newNextMap
                #到这个词末尾字符
                if i==len(word)-1:
                    nowMap["isEnd"]=1
        #print(sensitiveWordMap)
        return sensitiveWordMap

    def checkSensitiveWord(self,txt,beginIndex=0):
        '''
        :param txt: 输入待检测的文本
        :param beginIndex: 输入文本开始的下标
        :return: 返回敏感词字符的长度
        '''
        nowMap=self.sensitiveWordMap
        sensitiveWordLen=0 #敏感词的长度
        containChar_sensitiveWordLen=0 #包括特殊字符敏感词的长度
        endFlag=False #结束标记位

        for i in range(beginIndex,len(txt)):
            char=txt[i]

            nowMap=nowMap.get(char)
            if nowMap != None:
                sensitiveWordLen+=1
                containChar_sensitiveWordLen+=1
                #结束位置为True
                if nowMap.get("isEnd")==1:
                    endFlag=True
            else:
                break
        if  endFlag==False:
            containChar_sensitiveWordLen=0
        #print(sensitiveWordLen)
        return containChar_sensitiveWordLen

    def getSensitiveWord(self,txt) -> list:
        '''返回所有敏感词
        '''
        cur_txt_sensitiveList=[]
        #注意，并不是一个个char查找的，找到敏感词会i增强敏感词的长度
        for i in range(len(txt)):
            length=self.checkSensitiveWord(txt,i)
            if length>0:
                word=txt[i:i+length]
                cur_txt_sensitiveList.append(word)
                i=i+length-1 #出了循环还要+1 i+length是没有检测到的，下次直接从i+length开始

        return cur_txt_sensitiveList

    def replaceSensitiveWord(self,txt: str,replaceChar='*') -> str:
        '''对字符串进行去敏

        Args:
            txt: 待去敏的文本
            replaceChar: 替换字符
        
        Returns:
            去敏后的字符串
        '''
        Lst=self.getSensitiveWord(txt)
        #print(Lst)
        for word in Lst:
            replaceStr=len(word)*replaceChar
            txt=txt.replace(word,replaceStr)

        return txt

if __name__ == "__main__":
    str="鸡你太美"
    Filter=SensitiveFilter()
    replaceStr=Filter.replaceSensitiveWord(str)
    print(replaceStr)
    Filter.add('你好')
    replaceStr=Filter.replaceSensitiveWord('你好')
    print(replaceStr)
    Filter.delete('你好')
    replaceStr=Filter.replaceSensitiveWord('你好')
    print(replaceStr)

