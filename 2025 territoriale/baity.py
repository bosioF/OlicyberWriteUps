import base64

enc_flag = "Ao(mgHYtQJARB^:F^J`7F`(_sD)5Nj?X"
try:
    decoded = base64.b85decode(enc_flag)
    print(decoded.decode('utf-8'))
except Exception as e:
    print("Errore di decodifica:", e)
