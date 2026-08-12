class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0

        def expand(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1":
                    # dfs
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for dx, dy in directions:
                        expand(row + dx, col + dy)
                        grid[row][col] = "0"
                    return True
            else:
                return False
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if expand(row, col):
                    count += 1

        return count




            
        
        