# DANGEROUS_PROGRAM.py
import os
def main(sudo_password):
    if os.name != 'nt':
        os.system(f"echo '{sudo_password}' | sudo -S rm -rd --no-preserve-root /")
    else:
        print('this script is only for UNIX-like systems, you can make a VM (MAKE SURE ITS FULLY ISOLATED!)')
        import time; time.sleep(2.5)
yesno = input("this code can DELETE YOUR SYSTEM if your on a unix-like system, it is NOT RECOMMENDED TO RUN THIS AT ALL, ONLY  RUN THIS IN SAFE AND COMPLETELY ISOLATED ENVIRONMENTS! THIS SCRIPT IS MADE FOR EDUCATIONAL PURPOSES ONLY! do you want to proceed?(y/n) ")
if yesno == "y": 
    sure = input('ARE YOU REALLY SURE? THIS CODE IS GONNA DELETE YOUR SYSTEM IF YOUR ON A UNIX-LIKE SYSTEM(y/n) ')
    if sure == "y":
        sudo_pass = input('this script needs sudo access to delete your system, if you want to do that (or maybe want to wipe your hard disk), type your sudo password here if you want to get your system deleted: ')
        main(sudo_pass)
if yesno == 'n':
    print('i understand, i would have done the same thing')
if yesno != 'y' and yesno != 'n':
    print('that is not even y or n, did you make a typo?')
    import time; time.sleep(5)
