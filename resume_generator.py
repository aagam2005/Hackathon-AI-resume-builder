from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        print("Adding Header")
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Resume", align="C", ln=True)
        self.ln(10)

    def add_section(self, title, content):
        print(f"Adding Section: {title}")
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 10, content)
        self.ln(5)

def generate_resume(name, contact, education, experience, skills, additional):
    try:
        print("Initializing PDF")
        pdf = ResumePDF()
        pdf.add_page()
        
        print("Adding sections")
        pdf.add_section("Name", name)
        pdf.add_section("Contact Information", contact)
        pdf.add_section("Education", education)
        pdf.add_section("Experience", experience)
        pdf.add_section("Skills", skills)
        if additional:
            pdf.add_section("Additional Information", additional)
        
        # Save the file
        file_name = "resume.pdf"
        print(f"Saving PDF as {file_name}")
        pdf.output(file_name)
        return file_name
    except Exception as e:
        print(f"Error: {e}")