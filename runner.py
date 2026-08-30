import time
import subprocess

print("GoldSniper Started...")

while True:

    try:

        subprocess.run(
            ["python", "main.py"]
        )

    except Exception as e:

        print(e)

    print("Waiting 60 seconds...")

    time.sleep(60)