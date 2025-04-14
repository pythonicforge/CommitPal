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

    Based on this, generate a concise and meaningful git commit message that accurately describes the changes made in the code. 
    Ensure the message is professional and adheres to conventional commit standards.

    IMPORTANT: Return only the commit message as a single line of text. Do not include any additional text, explanations, or formatting. 
    Do not include phrases like "Based on the `git diff` output" or "Here is the commit message". Just return the commit message itself.
    """

    try:
        logger.info("Generating commit message...")
        commit_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt.strip()}],
            model="llama3-70b-8192",
            temperature=0.8,
            max_tokens=4096,
        )
        commit_msg = commit_completion.choices[0].message.content.strip()

        # Remove surrounding quotes if present
        if commit_msg.startswith('"') and commit_msg.endswith('"'):
            commit_msg = commit_msg[1:-1]

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

@logger.catch
def auto_push_to_github(commit_message: str) -> None:
    """Automate committing and pushing changes to GitHub."""
    try:
        logger.info("Staging changes...")
        subprocess.run(["git", "add", "."], check=True)

        logger.info("Committing changes...")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        logger.info("Pushing changes to GitHub...")
        subprocess.run(["git", "push"], check=True)

    except subprocess.CalledProcessError as e:
        logger.error(f"Git command failed: {e}")
        raise

    except Exception as e:
        logger.critical(f"Unexpected error during Git operations: {e}")
        raise

def parse_args(args: str) -> tuple[str, bool, bool]:
    args = args.strip()
    changelog = "--changelog" in args
    auto_push = "--auto-push" in args

    args = args.replace("--auto-push", "").strip()
    args = args.replace("--changelog", "").strip()
    return args, changelog, auto_push