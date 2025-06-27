import qrcode
def generate_qr():
    data=input("Enter text or URLto encode into QR code".strip())
    filename=input("Enter output filename:").strip()
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    img.save(f"{filename}.png")
    print(f"QR code saved as {filename}.png")
if __name__=="__main__":
    generate_qr()    