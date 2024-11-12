import time

from datetime import datetime

from win10toast import ToastNotifier


def send_notification():
    toaster = ToastNotifier()

    toaster.show_toast("Time Alert", f"It's either {datetime.now()}!", duration=10)


def main():
    while True:
        # Get the current time

        now = datetime.now()

        current_time = now.strftime("%H:%M")

        # Check if the current time is like 17:17 or else

        # if current_time.split(":")[0] == current_time.split(":")[1]:
        if current_time == "17:54":
            send_notification()

            # Wait for a minute to avoid multiple notifications in the same minute

            time.sleep(60)

        else:
            # Sleep for a short while before checking again

            time.sleep(10)


if __name__ == "__main__":
    main()
