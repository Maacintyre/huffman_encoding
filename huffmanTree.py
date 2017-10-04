class node:

    def __init__(self, character='', frequency=0):
        self.left = None
        self.right = None
        self.head = None
        self.character = character
        self.frequency = frequency

    def addLeft(self, pNode):
        if self.left is None:
            self.left = pNode
            self.frequency += self.left.frequency
            self.head = self
            return True
        else:
            return False

    def addRight(self, pNode):
        if self.right is None:
            self.right = pNode
            self.frequency += self.right.frequency
            self.head = self
            return True
        else:
            return False


class huffmanTree:

    def __init__(self):
        self.head = None
        self.currentNode = None

    def left(self):
        if self.currentNode.left is not None:
            self.currentNode = self.currentNode.left
            return True
        else:
            return False

    def right(self):
        if self.currentNode.right is not None:
            self.currentNode = self.currentNode.right
            return True
        else:
            return False

    def up(self):
        if self.currentNode.head is not None:
            self.currentNode = self.currentNode.head
            return True
        else:
            return False

    def head(self):
        if self.head is not None:
            self.currentNode = self.head
            return True
        else:
            return False


def main():
    testNode1 = node()
    testNode1.right = node()
    testNode1.right.count = 1
    print 'Output of test node 1: {}'.format(testNode1.right.count)

    testNodeKeep = node()
    testNodeForget = node()
    testNodeForget.count = 55
    testNodeKeep.right = testNodeForget
    print ('Output of test node keep before forget: {}'.format(testNodeKeep.right.count))
    testNodeForget = None
    try:
        print 'Output of test node forget: {}'.format(testNodeForget.count)
    except AttributeError:
        print 'Test Node Forget does not have count'
    try:
        print 'Output of test node keep after forget: {}'.format(testNodeKeep.right.count)
    except AttributeError:
        print 'Test Node Keep has lost it\'s value'


if __name__ == '__main__':
    main()
