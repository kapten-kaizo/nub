# Ya Maaf Codingannya berantakan:v
import os
import sys
import requests
if not os.path.isfile("/data/data/com.termux/files/usr/bin/termux-open"): exit("\n[×] Tools ini hanya support untuk termux\n")
if not os.path.isfile("run.py"):
    try: open("run.py","wb").write(requests.get("https://github.com/dahlahmales/nub/raw/main/run.py").content)
    except requests.exceptions.ConnectionError: exit("\n[×] Koneksi Internet Terganggu\n")
os.system("reset")
print("\n[01] Mulai Script")
print("[02] Update Script")
print("[03] Report Bug")
print("[04] Remove Script\n")
while True:
    nanya=input("[?] Pilih : ")
    if nanya.lower() in ["1","01"]:
        os.system("python run.py")
    elif nanya.lower() in ["2","02"]:
        os.system("git pull"); continue
    elif nanya.lower() in ["3","03"]:
        os.system("termux-open https://api.whatsapp.com/send?phone=6281210160358&text=Assalamualaikum%20bang.%20saya%20mau%20report%20bug%20script%20nub%20cracker"); continue
    elif nanya.lower() in ["4","04"]:
        os.remove("run.py"); exit(os.remove(sys.argv[0]))
    elif nanya.lower() in [""," "]:
        print("[×] Jangan Kosong Dong Bang"); continue
    else: print("[×] Pilih Yang Bener Dong Bang"); continue