from docxtpl import DocxTemplate
from datetime import datetime as dt

current_date = dt.now().strftime("%m-%d-%Y")
str_current_date = str(current_date)
doc = DocxTemplate("invoice_template.docx")
context = {}

doc.render(context)
doc.save(f"invoice-{str_current_date}.docx")
