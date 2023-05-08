import cv2
from pyzbar.pyzbar import decode

# Uruchomienie kamery
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

# Zakończenie kamery i zamknięcie okna
cap.release()
cv2.destroyAllWindows()