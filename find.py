

def codify_maze(maze):
    maze_repr = []
    row_count = len(maze)
    column_count = len(maze[0])

    cur_row_num = 1
    while cur_row_num  < row_count:
        row_repr = []
        row = maze[cur_row_num]
        count = 1
        while count < column_count:
            down = False
            left = False
            right = False
            top = False
            char = row[count]
            if char != "_":
                down = True

            try:
                if row[count - 1] != "|":
                    left = True
            except:
                pass

            try:
                if row[count + 1] != "|":
                    right = True
            except:
                pass

            try:
                if maze[cur_row_num - 1][count] != "_":
                    top = True
            except:
                pass
            count += 2

            row_repr.append([top,right,down,left])
        maze_repr.append(row_repr)
        cur_row_num += 1

    return maze_repr


def solve(maze, cur_row, cur_lev, collected):
    cur_block = maze[cur_row][cur_lev]
    print cur_row,cur_lev

    if cur_row == len(maze) - 1 and cur_lev == len(maze[0]) - 1:
        return collected

    elif global_maze[cur_row][cur_lev]:
        global_maze[cur_row][cur_lev] = ""
        if cur_block[1]:
            if global_maze[cur_row][cur_lev+1]:
                val1 = solve(maze, cur_row, cur_lev + 1, collected + " 1E")
                if val1:
                    return val1
        if cur_block[2]:
            if global_maze[cur_row+1][cur_lev]:
                val2 = solve(maze, cur_row + 1, cur_lev, collected + " 1S")
                if val2:
                    return val2
        if cur_block[3]:
            if global_maze[cur_row][cur_lev-1]:
                val3 = solve(maze, cur_row, cur_lev - 1, collected + " 1W")
                if val3:
                    return val3
        if cur_block[0]:
            if global_maze[cur_row - 1][cur_lev]:
                val4 = solve(maze, cur_row - 1,  cur_lev, collected + " 1N")
                if val4:
                    return val4



if __name__ == "__main__":
    maze = []
    f = open("tinymaze.txt")
    while 1:
        line = f.readline().strip()
        if not line:
            break
        row = list(line)
        maze.append(row)
    codified_maze = codify_maze(maze)
    for l in codified_maze:
        print l

    global_maze = codified_maze[:]
    path = solve(codified_maze, 0 , 0, "" )
    if path:
        print path.strip()
    else:
        print -1






