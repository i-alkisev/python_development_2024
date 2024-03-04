import argparse
import random
import urllib.request
import cowsay


def parse_argse():
    parser = argparse.ArgumentParser(
        description='Bulls and cows game'
    )
    parser.add_argument(
        'path_to_dict',
        help='Path to local file or link'
    )
    parser.add_argument(
        'word_length',
        nargs='?',
        default=5,
        type=int,
        help='Define lenght of used words. Default 5.'
    )
    return parser.parse_args()


def bullscows(guess: str, secret: str) -> tuple[int, int]:
    is_bull = [True if a == b else False for a, b in zip(guess, secret)]
    bulls_cnt = sum(is_bull)
    set_secret = set(secret)
    cows_cnt = 0
    for idx, char in enumerate(guess):
        if idx < len(is_bull) and is_bull[idx]:
            continue
        if char in set_secret:
            cows_cnt += 1
    return (bulls_cnt, cows_cnt)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret_idx = random.randrange(len(words))
    secret = words[secret_idx]
    guess = None
    guess_cnt = 0
    while True:
        guess = ask("Введите слово: ", words)
        guess_cnt += 1
        bulls, cows = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", bulls, cows)
        if guess == secret:
            break
    return guess_cnt


def print_as_cow(message: str) -> None:
    output = cowsay.cowsay(
        message,
        cow=cowsay.get_random_cow()
    )
    print(output)


def ask(prompt: str, valid: list[str] = None) -> str:
    while True:
        print_as_cow(prompt)
        guess = input()
        if valid is not None and guess not in valid:
            print_as_cow('Invalid word')
        else:
            return guess


def inform(format_string: str, bulls: int, cows: int) -> None:
    print_as_cow(format_string.format(bulls, cows))


def load_words(path: str, word_length: int) -> list[str]:
    if path.startswith('https://'):
        with urllib.request.urlopen(path) as f:
            data = f.read().decode('utf-8')
    else:
        with open(path, 'r') as f:
            data = f.read()
    words = data.split()
    return list(filter(lambda word: len(word) == word_length, words))


def main():
    args = parse_argse()
    words = load_words(args.path_to_dict, args.word_length)
    guess_cnt = gameplay(ask, inform, words)
    print(f'Вы угадали слово! Число попыток, которое Вам потребовалось для победы: {guess_cnt}')


if __name__ == '__main__':
    main()
