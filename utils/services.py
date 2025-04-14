import os
import datetime
import subprocess
from . import logger
from groq import Groq
from dotenv import load_dotenv

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

    Using the following template, generate a concise and meaningful git commit message that accurately describes the changes made in the code:
    Template: "<type>(<scope>): <short description>"
    
    - <type>: The type of change (e.g., feat, fix, docs, style, refactor, test, chore).
    - <scope>: The scope of the change (e.g., file or module name, optional).
    - <short description>: A brief description of the change (imperative mood, max 50 characters).

    Based on this template generate me a commit message. 
    """

    try:
        logger.info("Generating commit message...")
        commit_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt.strip()}],
            model="gemma2-9b-it",
            temperature=0.8,
        )
        commit_msg = commit_completion.choices[0].message.content.strip()

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
            model="gpt-4",
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