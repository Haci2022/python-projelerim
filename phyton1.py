import os 

import platform 


if platform.system() == "linux":

    os.system("shutdown /s /T 0")

else:

        os.system("sudo poweroff")