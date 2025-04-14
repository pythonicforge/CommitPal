import cmd
import sys
from typing import TextIO
from utils import logger, get_git_diff, generate_commit_message

class ComitPal(cmd.Cmd):
    intro = ""
    prompt = "\n(comitpal) "

    def __init__(self, completekey: str = "tab", stdin: TextIO | None = None, stdout: TextIO | None = None) -> None:
        super().__init__(completekey, stdin, stdout)

    def do_diff(self, args):
        git_diff = get_git_diff()
        print(generate_commit_message(git_diff))

    def do_bye(self, args):
        logger.info("Shutting down whisper..")
        logger.success("Done")
        sys.exit(0)