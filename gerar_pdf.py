from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Relatório de Documentos", ln=True, align='C')
pdf.output("relatorio_documentos.pdf")
