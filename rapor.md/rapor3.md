### Ağ Temelleri
Bilgisayar ağları, cihazlar arasında veri iletişimini sağlayan karmaşık sistemlerdir. İnternetin temelini oluşturan bu sistemler, belirli protokoller ve adresleme mekanizmaları ile çalışır. Bu bağlamda IP, Port, DNS, TCP ve UDP kavramları ağ iletişiminin temel yapı taşlarıdır.

1. Internet Protocol (IP)
IP (Internet Protocol), ağ üzerindeki cihazların birbirini tanımlamasını ve veri paketlerinin doğru hedefe yönlendirilmesini sağlayan temel adresleme sistemidir. OSI modelinin ağ katmanında çalışır.
- Görevleri
Paketlerin kaynak ve hedef adreslerini belirlemek
Verinin ağ üzerinde yönlendirilmesini sağlamak
- IPv4 ve IPv6
IPv4: 32-bit adresleme kullanır (örneğin: 192.168.1.1)
IPv6: 128-bit adresleme kullanır ve daha geniş adres alanı sunar

2. Port (Bağlantı Noktası)
Bir cihazın IP adresi o cihazın ağdaki "ev adresi" ise, Port o evin içindeki spesifik "kapıdır". Portlar, ağ trafiğinin hangi uygulama veya servis tarafından işleneceğini belirler.
- Yapı: 0 ile 65535 arasında numaralandırılırlar.

- Port Türleri
Yaygın Örnekler: HTTP için 80, HTTPS için 443, FTP için 21 numaralı portlar kullanılır.

- Amacı: Aynı IP adresine sahip bir bilgisayarda web tarayıcısı, e-posta istemcisi ve bir oyunun aynı anda veri alışverişi yapabilmesini sağlar (Multiplexing).

3. DNS (Domain Name System)
DNS, insanların kullandığı anlamlı alan adlarını (Örn: google.com) bilgisayarların anlayabileceği IP adreslerine (142.250.184.206) çeviren bir rehber sistemidir.

- Çalışma Mantığı: Kullanıcı bir URL girdiğinde, tarayıcı bir DNS sunucusuna sorgu gönderir. Sunucu, bu isme karşılık gelen IP adresini döndürür ve bağlantı bu IP üzerinden kurulur.

- Önemi: 
IP adreslerinin ezberlenmesi zor olduğu için internetin kullanıcı dostu olmasını sağlar.
DNS, kullanıcıların karmaşık IP adreslerini ezberlemeden interneti kullanmasını sağlar.

4. Aktarım Katmanı Protokolleri: TCP ve UDP
Verinin nasıl iletileceğini belirleyen iki ana protokoldür. OSI modelinin Taşıma Katmanında (Transport Layer) görev yaparlar.

# A. TCP (Transmission Control Protocol)
Bağlantı yönelimli bir protokoldür. Veri gönderilmeden önce gönderici ve alıcı arasında bir "el sıkışma" (Three-way handshake) gerçekleşir.

Güvenilirlik: Paketlerin sırasıyla ve eksiksiz ulaştığını kontrol eder. Hata varsa veriyi tekrar ister.

Kullanım Alanları: Web tarama (HTTP/HTTPS), Dosya aktarımı (FTP), E-posta (SMTP).
# B. UDP (User Datagram Protocol)
Bağlantısız bir protokoldür. Veriyi kontrol etmeden, olabildiğince hızlı bir şekilde karşı tarafa gönderir.

Hız: Onay mekanizması olmadığı için TCP'den çok daha hızlıdır ancak veri kaybı yaşanabilir.

Kullanım Alanları: Canlı yayınlar, Online oyunlar, VoIP (Görüntülü/Sesli görüşme).



