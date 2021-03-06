import fpdf
from fpdf import FPDF, HTMLMixin

# Create pdf report to show the results in a readable way
# The content of the pdf has to be written following the 
# HTML standard. It will be converted in pdf at the end, 
# using output_pdf()

class MyFPDF(FPDF, HTMLMixin):
    pass

# parameters for the pdf
pdf = MyFPDF()
font_size = 11
html = ''
check = False


# initialize the structure of the pdf and append the title of the report in an HTML format
def init():
    global html
    global check
    pdf.add_page()
    html += '<H1 align="center">MQTTSA Report</H1>'
    check = True

# append a paragraph to the HTML 
def add_paragraph(title, msg=None):
    global html
    global check
    if check == False:
        init()
    if msg != None:
        html += '<h2 align="left">'+title+"</h2><font size="+str(font_size)+">"+msg+'</p><br>'
    else:
        html += '<h2 align="left">'+title+'</h2>'

# append a sub-paragraph to the HTML
def add_sub_paragraph(title, msg=None):
    global html
    if msg != None:
        html += '<h4 align="left">'+title+"</h4><font size="+str(font_size)+">"+msg+'</p><br>'
    else:
        html += '<h4 align="left">'+title+'</h4>'

# append to an existing paragraph of the HTML
def add_to_existing_paragraph(msg):
    global html
    html += "<font size="+str(font_size)+">"+msg+'</font><br>'

# generate the pdf using the HTML
def output_pdf():
    global html
    pdf.write_html(html.encode('utf-8').decode('latin-1'))
    pdf.output("../report.pdf")
