"""
QR Code Generator
MSCS-633 Advanced Artificial Intelligence - Assignment 2

Prompts the user for a URL and generates a QR code image from it
using the qrcode library.
"""

import sys
import qrcode


def build_qr_code(url: str) -> qrcode.image.pil.PilImage:
    """Create a QR code image encoding the given URL."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")


def main() -> None:
    url = input("Enter the URL to encode as a QR code: ").strip()

    if not url:
        print("No URL entered. Exiting.")
        sys.exit(1)

    img = build_qr_code(url)

    output_file = "qr_code.png"
    img.save(output_file)
    print(f"QR code saved to {output_file}")

    # Open the saved image in the system's default viewer.
    img.show()


if __name__ == "__main__":
    main()
