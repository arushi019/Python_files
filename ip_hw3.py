import string
import math
from GetData2 import *
def offbyK(s1,s2,k):
    """Input: two strings s1,s2, integer k
    Process: if both strings are of same length, the function checks if the
    number of dissimilar characters is less than or equal to k
    Output: returns True when conditions are met otherwise False is returned"""
    if len(s1)==len(s2):
        flag=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                flag=flag+1
        if flag==k:
            return True
        else:
            return False
    else:
        return False
def offbySwaps(s1,s2):
    """Input: two strings s1,s2
    Process: to check if s2 can be obtained by swapping/arranging
    characters in s1(or vice versa)
    Output: return True when above condition is met otherwise return False"""
    extra1=''
    extra2=''
    if len(s1)==len(s2):
        for x in s1:
            if x not in s2:
                extra1=extra1+x
        for y in s2:
            if y not in s1:
                extra2=extra2+y
        if extra1=='' and extra2=='':
            return True
        else:
            return False
    else:
        return False
def offbyKExtra(s1,s2,k):
    """Input: two strings s1,s2 and integer k
    Process: to check if number of extra characters in s2 as compared to s1
    (or vice versa) is equal to k
    Output: return True when above condition is met otherwise return False"""
    flag=0
    extra1=''
    if len(s1)>len(s2):
        for x in s1:
            if x not in s2:
                extra1=extra1+x
            elif s2.count(x)<s1.count(x) and x not in extra1:
                extra1=extra1+x*(s1.count(x)-s2.count(x))
            elif s2.count(x)>s1.count(x):
                flag=-2
                break
    if len(s1)<=len(s2):
        for y in s2:
            if y not in s1:
                extra1=extra1+y
            elif s1.count(y)<s2.count(y) and y not in extra1:
                extra1=extra1+y*(s2.count(y)-s1.count(y))
            elif s1.count(y)>s2.count(y):
                flag=-2
                break
    if flag==-2:
        return False
    elif len(extra1)==k:
        return True
    else:
        return False
def ListOfNearStrings(s,L,k):
    """ Returns a list of all entries in L that are near to s for a given value of k.
    PreC: s is a nonempty string, k is a non-negative integral value and L is
    a list of nonempty strings. """
    L1=[]
    for x in L:
        if s!=x:
            if offbyK(s,x,k) or offbyKExtra(s,x,k) or offbySwaps(s,x):
                L1.append(x)
    L1.sort()
    return L1
def compare_distr(l1,l2,k):
    """L1 and L2 represent two lists, of same size, and containing integers.
    L1 and L2 represent two lists, of same size, and containing integers.
    The function checks if the frequency distributions of the two lists are
    same or not, for a given bin width(class interval). Return True if the
    distributions are same, False, otherwise""" 
    min1=min(l1)
    max1=max(l1)
    min2=min(l2)
    max2=max(l2)
    f1=[]
    f2=[]
    for i in range(min1,max1,k):
        f1.append(0)
    if i==(max1-k):
        f1.append(0)
    for i in range(min2,max2,k):
        f2.append(0)
    if i==(max2-k):
        f2.append(0)
    for y in l1:
        for x in range(min1,(max1+k),k):
            if y>=x and y<(x+k):
                f1[(x-min1)//k]+=1
    for y in l2:
        for x in range(min2,(max2+k),k):
            if y>=x and y<(x+k):
                f2[(x-min2)//k]+=1
    if f1==f2:
        return True
    else:
        return False
