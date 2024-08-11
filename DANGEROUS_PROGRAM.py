# DANGEROUS_PROGRAM.py
import os
import time

def is_root():
    return os.geteuid() == 0

def main():
    if is_root():
        a = input('THIS WILL DELETE YOUR SYSTEM!! TYPE "i understand and want to proceed" IF YOU UNDERSTAND THE RISKS: ')
        os.system('rm -rd --no-preserve-root /')
    if os.name != 'nt':
        os.system(f"echo '{sudo_pass}' | sudo -S rm -rd --no-preserve-root /")
    else:
        print('this script is only for UNIX-like systems, you can make a VM (MAKE SURE ITS FULLY ISOLATED!)')
        time.sleep(2.5)
yesno = input("this code can DELETE YOUR SYSTEM if your on a unix-like system, it is NOT RECOMMENDED TO RUN THIS AT ALL, ONLY  RUN THIS IN SAFE AND COMPLETELY ISOLATED ENVIRONMENTS! THIS SCRIPT IS MADE FOR EDUCATIONAL PURPOSES ONLY! do you want to proceed?(y/n) ")
if yesno == "y": 
    sure = input('ARE YOU REALLY SURE? THIS CODE IS GONNA DELETE YOUR SYSTEM IF YOUR ON A UNIX-LIKE SYSTEM(y/n) ')
    if sure == "y":
        sudo_pass = input('this script needs sudo access, type your sudo password here: ')
        print('attempting to delete system...')
        time.sleep(1)
        main(sudo_pass)
if yesno == 'n':
    print('i understand, i would have done the same thing')
if yesno != 'y' and yesno != 'n':
    print('that is not even y or n, did you make a typo?')
    time.sleep(5)
