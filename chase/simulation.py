from chase.animal import Animal
from chase.sheep import Sheep
from chase.wolf import Wolf
from typing import List
from getch import getch
import logging


class Simulation:
    def __init__(self, tours_number: int, sheep_number: int, init_pos_limit: float, sheep_move_dist: float,
                 wolf_move_dist: float, wait: bool):

        self.tours_number = tours_number
        self._animal = []

        for _ in range(sheep_number):
            s = Sheep(init_pos_limit, sheep_move_dist)
            logging.info('sheep #' + str(_) + 'start position:' + str(s.position))
            self.animal.append(s)

        self._wolf = Wolf(wolf_move_dist, self.animal)
        logging.info(str(self.wolf))
        self.wait = wait

    @property
    def animal(self):
        return self._animal

    @animal.setter
    def animal(self, animal):
        if isinstance(animal, List) is False:
            raise TypeError('sheep must be a list')
        else:
            for _ in animal:
                if isinstance(_, Animal) is False:
                    raise TypeError('animal must include only Animals')
        self._animal = animal

    @property
    def wolf(self):
        return self._wolf

    @wolf.setter
    def wolf(self, wolf):
        if isinstance(wolf, Wolf) is False:
            raise TypeError("wolf must be Wolf class object")
        self._wolf = wolf

    def is_not_all_killed(self) -> bool:
        num_killed = 0
        for _animal in self.animal:
            if _animal is None:
                num_killed += 1
        return num_killed != len(self.animal)

    def get_live_animals(self):
        res = []
        for _animal in self.animal:
            if _animal is not None:
                res.append(_animal)
        return res

    def start_simulation(self) -> [List, List]:
        res_json = []
        res_csv = []
        tour = 0

        logging.info('Simulation starts')
        print('Simulation starts')

        while tour != self.tours_number and self.is_not_all_killed():
            logging.info('tour#' + str(tour) + 'has started')
            print("Tour #" + str(tour))

            for _ in self.animal:
                if _ is not None:
                    logging.info('sheep #' + str(self.animal.index(_)) + ' is moving')
                    _.move()
                    logging.info('Actual position is' + str(_.position))

            self.wolf.move()

            print("---")
            print(self.wolf)
            live_message = str(len(self.get_live_animals())) + ' live animals remain'
            logging.info(live_message)
            print(live_message)
            print("---")
            print("-------")

            animal_positions = []

            for _ in self.animal:
                animal_positions.append([_.position.x, _.position.y] if _ is not None else None)

            res_json.append({
                'round_no': tour,
                'wolf_pos': [self.wolf.position.x, self.wolf.position.y],
                'sheep_pos':  animal_positions
            })

            res_csv.append([tour, len(self.get_live_animals())])

            tour += 1

            if self.wait:
                getch()

        logging.info('Simulation has ended')
        print('Simulation has ended')

        return [res_json, res_csv]

