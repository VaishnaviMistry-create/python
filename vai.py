import networkx as nx

def recommend_friends(graph, user_id):
    """
    Recommends friends for a given user based on the Jaccard coefficient.
    """
    if user_id not in graph:
        return []
    
    # Get current friends of the user
    user_friends = set(graph.neighbors(user_id))
    
    # Find potential nodes that are not already friends (and not the user itself)
    potential_friends = [
        (user_id, node) for node in graph.nodes() 
        if node != user_id and node not in user_friends
    ]
    
    # Calculate Jaccard coefficient for potential connections
    predictions = nx.jaccard_coefficient(graph, potential_friends)
    
    # Sort recommendations by score in descending order
    recommendations = sorted(predictions, key=lambda x: x[2], reverse=True)
    
    # Return recommendations with a score greater than 0
    return [(rec[1], rec[2]) for rec in recommendations if rec[2] > 0]

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Initialize social network graph
    social_network = nx.Graph()
    
    # 2. Add friendships (edges)
    social_network.add_edges_from([
        ('Alice', 'Bob'), 
        ('Alice', 'Charlie'),
        ('Bob', 'Charlie'), 
        ('Bob', 'David'),
        ('Charlie', 'David'), 
        ('Charlie', 'Eve'),
        ('David', 'Frank')
    ])

    # 3. Generate recommendations for 'Alice'
    target_user = 'Alice'
    print(f"Friend recommendations for {target_user}:")
    
    results = recommend_friends(social_network, target_user)
    for friend, score in results:
        print(f"👉 Recommended: {friend} (Similarity Score: {score:.2f})")
