import re
from PyPDF2 import PdfReader

# Abra o arquivo PDF
with open('C:\oletos\este.pdf', 'rb') as pdf_file:
    pdf_reader_bb = PdfReader(pdf_file)

    # Itere pelas páginas do PDF
    for page_num, page in enumerate(pdf_reader_bb.pages):
        page_text = page.extract_text()

        # Padrão para data
        date_pattern = r'\d{2}/\d{2}/\d{4}'
        dates = re.findall(date_pattern, page_text)

        # Padrão para valores monetários
        value_pattern = r'\(=\) Valor Cobrado\s*([\d.,]+)'
        values = re.findall(value_pattern, page_text)

        # Padrão para beneficiário
        beneficiario_pattern = r'Beneficiário\s*([^Espécie]+)'
        beneficiario = re.findall(beneficiario_pattern, page_text)

        # Padrão para o código de barras
        codigo_de_barras_pattern = r'(\d{5}\.\d{5} \d{5}\.\d{6} \d{5}\.\d{6} \d{1} \d{14})'
        codigo_de_barras = re.findall(codigo_de_barras_pattern, page_text)

        numero_documento_pattern = r'(\d{4}-\d{1}/\d{1})'
        numero_documento = re.findall(numero_documento_pattern, page_text)

        if dates:
            print(f'Página {page_num + 1} - Vencimento: {dates[0]}')
        if values:
            print(f'Página {page_num + 1} - Valor: {values[0]}')
        if beneficiario:
            beneficiario_text = beneficiario[0].strip()
            print(f'Página {page_num + 1} - Empresa: {beneficiario_text}')
        if codigo_de_barras:
            print(
                f'Página {page_num + 1} - Código de Barras: {codigo_de_barras[0]}')
        if numero_documento:
            print(
                f'Página {page_num + 1} - NF: {numero_documento[0]}')


pdf_file.close()


print("-"*50)

with open('C:\oletos\este2.pdf', 'rb') as pdf_file:
    pdf_reader_bb_correios = PdfReader(pdf_file)

    # Itere pelas páginas do PDF
    for page_num, page in enumerate(pdf_reader_bb_correios.pages):
        page_text = page.extract_text()

        # Padrão para data (DD/MM/AAAA)
        date_pattern = r'\d{2}/\d{2}/\d{4}'
        dates = re.findall(date_pattern, page_text)

        # Padrão para valores monetários (R$ X.XXX,XX)
        value_pattern = r'R\$\s*([\d.,]+)'
        values = re.findall(value_pattern, page_text)

        # Padrão para beneficiário
        beneficiario_pattern = r'Beneficiário\s*([^\n]+)'
        beneficiario = re.findall(beneficiario_pattern, page_text)

        # Padrão para o código de barras (na estrutura "00190.00009 03164.048005 00015.619174 1 96670000260316")
        codigo_de_barras_pattern = r'(\d{5}\.\d{5} \d{5}\.\d{6} \d{5}\.\d{6} \d{1} \d{14})'
        codigo_de_barras = re.findall(codigo_de_barras_pattern, page_text)

        # Padrão para o número do documento (estrutura "682914")
        numero_documento_pattern = r'(\d{6})'
        numero_documento = re.findall(numero_documento_pattern, page_text)

        # Verifique se encontrou alguma data e valor
        if len(dates) >= 2:
            segunda_data = dates[1]
            print(
                f'Página {page_num + 1} - Vencimento: {segunda_data}')
        if values:
            print(f'Página {page_num + 1} - Valor: {values[0]}')
        if beneficiario:
            print(f'Página {page_num + 1} - Empresa: {beneficiario[0]}')
        if codigo_de_barras:
            print(
                f'Página {page_num + 1} - Código de Barras: {codigo_de_barras[0]}')
        if numero_documento:
            print(
                f'Página {page_num + 1} - NF: {numero_documento[0]}')

pdf_file.close()


print("-"*50)


with open('C:\oletos\este3.pdf', 'rb') as pdf_file:
    pdf_reader_san = PdfReader(pdf_file)

    # Itere pelas páginas do PDF
    for page_num, page in enumerate(pdf_reader_san.pages):
        page_text = page.extract_text()

        # Padrão para data
        date_pattern = r'\d{2}/\d{2}/\d{4}'
        dates = re.findall(date_pattern, page_text)

        # Padrão para valores monetários
        value_pattern = r'Valor da fatura\s*R\$\s*([\d.,]+)'
        values = re.findall(value_pattern, page_text)

        # Padrão para beneficiário
        beneficiario_pattern = r'Beneficiário\s*([^\n]+)'
        beneficiario = re.findall(beneficiario_pattern, page_text)

        # Padrão para o código de barras
        codigo_de_barras_pattern = r'(\d{5}\.\d{5} \d{5}\.\d{6} \d{5}\.\d{6} \d{1} \d{14})'
        codigo_de_barras = re.findall(codigo_de_barras_pattern, page_text)

        # Padrão para o número do documento
        numero_documento_pattern = r'\d{7}-\d{2}'
        numero_documento = re.findall(numero_documento_pattern, page_text)

        # Verifique se encontrou alguma data e valor
        if len(dates) >= 2:
            segunda_data = dates[1]
            print(
                f'Página {page_num + 1} - Vencimento: {segunda_data}')
        if values:
            print(f'Página {page_num + 1} - Valor: {values[0]}')

        if beneficiario:
            beneficiario_inicio = beneficiario[0].split('- ')
            beneficiario_inicio = beneficiario_inicio[1].split(' /')
            print(f'Página {page_num + 1} - Empresa: {beneficiario_inicio[0]}')
        if codigo_de_barras:
            print(
                f'Página {page_num + 1} - Código de Barras: {codigo_de_barras[0]}')

        if numero_documento:
            print(
                f'Página {page_num + 1} - NF: {numero_documento[0]}')

pdf_file.close()
