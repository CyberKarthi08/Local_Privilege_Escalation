import Linux_LPE

class privilege_escalation():

    def __init__(self):

        self.linux_01 = None
        self.windows_02 = None

    def startup_privilege():
        # TODO #1 --> If you want to checkout which operating system
        print("\nTODO : linux Local Privilege Eacalation\n")


class master_excution():
    def __init__(self):
        super().__init__()

    def kernel_excution():
        Linux_LPE.KernelBase.kernel_info()   
    
    def user_excution():
        Linux_LPE.UserBase.check_user_privilege()
        Linux_LPE.UserBase.kernel_info()
        


if __name__ == "__main__":

    privilege_escalation.startup_privilege()
    master_excution.user_excution()
    

    