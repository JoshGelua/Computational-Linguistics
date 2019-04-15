import networkx as nx
import matplotlib.pyplot as plt


def plot_graph(G, arrows=False):
    """
    G: nx.DiGraph -- graph to plot
    arrows: boolean -- whether or not to display arrows on the directed graph
    
    Plot G, representing edge weights using line width.
    Adapted from code at https://qxf2.com/blog/drawing-weighted-graphs-with-networkx/
    """
 
    #Note: You can also try a spring_layout
    pos=nx.fruchterman_reingold_layout(G)
    nx.draw_networkx_nodes(G,pos)

    # If you want, add labels to the nodes
    labels = {}
    for node_name in G.nodes():
        labels[str(node_name)] =str(node_name)
    nx.draw_networkx_labels(G,pos,labels)
 
    all_weights = []
    # Iterate through the graph nodes to gather all the weights
    for (node1,node2,data) in G.edges(data=True):
        all_weights.append(data['weight']) #we'll use this when determining edge thickness
 
    # Get unique weights
    unique_weights = list(set(all_weights))
 
    # Plot the edges - one by one!
    for weight in unique_weights:
        #4 d. Form a filtered list with just the weight you want to draw
        weighted_edges = [(node1,node2) for (node1,node2,edge_attr) in G.edges(data=True) if edge_attr['weight']==weight]
        #4 e. I think multiplying by [num_nodes/sum(all_weights)] makes the graphs edges look cleaner
        width = weight*len(G)*3.0/sum(all_weights)
        nx.draw_networkx_edges(G,pos,edgelist=weighted_edges,width=width, arrows=arrows)
 
    # Plot the graph
    plt.axis('off')
    plt.show()
