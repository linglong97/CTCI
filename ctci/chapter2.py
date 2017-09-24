
class Node:
	def __init__(self,data):
		self.val = data
		self.next = None

class linkedlist:
	def __init__(self,node):
		self.head = node

	def add(self, nodes):
		pointer = self.head
		for node in nodes:
			if not self.head:
				self.head = node
			pointer.next = Node(node)
			pointer = pointer.next

	def print_nodes(self):
		pointer = self.head
		ans = []
		while pointer:
			ans.append(pointer.val)
			pointer = pointer.next
		print ans

	def delete_duplicates(self):
		seen = set()
		pointer = self.head
		while pointer:
			if pointer.val not in seen:
				seen.add(pointer.val)
				prev = pointer
				pointer = pointer.next
			else:
				pointer = pointer.next
				prev.next = pointer

	def delete_duplicates_no_mem(self):
		pass
		#do the previous but without a set	

	def kthtolast(self, k):
		pointer = self.head
		while k > 0:
			pointer = pointer.next
			k -= 1
		copy = self.head
		while pointer:
			pointer = pointer.next
			copy = copy.next
		return copy.val

	def delete_middle(self, node):
		pointer = node.next
		node.val = pointer.val
		node.next = pointer.next


	def reverse_linked_list(self):
		prev = None
		pointer = self.head
		while pointer:
			if not pointer.next:
				self.head = pointer
			after = pointer.next
			pointer.next = prev
			prev = pointer
			pointer = after

	def is_palindrome(self):
		#checks if the ll is palindrome
		stack = []
		pointer = self.head
		if self.head.next:
			fast = self.head.next
		while fast:
			pointer = pointer.next
			fast = fast.next.next
			stack.append(pointer.val)
		if len(stack) % 2 == 1:
			stack.pop()
		while pointer:
			value = stack.pop()
			if pointer.val != value:
				return False
			pointer = pointer.next
		return True

		pass

	def has_cycle(self):
		try:
			pointer = self.head
			fast = self.head.next
			while pointer is not fast:
				pointer = pointer.next
				fast = pointer.next.next
			return True
		except:
			return False

	def get_cycle_node(self):
		slow = self.head
		fast = self.head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		if not fast or not fast.next:
			return None
		slow = self.head
		while slow is not fast:
			slow = slow.next
			fast = fast.next
		return slow

def add_two_linked_lists(ll1, ll2):
	carry = 0
	Dummy = linkedlist(Node(0))
	while ll1.head or ll2.head or carry:
		res = carry
		if ll1.head:
			res += ll1.head.val
			ll1.head = ll1.head.next
		if ll2.head:
			res += ll2.head.val
			ll2.head = ll2.head.next
		Dummy.add([res % 10])
		carry = res // 10
	return Dummy

def getIntersectionNode(headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pointerA = headA
        pointerB = headB
        if not headA or not headB:
            return None
        
        while pointerA is not pointerB:
            if not pointerA:
                pointerA = headB
            else:
                pointerA = pointerA.next
            if not pointerB:
                pointerB = headA
            else:
                pointerB = pointerB.next
        return pointerA



if __name__ == "__main__":
	l = linkedlist(Node(1))
	l.add([1,3,1,5,6,2,8,10])
	l.print_nodes()
	l.reverse_linked_list()
	l.print_nodes()
	p = linkedlist(Node(2))
	p.add([2,3,4])
	q = linkedlist(Node(1))
	q.add([8,2,0])
	d = add_two_linked_lists(p,q)
	d.print_nodes()
	e = linkedlist(Node(1))
	e.add([2,3,4,3,2,1])
	print e.is_palindrome()
