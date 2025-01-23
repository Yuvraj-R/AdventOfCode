import heapq
from collections import defaultdict, deque


def solve_reindeer_maze(filename="input.txt"):
    # --- Step 1: Parse the Grid ---
    with open(filename, 'r') as f:
        grid = [list(line.rstrip('\n')) for line in f]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Locate Start 'S' and End 'E'
    start_pos = None
    end_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_pos = (r, c)
            elif grid[r][c] == 'E':
                end_pos = (r, c)

    if not start_pos or not end_pos:
        raise ValueError(
            "Grid must contain both 'S' (start) and 'E' (end) positions.")

    # --- Step 2: Define Directions ---
    # Directions: 0=East, 1=South, 2=West, 3=North
    direction_offsets = [
        (0, 1),   # East
        (1, 0),   # South
        (0, -1),  # West
        (-1, 0)   # North
    ]

    # --- Step 3: Initialize Dijkstra's ---
    INF = float('inf')
    dist = [[[INF for _ in range(4)] for _ in range(cols)]
            for _ in range(rows)]
    predecessors = defaultdict(list)  # state -> list of predecessor states

    sr, sc = start_pos
    start_dir = 0  # Facing East
    dist[sr][sc][start_dir] = 0

    # Priority queue: (cost, r, c, d)
    heap = [(0, sr, sc, start_dir)]

    while heap:
        current_cost, r, c, d = heapq.heappop(heap)

        # If we reached the end, no need to continue popping higher cost states
        if (r, c) == end_pos:
            # However, continue to find all predecessors for Part 2
            pass

        # If this cost is not the current best, skip
        if current_cost > dist[r][c][d]:
            continue

        # --- Explore Transitions ---

        # 1. Move Forward
        dr, dc = direction_offsets[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
            new_cost = current_cost + 1
            if new_cost < dist[nr][nc][d]:
                dist[nr][nc][d] = new_cost
                heapq.heappush(heap, (new_cost, nr, nc, d))
                predecessors[(nr, nc, d)] = [(r, c, d)]
            elif new_cost == dist[nr][nc][d]:
                predecessors[(nr, nc, d)].append((r, c, d))

        # 2. Turn Left
        left_dir = (d - 1) % 4
        new_cost = current_cost + 1000
        if new_cost < dist[r][c][left_dir]:
            dist[r][c][left_dir] = new_cost
            heapq.heappush(heap, (new_cost, r, c, left_dir))
            predecessors[(r, c, left_dir)] = [(r, c, d)]
        elif new_cost == dist[r][c][left_dir]:
            predecessors[(r, c, left_dir)].append((r, c, d))

        # 3. Turn Right
        right_dir = (d + 1) % 4
        new_cost = current_cost + 1000
        if new_cost < dist[r][c][right_dir]:
            dist[r][c][right_dir] = new_cost
            heapq.heappush(heap, (new_cost, r, c, right_dir))
            predecessors[(r, c, right_dir)] = [(r, c, d)]
        elif new_cost == dist[r][c][right_dir]:
            predecessors[(r, c, right_dir)].append((r, c, d))

    # --- Part 1: Find the Lowest Score ---
    # Find the minimal cost among all directions at the end position
    er, ec = end_pos
    min_cost = min(dist[er][ec])

    print(min_cost)  # Part 1 Output

    # --- Step 4: Collect All Tiles on Any Optimal Path ---

    # Find all states at end position with minimal cost
    end_states = []
    for d in range(4):
        if dist[er][ec][d] == min_cost:
            end_states.append((er, ec, d))

    # BFS to traverse predecessors and collect all unique tiles
    tiles_on_best_paths = set()
    visited_states = set()
    queue = deque(end_states)

    while queue:
        state = queue.popleft()
        if state in visited_states:
            continue
        visited_states.add(state)

        r, c, d = state
        tiles_on_best_paths.add((r, c))

        for pred in predecessors.get(state, []):
            queue.append(pred)

    print(len(tiles_on_best_paths))  # Part 2 Output


# Example usage:
if __name__ == "__main__":
    solve_reindeer_maze("input.txt")
