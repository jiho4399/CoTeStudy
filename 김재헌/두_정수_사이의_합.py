# -*- coding: utf-8 -*-
"""두 정수 사이의 합.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qHBKtDUgZpyBVGyhZQZDo1UBg3MfWC8X
"""

def solution(a, b):
    answer = 0
    if a>b:
        a,b=b,a
    for i in range(a,b+1):
        answer+=i
    return answer