""" Main """

from __future__ import print_function
import argparse
import tabulate
from vasttrafik import JournyPlanner


def print_table(document, *columns):
    """ Print json document as table """
    headers = []
    for _, header in columns:
        headers.append(header)
    table = []
    for element in document:
        row = []
        for item, _ in columns:
            if item in element:
                row.append(element[item])
            else:
                row.append(None)
        table.append(row)
    print(tabulate.tabulate(table, headers))


def print_trip_table(document):
    """ Print trip table """
    headers = [
        'Alt.',
        'Name',
        'Time',
        'Track',
        'Direction',
        'Dest.',
        'Track',
        'Arrival']
    table = []
    altnr = 0
    for alternative in document:
        altnr += 1
        first_trip_in_alt = True
        for part in alternative['Leg']:
            orig = part['Origin']
            dest = part['Destination']
            row = [
                altnr if first_trip_in_alt else None,
                part['name'],
                orig['rtTime'] if 'rtTime' in orig else orig['time'],
                orig['track'],
                part['direction'] if 'direction' in part else None,
                dest['name'],
                dest['track'],
                dest['rtTime'] if 'rtTime' in dest else dest['time'],
                ]
            table.append(row)
            first_trip_in_alt = False
    print(tabulate.tabulate(table, headers))


# pylint: disable=too-many-statements
def main():
    """ Main function """
    parser = argparse.ArgumentParser(
        description='Västtrafik journy planner (vtjp)')
    parser.add_argument(
        'key')
    parser.add_argument(
        'secret')
    service_parser = parser.add_subparsers(
        dest='service',
        help='service')

    # LOCATION
    location_parser = service_parser.add_parser(
        'location')
    location_subparser = location_parser.add_subparsers(
        help='method',
        dest='location_method')
    location_name_parser = location_subparser.add_parser(
        'name')
    location_name_parser.add_argument(
        'name')
    location_subparser.add_parser(
        'allstops')
    location_nearbystops_parser = location_subparser.add_parser(
        'nearbystops')
    location_nearbystops_parser.add_argument(
        'lat')
    location_nearbystops_parser.add_argument(
        'lon')
    location_nearbystops_parser = location_subparser.add_parser(
        'nearbyaddress')
    location_nearbystops_parser.add_argument(
        'lat')
    location_nearbystops_parser.add_argument(
        'lon')

    # ARIVAL BOARD
    arrival_parser = service_parser.add_parser(
        'arrivalboard')
    arrival_parser.add_argument(
        'id')
    arrival_parser.add_argument(
        'date',
        nargs='?')
    arrival_parser.add_argument(
        'time',
        nargs='?')

    # DEPARTURE BOARD
    departure_parser = service_parser.add_parser(
        'departureboard')
    departure_parser.add_argument(
        'id')
    departure_parser.add_argument(
        'date',
        nargs='?')
    departure_parser.add_argument(
        'time',
        nargs='?')

    # DEPARTURE BOARD
    departure_parser = service_parser.add_parser(
        'trip')
    departure_parser.add_argument(
        'originId')
    departure_parser.add_argument(
        'destinationId')
    departure_parser.add_argument(
        'date',
        nargs='?')
    departure_parser.add_argument(
        'time',
        nargs='?')

    args = parser.parse_args()

    planner = JournyPlanner(
        response_format='JSON',
        key=args.key,
        secret=args.secret)

    if hasattr(args, 'id') and not args.id.isdigit():
        args.id = planner.location_name(args.id)[0]['id']
    if hasattr(args, 'originId') and not args.originId.isdigit():
        args.originId = planner.location_name(args.originId)[0]['id']
    if hasattr(args, 'destinationId') and not args.destinationId.isdigit():
        args.destinationId = planner.location_name(args.destinationId)[0]['id']

    # LOCATION
    if args.service == 'location':
        if args.location_method == 'allstops':
            print_table(
                planner.location_allstops(),
                ('id', 'ID'),
                ('name', 'Name'),
                ('track', 'Track'))
        if args.location_method == 'name':
            print_table(
                planner.location_name(args.name),
                ('id', 'ID'),
                ('name', 'Name'))
        if args.location_method == 'nearbystops':
            print_table(
                planner.location_nearbystops(args.lat, args.lon),
                ('id', 'ID'),
                ('name', 'Name'),
                ('track', 'Track'))
        if args.location_method == 'nearbyaddress':
            print_table(
                [planner.location_nearbyaddress(args.lat, args.lon)],
                ('name', 'Name'),
                ('lon', 'Longitude'),
                ('lat', 'Latitude'))

    # ARRIVALBOARD
    if args.service == 'arrivalboard':
        print_table(
            planner.arrivalboard(args.id, args.date, args.time),
            ('sname', 'Line'),
            ('time', 'Arrival'),
            ('rtTime', 'Prel.Arrival'),
            ('track', 'Track'),
            ('origin', 'Origin'))

    # DEPARTUREBOARD
    if args.service == 'departureboard':
        print_table(
            planner.departureboard(args.id, args.date, args.time),
            ('sname', 'Line'),
            ('time', 'Departure'),
            ('rtTime', 'Prel.Departure'),
            ('track', 'Track'),
            ('direction', 'Direction'))

    # TRIP
    if args.service == 'trip':
        print_trip_table(
            planner.trip(
                args.originId,
                args.destinationId,
                args.date,
                args.time))


if __name__ == '__main__':
    main()
