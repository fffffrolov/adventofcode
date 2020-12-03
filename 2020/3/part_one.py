import sys
from pathlib import Path


def get_next_index(index: int, width: int) -> int:
	return (index + 3) % width


def slither() -> int:
	trees = 0
	index = 0
	started = False
	with Path('./input.txt').open() as input_file:
		for line in input_file.readlines():
			if not started: 
				started = True
				continue
			line = line.strip()
			index = get_next_index(index, len(line))
			if line[index] == '#':
				trees += 1

	return trees


if __name__ == '__main__':
	result = slither()
	sys.stdout.write(f'Total: {result}\n')
