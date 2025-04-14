import os
import cmd
import sys
from typing import TextIO, Any
from utils import logger, get_git_diff, generate_commit_message, parse_args, generate_changelog, auto_push_to_github

class ComitPal(cmd.Cmd):
    intro = ""
    prompt = "\n(comitpal) "

    def __init__(self, completekey: str = "tab", stdin: TextIO | None = None, stdout: TextIO | None = None) -> None:
        super().__init__(completekey, stdin, stdout)

    def do_diff(self, args: Any) -> None:
        args, changelog, auto_push = parse_args(args)

        git_diff = get_git_diff()
        commit_message = generate_commit_message(git_diff)
        logger.success("Commit message generated!")

        if changelog:
            generate_changelog(git_diff)
            logger.success("Changelog generated!")

        if auto_push:
            try:
                auto_push_to_github(commit_message)
                logger.success("Changes pushed to GitHub successfully!")
            except Exception as e:
                logger.error(f"Failed to push changes to GitHub: {e}")

    def do_clear(self, args: None) -> None:
        os.system('clear')

    def do_bye(self, args: None) -> None:
        logger.info("Shutting down whisper..")
        logger.success("Done")
        sys.exit(0)