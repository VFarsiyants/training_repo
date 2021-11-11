

def find_lowest_cost(costs_dict: dict, processed: list):
    min_price = float('inf')
    min_price_node = None
    for k, v in costs_dict.items():
        if v < min_price and k not in processed:
            min_price = v
            min_price_node = k
    return min_price_node


def find_lowest_cost_ways(graph, parents, costs):
    processed = []
    node = find_lowest_cost(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost(costs, processed)
    return costs


if __name__ == "__main__":
    graph = dict()
    graph['start'] = {}
    graph['a'] = {}
    graph['b'] = {}
    graph['start']['a'] = 6
    graph['start']['b'] = 2
    graph['a']['fin'] = 1
    graph['b']['a'] = 3
    graph['b']['fin'] = 5
    graph['fin'] = {}
    infinity = float('inf')
    costs = dict()
    costs['a'] = 6
    costs['b'] = 2
    costs['fin'] = infinity
    parents = dict()
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['fin'] = None
    print(find_lowest_cost_ways(graph, parents, costs)['fin'])
