'''We’ve just made our robot do something automatically without human help. This is what
 Control-M does at an enterprise level — scheduling jobs.'''

import schedule
import time
import os
from datetime import datetime

def check_file():
    filename = "hello.txt"
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("This file was created automatically.\n")
        print(f"[{datetime.now()}] File created: {filename}")
    else:
        print(f"[{datetime.now()}] File already exists.")

# Run the task every 1 minute
schedule.every(1).minutes.do(check_file)

print("🤖 Automation bot is running...")

while True:
    schedule.run_pending()
    time.sleep(1)
