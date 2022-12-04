import sys
from pathlib import Path
from typing import Optional, Tuple


class BaseExecutor:
    def __init__(
        self,
        commands: list,
        steps: list = None,
        cursor: int = 0,
        accumulator: int = 0,
    ):
        self.commands = commands
        self.steps = steps or []
        self.cursor = cursor
        self.accumulator = accumulator

    def __call__(self):
        return self.run()

    @property
    def is_looped(self) -> bool:
        next_step = self.get_command_key(
            self.cursor, self.commands[self.cursor],
        )
        return next_step in self.steps

    def run(self) -> Optional[int]:
        while True:
            self.execute()
            if self.cursor == len(self.commands):
                return self.accumulator
            if self.is_looped:
                return

    def read_command(self, command: str) -> Tuple[str, int]:
        name, num = command.split(' ')
        return name, int(num)

    def get_command_key(self, index: int, command: str) -> str:
        return f'{index} {command}'

    def execute(self):
        command = self.commands[self.cursor]
        name, num = self.read_command(command)

        jump = 1
        if name == 'acc':
            self.accumulator += int(num)
        elif name == 'jmp':
            jump = num

        self.steps.append(self.get_command_key(self.cursor, command))
        self.cursor += jump


class MainExecutor(BaseExecutor):

    def run(self) -> Optional[int]:
        while True:
            self.execute()
            if self.cursor == len(self.commands):
                return self.accumulator
            if self.can_fork():
                forked_accumulator = self.fork()
                if forked_accumulator is not None:
                    return forked_accumulator

    def can_fork(self):
        command = self.commands[self.cursor]
        return 'jmp' in command or 'nop' in command

    def fork(self) -> Optional[int]:
        commands = self.commands[:]
        replace_command = commands[self.cursor]
        if 'jmp' in replace_command:
            commands[self.cursor] = replace_command.replace('jmp', 'nop')
        elif 'nop' in replace_command:
            commands[self.cursor] = replace_command.replace('nop', 'jmp')

        forked_executor = BaseExecutor(
            commands, self.steps, self.cursor, self.accumulator,
        )
        return forked_executor()


def count() -> int:
    with Path('./input.txt').open() as input_file:
        commands = input_file.read().splitlines()

    executor = MainExecutor(commands)
    return executor()


if __name__ == '__main__':
    accumulator = count()
    sys.stdout.write(f'Result: {accumulator}\n')
