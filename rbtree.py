# coding=utf-8
import graph

RED = 1
BLACK = 0


# 红黑树属性:
# 1. 每个结点为红或黑.
# 2. 根结点是黑色.
# 3. 叶子（空结点为黑色）.
# 4. 红色结点的两个孩子都是黑色.
# 5. 对于每个结点, 从结点到每个后代叶子的路径包含相同数量的黑色节点.


# 红黑树结点
class RBNode(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.p = None
        self.color = RED


class RBTree(object):
    def __init__(self):
        self.root = None

    # 左旋转(从右向左)
    # x的右孩子y变为x的父亲，y的左孩子变为x的右孩子

    def leftRotate(self, x):
        y = x.right

        x.right = y.left  # y的左孩子变为x的右孩子
        if y.left != None:
            y.left.p = x

        y.p = x.p  # x原先的父亲指向y
        if x.p == None:
            self.root = y
        elif x == x.p.left:
            x.p.right = y
        else:
            x.p.right = y

        y.left = x  # y变为x的父亲
        x.p = y

    # 右旋转(从左向右)
    # x的左孩子y变为x的父亲，y的右孩子变为x的左孩子

    def rightRotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != None:  # y的右孩子变为x的左孩子
            y.right.p = x

        y.p = x.p
        if x.p == None:
            self.root = y
        elif x.p.left == x:
            x.p.left = y
        else:
            x.p.right = y

        y.right = x
        x.p = y

    # 插入节点，每次插入的节点均为红色
    def insert(self, z):
        # z 为要插入的结点
        y = None
        x = self.root  # x 指向root
        while x != None:  # 找到z的父亲y
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.p = y
        if y == None:  # 如果是没有数据则为根结点，否则插入到对应位置
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = None
        z.right = None
        z.color = RED
        self.insertFixUp(z)

    # 维护红黑树
    def insertFixUp(self, z):
        while self.root != z and z.p.color == RED:
            # 如果z的父亲是祖父的左孩子
            if self.root != z.p and z.p == z.p.p.left:
                y = z.p.p.right  # z的祖父结点的右节点y为z的叔叔(可能为空结点)

                # case 1: 如果z的叔叔为红色
                # 1. 将父亲和叔叔都改为黑色
                # 2. 祖父结点改为红色
                # 3. z重新指向他的祖父结点
                if y != None and y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p

                # case 2: z的叔叔y是黑色并且z是父亲的右孩子
                # case 3: z的叔叔y是黑色并且z是父亲的左孩子
                else:
                    # 如果是case 2，z指向z的父亲, 进行一次左旋，转化为case 3
                    if z == z.p.right:
                        z = z.p
                        self.leftRotate(z)
                    # case 3:
                    # 1. 父亲结点变为黑色
                    # 2. 祖父结点变为红色
                    # 3. 以祖父结点为基准进行一次右旋
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.rightRotate(z.p.p)

            # 如果z的父亲是祖父的右孩子
            elif self.root != z.p and z.p == z.p.p.right:
                y = z.p.p.left  # z的祖父结点的左节点y为z的叔叔(可能为空结点)
                # case 1: 如果z的父亲和叔叔都为红色
                # 1. 将它们都改为黑色
                # 2. 祖父结点改为红色
                # 3. z重新指向他的祖父结点
                if y != None and y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p

                # case 2: z的叔叔y是黑色并且z是父亲的左孩子
                # case 3: z的叔叔y是黑色并且z是父亲的右孩子
                else:
                    # 如果是case 2，z指向z的父亲, 进行一次右旋，转化为case 3
                    if z == z.p.left:
                        z = z.p
                        self.rightRotate(z)
                    # case 3:
                    # 1. 父亲结点变为黑色
                    # 2. 祖父结点变为红色
                    # 3. 以祖父结点为基准进行一次左旋
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.leftRotate(z.p.p)
            else:
                break

        self.root.color = BLACK


if __name__ == '__main__':
    tree = RBTree()
    tree.insert(RBNode(26))
    tree.insert(RBNode(17))
    tree.insert(RBNode(41))
    # tree.insert(RBNode(14))
    # tree.insert(RBNode(21))
    # tree.insert(RBNode(30))
    # tree.insert(RBNode(47))
    # tree.insert(RBNode(10))
    # tree.insert(RBNode(16))
    # tree.insert(RBNode(19))
    # tree.insert(RBNode(23))
    # tree.insert(RBNode(28))
    # tree.insert(RBNode(38))
    # tree.insert(RBNode(7))
    # tree.insert(RBNode(12))
    # tree.insert(RBNode(15))
    # tree.insert(RBNode(20))
    # tree.insert(RBNode(35))
    # tree.insert(RBNode(39))
    # tree.insert(RBNode(3))

    g = graph.Graph()
    g.GraphTree(tree)
    g.Render()
