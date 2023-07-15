from django.shortcuts import render

# Create your views here.


# Emri i skedarit: views.py
import qrcode


def generate_wifi_qrcode(request):
    if request.method == 'POST':
        ssid = request.POST.get('ssid')
        password = request.POST.get('password')

        # Format the WiFi network information as a string
        wifi_info = f"WIFI:T:WPA;S:{ssid};P:{password};;"

        # Generate the QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(wifi_info)
        qr.make(fit=True)

        # Create an image from the QR code
        qr_image = qr.make_image(fill="black", back_color="white")

        # Save the QR code image
        qr_image.save("app/static/assets/img/wifi_qrcode.png")
        print("QR code generated successfully!")
        return render(request, 'result.html')
    else:
        return render(request, 'generate.html')
    
