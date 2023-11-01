import qrcode

# Create the qr code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Add your unique data to the qr code
data = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to disk
img.save("unique_qr_code.png")
