class Solution:

    def getTotalIsles(self, map_grid: list[list[str]]) -> int:
        if not map_grid:
            return 0

        num_rows, num_cols = len(map_grid), len(map_grid[0])
        visited_cells = set()
        island_count = 0

        def explore_island(row, col):

            visited_cells.add((row, col))


            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for d_row, d_col in directions:
                new_row, new_col = row + d_row, col + d_col

                if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
                    map_grid[new_row][new_col] == 'L' and (new_row, new_col) not in visited_cells):
                    explore_island(new_row, new_col)

        for row in range(num_rows):
            for col in range(num_cols):
                if map_grid[row][col] == 'L' and (row, col) not in visited_cells:

                    explore_island(row, col)
                    island_count += 1

        return island_count

