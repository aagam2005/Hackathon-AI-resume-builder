from ai_helper import suggest_improvements
from fpdf import FPDF

class ResumePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.first_page = True  # Flag to indicate if it's the first page

    def header(self):
        if self.first_page:  # Only add the heading on the first page
            self.set_font("Arial", "B", 16)
            self.cell(0, 10, "Resume", align="C", ln=True)
            self.ln(10)
            self.first_page = False  # After the first page, don't add the heading again

    def add_section(self, title, content):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 10, content)
        self.ln(5)

def generate_resume(name, contact, education, experienc
