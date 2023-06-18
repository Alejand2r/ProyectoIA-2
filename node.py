class Nodo:
    def __init__(self, estado: str, player_points: int = 0, machine_points: int = 0):
        self.estado = estado
        self.player_pos = estado.index("9")
        self.machine_pos = estado.index("8")
        self.player_points = player_points
        self.machine_points = machine_points

    def __get_posible_next_play(self, pos):
        pos_x, pos_y = pos // 8, pos % 8
        posible_next_play = []
        if pos_x > 1:
            if pos_y > 0 and int(self.estado[pos - 17]) in range(8):
                posible_next_play.append(pos - 17)
            if pos_y < 7 and int(self.estado[pos - 15]) in range(8):
                posible_next_play.append(pos - 15)
        if pos_y < 6:
            if pos_x > 0 and int(self.estado[pos - 6]) in range(8):
                posible_next_play.append(pos - 6)
            if pos_x < 7 and int(self.estado[pos + 10]) in range(8):
                posible_next_play.append(pos + 10)
        if pos_x < 6:
            if pos_y > 0 and int(self.estado[pos + 15]) in range(8):
                posible_next_play.append(pos + 15)
            if pos_y < 7 and int(self.estado[pos + 17]) in range(8):
                posible_next_play.append(pos + 17)
        if pos_y > 1:
            if pos_x > 0 and int(self.estado[pos - 10]) in range(8):
                posible_next_play.append(pos - 10)
            if pos_x < 7 and int(self.estado[pos + 6]) in range(8):
                posible_next_play.append(pos + 6)
        return posible_next_play

    def get_posible_next_play_player(self):
        return self.__get_posible_next_play(self.player_pos)

    def get_posible_next_play_machine(self):
        return self.__get_posible_next_play(self.machine_pos)
