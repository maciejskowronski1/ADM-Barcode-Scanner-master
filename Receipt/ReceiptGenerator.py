import os
import pdfkit
from Model import Barcode


class Receipt:
    def __init__(self):
        pass

    def __calculate_price(self, product_list: list[Barcode]):
        return sum([barcode.price for barcode in product_list])

    def generate_pdf(self, file_name, barcodes, save_path=None) -> bool:
        html = "<html><head><title>Barcodes</title><style>h1{text-align:center;font-size:36px;} h2{" \
               "font-size:24px;}</style></head><body>"
        html += "<h1>ADM</h1>"
        html += "<h2>Twój Rachunek:</h2><br><br>"
        for barcode in barcodes:
            html += f"<div><p>Code: {barcode.code}</p></div>"
            html += f"<div><p>Name: {barcode.name}</p></div>"
            html += f"<div><p>Price: ${barcode.price}</p></div>"
            html += "<hr>"
        html += f"<div><p>Total: {self.__calculate_price(barcodes)}$</p></div>"
        html += "</body></html>"
        options = {
            'page-size': 'Letter',
            'encoding': 'UTF-8',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
        }
        if save_path:
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            pdf_file_name = os.path.join(save_path, file_name)
        else:
            pdf_file_name = file_name
        pdfkit.from_string(html, pdf_file_name, options=options)
        print(f'Barcodes PDF generated successfully: {pdf_file_name}')
        if os.path.isfile(pdf_file_name):
            return True
        else:
            return False
