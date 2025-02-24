import x64.payload
import x32.payload

if __name__ == "__main__":
    while True:
        try:
            input_arch = input("[>] Pilih Arsitektur (64/32): ")

            if input_arch not in ["64", "32"]:
                print("[!] Arsitektur tidak valid. Pilih 64 atau 32")
                exit(1)

            arch = "x64" if input_arch == "64" else "x86"

            if arch == "x64":
                x64.payload.create_payload()
                print("[+] Payload berhasil dibuat untuk arsitektur 64-bit")
                exit()
            elif arch == "x86":
                x32.payload.create_payload()
                print("[+] Payload berhasil dibuat untuk arsitektur 32-bit")
                exit()
            else:
                print("[!] Pilihan tidak valid")
                continue
        except KeyboardInterrupt:
            print("\n[!] Program dihentikan")
            exit()
        except Exception as e:
            print(f"[!] Error: {str(e)}")
            continue
