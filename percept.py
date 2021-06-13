import Tile
import Abstract_agent
import Queue


# Returns what tiles on the board the agent can hear
def hear(agent, board):
    x = agent.position[0]
    y = agent.position[1]
    return [board[x - 2][y + 2], board[x - 1][y + 2], board[x][y + 2], board[x + 1][y + 2], board[x + 2][y + 2],
            board[x - 2][y + 1], board[x - 1][y + 1], board[x][y + 1], board[x + 1][y + 1], board[x + 2][y + 1],
            board[x - 2][y], board[x - 1][y], board[x + 1][y], board[x + 2][y],
            board[x - 2][y - 1], board[x - 1][y - 1], board[x][y - 1], board[x + 1][y - 1], board[x + 2][y - 1],
            board[x - 2][y - 2], board[x - 1][y - 2], board[x][y - 2], board[x + 1][y - 2], board[x + 2][y - 2]]


# Returns what tiles on teh board the agent can see
def see(agent, board):
    x = agent.position[0]
    y = agent.position[1]
    tiles = []

    queue = [Cell(x - 1, y + 1, x, y), Cell(x, y + 1, x, y), Cell(x + 1, y + 1, x, y),
             Cell(x - 1, y, x, y), Cell(x + 1, y, x, y),
             Cell(x - 1, y - 1, x, y), Cell(x, y - 1, x, y), Cell(x + 1,  - 1, x, y)]

    while len(queue) != 0:
        cell = queue.pop()
        tiles.append(board[cell.x][cell.y])
        if cell.dif_x < 2 and cell.dif_y < 2:
            if not board[cell.x][cell.y].is_wall:
                if cell.pos == 'topRight':
                    queue.append(Cell(cell.x + 1, cell.y, x, y))
                    queue.append(Cell(cell.x + 1, cell.y + 1, x, y))
                    queue.append(Cell(cell.x, cell.y + 1, x, y))
                if cell.pos == 'topLeft':
                    queue.append(Cell(cell.x - 1, cell.y, x, y))
                    queue.append(Cell(cell.x - 1, cell.y + 1, x, y))
                    queue.append(Cell(cell.x, cell.y + 1, x, y))
                if cell.pos == 'above':
                    queue.append(Cell(cell.x, cell.y + 1, x, y))
                if cell.pos == 'bottomRight':
                    queue.append(Cell(cell.x + 1, cell.y, x, y))
                    queue.append(Cell(cell.x + 1, cell.y - 1, x, y))
                    queue.append(Cell(cell.x, cell.y - 1, x, y))
                if cell.pos == 'bottomLeft':
                    queue.append(Cell(cell.x - 1, cell.y, x, y))
                    queue.append(Cell(cell.x - 1, cell.y - 1, x, y))
                    queue.append(Cell(cell.x, cell.y - 1, x, y))
                if cell.pos == 'below':
                    queue.append(Cell(cell.x, cell.y - 1, x, y))
                if cell.pos == 'right':
                    queue.append(Cell(cell.x + 1, cell.y, x, y))
                if cell.pos == 'left':
                    queue.append(Cell(cell.x - 1, cell.y, x, y))
    return tiles


# Helper class for determining what is around current agent
class Cell:
    def __init__(self, x_pos, y_pos, agent_x, agent_y):
        self.x = x_pos
        self.y = y_pos
        self.dif_x = abs(agent_x - x_pos)  # How far away on x axis
        self.dif_y = abs(agent_y - y_pos)  # How far away on y axis
        x_val = agent_x - x_pos
        y_val = agent_y - y_pos
        # Pos used for cell position relative to agent position
        if y_val > 0 and x_val > 0:
            self.pos = 'topRight'
        elif y_val > 0 and x_val < 0:
            self.pos = 'topLeft'
        elif y_val > 0:
            self.pos = 'above'
        if y_val < 0 and x_val > 0:
            self.pos = 'bottomRight'
        elif y_val < 0 and x_val < 0:
            self.pos = 'bottomLeft'
        elif y_val < 0:
            self.pos = 'below'
        elif x_val > 0:
            self.pos = 'right'
        else:
            self.pos = 'left'
