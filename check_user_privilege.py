import os
import logging

def check_user_privileges():
    if os.getuid() == 0:
        logging.warning("Current user has root/administrator privileges.")
        print("Yes")
    else:
        logging.info("Current user does not have root/administrator privileges.")
        print("No")

if __name__ == "__main__":

    check_user_privileges()