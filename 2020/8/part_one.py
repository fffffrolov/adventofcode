import sys
from pathlib import Path

accumulator = 0


def execute_and_jump(command: str) -> int:
    global accumulator
    name, num = command.split(' ')
    num = int(num)
    jump = 1
    if name == 'acc':
        accumulator += int(num)
    elif name == 'jmp':
        jump = num
    return jump


def execute() -> int:
    executed = set()

    with Path('./input.txt').open() as input_file:
        commands = input_file.read().splitlines()

    index = 0
    next_command = f'{index} {commands[index]}'
    while next_command not in executed:
        command = commands[index]
        index += execute_and_jump(command)
        executed.add(next_command)
        next_command = f'{index} {commands[index]}'


if __name__ == '__main__':
    execute()
    sys.stdout.write(f'Result: {accumulator}\n')
