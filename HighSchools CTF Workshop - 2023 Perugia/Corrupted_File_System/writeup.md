# 4th HighSchools CTF Workshop - Perugia 2023

## Corrupted File System

### Challenge description

`Volevo caricare un'immagine nella presentazione, ma non mi aspettavo questo risultato...`

## Challenge overview

We are given a .pcapng file that shows communication between a client and an FTP server. We're looking for an image to try Wireshark's Export Objects feature. Using that feature yields Corruped_reiser.jpg, and opening the file shows it is corrupted.

A quick inspection of the file's hex reveals that the JPEG magic bytes are missing and have been replaced by the ASCII string HANSREISER. By restoring the correct magic bytes we can fix the JPG; opening the repaired image reveals the flag.

### Flag

`flag{controv3rs1al_f1les}`