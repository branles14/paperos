from datetime import datetime
import calendar
from reportlab.lib.pagesizes import A6
from reportlab.lib import colors
from reportlab.lib.units import mm


def draw(c, top_y, bottom_y, margin=6 * mm):
    """Draw a simple month grid inside the given header bounds."""
    today = datetime.today()
    year = today.year
    month = today.month
    day = today.day

    month_matrix = calendar.monthcalendar(year, month)
    rows = len(month_matrix)

    cell_size = (top_y - bottom_y) / rows

    start_x = margin
    start_y = top_y - cell_size
    padding = cell_size * 0.3

    c.setFont("Courier", 8)

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

