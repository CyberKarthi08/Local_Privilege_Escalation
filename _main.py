import linux_user_base

class privilege_escalation():

    def __init__(self):

        self.linux_01 = None
        self.windows_02 = None

    def check_operting_system():
        # TODO #1 --> If you want to checkout which operating system
        print("\nTODO : linux Local Privilege Eacalation\n")

class master_excution(linux_user_base.LinuxUserBase):
    def __init__(self):
        super().__init__()
    
    def main_excution():
        linux_user_base.LinuxUserBase.check_user_privilege()


if __name__ == "__main__":
    privilege_escalation.check_operting_system()
    master_excution.main_excution()
    

    