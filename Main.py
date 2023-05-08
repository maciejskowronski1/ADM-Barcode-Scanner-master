from Db import DbFunctions as db
from Model.Barcode import Barcode
# import Receipt.ReceiptGenerator
import cv2
from pyzbar.pyzbar import decode


def main() -> None:
    #try:
    db.create_table('barcode', 'code varchar(75) not null', 'name varchar(100) not null, price double not null')
    aa = db.get_all('barcode')
    for i in aa:
        print(i)
     barcodes = [
            Barcode(code='T', name='Product 1', price=9.99),
            Barcode(code='E', name='Product 2', price=19.99),
            Barcode(code='F', name='Product 3', price=29.99)
     ]
     bb = db.insert_multiple('barcode', barcodes)

         receipt = Receipt()
         receipt.generate_pdf("Test", barcodes, "/home/dawid")

         print(aa)
    barcode = Barcode(code='ABC123', name='Product 2', price=9.99)
    db.insert('barcode', barcode)
         aa.price = 2333
         print(aa)
         db.update('barcodes', aa)
             bb = db.get_all('barcodes')
             for i in bb:
                 print(i)
         except Exception as e:
             print(e.args[0])

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # Dekodowanie kodu kreskowego
    decoded_objects = decode(frame)

    # Wyświetlenie wyniku
    for obj in decoded_objects:
        print("Data:", obj.data.decode("utf-8"))
        cv2.putText(frame, str(obj.data.decode("utf-8")), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Wyświetlenie obrazu z kamerki
    cv2.imshow("Scanner", frame)

    # Zakończenie programu po naciśnięciu klawisza 'q'
    if cv2.waitKey(1) == ord('q'):
        break
        cap.release()
        cv2.destroyAllWindows()
if __name__ == '__main__':
    main()
