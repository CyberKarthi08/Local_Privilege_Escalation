import os 
import pwd
import logging
import subprocess



class LinuxUserBase():

    def __init__(self) -> None:
        pass

    def check_user_privilege():
        logging.warning("Hacked.....")
        logging.info("Y")
        that_uid = os.getuid()
        that_user_name = pwd.getpwuid(that_uid).pw_name
        print("UID : {0}" . format(that_uid))
        print("USER_NAME : {0}" . format(that_user_name))


    


