Dfs: 
graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': [], 
    'F': [] 
} 
def dfs(node, goal, visited):   
    if node == goal: 
        return True 
    visited.add(node)     
    for neighbor in graph[node]: 
        if neighbor not in visited: 
            if dfs(neighbor, goal, visited): 
                return True 
    return False 
start = input("Enter start node: ") 
goal = input("Enter goal node: ") 
if dfs(start, goal, set()): 
    print("Goal found!") 
else: 
    print("Goal not found") 
 
 
 
 
 
 
 
dfs Traversal: 
graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': [], 
    'F': [] 
} 
visited = set() 
def dfs(node): 
    if node not in visited: 
        print(node, end=" ") 
        visited.add(node) 
        for neighbor in graph[node]: 
            dfs(neighbor) 
start = input("Enter starting node: 
") 
print("DFS Traversal:") 
dfs(start) 
 
bfs: 
from collections import deque 
graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': [], 
    'F': [] 
} 
def bfs(start, goal): 
    queue = deque([start]) 
    visited = set()   
    while queue: 
        node = queue.popleft() 
        if node == goal: 
            return True         
        if node not in visited: 
            visited.add(node) 
            for neighbor in graph[node]: 
                queue.append(neighbor)     
    return False 
start = input("Enter start node: ") 
goal = input("Enter goal node: ") 
if bfs(start, goal): 
    print("Goal found!") 
else: 
    print("Goal not found") 
 
 
 
bfs traversal: 
from collections import deque 
graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': [], 
    'F': [] 
} 
def bfs(start): 
    queue = deque([start]) 
    visited = set()   
    while queue: 
        node = queue.popleft() 
        if node not in visited: 
            print(node, end=" ") 
            visited.add(node) 
            for neighbor in graph[node]: 
                queue.append(neighbor) 
start = input("Enter starting node: ") 
print("BFS Traversal:") 
bfs(start) 
 
Mc bfs: 
from collections import deque 
def valid(m1, c1, m2, c2): 
    if m1 < 0 or c1 < 0 or m2 < 0 or c2 < 0: 
        return False 
    if (m1 > 0 and m1 < c1) or (m2 > 0 and m2 < c2): 
        return False 
    return True 
def bfs(m, c): 
    start = (m, c, 0)   # (left M, left C, boat: 0=left,1=right) 
    goal = (0, 0, 1) 
    q = deque([(start, [])]) 
    visited = set() 
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)] 
    while q: 
        (ml, cl, b), path = q.popleft() 
        if (ml, cl, b) == goal: 
            return path + [(ml, cl, b)] 
        if (ml, cl, b) in visited: 
            continue 
        visited.add((ml, cl, b)) 
        for m1, c1 in moves: 
            if b == 0: 
                new = (ml-m1, cl-c1, 1) 
                mr, cr = m-(ml-m1), c-(cl-c1) 
            else: 
                new = (ml+m1, cl+c1, 0) 
                mr, cr = m-(ml+m1), c-(cl+c1) 
            if valid(new[0], new[1], mr, cr): 
                q.append((new, path + [(ml, cl, b)])) 
    return None 
m = int(input("Missionaries: ")) 
c = int(input("Cannibals: ")) 
res = bfs(m, c) 
print("\nSolution:") 
if res: 
    for i in res: 
        print(i) 
else: 
    print("No solution") 
 
mcdfs: 
m = int(input("Enter number of Missionaries: ")) 
c = int(input("Enter number of Cannibals: ")) 
def is_valid(state): 
    ml, cl, b, mr, cr = state 
    if ml < 0 or cl < 0 or mr < 0 or cr < 0: 
        return False 
    if ml > 0 and ml < cl: 
        return False 
    if mr > 0 and mr < cr: 
        return False 
    return True 
def dfs(state, goal, visited, path): 
    if state == goal: 
        return path + [state] 
    visited.add(state) 
    ml, cl, b, mr, cr = state 
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)] 
    for m_move, c_move in moves: 
        if b == 0: 
            new_state = (ml - m_move, cl - c_move, 1, 
                         mr + m_move, cr + c_move) 
        else: 
            new_state = (ml + m_move, cl + c_move, 0, 
                         mr - m_move, cr - c_move) 
        if is_valid(new_state) and new_state not in visited: 
            result = dfs(new_state, goal, visited, path + [state]) 
            if result: 
                return result 
    return None 
