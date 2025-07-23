from datetime import datetime
import calendar
from reportlab.lib import colors
from reportlab.lib.units import mm


def draw(c, top_y, bottom_y, margin=6 * mm, bottom_pad=5 * mm):
    """Draw a simple month grid inside the given header bounds.

    ``margin`` is the left margin used to align the grid with the rest of
    the page. ``bottom_pad`` adds a gap below the grid while allowing the
    top row to sit flush with ``top_y``.
    """
    today = datetime.today()
    year = today.year
    month = today.month
    day = today.day

    width, _ = A6

    month_matrix = calendar.monthcalendar(year, month)
    rows = len(month_matrix)

    cell_size = (top_y - bottom_y - bottom_pad) / rows

    start_x = margin
    start_y = top_y - margin - cell_size
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

