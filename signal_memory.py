def should_send_signal(signal):

    try:

        with open("last_signal.txt", "r") as file:
            last_signal = file.read().strip()

    except:
        last_signal = ""

    if signal == last_signal:
        return False

    with open("last_signal.txt", "w") as file:
        file.write(signal)

    return True