start = (m, c, 0, 0, 0) 
goal = (0, 0, 1, m, c) 
solution = dfs(start, goal, set(), []) 
print("\nDFS Solution Path:") 
if solution: 
    for s in solution: 
        print(s) 
else: 
    print("No solution exists") 
 
jug: 
from collections import deque 
def bfs(j1, j2, goal): 
    q = deque([((0,0), [])]) 
    visited = set() 
    while q: 
        (x,y), path = q.popleft() 
        if x == goal or y == goal: 
            return path + [(x,y)] 
         
        if (x,y) in visited: 
            continue 
        visited.add((x,y)) 
        moves = [ 
            (j1,y),(x,j2),(0,y),(x,0), 
            (x-min(x,j2-y), y+min(x,j2-y)), 
            (x+min(y,j1-x), y-min(y,j1-x)) 
        ] 
        for m in moves: 
            q.append((m, path+[(x,y)])) 
    return None 
j1 = int(input()) 
j2 = int(input()) 
g = int(input()) 
for s in bfs(j1, j2, g): 
    print(s) 
 
dls: 
def dls(node, goal, depth_limit): 
    if node == goal: 
        return True 
    if depth_limit <= 0: 
        return False 
    graph = { 
        'A': ['B', 'C'], 
        'B': ['D', 'E'], 
        'C': ['F'], 
        'D': [], 
        'E': [], 
        'F': [] 
    } 
    for child in graph.get(node, []): 
        if dls(child, goal, depth_limit - 1): 
            return True 
    return False 
start = input("Enter start node: ") 
goal = input("Enter goal node: ") 
limit = int(input("Enter depth limit: ")) 
if dls(start, goal, limit): 
    print("Goal found within depth limit") 
else: 
    print("Goal not found within depth limit") 
 
 
idds: 
def dls(node, goal, depth_limit):     
    if node == goal: 
        return True 
    if depth_limit <= 0: 
        return False 
    graph = { 
        'A': ['B', 'C'], 
        'B': ['D', 'E'], 
        'C': ['F'], 
        'D': [], 
        'E': [], 
        'F': [] 
    } 
    for child in graph.get(node, []): 
        if dls(child, goal, depth_limit - 1): 
            return True 
    return False 
start = input("Enter start node: ") 
goal = input("Enter goal node: ") 
limit = int(input("Enter depth limit: ")) 
if dls(start, goal, limit): 
    print("Goal found within depth limit") 
else: 
    print("Goal not found within depth limit") 
 
ugs: 
import heapq 
graph = { 
    'A': [('B', 1), ('C', 3)], 
    'B': [('D', 2), ('E', 4)], 
    'C': [('F', 5)], 
    'D': [], 
    'E': [], 
    'F': [] 
} 
def ucs(start, goal): 
    pq = [(0, start)]   # (cost, node) 
    visited = set()   
    while pq: 
        cost, node = heapq.heappop(pq) 
        if node == goal: 
            return cost         
        if node in visited: 
            continue 
        visited.add(node) 
        for neighbor, weight in graph[node]: 
            heapq.heappush(pq, (cost + weight, neighbor)) 
    return None 
start = input("Enter start node: ") 
goal = input("Enter goal node: ") 
result = ucs(start, goal) 
if result is not None: 
    print("Minimum cost:", result) 
else: 
    print("No path found") 
 
alphabeta: 
def alphabeta(depth, node, isMax, values, alpha, beta): 
    if depth == 3: 
        return values[node]     
    if isMax: 
        best = -999 
        for i in range(2): 
            val = alphabeta(depth+1, node*2+i, False, values, alpha, beta) 
            best = max(best, val) 
            alpha = max(alpha, best)             
            if beta <= alpha: 
                break   # pruning 
        return best     
    else: 
        best = 999 
        for i in range(2): 
            val = alphabeta(depth+1, node*2+i, True, values, alpha, beta) 
            best = min(best, val) 
            beta = min(beta, best) 
            if beta <= alpha: 
                break   # pruning 
        return best 
values = [3, 5, 6, 9, 1, 2, 0, -1] 
result = alphabeta(0, 0, True, values, -999, 999) 
print("Optimal value:", result) 
 
