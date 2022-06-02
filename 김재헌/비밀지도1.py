# -*- coding: utf-8 -*-
"""비밀지도1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MHDQtRp7yUcpTryVe9ANqCfpkbm7seGl
"""

def solution(n, arr1, arr2):
    new1=[]
    for i in arr1:
      new1.append(str(format(i,'b')).zfill(len(arr1)))
    new2=[]
    for i in arr2:
      new2.append(str(format(i,'b')).zfill(len(arr1)))
    answer=[]
    for j in range(len(str(new1[0]))):
      temp=[]
      for i in range(len(arr1)):
        if new1[j][i]=='0' and new2[j][i]=='0':
          temp.append(' ')
        else:
          temp.append('#')
        a=''.join(temp)
      answer.append(a)
    return answer