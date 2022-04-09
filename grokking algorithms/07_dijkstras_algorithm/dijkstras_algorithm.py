'''
    6        1
  ------>A ----->
start    ^3       fin
  ------>B ----->
    2        5
'''
# the graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# the costs table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# the parents table
# {child: parent} or {neighbor, directed: not directed} 
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = set()

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# find the lowest-cost nod ethat you haven't processed yet
# print('1', costs)
node = find_lowest_cost_node(costs)
# print('2', costs)
# print(node)
while node is not None:
    cost = costs[node]
    # go through all the neighbors of this node
    neighbors = graph[node]
    # print('neighbors', neighbors)
    for n in neighbors.keys():
        # print('n', n)
        new_cost = cost + neighbors[n]
        # if it's cheaper to get to this neighbor by going through this node...
        if costs[n] > new_cost:
            # ... update the cost for this node
            costs[n] = new_cost
            # print('1parents', parents)
            # this node becomes the new parent for this negihbor
            parents[n] = node
            # print('2parents', parents)
    # mark the node as processed
    processed.add(node)
    # find the next node to process and loop
    # print('3costs', costs)
    # print('processed', processed)
    # print('graph', graph)
    node = find_lowest_cost_node(costs)
    # print('node', node)

print("cost from the start of each node:")
print(costs)
# lowest cost goes from: start => b => a => fin