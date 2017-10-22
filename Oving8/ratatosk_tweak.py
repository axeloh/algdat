from sys import stdin

# Dybde-først-søk
def dfs(root):
    stack = [root]
    depth = 0
    while True:
        node = stack[-1]
        if node[1]:
            return depth
        if node[0]:
            stack.append(node[0].pop(0))
            depth += 1
        else:
            stack.pop()
            depth -= 1

# Bredde-først-søk
def bfs(root):
    q = [root]
    depth = 0
    while True:
        l = len(q)
        for i in range(l):
            node = q[-1]
            if node[1]:
                return depth
            for child in node[0]:
                q.insert(0, child)
            q.pop()
        depth += 1


def main():
    function = stdin.readline().strip()
    number_of_nodes = int(stdin.readline())
    # En node representeres ved en liste
    # node = [[liste over barn], is_ratatosk]
    nodes = []
    for i in range(number_of_nodes):
        nodes.append([[], False])
    start_node = nodes[int(stdin.readline())]
    ratatosk_node = int(stdin.readline())
    nodes[ratatosk_node][1] = True
    for line in stdin:
        number = line.split()
        temp_node = nodes[int(number.pop(0))]
        for child_number in number:
            temp_node[0].append(nodes[int(child_number)])

    if function == 'dfs':
        print(dfs(start_node))
    elif function == 'bfs':
        print(bfs(start_node))
    elif function == 'velg':
        print(bfs(start_node))


main()