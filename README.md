# Giriş
Bu README dosyası, Python'da GUI geliştirmek ve internet hızını hesaplamak için kullanılan üç popüler kütüphaneyi detaylı bir şekilde ele almaktadır:
- **CustomTkinter**: Tkinter'in modern ve özelleştirilebilir bir versiyonu.
- **Tkinter**: Python'un yerleşik GUI kütüphanesi.
- **Speedtest**: İnternet hızını hesaplamak için kullanılan bir kütüphane.

---
Bu README dosyası, Python'da GUI geliştirmek ve internet hızını hesaplamak için kullanılan üç popüler kütüphaneyi detaylı bir şekilde ele almaktadır:
- **CustomTkinter**: Tkinter'in modern ve özelleştirilebilir bir versiyonu.
- **Tkinter**: Python'un yerleşik GUI kütüphanesi.
- **Speedtest**: İnternet hızını hesaplamak için kullanılan bir kütüphane.

---
# CustomTkinter, Tkinter ve Speedtest Kütüphaneleri Hakkında Detaylı Bilgi

## İçindekiler
1. [Giriş](#giriş)
2. [CustomTkinter](#customtkinter)
   - [Nedir?](#nedir)
   - [Özellikleri](#özellikleri)
   - [Kurulum](#kurulum)
   - [Temel Kullanım](#temel-kullanım)
3. [Tkinter](#tkinter)
   - [Nedir?](#nedir-1)
   - [Özellikleri](#özellikleri-1)
   - [Kurulum](#kurulum-1)
   - [Temel Kullanım](#temel-kullanım-1)
4. [Speedtest (internet hızını hesaplama)](#speedtest-internet-hızını-hesaplama)
   - [Nedir?](#nedir-2)
   - [Özellikleri](#özellikleri-2)
   - [Kurulum](#kurulum-2)
   - [Temel Kullanım](#temel-kullanım-2)
5. [Kaynaklar](#kaynaklar)

---

## Kaynaklar
- [CustomTkinter GitHub](https://github.com/TomSchimansky/CustomTkinter)
- [Tkinter Resmi Dokümantasyonu](https://docs.python.org/3/library/tkinter.html)
- [Speedtest CLI](https://github.com/sivel/speedtest-cli)

---

## Speedtest (İnternet Hızını Hesaplama)
### Nedir?
Speedtest, internet hızını ölçmek için kullanılan bir Python kütüphanesidir. Kullanıcıların indirme (download) ve yükleme (upload) hızlarını test eder ve ping sürelerini gösterir.

### Özellikleri
- İndirme ve yükleme hızlarını ölçer
- Ping süresini hesaplar
- Detaylı hız testi sonuçları verir
- Komut satırı ve Python kodu ile kullanılabilir

### Kurulum
```bash
pip install speedtest-cli
```

### Temel Kullanım
```python
import speedtest

st = speedtest.Speedtest()
st.download()  # İndirme hızını ölçer
st.upload()    # Yükleme hızını ölçer

server_names = []
st.get_servers(server_names)
print("Ping:", st.results.ping)
```

---

## Tkinter
### Nedir?
Tkinter, Python'un standart GUI (Grafiksel Kullanıcı Arayüzü) kütüphanesidir. Basit ve hızlı bir şekilde masaüstü uygulamaları geliştirmek için kullanılır. Platformlar arası uyumluluğu sayesinde hem Windows hem de macOS hem de Linux üzerinde çalışır.

### Özellikleri
- Hafif ve hızlı bir GUI geliştirme imkanı
- Python'un yerleşik kütüphanesi, ek kurulum gerektirmez
- Widget çeşitliliği (düğmeler, etiketler, giriş kutuları, listeler, menüler, vb.)
- Kolay olay yönetimi ve düzen yerleşimi

### Kurulum
Tkinter, Python'un standart kütüphanesi ile birlikte gelir. Eğer yüklü değilse, aşağıdaki komutla kurulabilir:
```bash
sudo apt-get install python3-tk
```

### Temel Kullanım
```python
import tkinter as tk

app = tk.Tk()
app.geometry("400x300")
app.title("Tkinter Örneği")

label = tk.Label(app, text="Merhaba, Tkinter!")
label.pack(pady=20)

app.mainloop()
```

---

## CustomTkinter
### Nedir?
CustomTkinter, klasik Tkinter kütüphanesinin modern bir versiyonudur. Daha estetik ve özelleştirilebilir bileşenler sunar. Karanlık ve açık tema desteği gibi gelişmiş özellikleriyle kullanıcı dostu arayüzler tasarlamak için kullanılır.

### Özellikleri
- Modern tasarım bileşenleri (düğmeler, giriş kutuları, sekmeler, vb.)
- Karanlık ve açık tema desteği
- Daha esnek ve özelleştirilebilir stil seçenekleri
- Tkinter ile uyumlu, kolay entegrasyon

### Kurulum
```bash
pip install customtkinter
```

### Temel Kullanım
```python
import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x300")
app.title("CustomTkinter Örneği")

label = ctk.CTkLabel(app, text="Merhaba, CustomTkinter!")
label.pack(pady=20)

app.mainloop()
```

---


