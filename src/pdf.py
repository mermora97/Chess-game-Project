from fpdf import FPDF

def createPdf(pdf):
    pdf.add_page()

    #Title
    pdf.set_font('Times',size=25)
    pdf.cell(200, 10, txt="Chess game report", ln=1, align="C")
    pdf.set_line_width(1)
    pdf.set_draw_color(0, 130, 0)
    pdf.line(20, 20, 200, 20)

def addImagesToPdf(pdf):
    
    #Insert images
    image_path = 'Output/probabilities.png'
    pdf.image(image_path, x=10, y=30, w=100)
    image_path = 'Output/chesstable.png'
    pdf.image(image_path, x=10, y=110, w=100)
    pdf.set_font("Arial", size=10)
    pdf.ln(180)  # move 85 down
    pdf.cell(10, 10, txt="Actual chess table", ln=16)

def save(pdf):
    #Save pdf
    pdf.output("Output/Chessreport.pdf")