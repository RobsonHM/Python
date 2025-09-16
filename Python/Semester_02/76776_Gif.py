import random
from collections import deque
from PIL import Image, ImageDraw

WIDTH = 31
HEIGHT = 31
CELL_SIZE = 20 

CARVING_DIRS = [(-2, 0), (2, 0), (0, -2), (0, 2)]

BFS_DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def generate_maze(width, height):

    maze = [['#'] * width for _ in range(height)]

    def carve(x, y):
        maze[y][x] = ' '  
        
        dirs_to_try = CARVING_DIRS[:]
        random.shuffle(dirs_to_try)
        
        for dx, dy in dirs_to_try:
            nx, ny = x + dx, y + dy 

            if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == '#':

                maze[ny - dy // 2][nx - dx // 2] = ' '
                carve(nx, ny) 
    carve(1, 1)
    
    maze[1][0] = 'S'  
    maze[height - 2][width - 1] = 'E'  
    return maze

def bfs_with_frames_single(maze, start, goal):
    queue = deque([start])
    visited = set([start])
    came_from = {}
    frames = [draw_maze(maze, visited, start, goal)]

    while queue:
        current_x, current_y = queue.popleft()
        for dx, dy in BFS_DIRS:
            next_x, next_y = current_x + dx, current_y + dy
            if 0 <= next_x < len(maze[0]) and 0 <= next_y < len(maze):
                if maze[next_y][next_x] in (' ', 'E', 'S') and (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    came_from[(next_x, next_y)] = (current_x, current_y)
                    queue.append((next_x, next_y))
                    frames.append(draw_maze(maze, visited, start, goal))

                    if (next_x, next_y) == goal:
                     
                        path = []
                        current = goal
                        while current != start:
                            path.append(current)
                            current = came_from[current]
                        path.append(start)
                        path.reverse()

                        
                        frames.append(draw_maze(maze, visited.union(set(path)), start, goal))
                        
                        return frames, visited
    return frames, visited

def bfs_with_frames(maze):
    start = (1, 0)
    goal = (len(maze[0]) - 1, len(maze) - 2)  

    frames1, _ = bfs_with_frames_single(maze, start, goal)  

    return frames1

def draw_maze(maze, visited, start, goal):
   
    img_width = len(maze[0]) * CELL_SIZE
    img_height = len(maze) * CELL_SIZE
    img = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(img)

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            top_left = (x * CELL_SIZE, y * CELL_SIZE)
            bottom_right = ((x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE)

            color = (0, 0, 0) if maze[y][x] == '#' else (255, 255, 255)
            draw.rectangle([top_left, bottom_right], fill=color)

    for x, y in visited:
        draw.rectangle(
            [x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE],
            fill=(200, 200, 255) 
        )

    sx, sy = start
    draw.rectangle([sx * CELL_SIZE, sy * CELL_SIZE, (sx + 1) * CELL_SIZE, (sy + 1) * CELL_SIZE], fill="blue")

    gx, gy = goal
    draw.rectangle([gx * CELL_SIZE, gy * CELL_SIZE, (gx + 1) * CELL_SIZE, (gy + 1) * CELL_SIZE], fill="green")

    return img

if __name__ == "__main__":

    maze = generate_maze(WIDTH, HEIGHT)

    frames = bfs_with_frames(maze)

    if frames: 
        frames[0].save("bfs_maze.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)
        print("Animação do labirinto BFS salva como bfs_maze.gif")
    else:
        print("Nenhum frame gerado para a animação.")

