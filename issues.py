import random

#SAFE MODE - True for demos/GitHub (non-destructive in VM), False for real time changes in VM.
SAFE_MODE = True

#FUNCTION TO CALL THE GET FIX COMMAND - Real or simulated.
def get_fix_cmd(real, simulated_description):
    if SAFE_MODE:
        return f"[Simulated Mode] {simulated_description}\n\n👉 Real Command: `{real}`"
    else:
        return real
    # return checks safe mode and determine if a real command is used or a simulated one

def generate_random_issue():
    return random.choice(issues)
    # return picks a random issue

issues = [
    {
        "title": "Apache service down",
        "description": "Website not loading. Apache service stopped.",
        "fix_command": get_fix_cmd(
            "sudo systemctl restart apache2",
            "Restart the Apache web service to restore website availability."
        )
    },
    {
        "title": "Disk space full",
        "description": "System running out of space in /tmp directory.",
        "fix_command": get_fix_cmd(
            "sudo rm -rf /tmp/*",
            "Clear temporary files to free up space in /tmp."
        )
    },
    {
        "title": "Network connectivity issue",
        "description": "No internet connection detected on server.",
        "fix_command": get_fix_cmd(
            "sudo systemctl restart NetworkManager",
            "Restart the network manager to restore connectivity."
        )
    },
    {
        "title": "SSH service stopped",
        "description": "Unable to connect to the server via SSH.",
        "fix_command": get_fix_cmd(
            "sudo systemctl restart ssh",
            "Restart the SSH service to allow remote access again."
        )
    },
    {
        "title": "High CPU usage",
        "description": "System lag caused by a runaway process.",
        "fix_command": get_fix_cmd(
            "sudo pkill -f stress",
            "Terminate the runaway process causing high CPU utilization."
        )
    },
    {
        "title": "Permission denied on folder",
        "description": "User cannot access /var/www/html directory.",
        "fix_command": get_fix_cmd(
            "sudo chmod -R 755 /var/www/html",
            "Reset folder permissions to allow web access."
        )
    },
    {
        "title": "Updates required",
        "description": "System pending critical security updates.",
        "fix_command": get_fix_cmd(
            "sudo apt update && sudo apt upgrade -y",
            "Apply all pending security updates to keep the system secure."
        )
    },
    {
        "title": "Hostname misconfigured",
        "description": "Server showing incorrect hostname.",
        "fix_command": get_fix_cmd(
            "sudo hostnamectl set-hostname webserver01",
            "Set the correct hostname for the server."
        )
    },
    {
        "title": "Firewall blocking port 80",
        "description": "Cannot reach web server; port 80 blocked by firewall.",
        "fix_command": get_fix_cmd(
            "sudo ufw allow 80/tcp",
            "Allow HTTP traffic by opening port 80 in the firewall."
        )
    },
    {
        "title": "Cron job failed",
        "description": "Backup job did not execute as scheduled.",
        "fix_command": get_fix_cmd(
            "sudo systemctl restart cron",
            "Restart the cron service to resume scheduled tasks."
        )
    }
]