from simulation import Simulation

import json
import csv

if __name__ == '__main__':
    simulation = Simulation(50, 15, 10.0, 0.5, 1.0)

    tour_data, alive_sheep_data = simulation.start_simulation()

    with open('pos.json', 'w') as pos:
        d = json.dumps(tour_data)
        pos.write(d.replace('},', '},\n'))

    with open('alive.csv', 'w') as alive:
        alive_writer = csv.writer(alive)
        alive_writer.writerow(['Rounds Number', 'Number of Live Sheep'])
        alive_writer.writerows(alive_sheep_data)
