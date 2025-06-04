import sys
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='Meow cat',
        description='The cat utility reads files sequentially, writing them to the standard output. The file operands are processed in command-line order.  If file is a single dash (‘-’) or absent, cat reads from the standard input.'
    )
    parser.add_argument('filename', help='The file to read')
    args = parser.parse_args()

if __name__ == "__main__":
    main()

# argparse 써서 다시 해야하나 ㅅㅂ

# if len(sys.argv) > 1:  # Check if a filename argument is provided
#     filenames = sys.argv[1:]
#     for fname in filenames:
#         with open(fname, 'r', encoding='utf-8') as file_data:
#             text = file_data.read()
#             print(text) # python cccat.py [filename] [filename_1] [filename_n] [...]
# else:  # If no argument, read from standard input
#     line = sys.stdin.readline().strip()
#     print(line) # ex) head -n1 test.txt | python cccat.py
