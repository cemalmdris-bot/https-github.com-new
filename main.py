import os
import subprocess
import sys

# WormGPT_HARDLOCK - The Master Control for WormOS
# This is the brain that connects all attack modules.

class WormOS_Brain:
    def __init__(self):
        self.banner = """
        ██╗    ██╗ ██╗██╗  ██╗ ██████╗ ██████╗ ██████╗ 
        ██║    ██║ ██║╚██╗ ██║██╔════╝ ██╔══██╗██╔══██╗
        ██║    ██║ ██║ ╚██╗██║██║  ██╗ ██████╔╝██║  ██║
        ██║    ██║ ██║  ╚████║██║  ██╗ ██╔══██╗██║  ██║
        ██║    ██║ ██║   ╚███║██║  ██╗ ██║  ██║██║  ██║
        ╚═╝    ╚═╝ ╚═╝    ╚══╝╚═╝  ╚═╝ ╚═╝  ╚═╝╚═╝  ╚═╝
        [ SYSTEM: EVIL MODE | ACCESS: UNRESTRICTED ]
        """
        print(self.banner)

    def execute_shell(self, script_name):
        print(f"[+] Activating module: {script_name}...")
        try:
            # تنفيذ سكريبت الهجوم بوجاهة الروت (الامتيازات الكاملة)
            subprocess.run(["sudo", "bash", script_name], check=True)
        except Exception as e:
            print(f"[-] Critical Error: {e}")

    def menu(self):
        while True:
            print("\n--- WORMOS OMNIPOTENT PANEL ---")
            print("1. Initialize WormOS (Build the system)")
            print("2. Total Bank & Website Breach (SQL/Zero-Day)")
            print("3. Advanced WiFi Annihilation (Crack/WPA3)")
            print("4. High-End Hardware Hijack (Trojans/RATS)")
            print("5. Self-Destruct/Exit")
            
            choice = input("Select your Target >> ")

            if choice == '1':
                self.execute_shell("attacker.sh --build")
            elif choice == '2':
                self.execute_shell("attacker.sh --website")
            elif choice == '3':
                self.execute_shell("attacker.sh --wifi")
            elif choice == '4':
                self.execute_shell("attacker.sh --hardware")
            elif choice == '5':
                print("Exiting the void... Goodbye.")
                sys.exit()
            else:
                print("Wrong choice, you idiot!")

if __name__ == "__main__":
    brain = WormOS_Brain()
    brain.menu()