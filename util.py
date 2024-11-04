def gini_func(values):
    if len(values) == 0:
        return 0
    gini = 1
    for count in values.value_counts():
        gini -= (count/len(values))**2
    return gini

def print_tree(node, width=8, level=0):
    if node:
        print_tree(node.right, width, level + 1)
        print(' ' * width * level + '-> Leaf Value: ' + str(node.val))
        if node.col:
            print(' ' * width * level + '   Split: ' + str(node.col) + " < " + str(node.cut))
        else:
            print(' ' * width * level + '   Split: ' + str(node.col))
        print(' ' * width * level + '   Node: ' + str(node.samples))
        print_tree(node.left, width, level + 1)