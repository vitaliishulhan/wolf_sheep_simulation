from chase.simulation import Simulation

import json
import csv

import argparse
from configparser import ConfigParser
from os import mkdir
import os.path

from chase.sheep import Sheep

import logging

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
                        type=int,
                        default=0,
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
                        help='if is set, simulation will stop after each round when information will has been '
                             'displayed')

    args = parser.parse_args()

    if args.level != 0 and [10, 20, 30, 40, 50].__contains__(args.level) is False:
        raise ValueError('level must be equal 10 (DEBUG), 20 (INFO), 30 (WARNING), 40 (ERROR), 50 (CRITICAL)')

    if args.directory != '' and args.directory[0] == '/':
        raise ValueError('you can save simulation data only in a subdirectory')

    directory = './' + args.directory + ('/' if args.directory != '' and args.directory[-1] != '/' else '')

    if os.path.exists(directory) is False:
        logging.debug('directory "' + directory + '" does not exist, creating')
        mkdir(directory)

    logging.basicConfig(filename=directory + 'chase.log',
                        level=args.level,
                        filemode='w',
                        format='%(asctime)s - %(module)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    if args.rounds_number <= 0:
        logging.error('fatal: round number is less than 0')
        raise ValueError('rounds number must be greater than 0')

    if args.sheep_number <= 0:
        logging.error('fatal: sheep number is less than 0')
        raise ValueError('sheep number must be greater than 0')

    if args.config is None:
        init_pos_limit = 10
        sheep_move_dist = 0.5
        wolf_move_dist = 1.0
    else:
        if os.path.exists(args.config) is False:
            logging.error('File does not exists')
            raise IOError('File does not exists')

        configuration = ConfigParser()
        configuration.read(args.config)
        init_pos_limit = float(configuration['Terrain']['InitPosLimit'])
        sheep_move_dist = float(configuration['Movement']['SheepMoveDist'])
        wolf_move_dist = float(configuration['Movement']['WolfMoveDist'])

        if init_pos_limit <= 0:
            logging.error('fatal: init pos limit is less than 0')
            raise ValueError('init pos limit must be greater than 0')
        if sheep_move_dist <= 0:
            logging.error('fatal: sheep move dist is less than 0')
            raise ValueError('sheep move dist must be greater than 0')
        if wolf_move_dist <= 0:
            logging.error('fatal: wolf move dist is less than 0')
            raise ValueError('wolf move dist must be greater than 0')

    simulation = Simulation(args.rounds_number, args.sheep_number, init_pos_limit, sheep_move_dist, wolf_move_dist,
                            args.wait)

    tour_data, alive_sheep_data = simulation.start_simulation()

    logging.debug('Attempt to write pos.json file to ' + directory)
    with open(directory + 'pos.json', 'w') as pos:
        d = json.dumps(tour_data)
        pos.write(d.replace('},', '},\n'))
    logging.debug(directory + 'pos.json has been written')

    logging.debug('Attempt to write alive.csv file to ' + directory)
    with open(directory + 'alive.csv', 'w') as alive:
        alive_writer = csv.writer(alive)
        alive_writer.writerow(['Rounds Number', 'Number of Live Sheep'])
        alive_writer.writerows(alive_sheep_data)
    logging.debug(directory + 'alive.csv has been written')
