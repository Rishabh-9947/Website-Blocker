import os

# Define the path to the hosts file
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # Windows hosts file location
# For Unix or MacOS, use "/etc/hosts"

# IP address to redirect the domains to
redirect_ip = "127.0.0.1"

# Websites to block
blocked_websites = [
    "www.example.com",
    "example.com"
]

def block_websites():
    with open(hosts_path, 'r+') as hosts_file:
        content = hosts_file.read()
        for website in blocked_websites:
            if website not in content:
                hosts_file.write(f"{redirect_ip} {website}\n")
    print("Websites have been blocked.")

def unblock_websites():
    with open(hosts_path, 'r+') as hosts_file:
        lines = hosts_file.readlines()
        hosts_file.seek(0)
        for line in lines:
            if not any(website in line for website in blocked_websites):
                hosts_file.write(line)
        hosts_file.truncate()
    print("Websites have been unblocked.")

# Main function
if __name__ == "__main__":
    action = input("Do you want to (B)lock or (U)nblock websites? [B/U]: ").upper()
    if action == 'B':
        block_websites()
    elif action == 'U':
        unblock_websites()
    else:
        print("Invalid option. Please choose 'B' to block or 'U' to unblock.")