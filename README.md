# MIMDos

MIMDos, belirli bir hedef IP adresine ve portuna UDP paketleri gönderen bir stres testi aracıdır. Bu proje, ağ bant genişliği performansını değerlendirmek veya belirli bir ağın yükünü test etmek için tasarlanmıştır. Kullanıcıların belirleyeceği hedeflere yönelik yüksek bant genişliğine ulaşmayı amaçlamaktadır.

## Özellikler

- **UDP Paket Gönderimi**: Seçilen hedef IP'ye ve porta rastgele veri içeren UDP paketleri gönderir.
- **Paralel Gönderim**: Çok sayıda thread kullanarak bant genişliğini artırmaya çalışır.
- **Hedef Bant Genişliği Ayarı**: Kullanıcılar hedef bant genişliğini belirleyebilirler.
- **ASCII Sanatı**: Başlatıldığında bir ASCII sanatı gösterimi sunar.

## Kullanılan Teknolojiler

- Python 3.x
- `socket` modülü
- `threading` modülü
- `random` modülü

## Kurulum

1. Python'un en son sürümünü sisteminize yükleyin.
2. Depoyu klonlayın:
   ```bash
   git clone https://github.com/mustafaemrertas/MIMDos.git
   cd MIMDos
3. Projeyi çalıştırın:
   ```bash
   python MIMDos.py

## Kullanım
1. Projeyi başlattığınızda, hedef IP adresini ve port numarasını girin.
2. Uygulama, belirttiğiniz bant genişliğini aşana kadar UDP paketleri göndermeye devam edecektir.
3. Gönderim süresi boyunca konsolda sonuçlar görüntülenir.

### Örnek Kullanım

   ```bash
   - **Hedef IP adresini girin**: 192.168.1.1
   - **Hedef Port numarasını girin**: 8080


## Katkıda Bulunma
Eğer bu projeye katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:

1. Forklayın
2. Yeni bir özellik oluşturun veya hata düzeltmeleri için bir dal (branch) açın
3. Değişikliklerinizi ayarlayın ve commit (tamamlama) işlemini yapın
4. Pull request (pull isteği) oluşturun
