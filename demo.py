import os
import platform
import subprocess
import logging



# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# User Privilege Analysis
def check_user_privileges():
    if os.getuid() == 0:
        logging.warning("Current user has root/administrator privileges.")
    else:
        logging.info("Current user does not have root/administrator privileges.")

# File and Directory Permissions
def check_file_permissions(file_path):
    try:
        permissions = oct(os.stat(file_path).st_mode)[-3:]
        if permissions != '600':
            logging.warning(f"Insecure permissions detected for file: {file_path}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")

def scan_system_files():
    system_files = [
        "/etc/shadow",
        "/etc/sudoers",
        "/etc/passwd",
        # Add more system files to scan if needed
    ]

    for file_path in system_files:
        check_file_permissions(file_path)

# Process Analysis
def check_process_privileges():
    try:
        cmd = 'ps -eo user,command'
        output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        for line in output.splitlines()[1:]:
            process_info = line.split(None, 1)
            username = process_info[0]
            command = process_info[1]
            
            if username.lower() not in ['root']:
                logging.warning(f"Suspicious process with elevated privileges detected: {command}\n")
    except subprocess.CalledProcessError:
        logging.error("Failed to retrieve process information.")

# Log Analysis
def analyze_system_logs():
    log_files = [
        "/var/log/auth.log",
        "/var/log/secure",
        # Add more log files to analyze if needed
    ]

    for log_file in log_files:
        if os.path.isfile(log_file):
            with open(log_file, 'r') as file:
                log_content = file.read()
                if "privilege escalation" in log_content.lower():
                    logging.warning(f"Privilege escalation attempt detected in log file: {log_file}")



# Main function    
def run_privilege_esc_detection():
    
        print("  __              _______         ________                                           \n")
        print(" |  \            |       \       |        \                                          \n")
        print(" | $$            | $$$$$$$\      | $$$$$$$$                                          \n")
        print(" | $$            | $$__/ $$      | $$__                                              \n")
        print(" | $$            | $$    $$      | $$  \                                             \n")
        print(" | $$            | $$$$$$$       | $$$$$                                             \n")
        print(" | $$_____       | $$            | $$_____                                           \n")
        print(" | $$     \      | $$            | $$     \                                          \n")
        print("  \$$$$$$$$       \$$             \$$$$$$$$                                          \n")
        print("  _______              __                            __      __                      \n")
        print(" |       \            |  \                          |  \    |  \                     \n")
        print(" | $$$$$$$\  ______  _| $$_     ______    _______  _| $$_    \$$  ______   _______   \n")
        print(" | $$  | $$ /      \|   $$ \   /      \  /       \|   $$ \  |  \ /      \ |       \  \n")
        print(" | $$  | $$|  $$$$$$\\$$$$$$  |  $$$$$$\|  $$$$$$$ \$$$$$$  | $$|  $$$$$$\| $$$$$$$\ \n")
        print(" | $$  | $$| $$    $$ | $$ __ | $$    $$| $$        | $$ __ | $$| $$  | $$| $$  | $$ \n")
        print(" | $$__/ $$| $$$$$$$$ | $$|  \| $$$$$$$$| $$_____   | $$|  \| $$| $$__/ $$| $$  | $$ \n")
        print(" | $$    $$ \$$     \  \$$  $$ \$$     \ \$$     \   \$$  $$| $$ \$$    $$| $$  | $$ \n")
        print("  \$$$$$$$   \$$$$$$$   \$$$$   \$$$$$$$  \$$$$$$$    \$$$$  \$$  \$$$$$$  \$$   \$$ \n")
        
        print("\nLocal Privilege Escalation Detection Tool(v0.1) by Pragadeesh\n")
        
        logging.info("User Privilege Analysis:")
        check_user_privileges()

        logging.info("\nFile and Directory Permissions:")
        scan_system_files()

        logging.info("\nProcess Analysis:")
        check_process_privileges()

        logging.info("\nLog Analysis:")
        analyze_system_logs()

# Run the privilege escalation detection tool
if __name__ == '__main__':
    run_privilege_esc_detection()

