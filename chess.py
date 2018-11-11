import heapq
from functools import total_ordering
import math


@total_ordering
class Piece():
    def __init__(self, curr_pos, goal_pos, move_counter):
        self.curr_pos = curr_pos
        self.goal_pos = goal_pos
        self.euc_dist = math.sqrt((goal_pos[1] - curr_pos[1])**2 + (ord(goal_pos[0]) - ord(curr_pos[0]))**2)
        self.move_counter = move_counter

    def __eq__(self, other):
        return ((self.euc_dist, self.move_counter, self.curr_pos) == (other.euc_dist, other.move_counter, other.curr_pos))

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if self.move_counter < other.move_counter:
            return True
        elif self.move_counter == other.move_counter:
            return self.euc_dist < other.euc_dist
        else:
            return False

    def check_pos(curr_pos):
        if ord(curr_pos[0]) >= ord('a') and ord(curr_pos[0]) <= ord('h') and curr_pos[1] >= 1 and curr_pos[1] <= 8:
            return True
        else:
            return False

    def __repr__(self):
        return "({}, {})".format(self.curr_pos[0], self.curr_pos[1])


class Knight(Piece):
    def open_move(self):
        new_knight_list = [
            Knight([chr(ord(self.curr_pos[0]) + 2), self.curr_pos[1] + 1], self.goal_pos, self.move_counter + 1), # 2 to right then up 1
            Knight([chr(ord(self.curr_pos[0]) + 2), self.curr_pos[1] - 1], self.goal_pos, self.move_counter + 1), # 2 to right then down 1
            Knight([chr(ord(self.curr_pos[0]) - 2), self.curr_pos[1] + 1], self.goal_pos, self.move_counter + 1), # 2 to left then up 1
            Knight([chr(ord(self.curr_pos[0]) - 2), self.curr_pos[1] - 1], self.goal_pos, self.move_counter + 1), # 2 to left then down 1
            Knight([chr(ord(self.curr_pos[0]) + 1), self.curr_pos[1] + 2], self.goal_pos, self.move_counter + 1), # 1 to right then up 2
            Knight([chr(ord(self.curr_pos[0]) - 1), self.curr_pos[1] + 2], self.goal_pos, self.move_counter + 1), # 1 to left then up 2
            Knight([chr(ord(self.curr_pos[0]) + 1), self.curr_pos[1] - 2], self.goal_pos, self.move_counter + 1), # 1 to right then down 2
            Knight([chr(ord(self.curr_pos[0]) - 1), self.curr_pos[1] - 2], self.goal_pos, self.move_counter + 1)  # 1 to left then down 2
        ]

        for knight in new_knight_list[:]:
            if not Knight.check_pos(knight.curr_pos):
                new_knight_list.remove(knight)
        return new_knight_list



class King(Piece):
    def open_move(self):
        new_king_list = [
            King([chr(ord(self.curr_pos[0]) + 1), self.curr_pos[1] + 1], self.goal_pos, self.move_counter + 1), # 1 to right then up 1
            King([chr(ord(self.curr_pos[0]) + 1), self.curr_pos[1] - 1], self.goal_pos, self.move_counter + 1), # 1 to right then down 1
            King([chr(ord(self.curr_pos[0]) - 1), self.curr_pos[1] + 1], self.goal_pos, self.move_counter + 1), # 1 to left then up 1
            King([chr(ord(self.curr_pos[0]) - 1), self.curr_pos[1] - 1], self.goal_pos, self.move_counter + 1), # 1 to left then down 1
            King([chr(ord(self.curr_pos[0]) + 1), self.curr_pos[1]], self.goal_pos, self.move_counter + 1), # 1 to right
            King([chr(ord(self.curr_pos[0]) - 1), self.curr_pos[1]], self.goal_pos, self.move_counter + 1), # 1 to left
            King([chr(ord(self.curr_pos[0])), self.curr_pos[1] + 1], self.goal_pos, self.move_counter + 1), # 1 up
            King([chr(ord(self.curr_pos[0])), self.curr_pos[1] - 1], self.goal_pos, self.move_counter + 1) # 1 down
        ]

        for king in new_king_list[:]:
            if not King.check_pos(king.curr_pos):
                new_king_list.remove(king)
        return new_king_list



class Bishop(Piece):
    def open_move(self):
        new_bishop_list = []
        for i in range(1, 9):
            new_bishop_list.extend([
                Bishop([chr(ord(self.curr_pos[0]) + i), self.curr_pos[1] + i], self.goal_pos, self.move_counter + 1), # any steps towards top right quad
                Bishop([chr(ord(self.curr_pos[0]) + i), self.curr_pos[1] - i], self.goal_pos, self.move_counter + 1), # any steps towards bottom right quad
                Bishop([chr(ord(self.curr_pos[0]) - i), self.curr_pos[1] + i], self.goal_pos, self.move_counter + 1), # any steps towards top left quad
                Bishop([chr(ord(self.curr_pos[0]) - i), self.curr_pos[1] - i], self.goal_pos, self.move_counter + 1) # any steps towards bottom let quad
                ])

        for bishop in new_bishop_list[:]:
            if not Bishop.check_pos(bishop.curr_pos) or bishop.curr_pos == self.curr_pos:
                new_bishop_list.remove(bishop)
        return new_bishop_list


class Pawn(Piece):
    def open_move(self):
        new_pawn_list = []

        if self.curr_pos[1] >= 8:
            return new_pawn_list

        if self.move_counter == 0 and self.curr_pos[1] == 2:
            new_pawn_list.append(Pawn([self.curr_pos[0], self.curr_pos[1] + 2], self.goal_pos, self.move_counter + 1))

        new_pawn_list.append(Pawn([self.curr_pos[0], self.curr_pos[1] + 1], self.goal_pos, self.move_counter + 1))
        return new_pawn_list



def main():
    pq = []
    piece = ''
    init_pos = ['a',1] # Default values
    goal_pos = ['a',8]
    move_counter = 0

    piece = input("Pick your piece: king, knight, or bishop\n").lower()
    init_pos_files = input("Initial position files: a-h\n").lower()
    init_pos_ranks = int(input("Initial postion ranks: 1-8\n"))
    goal_pos_files = input("Goal position files: a-h\n").lower()
    goal_pos_ranks = int(input("Goal position ranks: 1-8\n"))

    init_pos = [init_pos_files, init_pos_ranks]
    goal_pos = [goal_pos_files, goal_pos_ranks]

    if piece == 'king':
        first_piece = King(init_pos, goal_pos, move_counter)
    elif piece == 'knight':
        first_piece = Knihgt(init_pos, goal_pos, move_counter)
    elif piece == 'bishop':
        first_piece = Bishop(init_pos, goal_pos, move_counter)
    else:
        print("Invalid input. Control + C to exit. \n")
        main()

    heapq.heappush(pq, first_piece)

    visited = set()
    while pq:
        first_obj = heapq.heappop(pq)
        if first_obj.curr_pos == first_obj.goal_pos:
            print('It took {} step(s) to get to goal!'.format(first_obj.move_counter))
            exit()
        else:
            children = first_obj.open_move()
            for child in children:
                if tuple(child.curr_pos) in visited:
                    continue
                else:
                    heapq.heappush(pq, child)
                    visited.add(tuple(child.curr_pos))

    print("It looks like it was impossible to reach the goal position.")

if __name__ == '__main__':
    main()
