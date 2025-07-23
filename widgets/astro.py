from datetime import date
from astral import LocationInfo
from astral.sun import sun, elevation
from reportlab.lib.pagesizes import A6
from reportlab.lib.units import mm


def draw(c, top_y, margin=6 * mm):
    """Draw basic solar information at the top right of the header."""
    location = LocationInfo("London", "England", "UTC", 51.5, -0.1)
    s = sun(location.observer, date=date.today(), tzinfo=location.timezone)

    sunrise = s["sunrise"].strftime("%H:%M")
    sunset = s["sunset"].strftime("%H:%M")
    noon = s["noon"]
    noon_time = noon.strftime("%H:%M")
    noon_angle = elevation(location.observer, noon)

    width, _ = A6
    x = width - margin
    y = top_y

    c.setFont("Courier", 10)
    c.drawRightString(x, y, f"Sunrise {sunrise}")
    c.drawRightString(x, y - 12, f"Sunset {sunset}")
    c.drawRightString(
        x,
        y - 24,
        f"Solar noon {noon_time} {noon_angle:.1f}\N{DEGREE SIGN}",
    )

