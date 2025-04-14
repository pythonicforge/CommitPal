# CommitPal
🦾 **Your AI-powered terminal buddy for writing smart, stylish, and crystal-clear Git commit messages.**

CommitPal is a command-line tool designed to simplify your Git workflow by generating professional, concise, and meaningful commit messages. It leverages AI to analyze your `git diff` output and create commit messages that adhere to conventional commit standards. Additionally, it supports changelog generation and automates Git operations like staging, committing, and pushing changes.

<br/>

### Features
- **AI-Powered Commit Messages**: Generates concise and meaningful commit messages based on your `git diff` output.
- **Changelog Generation**: Automatically creates changelog entries for your changes.
- **Git Automation**: Supports staging, committing, and pushing changes with a single command.
- **Interactive Shell**: Provides an interactive shell for executing commands.
- **Customizable Templates**: Uses a structured template for commit messages to ensure consistency.

<br/>

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/pythonicforge/CommitPal.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CommitPal
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment variables:
   - Create a `.env` file in the root directory.
   - Add your API key for the AI model:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

<br/>

### Usage
Run the tool by executing the following command:
```bash
python main.py
```

#### Interactive Shell Commands
- **`diff`**: Generate a commit message based on the current `git diff`.
  ```bash
  diff [--changelog] [--auto-push]
  ```
  - `--changelog`: Generate a changelog entry for the changes.
  - `--auto-push`: Automatically stage, commit, and push the changes to GitHub.

- **`clear`**: Clear the terminal screen.
  ```bash
  clear
  ```

- **`bye`**: Exit the interactive shell.
  ```bash
  bye
  ```

<br/>

### Example Workflow
1. Start the interactive shell:
   ```bash
   python main.py
   ```
2. Generate a commit message:
   ```bash
   (comitpal) diff
   ```
   Output:
   ```
   feat(utils): add support for changelog generation
   ```
3. Generate a changelog and push changes:
   ```bash
   (comitpal) diff --changelog --auto-push
   ```

<br/>

### File Structure
```
comitpal/
├── cli/
│   └── shell.py          # Interactive shell implementation
├── utils/
│   ├── __init__.py       # Utility module initialization
│   ├── log_manager.py    # Logger setup
│   ├── services.py       # Core services (commit message generation, changelog, etc.)
├── changelogs/
│   └── changelog.md      # Auto-generated changelog entries
├── main.py               # Entry point for the application
└── README.md             # Project documentation
```

<br/>

### How It Works
1. **Commit Message Generation**:
   - Parses the `git diff` output.
   - Uses an AI model (e.g., `gemma2-9b-it`) to generate a commit message based on a predefined template:
     ```
     <type>(<scope>): <short description>
     ```
   - Example:
     ```
     feat(cli): add support for auto-push flag
     ```

2. **Changelog Generation**:
   - Creates a changelog entry based on the `git diff` output.
   - Appends the entry to `changelogs/changelog.md`.

3. **Git Automation**:
   - Stages all changes (`git add .`).
   - Commits changes with the generated commit message.
   - Pushes changes to the remote repository.

<br/>

### Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve ComitPal.

<br/>

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
