# # from lex import detect_qr_and_number
# # from parse import parse_colors
# # from eval import generate_output
# # import cv2
# # from color_extractor import extract_colors_after_qr

# # if __name__ == "__main__":
# #     image_path = "C:\\Users\\ADMIN\\OneDrive\\Pictures\\Screenshots\\Screenshot (554).png"

# #     print("Processing image...")

# #     # 🖼 Read the image first
# #     img = cv2.imread(image_path)

# #     # 🧠 Detect QR and loop number
# #     qr_x, loop_count = detect_qr_and_number(img)

# #     if qr_x is None:
# #         # No loop QR detected, just extract and return color sequence as it is
# #         print("No 'loop' QR code found. Returning colors in order...")
# #         color_sequence = extract_colors_after_qr(img, qr_x=None)  # No QR, so no x position

# #         # No loop count — just return the color sequence
# #         final_output = generate_output(color_sequence)
# #     else:
# #         # QR is found, handle looping
# #         color_sequence = extract_colors_after_qr(img, qr_x)
# #         parsed_data = parse_colors(color_sequence, loop_count)

# #         final_output = generate_output(parsed_data)

# #     print("\nFinal Output:")
# #     print(final_output)


# from lex import detect_qr_and_number
# from eval import generate_output
# import cv2
# from color_extractor import extract_colors_after_qr

# if __name__ == "__main__":
#     image_path = "C:\\Users\\ADMIN\\OneDrive\\Pictures\\Screenshots\\Screenshot (555).png"

#     print("Processing image...")

#     # 🖼 Read the image
#     img = cv2.imread(image_path)

#     # 🧠 Detect QR and loop number
#     qr_x, loop_count = detect_qr_and_number(img)

#     if qr_x is None:
#         # No loop QR detected, just extract and return color sequence in order
#         print("No 'loop' QR code found. Returning colors in order...")
#         color_sequence = extract_colors_after_qr(img, qr_x=None)  # No QR, so no x position

#         # Directly print the color sequence
#         final_output = ' '.join(color_sequence)  # Just join the colors as a string
#     else:
#         # QR is found, handle looping (this part is not relevant now)
#         color_sequence = extract_colors_after_qr(img, qr_x)
#         final_output = ' '.join(color_sequence)

#     print("\nFinal Output:")
#     print(final_output)


from lex import detect_qr_and_number
from eval import generate_output
import cv2
from color_extractor import extract_colors_after_qr

if __name__ == "__main__":
    image_path = "C:\\Users\\ADMIN\\OneDrive\\Pictures\\Screenshots\\Screenshot (554).png"

    print("Processing image...")

    # 🖼 Read the image
    img = cv2.imread(image_path)

    # 🧠 Detect QR and loop number
    qr_x, loop_count = detect_qr_and_number(img)

    # Extract color sequence after the QR (if QR found, we start after it, otherwise from the start)
    if qr_x is None:
        print("No 'loop' QR code found. Returning colors in order...")
        color_sequence = extract_colors_after_qr(img, qr_x=None)  # No QR, so no x position
    else:
        print(f"Loop QR detected with loop count: {loop_count}. Returning colors with repetition...")
        color_sequence = extract_colors_after_qr(img, qr_x)  # Start after QR

        # Repeat the color sequence based on loop count
        color_sequence = color_sequence * loop_count

    # Join and print the color sequence as final output
    final_output = ' '.join(color_sequence)
    print("\nFinal Output:")
    print(final_output)
