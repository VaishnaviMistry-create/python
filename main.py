# MODULE 1: Create Social Network
def create_network():
    graph = {
        'Alice': {'Bob', 'Charlie'},
        'Bob': {'Alice', 'Charlie', 'David'},
        'Charlie': {'Alice', 'Bob', 'David', 'Eve'},
        'David': {'Bob', 'Charlie', 'Frank'},
        'Eve': {'Charlie'},
        'Frank': {'David'}
    }
    return graph


# MODULE 2: Find Potential Friends
def find_potential_friends(graph, user):
    if user not in graph:
        return []

    return [
        person for person in graph
        if person != user and person not in graph[user]
    ]


# MODULE 3: Calculate Similarity
def calculate_similarity(graph, user, person):
    common = len(graph[user] & graph[person])
    total = len(graph[user] | graph[person])

    if total == 0:
        return 0

    return common / total


# MODULE 4: Recommend Friends
def recommend_friends(graph, user):
    potential = find_potential_friends(graph, user)
    results = []

    for person in potential:
        score = calculate_similarity(graph, user, person)

        if score > 0:
            results.append((person, score))

    return sorted(results, key=lambda x: x[1], reverse=True)


# MAIN PROGRAM
network = create_network()

print("Available users:", ", ".join(network.keys()))
user = input("Enter your name: ").strip().title()

if user not in network:
    print("User not found!")
else:
    print("Your friends:", ", ".join(sorted(network[user])))

    results = recommend_friends(network, user)

    print("\nRecommended Friends:")

    if results:
        for person, score in results:
            print(person, "- Similarity Score:", round(score, 2))
    else:
        print("No recommendations available.")
