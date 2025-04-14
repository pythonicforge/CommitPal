import sys
from utils import logger
from cli import ComitPal

if __name__ == "__main__":
    try:
        ComitPal().cmdloop()
    except KeyboardInterrupt:
        logger.info("Keyboard Interrupt! Shutting down ComitPal...\nDone")
        sys.exit(0)
    except Exception as e:
        logger.error(e)