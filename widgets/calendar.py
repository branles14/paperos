from datetime import datetime
import calendar
from reportlab.lib.pagesizes import A6
from reportlab.lib import colors


def draw(c):
    """Draw a simple month calendar on the given canvas."""
    today = datetime.today()
    year = today.year
    month = today.month
    day = today.day

    width, height = A6

    cell_size = 20
    start_x = 20
    start_y = height - 40
    padding = 6

    c.setFont("Courier", 10)

    month_name = calendar.month_name[month]
    c.drawString(start_x, start_y + 20, f"{month_name} {year}")

    month_matrix = calendar.monthcalendar(year, month)

    for row_idx, week in enumerate(month_matrix):
        for col_idx, date in enumerate(week):
            if date == 0:
                continue
            x = start_x + col_idx * cell_size
            y = start_y - row_idx * cell_size

            if date == day:
                c.setFillColor(colors.black)
                c.rect(x, y, cell_size, cell_size, fill=1)
                c.setFillColor(colors.white)
            else:
                c.setFillColor(colors.transparent)
                c.rect(x, y, cell_size, cell_size, fill=0)
                c.setFillColor(colors.black)

            c.drawCentredString(x + cell_size / 2, y + padding, f"{date:2}")

    c.setFillColor(colors.black)

