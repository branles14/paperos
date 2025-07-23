from datetime import datetime
import calendar
from reportlab.lib.pagesizes import A6
from reportlab.lib import colors
from reportlab.lib.units import mm


def draw(c, top_y, bottom_y, margin=5 * mm):
    """Draw a simple month grid inside the given header bounds.

    The ``margin`` parameter controls the padding inside the header on
    all sides.  The calendar grid starts ``margin`` units from the
    header's edges and fits within the remaining space.
    """
    today = datetime.today()
    year = today.year
    month = today.month
    day = today.day

    width, _ = A6

    month_matrix = calendar.monthcalendar(year, month)
    rows = len(month_matrix)

    available_height = top_y - bottom_y - 2 * margin
    available_width = width - 2 * margin

    cell_size = min(available_height / rows, available_width / 7)

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

