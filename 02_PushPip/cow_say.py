import argparse
import cowsay
import sys
from io import StringIO


def parse_args():
    parser = argparse.ArgumentParser(
        description='Implementation linux command-line utility cowsay via python module'
    )
    parser.add_argument(
        '-b',
        action='store_const',
        const='b',
        dest='preset'
    )
    parser.add_argument(
        '-g',
        action='store_const',
        const='g',
        dest='preset'
    )
    parser.add_argument(
        '-p',
        action='store_const',
        const='p',
        dest='preset'
    )
    parser.add_argument(
        '-s',
        action='store_const',
        const='s',
        dest='preset'
    )
    parser.add_argument(
        '-t',
        action='store_const',
        const='t',
        dest='preset'
    )
    parser.add_argument(
        '-w',
        action='store_const',
        const='w',
        dest='preset'
    )
    parser.add_argument(
        '-y',
        action='store_const',
        const='y',
        dest='preset'
    )
    parser.add_argument(
        '-pstwy',
        action='store_const',
        const='g',
        dest='preset'
    )
    parser.add_argument(
        '-e',
    )
    parser.add_argument(
        '-f'
    )
    parser.add_argument(
        '-l',
        action='store_true',
        help='list available cow pictures'
    )
    parser.add_argument(
        '-T',
    )
    parser.add_argument(
        '-W',
        type=int
    )
    parser.add_argument(
        'message',
        nargs='*',
        default=None
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if args.l:
        list_cows = cowsay.list_cows()
        list_cows.sort()
        print(*list_cows)
        return
    cowsay_params = {}
    cowsay_params['message'] = ' '.join(args.message) if len(args.message) > 0 else None
    if cowsay_params['message'] is None:
        cowsay_params['message'] = ''.join(sys.stdin.readlines())
    if args.f is not None:
        with open(args.f, 'r') as cowfile:
            cow = StringIO(cowfile.read())
        cowsay_params['cowfile'] = cowsay.read_dot_cow(cow)
    if args.preset is not None:
        cowsay_params['preset'] = args.preset
    if args.e is not None:
        cowsay_params['eyes'] = args.e
    if args.T is not None:
        cowsay_params['tongue'] = args.T
    if args.W is not None:
        cowsay_params['width'] = args.W
    output = cowsay.cowsay(
        **cowsay_params
    )
    print(output)


if __name__ == '__main__':
    main()
