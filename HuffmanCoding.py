import sys

class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
    def __lt__(self,other):
        return not str(self.val).isnumeric()

# traverse and collect
def DFS(node,curr,direction,coding):
    if not node:
        return
    left = DFS(node.left,curr+direction,"0",coding)
    right = DFS(node.right,curr+direction,"1",coding)
    if not left and not right:
        curr += str(direction)
        coding[node.val] = curr
    return node

def huffman_encoding(data):
    from collections import Counter
    import heapq
    if len(set(data)) <= 1:
        return "0", TreeNode(data)
    fre_lst = [(val,TreeNode(key)) for key, val in Counter(data).items()]
    heapq.heapify(fre_lst)
    # get coding
    while len(fre_lst) > 1:
        elem1, elem2 = heapq.heappop(fre_lst), heapq.heappop(fre_lst)
        temp_val = elem1[0]+elem2[0]
        InsertNode = TreeNode(temp_val)
        InsertNode.left,InsertNode.right  = elem1[1], elem2[1]
        heapq.heappush(fre_lst,(temp_val,InsertNode))
    coding = {}
    DFS(fre_lst[0][1],"","",coding)
    chars = [coding[val] for val in data]
    return "".join(chars), fre_lst[0][1]

def huffman_decoding(data,tree):
    if not tree.left and not tree.right:
        return tree.val
    ans = []
    track = 0
    while track < len(data):
        temp = tree
        while temp.left or temp.right:
            if data[track] == "0":
                temp = temp.left
            else:
                temp = temp.right
            track += 1
        ans.append(temp.val)
    return "".join(ans)

"""
explanation: 

Effciency:

Space Complexity:

obvious O(n) since we need to store each character in the string in a tree.

Time Complexity:

1. The encoding process takes O(nlogn), heapify takes O(n), during each iteration in the loop it takes O(logn) for heappush, 
and it takes n iterations. The DFS takes approximately O(n) where n is the number of characters in the string, which are the leaves
in the tree. The while loop dominate the asymptotic terms, giving O(nlogn).

2. The decoding process takes approximately O(n) where n is the number of characters in the string, which are the leaves
in the tree. This is because the sum of nodes before the leaf level is approximately the number of leaves, giving O(2n)=O(n).


Design Choice:
I use a heap for maintaining minimum elements, and design a treeNode class for storing data for encoding and decoding.
"""


if __name__ == "__main__":
    codes = {}

    a_great_sentence = input("type your words \n")

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))