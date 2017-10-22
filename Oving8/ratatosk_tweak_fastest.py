
def main():
    from sys import stdin
    stdin.readline()
    stdin.readline()
    start_node = stdin.readline().strip()
    ratatosk_node = stdin.readline().strip()
    if start_node == ratatosk_node:
        print(0)
        return
    parents = {}
    for line in stdin:
        nodes = line.split()
        parent = nodes.pop(0)
        # hver node får sin forelder
        for kid in nodes:
            parents[kid] = parent
    
    # Starter med å finne ratatosk-noden sin forelder
    # Deretter finner jeg den sin forelder igjen, osv. osv. helt til jeg når startnoden
    # Plusser på 1 på dybden for hver gang
    parent = parents[ratatosk_node]
    depth = 1
    while parent != start_node:
        parent = parents[parent]
        depth += 1
    print(depth)

main()