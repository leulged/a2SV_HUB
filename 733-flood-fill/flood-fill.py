class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        val = image[sr][sc]
        n = len(image)
        m = len(image[0])

        if val == color:
            return image

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m

        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = color 

        while queue:
            row, col = queue.popleft()
            for dx, dy in dir:
                new_row = row + dx
                new_col = col + dy
                if inbound(new_row, new_col) and image[new_row][new_col] == val:
                    image[new_row][new_col] = color
                    queue.append((new_row, new_col))

        return image
