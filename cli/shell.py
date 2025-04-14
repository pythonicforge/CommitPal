import cmd
from typing import TextIO

class ComitPal(cmd.Cmd):
    intro = ""
    prompt = "\n(comitpal) "

    def __init__(self, completekey: str = "tab", stdin: TextIO | None = None, stdout: TextIO | None = None) -> None:
        super().__init__(completekey, stdin, stdout)

    