import random
import curses

def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    speed = 120  # initial speed (ms)
    w.timeout(speed)

    snk_x = sw//4
    snk_y = sh//2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1]
    ]
    food = [random.randint(1, sh-2), random.randint(1, sw-2)]
    w.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT
    grow = 0
    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        new_head = [snake[0][0], snake[0][1]]
        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        # Die if hit wall or self
        if (
            new_head in snake or
            new_head[0] in [0, sh] or
            new_head[1] in [0, sw]
        ):
            break
        snake.insert(0, new_head)
        if new_head == food:
            grow += 1  # Only grow by 1
            speed = max(40, speed - 8)  # Increase speed, min 40ms
            w.timeout(speed)
            food = None
            while food is None:
                nf = [random.randint(1, sh-2), random.randint(1, sw-2)]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
        if grow > 0:
            grow -= 1
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')
        # Draw snake: head 'O', body '#'
        w.addch(snake[0][0], snake[0][1], 'O')
        for y, x in snake[1:]:
            w.addch(y, x, '#')

curses.wrapper(main)
