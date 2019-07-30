import hashlib
import datetime

class Block:

	def __init__(self, timestamp, data, previous_hash):
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.calc_hash()
		self.prev = None
		self.next = None

	def calc_hash(self):
	      sha = hashlib.sha256()

	      hash_str = "timestamp: {}, data: {}, previous_hash:{}"\
	      .format(self.timestamp,self.data,self.previous_hash).encode('utf-8')

	      sha.update(hash_str)

	      return sha.hexdigest()


class Blockchain:
	def __init__(self):
		self.previous_hash = 0
		self.curr = None
		self.head = None
		self.size = 0
	def addBlocks(self,data):
		newBlock = Block(datetime.datetime.now(datetime.timezone.utc), data, self.previous_hash)
		self.previous_hash = newBlock.hash
		if not self.head:
			self.head = newBlock
			self.curr = self.head
		else:
			self.curr.next = newBlock
			newBlock.prev = self.curr
			self.curr = self.curr.next
		self.size += 1
	def getSize(self):
		return self.size
	def getPrevHash(self):
		return self.previous_hash

if __name__ == "__main__":
	print("Demonstration of Blockchain: \n")
	bc = Blockchain()
	keep_going = True
	while keep_going:
		data = input("type the data of block\n")
		bc.addBlocks(data)
		keep_going = input("Continue Add? \n yes/no \n") == "yes"
	print("Loop through Blocks: \n")
	curr = bc.head
	while curr:
		print("At current block, timestamp is {}, data is {}, previous_hash is {}, current hash is {}, \
			previous block is {}, next block is {} \n"\
			.format(curr.timestamp, curr.data, curr.previous_hash, curr.hash, curr.prev if curr.prev else "None",\
			 curr.next if curr.next else "None")
			)
		curr = curr.next


"""
explanation: 

Effciency: Adding Block operation is O(1), assuming the hash calculation operates at O(1).

Design Choice: Design Block with prev and next, making it easy to reference as a doubly linkedList. 
The Blockchain class integrates the blocks together.
"""











