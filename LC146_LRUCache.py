"""
LRU - Least Recently Used 
Application : When the cache memory is getting full and we have more data coming in, we remove the least recently used data from the cache
              We need to maintain an order inorder to find out the least recently used data
             Amazon, Netflix : Recently viewed 

Similar DS :
Ordered dictionary - Python can maintain the order of the keys
Ordered Map - C++
Tree Map - Java

OM and TM are - BST under the hood
TC - Inserting - log n

For implementation:
M1 : 
Basic DS to be used - Any linear data structure which is ordered - array, LinkedList, Stack

We can keep the most recently used object at the head of the Linked List, and if the memory exceeds, we pick the last element
get - O(n)
put - O(n)

M2 : (to improve time complexity)
We can maintain the hashmap :
In case we keep a K:V hashmap, we will not be able to track the order of LRU node
so we use a key : node hashmap, AND inorder to remove the nodes in O(1) TC, we use a doubly linked list
We can keep a dummy tail node to access the last node-> tail.prev 

Keep in mind that you should always process the new node pointers before the other pointers in linked list questions

Initialization :  head and tail will be pointing each other

TC = O(1) for all operations
SC = Linked List + Hashmap =  O(n)
"""

class dLinkNode:
        def __init__(self):
            self.key = 0
            self.val = 0
            self.prev = None
            self.next = None
            
class LRUCache:

    def __init__(self, capacity: int):
        self.nodeMap= {}
        self.head, self.tail = dLinkNode(), dLinkNode()
        self.size = 0
        self.capacity= capacity
        
        # linking head and tail nodes 
        self.head.next = self.tail
        self.tail.prev = self.head
    def removeNode (self, node):
        
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def addNode (self, node):
        
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next = node
        node.next.prev = node
        
    def movetoHead(self, node):
        self.removeNode(node)
        self.addNode(node)
        
    def popTail(self):
        temp = self.tail.prev
        self.removeNode(temp)
        return temp
        
    def get(self, key: int) -> int:
        
        node = self.nodeMap.get(key, None)
        if not node:
            return -1
        
        self.movetoHead(node)
        
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.nodeMap.get(key)
        if not node:
            newNode = dLinkNode()
            newNode.key = key
            newNode.value = value
            
            self.nodeMap[key]=newNode
            self.addNode(newNode)
            
            self.size+=1
            
            if self.size >self.capacity:
                
                tail = self.popTail()
                del self.nodeMap[tail.key]
                self.size -=1
                
        else:
            node.value = value
            self.movetoHead(node)
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)