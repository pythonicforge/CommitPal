import sys
from utils import logger
from cli import ComitPal

def app():
    """Entry point for the CLI tool."""
    try:
        ComitPal().cmdloop()
    except KeyboardInterrupt:
        logger.info("Keyboard Interrupt! Shutting down ComitPal...")
        logger.success("Done")
        sys.exit(0)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    app()