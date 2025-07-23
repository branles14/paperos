from reportlab.lib.pagesizes import A6
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

from widgets import calendar, astro

DEFAULT_PATH = "page.pdf"

HEADER_HEIGHT = 30 * mm
MARGIN = 6 * mm
CALENDAR_BOTTOM_PAD = 5 * mm


def create_page(output_path=DEFAULT_PATH):
    """Create a PDF page with calendar and astronomy info."""
    c = canvas.Canvas(output_path, pagesize=A6)

    width, height = A6
    header_top = height - MARGIN
    header_bottom = header_top - HEADER_HEIGHT

    calendar.draw(c, header_top, header_bottom, margin=MARGIN,
                  bottom_pad=CALENDAR_BOTTOM_PAD)
    astro.draw(c, header_top - 12, margin=MARGIN)

    c.setLineWidth(1)
    c.line(MARGIN, header_bottom, width - MARGIN, header_bottom)

    c.save()
    return output_path


if __name__ == "__main__":
    create_page()

