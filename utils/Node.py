'''
定义node类：
    Node：用于链表
    TreeNode：用于树
'''
class Node(object):
    def __init__(self,value=None):
        self.value = value
        self.next = None

class TreeNode(object):
    def __init__(self,value=None):
        self.value = value
        self.right = None
        self.left = None