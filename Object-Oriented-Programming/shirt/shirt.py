# Description: This task generates a personalized CS50 shirtificate PDF. 
# It prompts the user for their name, overlays it in white text onto the 
# center of a red t-shirt template, and adds the "CS50 Shirtificate" title above.

from fpdf import FPDF

def main():
    pdf = FPDF()

    name = input('Name: ')

    pdf.add_page()

    pdf.image('shirtificate.png', x=10, y=50, w=180)

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("helvetica", "B", 24)
    pdf.cell(0, 10, 'CS50 shirtificate', align="C")

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 18)
    pdf.text(x=50, y=100, text=f'{name} took CS50')
    pdf.output('shirtificate.pdf')

main()