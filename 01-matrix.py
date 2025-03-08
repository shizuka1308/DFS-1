# The code uses BFS to propagate the shortest distances from all 0 cells to their neighboring cells, 
# updating the matrix with the minimum distance to the nearest 0. The algorithm processes each cell once, 
# ensuring an optimal solution.

# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns. We visit each cell once, 
# and each cell's neighbors are processed at most once.
# Space Complexity: O(m * n) for the queue used in BFS and the matrix itself.
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat

        rows, cols = len(mat), len(mat[0])
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0<=nr<rows and 0<=nc<cols and mat[nr][nc] > mat[r][c] + 1:
                        mat[nr][nc] =  mat[r][c] + 1
                        queue.append((nr, nc))

        return mat
