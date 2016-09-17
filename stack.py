class MyStack:
	def __init__(self, *args, **kwargs):
	    super(MyStack, self).__init__(*args, **kwargs)
	    self.stack_storage = []


	def pop(self):
		if len(self.stack_storage) == 0:
			raise IndexError
		return self.stack_storage.pop()

	def push(self,val):
		self.stack_storage.append(val)


class StackQueue:
	def __init__(self, *args, **kwargs):
	    super(StackQueue, self).__init__(*args, **kwargs)
	    self.stack1 = MyStack()
	    self.stack2 = MyStack()
	    self.stack_to_use = 1		

	def pop(self):
		if self.stack_to_use == 1:
			res = self.stack2.pop()
			self.stack_to_use = 2
		else:
			res = self.stack1.pop()
			self.stack_to_use = 1
		return res

	def push(self,val):
		if self.stack_to_use == 1:
			self.stack1.push(val)
			self.stack_to_use = 2
		else:
			self.stack2.push(val)
			self.stack_to_use = 1

if __name__ == "__main__":
	sq = StackQueue()
	print(sq.push(1))
	print(sq.push(2))
	print(sq.push(3))
	print(sq.pop())
	print(sq.push(4))
	print(sq.pop())
	print(sq.pop())
	print(sq.pop())
	print(sq.push(5))
	print(sq.push(6))
