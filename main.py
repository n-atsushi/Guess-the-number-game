import sys
import random

def write_and_flush(message):
    sys.stdout.buffer.write(message.encode())
    sys.stdout.flush()

def play_game(n, count_max):
    count = 0

    while True:
        write_and_flush('Please input a guess value (n) : ')
        guess_number = int(sys.stdin.buffer.readline())

        if n == guess_number:
            write_and_flush('The numbers matched! ')
            break
        elif n < guess_number:
            write_and_flush('The numbers entered are large.\n')
        else:
            write_and_flush('The numbers entered are small\n')

        if count == count_max - 1:
            write_and_flush('** GAME OVER **.\n')
            write_and_flush('** The answer is ')
            write_and_flush(str(n))
            write_and_flush(' **\n')
            break

        count += 1

def chose_levels(times):
    if times == -1:
        return float('inf')
    else:
        return times

def main():
    write_and_flush('Guess-the-number-game Start!\n')

    try:
        write_and_flush('Please input a minimum value (n) : ')
        n1 = int(sys.stdin.buffer.readline())

        write_and_flush('Please input a maximum value (n) : ')
        n2 = int(sys.stdin.buffer.readline())

        if n1 >= n2:
            raise ValueError

        levels = {
            'easy'  : -1,
            'midium': 10,
            'hard': 5,
        }

        write_and_flush('Please select a level: easy, midium, hard :')
        level = sys.stdin.buffer.readline().decode().rstrip('\n')
        count_max = chose_levels(levels.get(level))
        play_game(random.randint(n1, n2), count_max)

    except Exception:
        write_and_flush('invlied value please restart game')

if __name__ == '__main__':
    main()
