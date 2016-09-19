from collections import deque


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def isBalanced(root):
    return balancedHeight(root) >= 0


def balancedHeight(root):
    if not root:
        return 0
    left = balancedHeight(root.left)
    right = balancedHeight(root.right)
    if left < 0 or right < 0:
        return -1
    if left - right > 1 or right - left > 1:
        return -1
    return max(left, right) + 1


def serialize(root):
    s = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            s.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            s.append('null')
    return s


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()

    return root


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    wn = turtle.Screen()
    # Set the window background color
    wn.bgcolor("lightgreen")
    wn.title("Tree Visualizer")
    t = turtle.Turtle()
    t.color("blue")
    t.pensize(3)

    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    s = serialize(root)
    print(s)
    t.hideturtle()
    turtle.mainloop()


if __name__ == '__main__':
    drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7,2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
