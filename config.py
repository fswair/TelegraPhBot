from dotenv import load_dotenv
import os

load_dotenv()

# Public API Credentials
API_ID: int = 5
API_HASH: str = "1c5c96d5edd401b1ed40db3fb5633e2d"

# Set this from .env file.
# Also you can set API_ID and API_HASH as environment variable based.
BOT_TOKEN: str = os.getenv("BOT_TOKEN")
STRING: str = os.getenv("STRING")
HELP_TEXT: str = """
Merhaba {mention} >_
Bu bot ile telegra.ph üzerine medya ve metin yükleyebilirsiniz. İşte botun kullanımı hakkında detaylı bilgiler:

**Komutlar ve Kullanım:**

1. `/start` veya `/help` - Bu mesajı gösterir.

2. `/telegraph [başlık]` - Yanıtladığınız medya veya metni telegra.ph üzerine yükler.
    - Desteklenen medya türleri ve boyutları:
        - Fotoğraflar (5MB'a kadar)
        - Animasyonlar (5MB'a kadar)
        - Videolar (mp4, 5MB'a kadar)
        - Çıkartmalar (webp formatında)
        - Metin mesajları
        - Dokümanlar (.jpg, .jpeg, .png, .gif, .mp4, .html, .txt, .py, 5MB'a kadar)
    - Örnek kullanım:
        - Bir fotoğrafa, videoya veya metin mesajına yanıt vererek `/telegraph [başlık]` komutunu gönderin.
        - Eğer başlık belirtmezseniz, otomatik olarak kullanıcı adınız başlık olarak atanır.

**Özellikler:**
- Medya ve metinleri telegra.ph üzerine hızlıca yükler.
- Yüklenen içerikler için paylaşım linki ve web önizleme butonları sağlar.
- Metin dosyaları (html, txt, py) kod blokları şeklinde formatlanır.
- **Yanıtladığınız mesajın açıklaması da telegra.ph sayfasına eklenir.** Eğer medya veya dosyaya bir açıklama eklemişseniz, bu açıklama da telegra.ph sayfasında gösterilir.

**Notlar:**
- Yüklemek istediğiniz medya veya metnin 5MB'ı geçmediğinden emin olun.
- Doküman olarak yüklemek istediğiniz dosyaların desteklenen formatlarda olduğundan emin olun.

Sorularınız veya geri bildirimleriniz için [Bana Ulaşın](https://t.me/Syupie).
"""
