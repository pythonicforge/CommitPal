import os
import cmd
import sys
from typing import TextIO, Any
from utils import logger, get_git_diff, generate_commit_message, parse_args, generate_changelog

class ComitPal(cmd.Cmd):
    intro = ""
    prompt = "\n(comitpal) "

    def __init__(self, completekey: str = "tab", stdin: TextIO | None = None, stdout: TextIO | None = None) -> None:
        super().__init__(completekey, stdin, stdout)

    def do_diff(self, args: Any) -> None:
        args, changelog = parse_args(args)
        git_diff = get_git_diff()
        generate_commit_message(git_diff)
        logger.success("Commit message generated!")

        if changelog:
            generate_changelog(git_diff)
            logger.success("Changelog generated!")

    def do_clear(self, args: None) -> None:
        os.system('clear')

    def do_bye(self, args: None) -> None:
        logger.info("Shutting down whisper..")
        logger.success("Done")
        sys.exit(0)