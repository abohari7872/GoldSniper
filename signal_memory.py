last_signal = None


def should_send_signal(signal):

    global last_signal

    if signal == last_signal:
        return False

    last_signal = signal

    return True