import cmd
import subprocess
from typing import TextIO


class ComitPal(cmd.Cmd):
    intro = ""
    prompt = "\n(comitpal) "

    

    def __init__(self, completekey: str = "tab", stdin: TextIO | None = None, stdout: TextIO | None = None) -> None:
        super().__init__(completekey, stdin, stdout)

    def get_git_diff(self):
        """Get the git diff of the current staged changes."""
        result = subprocess.run(['git', 'diff'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    
    def generate_commit_message(self):
        pass

    def do_diff(self, args):
        print(self.get_git_diff())