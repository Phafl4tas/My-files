import os

def install_dependencies():
    print("Installing necessary dependencies...")
    os.system("sudo apt update && sudo apt install -y dkms build-essential libelf-dev linux-headers-$(uname -r) git")

def remove_existing_drivers():
    print("Removing existing drivers...")
    os.system("sudo rmmod r8188eu 2>/dev/null")  # Remove the existing driver if loaded
    os.system("sudo rmmod rtl8xxxu 2>/dev/null")  # Remove additional conflicting driver
    os.system("sudo apt remove -y realtek-rtl88xxau-dkms")  # Remove conflicting Realtek driver
    os.system("sudo rm -rf /lib/modules/$(uname -r)/kernel/drivers/net/wireless/realtek/rtl8188eu")  # Remove old driver files
    os.system("sudo depmod -a")  # Update module dependencies

def install_correct_driver():
    print("Cloning and installing the correct driver...")
    os.system("git clone https://github.com/aircrack-ng/rtl8188eus.git")
    os.system("cd rtl8188eus && sudo make && sudo make install")
    os.system("echo 'blacklist r8188eu' | sudo tee -a /etc/modprobe.d/realtek.conf")  # Prevent conflicts
    os.system("echo 'blacklist rtl8xxxu' | sudo tee -a /etc/modprobe.d/realtek.conf")  # Blacklist rtl8xxxu as well
    os.system("sudo modprobe 8188eu")  # Load the correct driver

def main():
    install_dependencies()
    remove_existing_drivers()
    install_correct_driver()
    print("Driver installation complete. You may need to reboot for changes to take effect.")

if __name__ == "__main__":
    main()
