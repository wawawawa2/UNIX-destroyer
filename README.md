# ***THIS PROGRAM IS REALLY DANGEROUS AND DESTRUCTIVE!*** 
## IT CAN DELETE YOUR SYSTEM! 
### DO NOT RUN THIS UNLESS YOU ARE IN A COMPLETELY ISOLATED AND SAFE ENVIRONMENT WITH NO IMPORTANT DATA!
****(MAKE SURE YOU ARE DOING EVERYTHING SAFELY AND CORRECTLY!)****
****I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY THIS PROGRAM****
****RUN THIS AT YOUR OWN RISK, MAKE SURE TO NOT RUN THIS ON REAL HARDWARE, AGAIN, I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY THIS PROGRAM****
code:
```python
# dont_run_this_code.py
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
    print('that is not even y or n, did you get a typo?')
    import time; time.sleep(5)
```
---
how to run it safely:
- 1. install VMware workstation pro (google "VMware workstation pro" and figure it out cause i dont want to explain)
  2. click on "create a new virtual machine" in VMware workstation pro
  3. click "typical (recommended)"
  4. get a linux ISO file of your choice
  5. click "installer disc image file (iso)"
  6. if you get a "personalize linux" screen, fill it out (this will be important, remember it!)
  7. click "next"
  8. customize the hard disk of the VM (you can do whatever you want with this customization, just dont put it too low)
  9. click "finish"
  10. to power on the VM, click "power on this virtual machine"
