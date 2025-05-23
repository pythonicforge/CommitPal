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
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        logger.error("GROQ_API_KEY not found in environment variables.")
        return None

    try:
        client = Groq(api_key=api_key)
    except Exception as e:
        logger.critical(f"Failed to initialize Groq client: {e}")
        return None

    prompt = f"""
    I have the following `git diff` output from my current working directory:

    {diff_msg}

    Using the following template, generate a concise and meaningful git commit message that accurately describes the changes made in the code:
    Template: "<type>(<scope>): <short description>"
    
    - <type>: The type of change (e.g., feat, fix, docs, style, refactor, test, chore).
    - <scope>: The scope of the change (e.g., file or module name, optional).
    - <short description>: A brief description of the change (imperative mood, max 50 characters).

    Based on this template generate me a commit message. No explanations or anything other stuff, just the commit message. Just a one-liner commit message.
    """

    try:
        logger.info("Generating commit message...")
        commit_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt.strip()}],
            model="gemma2-9b-it",
            temperature=0.8,
        )
        commit_msg = commit_completion.choices[0].message.content.strip()

        if not commit_msg:
            logger.error("Generated commit message is empty.")
            return None

        if len(commit_msg) > 72:
            logger.warning("Generated commit message exceeds 72 characters. Consider shortening it.")

        return commit_msg

    except KeyError as e:
        logger.critical(f"Unexpected response structure from Groq API: {e}")
        return None

    except ConnectionError as e:
        logger.error(f"Failed to connect to Groq API: {e}")
        return None

    except TimeoutError as e:
        logger.error(f"Request to Groq API timed out: {e}")
        return None

    except Exception as e:
        logger.critical(f"Unexpected error while generating commit message: {e}")
        return None
    
@logger.catch
def generate_changelog(diff_msg):
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        logger.error("GROQ_API_KEY not found in environment variables.")
        return None

    CHANGELOG_DIR = "changelogs"
    os.makedirs(CHANGELOG_DIR, exist_ok=True)
    CHANGELOG_FILE = os.path.join(CHANGELOG_DIR, "changelog.md")
    client = Groq(api_key=api_key)

    prompt = f"""
    I have the following `git diff` output from my current working directory:

    {diff_msg}

    Based on this, please generate a concise and meaningful changelog message that accurately describes the changes made in the code. Ensure the message is professional and adheres to conventional commit standards. Without anything else, just the changelog text and nothing else.
    """

    try:
        logger.info("Generating changelog message...")
        changelog_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt.strip()}],
            model="gemma2-9b-it",
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
    """Automate committing and pushing changes to GitHub with enhanced error handling."""
    try:
        logger.info("Pulling latest changes from remote...")
        subprocess.run(["git", "pull"], check=True)

        logger.info("Staging changes...")
        subprocess.run(["git", "add", "."], check=True)

        logger.info("Committing changes...")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        logger.info("Pushing changes to GitHub...")
        subprocess.run(["git", "push"], check=True)

    except subprocess.CalledProcessError as e:
        if "nothing to commit" in e.stderr.decode().lower():
            logger.warning("No changes to commit. Skipping push.")
        elif "could not read from remote repository" in e.stderr.decode().lower():
            logger.error("Failed to connect to the remote repository. Check your SSH keys or network connection.")
        elif "merge conflict" in e.stderr.decode().lower():
            logger.error("Merge conflict detected. Resolve conflicts manually before pushing.")
        else:
            logger.error(f"Git command failed: {e.stderr.decode().strip()}")
        raise

    except FileNotFoundError as e:
        logger.critical("Git is not installed or not found in PATH. Please install Git and try again.")
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