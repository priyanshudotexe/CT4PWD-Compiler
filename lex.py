# # import cv2
# # import pytesseract
# # from pyzbar.pyzbar import decode

# # def detect_qr_and_number(image):
# #     qr_codes = decode(image)
# #     for qr in qr_codes:
# #         qr_text = qr.data.decode("utf-8").strip().lower()
# #         if qr_text == "loop":
# #             x, y, w, h = qr.rect
# #             print(f"Detected QR Text: '{qr_text}'")

# #             # 🛠 Make region next to QR bigger for number
# #             number_region = image[y:y+h, x+w:x+w+80]  # previously +40, now +80

# #             # Preprocessing
# #             gray = cv2.cvtColor(number_region, cv2.COLOR_BGR2GRAY)
# #             gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)  # resize 2x
# #             blur = cv2.GaussianBlur(gray, (5, 5), 0)
# #             _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# #             # 🧠 OCR config to detect only digits
# #             custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'

# #             text = pytesseract.image_to_string(thresh, config=custom_config)
# #             text = text.strip()
# #             print(f"OCR Read: '{text}'")

# #             if text.isdigit():
# #                 loop_count = int(text)
# #                 print(f"Detected Loop Count: {loop_count}")
# #             else:
# #                 loop_count = 1
# #                 print(f"Could not detect loop number properly, defaulting to 1")

# #             return x + w + 80, loop_count
# #     return None, 1


# import cv2
# import pytesseract
# from pyzbar.pyzbar import decode

# def detect_qr_and_number(image):
#     qr_codes = decode(image)
#     for qr in qr_codes:
#         qr_text = qr.data.decode("utf-8").strip().lower()
#         if qr_text == "loop":
#             x, y, w, h = qr.rect
#             print(f"Detected QR Text: '{qr_text}'")

#             # 🛠 Make region next to QR bigger for number
#             number_region = image[y:y+h, x+w:x+w+80]  # previously +40, now +80

#             # Preprocessing
#             gray = cv2.cvtColor(number_region, cv2.COLOR_BGR2GRAY)
#             gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)  # resize 2x
#             blur = cv2.GaussianBlur(gray, (5, 5), 0)
#             _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#             # 🧠 OCR config to detect only digits
#             custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'

#             text = pytesseract.image_to_string(thresh, config=custom_config)
#             text = text.strip()
#             print(f"OCR Read: '{text}'")

#             if text.isdigit():
#                 loop_count = int(text)
#                 print(f"Detected Loop Count: {loop_count}")
#             else:
#                 loop_count = 1
#                 print(f"Could not detect loop number properly, defaulting to 1")

#             return x + w + 80, loop_count
#     return None, 1


import cv2
import pytesseract
from pyzbar.pyzbar import decode

def detect_qr_and_number(image):
    qr_codes = decode(image)
    for qr in qr_codes:
        qr_text = qr.data.decode("utf-8").strip().lower()
        if qr_text == "loop":
            x, y, w, h = qr.rect
            print(f"Detected QR Text: '{qr_text}'")

            # 🛠 Make region next to QR bigger for number
            number_region = image[y:y+h, x+w:x+w+80]  # previously +40, now +80

            # Preprocessing
            gray = cv2.cvtColor(number_region, cv2.COLOR_BGR2GRAY)
            gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)  # resize 2x
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # 🧠 OCR config to detect only digits
            custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'

            text = pytesseract.image_to_string(thresh, config=custom_config)
            text = text.strip()
            print(f"OCR Read: '{text}'")

            if text.isdigit():
                loop_count = int(text)
                print(f"Detected Loop Count: {loop_count}")
            else:
                loop_count = 1
                print(f"Could not detect loop number properly, defaulting to 1")

            return x + w + 80, loop_count
    return None, 1
