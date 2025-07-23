from datetime import date
from astral import LocationInfo
from astral.sun import sun
from reportlab.lib.pagesizes import A6


def draw(c):
    """Draw sunrise and sunset times on the given canvas."""
    location = LocationInfo("London", "England", "UTC", 51.5, -0.1)
    s = sun(location.observer, date=date.today(), tzinfo=location.timezone)

    sunrise = s['sunrise'].strftime('%H:%M')
    sunset = s['sunset'].strftime('%H:%M')

    width, height = A6
    margin = 20
    x = width - margin
    y = height - margin

    c.setFont("Courier", 10)
    c.drawRightString(x, y, f"Sunrise {sunrise}")
    c.drawRightString(x, y - 12, f"Sunset {sunset}")

