
class Nodo:
    def __init__(self, state: str, player_points: int = 0, machine_points: int = 0, player_move: bool = False,
                 max_deep: int = 2, parent=None, deep: int = 0):
        self.state = state
        self.player_pos = state.index("9")
        self.machine_pos = state.index("8")
        self.player_points = player_points
        self.machine_points = machine_points
        self.player_move = player_move
        self.max_deep = max_deep
        self.parent = parent
        self.deep = deep
        self.branch_end = all([str(num) not in state for num in range(1, 8)])

    def __get_posible_next_play(self, pos):
        pos_x, pos_y = pos // 8, pos % 8
        posible_next_play = []
        if pos_x > 1:
            if pos_y > 0 and int(self.state[pos - 17]) in range(8):
                posible_next_play.append(pos - 17)
            if pos_y < 7 and int(self.state[pos - 15]) in range(8):
                posible_next_play.append(pos - 15)
        if pos_y < 6:
            if pos_x > 0 and int(self.state[pos - 6]) in range(8):
                posible_next_play.append(pos - 6)
            if pos_x < 7 and int(self.state[pos + 10]) in range(8):
                posible_next_play.append(pos + 10)
        if pos_x < 6:
            if pos_y > 0 and int(self.state[pos + 15]) in range(8):
                posible_next_play.append(pos + 15)
            if pos_y < 7 and int(self.state[pos + 17]) in range(8):
                posible_next_play.append(pos + 17)
        if pos_y > 1:
            if pos_x > 0 and int(self.state[pos - 10]) in range(8):
                posible_next_play.append(pos - 10)
            if pos_x < 7 and int(self.state[pos + 6]) in range(8):
                posible_next_play.append(pos + 6)
        return posible_next_play

    def get_posible_next_play_player(self):
        return self.__get_posible_next_play(self.player_pos)

    def get_posible_next_play_machine(self):
        return self.__get_posible_next_play(self.machine_pos)

    def set_max_deep(self, max_deep):
        self.max_deep = max_deep

    def get_branch(self):
        branch = []
        current_node = self
        while current_node is not None:
            branch.append(current_node)
            current_node = current_node.parent
        branch.reverse()
        return branch
    
    def make_player_move(self, new_position: int):
        puntos_recolectados = 0
        if self.state[new_position] != 0:
            puntos_recolectados = int(self.state[new_position])
        nuevo_estado = self.state[:self.player_pos] + "0" + self.state[self.player_pos + 1:]
        nuevo_estado = nuevo_estado[:new_position] + "9" + nuevo_estado[new_position + 1:]
        nuevo_nodo = Nodo(state=nuevo_estado, player_points=self.player_points + puntos_recolectados,
                              machine_points=self.machine_points, player_move=False,
                              max_deep=self.max_deep, parent=self, deep=self.deep + 1)
        return nuevo_nodo