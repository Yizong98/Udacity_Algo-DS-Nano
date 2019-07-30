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
# test case 1:

"""
type the data of block
kaka
Continue Add? 
 yes/no 
yes
type the data of block
baba
Continue Add? 
 yes/no 
gaga
Loop through Blocks: 

At current block, timestamp is 2019-07-29 22:10:37.013763+00:00, data is kaka, previous_hash is 0, current hash is 19929d0debd4cf75da33a3ab7904a1394a3977f9d0535fae33ca2117ead12edd, 			previous block is None, next block is <__main__.Block object at 0x10d19c630>
At current block, timestamp is 2019-07-29 22:10:40.110990+00:00, data is baba, previous_hash is 19929d0debd4cf75da33a3ab7904a1394a3977f9d0535fae33ca2117ead12edd, current hash is c5d16497a55599e82c7fc3bcafc19061821bb8ac3f8c5ed6649eb83032e545f4, 			previous block is <__main__.Block object at 0x10d175a58>, next block is None

"""

# test case 2:

"""
type the data of block
baba
Continue Add? 
 yes/no 
yes
type the data of block
kaka
Continue Add? 
 yes/no 
yes
type the data of block
gaga
Continue Add? 
 yes/no 
yes
type the data of block
shdishfs
Continue Add? 
 yes/no 

Loop through Blocks: 

At current block, timestamp is 2019-07-29 22:11:27.153523+00:00, data is baba, previous_hash is 0, current hash is 8743e965d6d25eb9ca3e323e8e104c8bacf2133b8069458ad345c8df3d1d988d, 			previous block is None, next block is <__main__.Block object at 0x1101b7668> 

At current block, timestamp is 2019-07-29 22:11:30.230782+00:00, data is kaka, previous_hash is 8743e965d6d25eb9ca3e323e8e104c8bacf2133b8069458ad345c8df3d1d988d, current hash is 62f381d06eeb22164d196a559f5a6014a8d0b4fa958ca733b0d2bed01b51e68b, 			previous block is <__main__.Block object at 0x11018fa90>, next block is <__main__.Block object at 0x110195390> 

At current block, timestamp is 2019-07-29 22:11:33.584772+00:00, data is gaga, previous_hash is 62f381d06eeb22164d196a559f5a6014a8d0b4fa958ca733b0d2bed01b51e68b, current hash is fde845b827433525ef5fd476988a3c9fb948cabbba20423ea40c0bde44c4f948, 			previous block is <__main__.Block object at 0x1101b7668>, next block is <__main__.Block object at 0x110195400> 

At current block, timestamp is 2019-07-29 22:11:37.407517+00:00, data is shdishfs, previous_hash is fde845b827433525ef5fd476988a3c9fb948cabbba20423ea40c0bde44c4f948, current hash is d2efc76053eb94aeb2f5fd3226a1b3e82b7c37ae14867fed2fff27dd2ab18064, 			previous block is <__main__.Block object at 0x110195390>, next block is None 

"""

# test case 3:

"""
type the data of block
""
Continue Add? 
 yes/no 
n
Loop through Blocks: 

At current block, timestamp is 2019-07-30 05:47:59.124471+00:00, data is "", previous_hash is 0, current hash is c431824cee78b718cf860459a8c84da69c50f01023fb4f2879e013596cd0793f, 			previous block is None, next block is None 
"""

"""
explanation: 

Effciency: Adding Block operation is O(1), assuming the hash calculation operates at O(1).

Design Choice: Design Block with prev and next, making it easy to reference as a doubly linkedList. 
The Blockchain class integrates the blocks together.
"""











