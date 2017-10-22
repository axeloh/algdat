from sys import stdin


class Node:
    def __init__(self):
        self.children = []
        self.ratatosk = False

# Dybde-først-søk
def dfs(root):
    stack = [root]
    depth = 0
    while len(stack) > 0:
        node = stack[-1]
        if node.ratatosk:
            return depth
        if node.children != []:
            stack.append(node.children.pop(0))
            depth += 1
        else:
            stack.pop()
            depth -= 1


# Bredde-først-søk
def bfs(root):
    if root.ratatosk:
        return 0
    q = []
    for child in root.children:
        q.insert(0, child)
    depth = 1
    while True:
        l = len(q)
        for i in range(l):
            node = q[-1]
            if node.ratatosk:
                return depth
            for child in node.children:
                q.insert(0, child)
            q.pop()
        depth += 1


def main():
    function = stdin.readline().strip()
    number_of_nodes = int(stdin.readline())
    nodes = []
    for i in range(number_of_nodes):
        nodes.append(Node())
    start_node = nodes[int(stdin.readline())]
    ratatosk_node = nodes[int(stdin.readline())]
    ratatosk_node.ratatosk = True
    for line in stdin:
        number = line.split()
        temp_node = nodes[int(number.pop(0))]
        for child_number in number:
            temp_node.children.append(nodes[int(child_number)])

    if function == 'dfs':
        print(dfs(start_node))
    elif function == 'bfs':
        print(bfs(start_node))
    elif function == 'velg':
        print(bfs(start_node))


main()