# LLM Text Generation with Google Gemini

## Proje Hakkında

Bu projede Google Gemini API kullanarak Python ile yapay zekâ destekli bir metin üretim fonksiyonu geliştirdim.

Kullanıcıdan alınan bir konu, Gemini modeline iletilerek işleniyor ve konu hakkında yapılandırılmış bir yanıt oluşturuluyor. Geliştirme sürecinde yalnızca API üzerinden metin üretmeye değil, modelin yanıtlarını farklı parametrelerle kontrol etmeye ve belirli bir JSON formatında çıktı almaya odaklandım.

Proje sayesinde büyük dil modellerinin API üzerinden nasıl kullanılabildiğini, prompt yapılandırmasını ve model çıktılarının nasıl kontrol edilebildiğini uygulamalı olarak deneyimledim.

## Kullanılan Teknolojiler

- **Python:** Uygulamanın geliştirilmesi.
- **Google Gemini API:** Metin üretimi için kullanılan yapay zekâ modeli.
- **Google Gen AI SDK:** Gemini API ile bağlantı kurulması ve içerik oluşturulması.
- **python-dotenv:** API anahtarının ortam değişkenleri üzerinden okunması.

## Özellikler

### 1. Konuya Göre Metin Üretimi
Kullanıcıdan alınan konu, Gemini modeline gönderilerek konu hakkında bir açıklama oluşturuluyor.

### 2. Model Parametrelerini Ayarlama

Metin üretim sürecini kontrol etmek için üç farklı parametre kullanılıyor:

- **Temperature:** Modelin yanıtlarındaki rastgelelik ve çeşitlilik düzeyini ayarlamak için kullanılıyor.
- **Top-P:** Modelin kelime seçimindeki olasılık dağılımını kontrol ediyor.
- **Max Output Tokens:** Oluşturulacak yanıtın maksimum token sayısını belirliyor.

Bu parametreler fonksiyon çağrısı sırasında değiştirilebiliyor.

### 3. System Instruction

Modelin nasıl yanıt vermesi gerektiğini belirlemek için system instruction kullanılıyor.

Mevcut yapılandırmada modelden:
- Türkçe yanıt vermesi,
- Profesyonel ve sade bir dil kullanması,
- Yanıtlarında kaynak belirtmesi isteniyor.

### 4. Structured Output (JSON)

Modelin yanıtlarını belirli bir yapıda alabilmek için JSON Schema kullanılıyor.

Oluşturulan yanıt üç temel alandan oluşuyor:

| Alan | Açıklama |
|---|---|
| `konu` | İşlenen konu |
| `seviye` | Konunun seviyesi |
| `aciklama` | Konuya ilişkin açıklama |

Böylece modelin yanıtı önceden tanımlanan bir JSON yapısına göre oluşturuluyor.

### 5. Hata Yönetimi

API isteği sırasında oluşabilecek hataları kontrol etmek için `try-except` yapısı kullanılıyor. Bir hata oluştuğunda hata mesajı yazdırılıyor ve fonksiyon `None` döndürüyor.

## Proje Yapısı

```text
llm-text-generation/
│
├── text_generate.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

**Dosyaların görevleri:**

- `text_generate.py`: Gemini API bağlantısını ve metin üretim fonksiyonunu içerir.
- `requirements.txt`: Projede kullanılan Python kütüphanelerini listeler.
- `.env`: API anahtarını ortam değişkeni olarak saklar.
- `.gitignore`: Gizli ve gereksiz dosyaların Git takibine alınmasını engeller.

## Kurulum

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

### 1. Repository'yi klonlayın

```bash
git clone REPOSITORY_URL
cd llm-text-generation
```

### 2. Sanal ortam oluşturun

```bash
python -m venv venv
```

Sanal ortamı etkinleştirin.

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Bağımlılıkları yükleyin

```bash
pip install -r requirements.txt
```

### 4. API anahtarını tanımlayın

Google AI Studio üzerinden bir Gemini API anahtarı edinin.

Proje ana dizininde `.env` isimli bir dosya oluşturun:

```env
google_apikey=YOUR_API_KEY
```

Kendi API anahtarınızı `YOUR_API_KEY` yerine yazın.

**Not:** `.env` dosyası gizli bilgiler içerdiğinden GitHub'a yüklenmemelidir.

## Kullanım

`text_generate.py` dosyasında bulunan `text_generate()` fonksiyonu kullanılarak metin üretimi gerçekleştirilebilir.

Örnek:

```python
from text_generate import text_generate

response = text_generate(
    topic="Yapay zekânın eğitim alanındaki kullanımı",
    temperature=0.7,
    max_output_tokens=1024,
    top_p=0.9
)

print(response)
```

Fonksiyon parametreleri:

| Parametre | Varsayılan değer | Açıklama |
|---|---:|---|
| `topic` | Zorunlu | Metin üretilecek konu |
| `temperature` | 0.7 | Yanıt çeşitliliğini kontrol eder |
| `max_output_tokens` | 1024 | Maksimum çıktı uzunluğu |
| `top_p` | 0.9 | Token seçimindeki olasılık aralığını kontrol eder |

## Geliştirme Sürecinde Kazandığım Deneyimler

Bu proje üzerinde çalışırken aşağıdaki konularda uygulamalı deneyim kazandım:

- Python ile API kullanımı
- Google Gemini API entegrasyonu
- LLM ve Prompt Engineering temelleri
- Temperature, Top-P ve Token parametreleri
- System Instruction kullanımı
- JSON Schema ile yapılandırılmış çıktı oluşturma
- Python fonksiyonları ve hata yönetimi
- `.env` ile API anahtarı yönetimi

## Geliştirici

**Meryem Küçük**

[GitHub Profilim](https://github.com/Meryemkerimekucuk)
