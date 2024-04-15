import argparse
from sys import stderr

parser = argparse.ArgumentParser(
                    prog='Count pairs',
                    description='Counts the number of pairs of given words with the given distance between them')

parser.add_argument('filename')
parser.add_argument('first')
parser.add_argument('second')
parser.add_argument('range')

args = parser.parse_args()

def tokenize(text: str) -> list[str]:
    words = text.split()
    words = [*map(lambda x: ''.join(filter(str.isalpha, x)).lower(), words)]
    words = [w for w in words if w]
    return words

if __name__ == '__main__':
    try:
        with open(args.filename, "r") as f:
            ans: int = 0
            cntr: int = -1 
            words = tokenize(f.read())
            for word in words:
                if cntr >= 0 and word == args.second.lower():
                    ans += 1
                    cntr = 0
                if word == args.first.lower():
                    cntr = int(args.range)
                else:
                    cntr -= 1
        print(ans)
    except OSError:
        print('Ошибка при работе с файлом "' + args.filename + '"', file=stderr)

