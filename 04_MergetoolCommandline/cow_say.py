import cowsay
import cmd
import shlex
import argparse

from typing import Optional


class CowsayShell(cmd.Cmd):
    """Cowsay comands interpreter"""

    def _get_cowfunction_parser(self, **parser_params) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(**parser_params)
        parser.add_argument(
            '--tongue',
            type=lambda s: s[:2],
            help='String representing tongue'
        )
        parser.add_argument(
            '--eyes',
            type=lambda s: s[:2],
            help='String representing eyes'
        )
        parser.add_argument(
            '--cow',
            help='Name of cow. Use list_cows to see all available cows'
        )
        parser.add_argument(
            'message'
        )
        return parser

    def _parse_cowfunction_args(self, cowfunction: str, args: str) -> Optional[dict]:
        try:
            splitted_args = shlex.split(args)
            parsed_args = self.cowfunction_parsers[cowfunction].parse_args(splitted_args)
            return {k: v for k, v in vars(parsed_args).items() if v is not None}
        except:
            return None

    def __init__(self):
        super().__init__()
        self.cowfunction_parsers = {
            'cowsay': self._get_cowfunction_parser(
                prog='cowsay',
                description='Make cowsay'
            ),
            'cowthink': self._get_cowfunction_parser(
                prog='cowthink',
                description='Make cowthink (OMG really?)'
            )
        }
        self.EYES = ['xx', '^^', 'oO', 'Oo', '><', 'o@']
        self.TONGUES = ['V', 'W', 'U', '{}', '[]']

    def do_cowsay(self, args: str):
        parsed_args = self._parse_cowfunction_args('cowsay', args)
        if parsed_args is None:
            return
        output = cowsay.cowsay(**parsed_args)
        print(output)
    
    def help_cowsay(self):
        self.cowfunction_parsers['cowsay'].print_help()
    
    def complete_cowsay(self, text: str, line: str, begidx: int, endidx: int) -> Optional[list[str]]:
        words = (line[:endidx] + ".").split()
        options = []
        if words[-2] == '--eyes' or words[-1].startswith('--eyes='):
            options = self.EYES
        elif words[-2] == '--tongue' or words[-1].startswith('--tongue='):
            options = self.TONGUES
        elif words[-2] == '--cow' or words[-1].startswith('--cow='):
            options = cowsay.list_cows()
        elif begidx >= 2 and line[begidx - 2: begidx] == '--':
            actions = self.cowfunction_parsers['cowsay'].__dict__['_actions']
            options = [x.__dict__['option_strings'][-1].strip('--') for x in actions if len(x.__dict__['option_strings']) > 0]
        return [opt for opt in options if opt.startswith(text)]

    def do_cowthink(self, args: str):
        parsed_args = self._parse_cowfunction_args('cowthink', args)
        if parsed_args is None:
            return
        output = cowsay.cowthink(**parsed_args)
        print(output)
    
    def complete_cowthink(self, text: str, line: str, begidx: int, endidx: int) -> Optional[list[str]]:
        words = (line[:endidx] + ".").split()
        options = []
        if words[-2] == '--eyes' or words[-1].startswith('--eyes='):
            options = self.EYES
        elif words[-2] == '--tongue' or words[-1].startswith('--tongue='):
            options = self.TONGUES
        elif words[-2] == '--cow' or words[-1].startswith('--cow='):
            options = cowsay.list_cows()
        elif begidx >= 2 and line[begidx - 2: begidx] == '--':
            actions = self.cowfunction_parsers['cowthink'].__dict__['_actions']
            options = [x.__dict__['option_strings'][-1].strip('--') for x in actions if len(x.__dict__['option_strings']) > 0]
        return [opt for opt in options if opt.startswith(text)]
    
    def help_cowthink(self):
        self.cowfunction_parsers['cowthink'].print_help()

    def do_list_cows(self, args: str):
        """List available cows"""
        list_cows = cowsay.list_cows()
        list_cows.sort()
        print(*list_cows)

    def do_make_bubble(self, args: str):
        """Wrap text"""
        output = cowsay.make_bubble(args)
        print(output)

    def do_exit(self, args: str):
        """Terminate shell execution"""
        return True

    def do_EOF(self, args: str):
        return True


def main():
    CowsayShell().cmdloop()


if __name__ == '__main__':
    main()
