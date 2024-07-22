import openpyxl


workbook = openpyxl.load_workbook('clientes.xlsx')
pagina_clientes = workbook['Sheet1']
for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[1]