nqueen: 
def is_safe(board, row, col, n): 
    for i in range(row): 
        if board[i][col] == 1: 
            return False 
    i, j = row-1, col-1 
    while i >= 0 and j >= 0: 
        if board[i][j] == 1: 
            return False 
        i -= 1 
        j -= 1 
    i, j = row-1, col+1 
    while i >= 0 and j < n: 
        if board[i][j] == 1: 
            return False 
        i -= 1 
        j += 1     
    return True 
def solve(board, row, n): 
    if row == n: 
        return True 
    for col in range(n): 
        if is_safe(board, row, col, n): 
            board[row][col] = 1 
            if solve(board, row + 1, n): 
                return True 
            board[row][col] = 0   # backtrack 
    return False 
n = int(input("Enter value of N: ")) 
board = [[0]*n for _ in range(n)] 
if solve(board, 0, n): 
    print("\nSolution:") 
    for row in board: 
        print(row) 
else: 
    print("No solution exists") 
 
csp: 
from itertools import permutations 
def solve(word1, word2, result): 
    letters = list(set(word1 + word2 + result)) 
    if len(letters) > 10: 
        print("Too many letters!") 
        return 
    for p in permutations(range(10), len(letters)): 
        mapping = dict(zip(letters, p)) 
        if mapping[word1[0]] == 0 or mapping[word2[0]] == 0 or mapping[result[0]] == 0: 
            continue 
        num1 = int("".join(str(mapping[ch]) for ch in word1)) 
        num2 = int("".join(str(mapping[ch]) for ch in word2)) 
        res  = int("".join(str(mapping[ch]) for ch in result)) 
        if num1 + num2 == res: 
            print("\nSolution Found:") 
            print(word1, "=", num1) 
            print(word2, "=", num2) 
            print(result, "=", res) 
            return 
    print("No solution found") 
w1 = input("Enter first word: ").upper() 
w2 = input("Enter second word: ").upper() 
res = input("Enter result word: ").upper() 
solve(w1, w2, res) 
 
 
map: 
regions = ['A', 'B', 'C', 'D'] 
colors = ['Red', 'Green', 'Blue'] 
neighbors = { 
    'A': ['B', 'C'], 
    'B': ['A', 'C', 'D'], 
    'C': ['A', 'B', 'D'], 
    'D': ['B', 'C'] 
} 
def is_valid(region, color, assignment): 
    for neighbor in neighbors[region]: 
        if neighbor in assignment and assignment[neighbor] == color: 
            return False 
    return True 
def backtrack(assignment): 
    if len(assignment) == len(regions): 
        return assignment 
    for region in regions: 
        if region not in assignment: 
            break 
    for color in colors: 
        if is_valid(region, color, assignment): 
            assignment[region] = color 
            result = backtrack(assignment) 
            if result is not None: 
                return result 
            del assignment[region] 
    return None 
solution = backtrack({}) 
print("Color Assignment:") 
print(solution) 
 
sudoku: 
grid = [ 
    [5,3,0,0,7,0,0,0,0], 
    [6,0,0,1,9,5,0,0,0], 
    [0,9,8,0,0,0,0,6,0], 
    [8,0,0,0,6,0,0,0,3], 
    [4,0,0,8,0,3,0,0,1], 
    [7,0,0,0,2,0,0,0,6], 
    [0,6,0,0,0,0,2,8,0], 
    [0,0,0,4,1,9,0,0,5], 
    [0,0,0,0,8,0,0,7,9] 
] 
def is_valid(grid, row, col, num): 
    for i in range(9): 
        if grid[row][i] == num: 
            return False 
    for i in range(9): 
        if grid[i][col] == num: 
            return False 
    start_row = row - row % 3 
    start_col = col - col % 3     
    for i in range(3): 
        for j in range(3): 
            if grid[start_row+i][start_col+j] == num: 
                return False 
    return True 
def solve(grid): 
    for row in range(9): 
        for col in range(9): 
            if grid[row][col] == 0: 
                for num in range(1, 10): 
                    if is_valid(grid, row, col, num): 
                        grid[row][col] = num 
                        if solve(grid): 
                            return True 
                        grid[row][col] = 0   # backtrack 
                return False 
    return True 
if solve(grid): 
    print("Solved Sudoku:") 
    for row in grid: 
        print(row) 
else: 
    print("No solution exists") 