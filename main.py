import networkx as nx

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    '''
    First example
    1---2
    |   |
    3---4________5______6
         \         \    |
          8___9     \   |
                     \  |
                       7
                       
    Weight of the vertices:
    node 1 = 5
    node 2 = 2
    node 3 = 10
    node 4 = 12
    node 5 = 2
    node 6 = 10
    node 7 = 1
    node 8 = 5
    node 9 = 6
    
    Weight of the edges, Calculated according to the combination of the weights of the two vertices:
    {1,2}=7
    {1,3}=15
    {3,4}=22
    {2,4}=14
    {4,8}=17
    {8,9}=11
    {4,5}=14
    {5,6}=12
    {5,7}=3
    {6,7}=11 
    '''

    #Graph construction
    graph = nx.Graph()

    #Adding vertices
    for i in range(0, 8):
        graph.add_node(i)

    #Adding edges and their weight
    graph.add_edge(1, 2, weight=7)
    graph.add_edge(1, 3, weight=15)
    graph.add_edge(3, 4, weight=22)
    graph.add_edge(2, 4, weight=14)
    graph.add_edge(4, 8, weight=17)
    graph.add_edge(8, 9, weight=11)
    graph.add_edge(4, 5, weight=14)
    graph.add_edge(5, 6, weight=12)
    graph.add_edge(5, 7, weight=3)
    graph.add_edge(6, 7, weight=11)

    #Execution of the algorithm
    edges = nx.max_weight_matching(graph, maxcardinality=False, weight='weight')

    #Print the result
    sum =0
    for v1, v2 in edges:
      dict = graph.get_edge_data(v1, v2)
      sum += dict.get("weight")

    print("First example:\nThe selected match: "+str(edges))
    print("The level of joy: "+str(sum)+"\n")

    '''
    Second example
    1---2
     \  |
      \ |
       3

    Weight of the vertices:
    node 1 = 5
    node 2 = 2
    node 3 = 10

    Weight of the edges, Calculated according to the combination of the weights of the two vertices:
    {1,2}=7
    {1,3}=15
    {3,2}=12
    '''

    #Graph construction
    graph1 = nx.Graph()

    #Adding vertices
    for i in range(0, 3):
        graph1.add_node(i)

    #Adding edges and their weight
    graph1.add_edge(1, 2, weight=7)
    graph1.add_edge(1, 3, weight=15)
    graph1.add_edge(3,2, weight=12)

    # Execution of the algorithm
    edges1 = nx.max_weight_matching(graph1, maxcardinality=False)

    #Print the result
    sum1 = 0
    for v1, v2 in edges1:
        dict1 = graph1.get_edge_data(v1, v2)
        sum1 += dict1.get("weight")

    print("Second example\nThe selected match: " + str(edges1))
    print("The level of joy: "+str(sum1))




