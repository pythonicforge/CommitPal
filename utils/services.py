import os
import subprocess
from . import logger
from groq import Groq
from dotenv import load_dotenv
from typing import List, Optional
import datetime

load_dotenv()

@logger.catch
def get_git_diff() -> str:
    """Get the git diff of the current staged changes."""
    result = subprocess.run(['git', 'diff'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode()

@logger.catch
def generate_commit_message(diff_msg: str) -> str | None:
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    prompt = f"""
    I have the following `git diff` output from my current working directory:

    {diff_msg}

    Based on this, please generate a concise and meaningful git commit message that accurately describes the changes made in the code. Ensure the message is professional and adheres to conventional commit standards. Just one liner answer, and nothing else! 
    """

    try:
        logger.info("Generating commit message...")
        commit_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt.strip()}],
            model="llama3-70b-8192",
            temperature=0.8,
            max_tokens=4096,
        )
        commit_msg = commit_completion.choices[0].message.content

        return commit_msg

    except Exception as e:
        logger.critical(f"Error: {e}")
        return ""
    
@logger.catch
def generate_changelog(diff_msg):
    CHANGELOG_DIR = "changelogs"
    os.makedirs(CHANGELOG_DIR, exist_ok=True)
    CHANGELOG_FILE = os.path.join(CHANGELOG_DIR, "changelog.md")
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    prompt = f"""
    I have the following `git diff` output from my current working directory:

    {diff_msg}

    Based on this, please generate a concise and meaningful changelog message that accurately describes the changes made in the code. Ensure the message is professional and adheres to conventional commit standards. Without anything else, just the changelog text and nothing else.
    """

    try:
        logger.info("Generating changelog message...")
        changelog_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt.strip()}],
            model="llama3-70b-8192",
            temperature=0.8,
            max_tokens=4096,
        )
        changelog_msg = changelog_completion.choices[0].message.content

        with open(CHANGELOG_FILE, "a") as file:
            file.write(f"## {datetime.datetime.now().strftime('%Y-%m-%d')}\n")
            file.write(f"{changelog_msg.strip()}\n\n")

        return changelog_msg

    except Exception as e:
        logger.critical(f"Error: {e}")
        return ""

def parse_args(args: str):
    args = args.strip()
    changelog = "--changelog" in args
    args = args.replace("--changelog", "").strip()
    return args, changelog