# The code uses Depth-First Search (DFS) to recursively change the color of all connected pixels with the same original color 
# starting from the given coordinates (sr, sc) to the new color. It checks each direction (down, up, right, left) using a 
# directions array.

# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns. Each cell is visited once.
# Space Complexity: O(m * n) due to the recursion stack in the worst case, where the entire image is filled.
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                for dr, dc in directions:  
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == color:
                        dfs(nr, nc)
        dfs(sr, sc)
        return image