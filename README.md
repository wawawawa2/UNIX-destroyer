# **WARNING: EXTREMELY DESTRUCTIVE PROGRAM**
### **I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY THIS PROGRAM!**
### **THIS SCRIPT IS MADE FOR EDUCATIONAL PURPOSES ONLY**
### **THIS SCRIPT IS MEANT TO BE RUN IN VIRTUAL MACHINES (VMs)**
### **DO NOT RUN THIS ON A REAL MACHINE.**
### **DO NOT USE THIS TO PRANK PEOPLE, THAT IS VERY DESTRUCTIVE AND ILLEGAL**

### **⚠️THIS PROGRAM IS EXTREMELY DANGEROUS AND CAN ERASE UNIX-LIKE SYSTEMS⚠️**
### **⚠️WHEN YOU RUN IT ON THE LATEST VERSION OF UBUNTU, IT BECOMES UNBOOTABLE⚠️**

**THIS PROGRAM IS MADE FOR EDUCATIONAL PURPOSES ONLY.**

**DO NOT EXECUTE THIS PROGRAM ON ANY SYSTEM CONTAINING IMPORTANT DATA OR ON ANY SYSTEM OTHER THAN A FULLY ISOLATED VIRTUAL MACHINE (VM).**

code:
```python
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
    print('that is not even y or n, did you get a typo?')
    import time; time.sleep(5)
```

---

## **Purpose**

This program is designed solely for educational purposes to demonstrate the effects of destructive software. It is not made for any malicious use. Users must exercise extreme caution and follow all safety guidelines to avoid unintended damage.

---

## **How to Safely Run the Program**

### **1. Install VMware Workstation Pro**

1. **Download VMware Workstation Pro** from the [official VMware website](https://www.vmware.com/products/workstation-pro.html).
2. **Install VMware Workstation Pro** following the provided instructions.

### **2. Create a New Virtual Machine**

1. **Open VMware Workstation Pro.**
2. Click **"Create a New Virtual Machine."**

### **3. Configure the Virtual Machine**

1. Select **"Typical (recommended)"** and click **"Next."**
2. **Choose a Linux ISO file** from a trusted source.
3. Click **"Installer disc image file (ISO)"** and select your Linux ISO file.
4. If prompted, **complete the "Personalize Linux"** screen. Document this information for future reference.
5. Click **"Next."**
6. **Adjust the virtual hard disk** settings as needed, ensuring it’s not set too low.
7. Click **"Finish."**

### **4. Start and Install Linux**

1. Click **"Power on this virtual machine."**
2. Follow the on-screen instructions to install Linux.

### **5. Execute the Program Safely**

1. Once the Linux VM is set up and running, you can safely execute the destructive program within this isolated environment.

---

## **Important Safety Guidelines**

- **Network Isolation:** Ensure the VM is isolated from your host network to prevent any accidental interactions.
- **Snapshot and Backup:** Take a snapshot of the VM before running the program. This allows you to restore the VM to a previous state if needed.
- **Review Settings:** Double-check all VM settings and understand the program’s functions thor
