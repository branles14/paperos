from reportlab.lib.pagesizes import A6
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime
import calendar

# Set up basic values
today = datetime.today()
year = today.year
month = today.month
day = today.day

# Create canvas
pdf_path = "calendar.pdf"
c = canvas.Canvas(pdf_path, pagesize=A6)
width, height = A6

# Calendar settings
cell_size = 20
start_x = 20
start_y = height - 20
padding = 6

# Fonts
c.setFont("Courier", 10)

# Draw month and year header
month_name = calendar.month_name[month]
c.drawString(start_x, start_y + 30, f"{month_name} {year}")

# Get calendar month matrix
month_matrix = calendar.monthcalendar(year, month)

# Draw calendar grid
for row_idx, week in enumerate(month_matrix):
    for col_idx, date in enumerate(week):
        x = start_x + col_idx * cell_size
        y = start_y - row_idx * cell_size

        if date == 0:
            continue  # Skip empty cells

        if date == day:
            c.setFillColor(colors.black)
            c.rect(x, y, cell_size, cell_size, fill=1)
            c.setFillColor(colors.white)
        else:
            c.setFillColor(colors.transparent)
            c.rect(x, y, cell_size, cell_size, fill=0)
            c.setFillColor(colors.black)

        c.drawCentredString(x + cell_size / 2, y + padding, f"{date:2}")

# Finish
c.save()