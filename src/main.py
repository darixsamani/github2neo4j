from database import init_database
import os
import logging



logger = logging.getLogger(__name__)




def main():
    github_content = os.environ.get("GITHUB_CONTEXT")
    logger.info(github_content)
    print(f"github context {github_content}")

    







if __name__=="__main__":

    # init database
    init_database()

    main()
