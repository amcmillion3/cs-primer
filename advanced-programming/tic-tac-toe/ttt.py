import os

PLAYER_SYMBOLS = ('X', 'O')
VICTORY_CONDITIONS = (
    {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, #horizontal
    {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, #vertical
    {0, 4, 8}, {2, 4, 6} #diagonal
)

class Game(object):
    def __init__(self):
        self.moves = []

    def __str__(self):
        board = list('abcdefghi')
        for i, m in enumerate(self.moves):
            board[m] = PLAYER_SYMBOLS[i % 2]
        return '\n---+---+---\n'.join(
            '|'.join(f' {c} ' for c in row)
            for row in (board[0:3], board[3:6], board[6:9]))

    def winner(self):
        for i, played in enumerate((set(self.moves[::2]), set(self.moves[1::2]))):
            for needed in VICTORY_CONDITIONS:
                if len(needed - played) == 0:
                    return i

    def add_move(self, m):
        try: 
            mi = ord(m.lower()) - ord('a')
            assert 0 <= mi < 9
            assert mi not in self.moves
        except (AttributeError, TypeError, AssertionError):
                return False
        self.moves.append(mi)
        return True

    def next_player(self):
        return len(self.moves) % 2

if __name__ == '__main__':
    g = Game()
    while g.winner() is None:
        os.system('clear')
        print(g)
        print()
        while True:
            m = input(f'Player {PLAYER_SYMBOLS[g.next_player()]} turn: ')
            if g.add_move(m):
                break
            print('Invalid move!')
    print(f'Player {PLAYER_SYMBOLS[g.winner()]} wins!!!')
