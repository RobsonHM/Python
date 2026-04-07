import qrcode

# pip3 install "qrcode[pil]" # MacOS/Linux
# pip install qrcode[pil] # Windows

data = "http://10.0.78.38:5501/home.html" # link you want to encode in the QR code
file_name = "meu_qrcode.png" # name of the file where the QR code will be saved

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save(file_name)

print(f"QR Code generated successfully and saved as: {file_name}")