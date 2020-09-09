import random
import copy


class Game2048:

    def __init__(self, size=4):
        self.game = [0 for _ in range(size)]
        self.game[random.randint(0, size-1)] = 2
        self.size = size
        self.score = 0

    def add_two(self):
        two_put = []
        i = 0
        for p in self.game:
            if p == 0:
                two_put.append(i)
            i += 1

        i_two = random.randint(0, len(two_put)-1)
        self.game[two_put[i_two]] = 2

    def checker(self):
        two_put = []
        i = 0
        cnt_same = 0
        previous = 0
        for p in self.game:
            if p == previous:
                cnt_same += 1
            if p == 0:
                two_put.append(i)
                previous = 0
            else:
                previous = p
            i += 1

        if len(two_put) == 0 and cnt_same == 0:
            return -1
        else:
            return ""

    def press_right(self):
        indicator = 0
        while True:
            slice_game = copy.copy(self.game)
            index = len(self.game) - 1
            for i in range(self.size):
                if index < 0:
                    break
                if slice_game[index] == 0:
                    slice_game.pop(index)
                    index -= 1
                elif index - 1 >= 0 and slice_game[index] == slice_game[index-1]:
                    slice_game[index] *= 2
                    self.score += slice_game[index]
                    slice_game.pop(index-1)
                    index -= 2
                    indicator = 1
                else:
                    index -= 1
            self.game = [0 for _ in range(self.size)]
            self.game[len(self.game)-len(slice_game):] = slice_game
            if indicator == 1:
                break
            indicator += 1

        self.add_two()
        return self.game

    def press_left(self):
        indicator = 0
        while True:
            slice_game = copy.copy(self.game)
            index = 0
            for i in range(self.size):
                if index >= len(slice_game):
                    break
                if slice_game[index] == 0:
                    slice_game.pop(index)
                elif index + 1 < len(slice_game) and slice_game[index] == slice_game[index + 1]:
                    slice_game[index] *= 2
                    self.score += slice_game[index]
                    slice_game.pop(index + 1)
                    index += 1
                    indicator = 1
                else:
                    index += 1
            self.game = [0 for _ in range(self.size)]
            self.game[:len(slice_game)] = slice_game
            if indicator == 1:
                break
            indicator += 1

        self.add_two()
        return self.game

    def block_key(self, key):
        temp_list = []
        i = 0
        cnt_same = 0
        for p in self.game:
            if p != 0:
                temp_list.append(p)
                if i + 1 < len(self.game) and self.game[i] == self.game[i+1]:
                    cnt_same += 1
            i += 1
        if key == "right":
            if cnt_same == 0 and "".join(list(map(str, self.game))).endswith("".join(list(map(str, temp_list)))):
                return True
            else:
                return False
        if key == "left":
            if cnt_same == 0 and "".join(list(map(str, self.game))).startswith("".join(list(map(str, temp_list)))):
                return True
            else:
                return False

