from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree


'''
Needs Python 3+

'''


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


class Solution(object):
    def preOrder(self, root):

        curr = root

        if curr is None:
            return

        s = []
        s.append(root)

        while len(s) > 0:
            node = s.pop()
            print(node.val)

            if node.right is not None:
                s.append(node.right)

            if node.left is not None:
                s.append(node.left)

    def postOrder1(self, root):
        '''
        Using 2 stacks to print a tree in post order
        '''
        curr = root

        s = []
        answer = []

        if curr is None:
            return

        s.append(curr)

        # while the stack is not empty, add left and then right elements to stack.
        while len(s) > 0:
            top = s.pop()
            answer.append(top)
            if top.left is not None:
                s.append(top.left)
            if top.right is not None:
                s.append(top.right)

        while len(answer) > 0:
            print(answer.pop().val)

    def postOrder2(self, root):
        '''
        Using 1 stack to print a tree in post order.
        source : https://www.youtube.com/watch?v=xLQKdq0Ffjg
        '''
        curr = root
        s=[]

        while (curr is not None) or (len(s) > 0):
            # Keep moving left until end of nodes
            if curr is not None:
                s.append(curr)
                curr = curr.left
            else:
                # if node has no right node (also no left node) , then pop from stack and print
                temp = s[-1].right
                if temp is None:
                    temp = s.pop()
                    print(temp.val)
                    # if stack is not empty and popped node equals the right node of its parent
                    while len(s) > 0 and temp == s[-1].right:
                        temp = s.pop()
                        print(temp.val)
                else:
                    curr = temp

    def inOrder(self, root):

        curr = root
        s = []
        done = None

        while not done:
            # Keep moving left until no nodes
            if curr is not None:
                s.append(curr)
                curr = curr.left
            else:
                # If stack is not empty, pop and print. Set current as last element's right.
                if len(s) > 0:
                    curr = s.pop()
                    print(curr.val)
                    curr = curr.right
                else:
                    done = True


if __name__ == '__main__':
    s = Solution()
    print(" # In Order #")
    s.inOrder(deserialize('[1,2,3,null,null,4,null,null,5]'))
    print(" # Pre Order #")
    s.preOrder(deserialize('[1,2,3,null,null,4,null,null,5]'))
    print(" # Post Order : Using 2 stacks #")
    s.postOrder1(deserialize('[1,2,3,null,null,4,null,null,5]'))
    print(" # Post Order : Using 1 stack #")
    s.postOrder2(deserialize('[1,2,3,null,null,4,null,null,5]'))