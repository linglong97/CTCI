class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Tree:
	def __init__(self, val):
		self.root = Node(val)

class minHeap:
	def __init__(self):
		self.heap = [0]
		self.size = 0

	def bubbleup(self, size):
		while size // 2 > 0:
			if self.heap[size//2] > self.heap[size]:
				self.heap[size//2], self.heap[size] = self.heap[size], self.heap[size//2]
			size = size //2

	def insert(self, item):
		self.heap.append(item)
		self.size += 1
		self.bubbleup(self.size)

	def show(self):
		print(self.heap)


m = minHeap()
for item in [8,8, 2, 1, 3 ,2 , 0, 4]:
	m.insert(item)
m.show()

#TODO : heapify, min heap, define TRIE
def heapify(list):
	n = len(list)
	for root in xrange(n//2-1,1, -1):
		val = list[root]
		child = root*2+1
		while child < n:
			if child+1 < n and list[child+1]< list[child]:
				child+= 1
			if val <= list[child]:
				break
			list[child], list[(child-1)//2] = list[(child-1)//2], list[child]
			child = child*2+1
	return list


def inorderTraversal(root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        ans = []
        while 1:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ans
            new = stack.pop()
            ans.append(new.val)
            root = new.right
        return ans
        '''
        stack, ans = [], []
        while stack or root:
        	if root:
        		stack.append(root)
        		root = root.left
        	else:
        		root = stack.pop()
        		ans.append(root.val)
        		root = root.right
        return ans





        '''
def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans
        '''
        stack, ans = [], []
        while stack or root:
        	if root:
        		stack.append(root)
        		ans.append(root.val)
        		root = root.left
        	else:
        		root = stack.pop()
        		root = root.right
        return ans
		'''

def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, ans = [], []
        while stack or root:
            if root:
                stack.append(root)
                ans.append(root.val)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        return list(reversed(ans))

def levelOrder(root):
	if not root:
		return
	ans, level = [], [root]
	while level:
		ans.append([node.val for node in level])
		temp = []
		for node in level:
			temp.append([node.left, node.right])
		level = [node for node in temp if node]
	return ans

def levelOrder2(root):
	ans = []
	levelOrder2helper(root, 0, ans)
	return ans


def levelOrder2helper(root, depth, ans):
	if not root:
		return
	if len(ans) == depth:
		ans.append([])
	ans[depth].append(root.val)
	levelOrder2helper(root.left)
	levelOrder2helper(root.right)

from collections import defaultdict

class Trie:
	def __init__(self):
		self.root = {}

	def insert(self, words):
		for word in words:
			current = self.root
			for letter in word:
				if letter not in current:
					current[letter] = {}
					current = current[letter]
				else:
					current = current[letter]
			

	def show(self):
		print self.root

t = Trie()
t.insert(['abc', 'food', 'abcd', 'see'])
t.show()


