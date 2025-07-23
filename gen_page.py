from reportlab.lib.pagesizes import A6
from reportlab.pdfgen import canvas

from widgets import calendar, astro

DEFAULT_PATH = "page.pdf"

def create_page(output_path=DEFAULT_PATH):
    """Create a PDF page with calendar and astronomy info."""
    c = canvas.Canvas(output_path, pagesize=A6)
    calendar.draw(c)
    astro.draw(c)
    c.save()
    return output_path


if __name__ == "__main__":
    create_page()

