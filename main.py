from simulation import Simulation

import json
import csv

import argparse
import configparser
from os import mkdir
import os.path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="wolf_chase_sheep_simulation")

    # config argument
    parser.add_argument('-c', '--config',
                        metavar='FILE',
                        dest='config',
                        help='set simulation arguments from config FILE')

    # directory argument
    parser.add_argument('-d', '--dir',
                        dest='directory',
                        type=str,
                        default='',
                        help='set directory where the pos.json, alive.csv and chase.log files must be writen')

    # level log argument
    parser.add_argument('-l', '--level',
                        dest='level',
                        default='10',
                        help='set recording of the events to the diary. LEVEL is a events level (DEBUG, INFO, '
                             'WARNING, ERROR or CRITICAL)')

    # rounds number argument
    parser.add_argument('-r', '--rounds',
                        metavar='NUM',
                        type=int,
                        default=50,
                        dest='rounds_number',
                        help='set a number of the rounds. NUM is an integer value')

    # sheep number argument
    parser.add_argument('-s', '--sheep',
                        metavar='NUM',
                        type=int,
                        default=15,
                        dest='sheep_number',
                        help='set a number of the sheep. NUM is an integer value')

    parser.add_argument('-w', '--wait',
                        action='store_true',
                        dest='wait',
                        help='if is setted, simulation will stop after each round when information will has been '
                             'displayed')

    args = parser.parse_args()

    if args.rounds_number <= 0:
        raise ValueError('rounds number must be greater than 0')

    if args.sheep_number <= 0:
        raise ValueError('sheep number must be greater than 0')

    if args.directory != '' and args.directory[0] == '/':
        raise ValueError('you can save simulation data only as a subdirectory')

    if ['10', '20', '30', '40', '50'].__contains__(args.level) is False \
            and ['DEBUG', 'WARNING', 'ERROR', 'CRITICAL'].__contains__(args.level) is False:
        raise ValueError('level must be equal 10 or DEBUG, 20 or INFO, 30 or WARNING, 40 or ERROR, 50 or CRITICAL')

    if args.config is None:
        init_pos_limit = 10
        sheep_move_dist = 0.5
        wolf_move_dist = 1.0
    else:
        if os.path.exists(args.config) is False:
            raise IOError('File does not exists')

        configuration = configparser.ConfigParser()
        configuration.read(args.config)
        init_pos_limit = float(configuration['Terrain']['InitPosLimit'])
        sheep_move_dist = float(configuration['Movement']['SheepMoveDist'])
        wolf_move_dist = float(configuration['Movement']['WolfMoveDist'])

        if init_pos_limit <= 0:
            raise ValueError('init pos limit must be greater than 0')
        if sheep_move_dist <= 0:
            raise ValueError('sheep move dist must be greater than 0')
        if wolf_move_dist <= 0:
            raise ValueError('wolf move dist must be greater than 0')

    directory = './' + args.directory

    if os.path.exists(directory) is False:
        mkdir(directory)

    # parser.print_help()

    # simulation = Simulation(50, 15, 10.0, 0.5, 1.0)

    # tour_data, alive_sheep_data = simulation.start_simulation()

    # with open('pos.json', 'w') as pos:
    #     d = json.dumps(tour_data)
    #     pos.write(d.replace('},', '},\n'))

    # with open('alive.csv', 'w') as alive:
    #     alive_writer = csv.writer(alive)
    #     alive_writer.writerow(['Rounds Number', 'Number of Live Sheep'])
    #     alive_writer.writerows(alive_sheep_data)
