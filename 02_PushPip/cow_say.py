import argparse
import cowsay
import sys
from io import StringIO


def parse_args():
    parser = argparse.ArgumentParser(
        description='Implementation linux command-line utility cowsay via python module'
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
    output = cowsay.cowsay(
        **cowsay_params
    )
    print(output)


if __name__ == '__main__':
    main()
