from sheep import Sheep
from wolf import Wolf
from typing import List
from getch import getch
import logging


class Simulation:
    def __init__(self, tours_number: int, sheep_number: int, init_pos_limit: float, sheep_move_dist: float,
                 wolf_move_dist: float, wait: bool):
        logging.debug('object initialization')

        self.tours_number = tours_number
        self.sheep = []

        for _ in range(sheep_number):
            s = Sheep(init_pos_limit, sheep_move_dist)
            self.sheep.append(s)
            logging.info('sheep #' + str(_) + ' start position: ' + str(self.sheep[_].position))

        self.wolf = Wolf(wolf_move_dist)
        logging.info(str(self.wolf))
        self.wait = wait

    def is_not_all_killed(self) -> bool:
        logging.debug('is_not_all_killed() method called')

        num_killed = 0
        for _sheep in self.sheep:
            if _sheep is None:
                num_killed += 1
        return num_killed != self.sheep.__len__()

    def get_live_sheep(self):
        logging.debug('get_live_sheep() method called')

        res = []
        for _sheep in self.sheep:
            if _sheep is not None:
                res.append(_sheep)
        return res

    def start_simulation(self) -> [List, List]:
        logging.debug('start_simulation() method called')

        res_json = []
        res_csv = []
        tour = 0

        logging.info('Simulation starts')
        print('Simulation starts')

        while tour != self.tours_number and self.is_not_all_killed():
            logging.info('tour#' + str(tour) + 'has started')
            print("Tour #" + str(tour))

            for _ in self.sheep:
                if _ is not None:
                    side = _.move()
                    logging.info('sheep #' + str(self.sheep.index(_)) + ' is moving to ' + side + '. Actual position is ' +
                                 str(_.position))

            [sheep_was_killed, victim] = self.wolf.move(self.get_live_sheep())

            if sheep_was_killed:
                murder_message = 'sheep #' + str(self.sheep.index(victim)) + ' has been killed'
                logging.info(murder_message)
                print(murder_message)
                self.sheep[self.sheep.index(victim)] = None
            else:
                chase_message = 'wolf is chasing the sheep #' + str(self.sheep.index(victim))
                logging.info(chase_message)
                print(chase_message)


            print("---")
            print(self.wolf)
            live_message = str(self.get_live_sheep().__len__()) + ' live sheep remain'
            logging.info(live_message)
            print(live_message)
            print("---")
            print("-------")

            sheep_positions = []

            for _ in self.sheep:
                sheep_positions.append([_.position.x, _.position.y] if _ is not None else None)

            res_json.append({
                'round_no': tour,
                'wolf_pos': [self.wolf.position.x, self.wolf.position.y],
                'sheep_pos':  sheep_positions
            })

            res_csv.append([tour, len(self.get_live_sheep())])

            tour += 1

            if self.wait:
                getch()

        logging.info('Simulation has ended')
        print('Simulation has ended')
        return [res_json, res_csv]

