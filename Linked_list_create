class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class SLinkedList:
    def __init__(self):
      self.headval = None
    def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.val)
         printval = printval.next
         
l1= SLinkedList()
l1.headval = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
l1.headval.next = node2
node2.next = node3

l1.listprint()
