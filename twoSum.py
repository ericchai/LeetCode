# 问题一：给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """   
        
        """
        # 方法一:
        for j,num in enumerate(nums):
            for k,second_num in enumerate(nums[j+1:]):
                if num+second_num == target:
                    return list((j,k+j+1))
        return False
        """ 
        
        # 方法二:
        list_num=[]
        for j,num in enumerate(nums):
            temp=target-num
            if temp in nums:
                if j!=nums.index(temp):
                    list_num.append(j)
                    list_num.append(nums.index(temp))
                    list_num.sort()
                    return list_num
        return False
    
# 问题二：给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # step1:先按链表顺序把节点的值转成字符，并且整合成一个字符串
        s1,s2=('','')
        while l1.next != None:
            s1 += ''.join(str(l1.val))
            l1=l1.next
        else:
            s1 += ''.join(str(l1.val))
        
        while l2.next != None:
            s2 += ''.join(str(l2.val))
            l2=l2.next
        else:
            s2 += ''.join(str(l2.val))
           
        # step2:按照反序的规则转成整型相加后再转成str而后反序，之后用循环提取出来
        node_list=[]     
        for str_node in str(int(s1[::-1])+int(s2[::-1]))[::-1]:
            node_list.append(ListNode(int(str_node)))
        
        # step3:形成链表
        for i,node in enumerate(node_list[:-1]):
            node_list[i].next=node_list[i+1]
           
        return node_list[0]   
   

# 问题七：给定一个 32 位有符号整数，将整数中的数字进行反转。
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp=int(str(x)[::-1]) if x >= 0 else int(str(x)[::-1][:-1])*(-1)
        if temp > pow(2,31)-1 or temp< pow(2,31)*(-1):
            return 0
        else:
            return temp
 

# 问题九：判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。    
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return x >= 0 and str(x)[::1] == str(x)[::-1]
