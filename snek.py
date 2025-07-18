import random
import curses

def generate_maze(height, width):
    # Ensure odd dimensions for maze
    maze_h, maze_w = (height // 2) * 2 + 1, (width // 2) * 2 + 1
    maze = [['#'] * maze_w for _ in range(maze_h)]
    stack = [(1, 1)]
    maze[1][1] = ' '
    while stack:
        y, x = stack[-1]
        neighbors = []
        for dy, dx in [(-2,0),(2,0),(0,-2),(0,2)]:
            ny, nx = y+dy, x+dx
            if 1 <= ny < maze_h-1 and 1 <= nx < maze_w-1 and maze[ny][nx] == '#':
                neighbors.append((ny, nx, dy, dx))
        if neighbors:
            ny, nx, dy, dx = random.choice(neighbors)
            maze[y+dy//2][x+dx//2] = ' '
            maze[ny][nx] = ' '
            stack.append((ny, nx))
        else:
            stack.pop()
    return maze

def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    # Leave a border for safety
    maze_h, maze_w = (sh-2) | 1, (sw-2) | 1
    maze = generate_maze(maze_h, maze_w)
    # Place snake at (1,1), food at (maze_h-2, maze_w-2)
    snake = [[1, 1]]
    food = [maze_h-2, maze_w-2]
    key = curses.KEY_RIGHT
    stdscr.timeout(100)
    while True:
        stdscr.clear()
        # Draw maze
        for y in range(maze_h):
            for x in range(maze_w):
                stdscr.addch(y, x, maze[y][x])
        # Draw food
        stdscr.addch(food[0], food[1], 'F')
        # Draw snake
        for y, x in snake:
            stdscr.addch(y, x, 'S')
        stdscr.refresh()
        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key
        head = snake[0][:]
        if key == curses.KEY_DOWN:
            head[0] += 1
        if key == curses.KEY_UP:
            head[0] -= 1
        if key == curses.KEY_LEFT:
            head[1] -= 1
        if key == curses.KEY_RIGHT:
            head[1] += 1
        # Check wall collision
        if maze[head[0]][head[1]] == '#':
            break
        snake.insert(0, head)
        if head == food:
            break  # Win condition
        else:
            snake.pop()

curses.wrapper(main)
