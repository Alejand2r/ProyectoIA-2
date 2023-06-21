from node import Nodo


def heuristica(nodo):
    return nodo.machine_points - nodo.player_points


def minimax(nodo, profundidad, alfa=float('-inf'), beta=float('inf')) -> tuple[int, Nodo]:
    if profundidad == 0 or nodo.branch_end:
        return heuristica(nodo), None
    if not nodo.player_move:
        valor_max, siguiente_nodo = float('-inf'), None
        for jugada in nodo.get_posible_next_play_machine():
            puntos_recolectados = 0
            if nodo.state[jugada] != 0:
                puntos_recolectados = int(nodo.state[jugada])
            nuevo_estado = nodo.state[:nodo.machine_pos] + "0" + nodo.state[nodo.machine_pos + 1:]
            nuevo_estado = nuevo_estado[:jugada] + "8" + nuevo_estado[jugada + 1:]
            nuevo_nodo = Nodo(nuevo_estado, player_points=nodo.player_points,
                              machine_points=nodo.machine_points + puntos_recolectados, player_move=True,
                              max_deep=nodo.max_deep, parent=nodo, deep=nodo.deep + 1)
            valorHijo, jugadaHijo = minimax(nuevo_nodo, profundidad - 1, alfa, beta)
            if valor_max < valorHijo:
                siguiente_nodo = nuevo_nodo
            valor_max = max(valor_max, valorHijo)
            alfa = max(alfa, valor_max)
            if beta <= alfa:
                break
        return valor_max, siguiente_nodo
    else:
        valor_min, siguiente_nodo = float('inf'), None
        for jugada in nodo.get_posible_next_play_player():
            puntos_recolectados = 0
            if nodo.state[jugada] != 0:
                puntos_recolectados = int(nodo.state[jugada])
            nuevo_estado = nodo.state[:nodo.player_pos] + "0" + nodo.state[nodo.player_pos + 1:]
            nuevo_estado = nuevo_estado[:jugada] + "9" + nuevo_estado[jugada + 1:]
            nuevo_nodo = Nodo(state=nuevo_estado, player_points=nodo.player_points + puntos_recolectados,
                              machine_points=nodo.machine_points, player_move=False,
                              max_deep=nodo.max_deep, parent=nodo, deep=nodo.deep + 1)
            valorHijo, hijo = minimax(nuevo_nodo, profundidad - 1, alfa, beta)
            if valorHijo < valor_min:
                siguiente_nodo = nuevo_nodo
            valor_min = min(valor_min, valorHijo)
            beta = min(beta, valor_min)
            if beta <= alfa:
                break
        return valor_min, siguiente_nodo