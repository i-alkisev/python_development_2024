import argparse
import cowsay
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description='Implementation linux command-line utility cowsay via python module'
    )
    parser.add_argument(
        '-l',
        action='store_true',
        help='list available cow pictures')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.l:
        list_cows = cowsay.list_cows()
        list_cows.sort()
        print(*list_cows)
        return
    message = ''.join(sys.stdin.readlines())
    output = cowsay.cowsay(
        message=message
    )
    print(output)


if __name__ == '__main__':
    main()
