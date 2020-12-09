from chase.animal import Animal
from typing import List, Tuple
from chase.point import Point
from math import sqrt, pow
import logging


class Wolf(Animal):
    def __init__(self, wolf_move_dist: float, animal: List[Animal]):
        super().__init__(Point(), wolf_move_dist)
        self.animal = animal

    def look_back(self, animal: List[Animal]) -> Tuple[Animal, bool, float]:
        dist = []
        live_animals = []
        for _animal in animal:
            if _animal is not None:
                live_animals.append(_animal)
                dist.append(sqrt(
                    pow(self.position.x - _animal.position.x, 2) +
                    pow(self.position.y - _animal.position.y, 2)
                ))

        dist_to_victim = min(dist)
        victim = live_animals[dist.index(dist_to_victim)]

        return victim, dist_to_victim <= self.distance, dist_to_victim

    def update_distance(self) -> Point:

        victim, can_be_killed, dist_to_victim = self.look_back(self.animal)

        if can_be_killed:
            murder_message = f'animal #{self.animal.index(victim)} has been killed'
            logging.info(murder_message)
            print(murder_message)
            self.position.set(victim.position)
            self.animal[self.animal.index(victim)] = None
            return Point()

        chase_message = f'wolf is chasing the animal #{self.animal.index(victim)}'
        logging.info(chase_message)
        print(chase_message)

        relation = self.distance / (dist_to_victim - self.distance)

        return Point(relation*(victim.position.x - self.position.x) / (1 + relation),
                     relation*(victim.position.y - self.position.y) / (1 + relation))

    def __str__(self):
        return f'wolf position: {str(self.position)}'
