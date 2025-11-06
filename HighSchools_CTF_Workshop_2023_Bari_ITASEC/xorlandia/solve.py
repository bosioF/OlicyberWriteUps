testo_hex = "2e35233a272114063e1a06103d0d3804131c030e1c38150d36013d0202000c1a3d01301f0e1036003d0a16140305113d1b083e03481f"
chiave_ascii = "gabibbo"

testo_bytes = bytes.fromhex(testo_hex)
chiave_bytes = chiave_ascii.encode()

risultato_bytes = bytes([testo_bytes[i] ^ chiave_bytes[i % len(chiave_bytes)] for i in range(len(testo_bytes))])

risultato_ascii = risultato_bytes.decode(errors="replace")
risultato_hex = risultato_bytes.hex()

print(risultato_ascii)
