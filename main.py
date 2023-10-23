# Define a function that takes a cost matrix, a start vertex, and a number of cycles as input
def gts2(cost_matrix, start_vertex, num_cycles):
    # Initialize an empty list to store the tour
    tour = []
    # Initialize a set to store the visited vertices
    visited = set()
    # Initialize a variable to store the total cost
    total_cost = 0
    # Initialize a variable to store the current vertex
    current_vertex = start_vertex
    # Add the start vertex to the tour and mark it as visited
    tour.append(current_vertex)
    visited.add(current_vertex)
    # Repeat until all vertices are visited
    while len(visited) < len(cost_matrix):
        # Initialize a variable to store the minimum cost
        min_cost = float('inf')
        # Initialize a variable to store the next vertex
        next_vertex = None
        # Loop through all vertices
        for i in range(len(cost_matrix)):
            # If the vertex is not visited and has a lower cost than the minimum cost
            if i not in visited and cost_matrix[current_vertex][i] < min_cost:
                # Update the minimum cost and the next vertex
                min_cost = cost_matrix[current_vertex][i]
                next_vertex = i
        # Add the next vertex to the tour and mark it as visited
        tour.append(next_vertex)
        visited.add(next_vertex)
        # Update the total cost by adding the minimum cost
        total_cost += min_cost
        # Update the current vertex to be the next vertex
        current_vertex = next_vertex
    # Return to the start vertex by adding the cheapest edge that connects to it
    tour.append(start_vertex)
    total_cost += cost_matrix[current_vertex][start_vertex]
    # Return the tour and the total cost as output
    return tour, total_cost


# Ask the user to enter the cost matrix as a list of lists
cost_matrix = eval(input("Enter the cost matrix as a list of lists: "))

# Ask the user to enter the start vertex as an integer
start_vertex = int(input("Enter the start vertex as an integer: "))

# Ask the user to enter the number of cycles as an integer
num_cycles = int(input("Enter the number of cycles as an integer: "))

# Call the gts2 function with the user-defined input
tour, total_cost = gts2(cost_matrix, start_vertex, num_cycles)

# Print the output
print("The tour is:", tour)
print("The cost is:", total_cost)
