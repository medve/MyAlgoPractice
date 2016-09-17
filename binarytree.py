class BinaryTreeNode:
    def __init__(self,key,val,parrent=None,left=None,right=None):
        self.val = val
        self.key = key
        self.left = left
        self.right = right
        self.parrent = parrent


class BinaryTree:
    def __init__(self,root=None):
        self.root = root

    def create_node(key,val, parrent=None, right=None, left=None):
        return BinaryTreeNode(key, val, parrent=parrent, 
                              right=right, left=left)

    def search(self,key):
        current_node = self.root
        res = None
        while res is None and current_node is not None:
            if key == current_node.key:
                res = current_node
                continue
            if key > current_node:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return res

    def add(self,key,val):
        current_node = self.root
        parrent_node = None
        while current_node is not None:
            parrent_node = current_node
            if key > current_node.key:
                current_node = current_node.right
            else:
                current_node = current_node.left
        if parrent_node is None:
            self.root = create_node(key,val)
        else:
            new_node = create_node(key,val, parrent=parrent_node)
            if key > parrent_node.key:
                parrent_node.left = new_node
            else:
                parrent_node.right = new_node


    def _transplant(self, new_node, repl_node):
        #копируем родителя
        if new_node is not None:
            new_node.parrent = repl_node.parrent
        #если у целевого узла нет родителя - значит он корень
        #заменяем корень
        if repl_node.parrent is None:
            self.root = repl_node
        #определяем каким поддеревом был целевой узел
        #заменяем старое поддерево, содержавшее узел новым
        elif repl_node is repl_node.parrent.left:
            repl_node.parrent.left = new_node
        else:
            repl_node.parrent.right = new_node

    def remove(self, node):
        if node is None:
            return
        if node.left is None:
            _transplant(node, node.right)
        elif node.right is None:
            _transplant(node, node.left)
        else:
            new_node = get_min(start_node=node.right)
            #перенесем детей нового узла
            #если он не дочерний для удаляемого узла
            if new_node.parrent is not node:
                _transplant(new_node, new_node.right)
                new_node.right = node.right
                new_node.right.parrent = new_node
            #переносим узел
            _transplant(node, new_node)
            new_node.left = node.left
            node.left.parrent = new_node

    def get_min(self, start_node = None):
        current_node = self.root if start_node is None else start_node
        if current_node is None:
            return None
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def get_max(self, start_node = None):
        current_node = self.root if start_node is None else start_node
        if current_node is None:
            return None
        while current_node.right is not None:
            current_node = current_node.right
        return current_node

    def from_list(self,lst):
        for val in lst:
            add(val,val)

    def print_inorder(self, node):
        if node is not None:
            self.print_inorder(node.left)
            print(node.val)
            self.print_inorder(node.right)
