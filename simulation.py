from sheep import Sheep
from wolf import Wolf


class Simulation:
    def __init__(self, tours_number: int, sheep_number: int, init_pos_limit: float, sheep_move_dist: float,
                 wolf_move_dist: float):
        self.tours_number = tours_number
        self.sheep = [Sheep(init_pos_limit, sheep_move_dist) for x in range(sheep_number)]
        self.wolf = Wolf(wolf_move_dist)

    def is_not_all_killed(self) -> bool:
        num_killed = 0
        for _sheep in self.sheep:
            if _sheep is None:
                num_killed += 1
        return num_killed != self.sheep.__len__()

    def get_live_sheep(self):
        res = []
        for _sheep in self.sheep:
            if _sheep is not None:
                res.append(_sheep)
        return res

    def start_simulation(self):
        tour = 0

        while tour != self.tours_number and self.is_not_all_killed():
            print("Tour #" + str(tour + 1))

            for _sheep in self.sheep:
                if _sheep is not None:
                    _sheep.move()

            [sheep_was_killed, victim] = self.wolf.move(self.get_live_sheep())

            if sheep_was_killed:
                print("Sheep #" + str(self.sheep.index(victim)) + " was killed")
                self.sheep[self.sheep.index(victim)] = None
            else:
                print("Wolf chase the sheep #" + str(self.sheep.index(victim)))

            print("---")
            print(self.wolf)
            print(str(self.get_live_sheep().__len__()) + " live sheep remain")
            print("---")
            print("-------")
            tour += 1
            pass
