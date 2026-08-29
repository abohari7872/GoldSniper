from datetime import datetime
import pytz

def get_session():

    india = pytz.timezone("Asia/Kolkata")
    now = datetime.now(india)

    hour = now.hour

    if hour >= 9 and hour < 13:
        return "ASIAN"

    elif hour >= 13 and hour < 18:
        return "LONDON"

    elif hour >= 18 and hour < 23:
        return "NEW YORK"

    else:
        return "OFF HOURS"