def goat_grass_cheetah_dfs():
    """
    Solve the goat-grass-cheetah river crossing problem using DFS.
    
    A farmer needs to cross a river with a goat, a bundle of grass, and a cheetah.
    The boat can only carry the farmer and at most one item.
    If left unsupervised:
    - The goat will eat the grass
    - The cheetah will eat the goat
    
    Returns:
        A list of states representing the solution path
    """
    # Define initial state: (farmer, goat, grass, cheetah)
    # 0 = start, 1 = finish
    initial_state = (0, 0, 0, 0)
    goal_state = (1, 1, 1, 1)
    
    # Define valid state function
    def is_valid(state):
        farmer, goat, grass, cheetah = state
        
        # Check if goat and grass are on the same bank without the farmer
        if goat == grass and farmer != goat:
            return False
        
        # Check if goat and cheetah are on the same bank without the farmer
        if goat == cheetah and farmer != goat:
            return False
        
        return True
    
    # Define successor function
    def get_successors(state):
        farmer, goat, grass, cheetah = state
        successors = []
        
        # Farmer crosses alone
        new_state = (1 - farmer, goat, grass, cheetah)
        if is_valid(new_state):
            successors.append(new_state)
        
        # Farmer takes goat
        new_state = (1 - farmer, 1 - goat, grass, cheetah)
        if is_valid(new_state):
            successors.append(new_state)
        
        # Farmer takes grass
        new_state = (1 - farmer, goat, 1 - grass, cheetah)
        if is_valid(new_state):
            successors.append(new_state)
        
        # Farmer takes cheetah
        new_state = (1 - farmer, goat, grass, 1 - cheetah)
        if is_valid(new_state):
            successors.append(new_state)
        
        return successors
    
    # DFS using a stack
    visited = set()
    stack = [(initial_state, [])]
    
    while stack:
        state, path = stack.pop()  # Pop from the end (LIFO - stack behavior)
        
        if state == goal_state:
            return path + [state]
        
        if state in visited:
            continue
        
        visited.add(state)
        
        for successor in get_successors(state):
            if successor not in visited:
                stack.append((successor, path + [state]))
    
    return None  # No solution found

# Run the demonstration
if __name__ == "__main__":
    print("Goat-Grass-Cheetah Problem Solution (DFS):")
    solution = goat_grass_cheetah_dfs()
    if solution:
        bank_names = ["Start", "Finish"]
        for i, state in enumerate(solution):
            farmer, goat, grass, cheetah = state
            print(f"Step {i}:")
            print(f"  Farmer: {bank_names[farmer]} bank")
            print(f"  Goat: {bank_names[goat]} bank")
            print(f"  Grass: {bank_names[grass]} bank")
            print(f"  Cheetah: {bank_names[cheetah]} bank")
            print()
    else:
        print("No solution found")