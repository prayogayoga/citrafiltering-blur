# Citra Filtering

Tugas dikerjakan oleh:
- [Agung Prayoga](https://github.com/prayogayoga)
- [Muh Isfhani Ghiath](https://github.com/isfaaghyth)

## Filtering

- [x] Salt Noise
- [x] Pepper Noise
- [x] Gaussian Noise
- [x] Speckle Noise
- [ ] Periodic Noise

dan lakukan filtering pada salt and pepper noise dengan menggunakan filter berikut ini,

- [x] Mean Filter
- [x] Median Filter

pada gaussian noise gunakan filter berikut ini:

- [x] Image Averaging
- [x] Average Filtering
- [x] Adaptive Filtering

sedangkan untuk periodic noise gunakan filter di domain frekuensi yaitu menggunakan

- [ ] low pass filter
- [ ] high pass filter
- [ ] band pass filter

## Hasil Ujicoba

gambar yang di ujicoba adalah buah melon. Gambarnya sebagai berikut:

![https://raw.githubusercontent.com/prayogayoga/citrafiltering-blur/master/melon.jpg](https://raw.githubusercontent.com/prayogayoga/citrafiltering-blur/master/melon.jpg)

pertama, kita akan bahas untuk pengujian pada MeanFiltering dan MedianFiltering. Hasil dari filtering akan tampak sebagai berikut.

- Mean

![https://raw.githubusercontent.com/prayogayoga/citrafiltering-blur/master/meanf.png](https://raw.githubusercontent.com/prayogayoga/citrafiltering-blur/master/meanf.png)

- Median

![https://raw.githubusercontent.com/prayogayoga/citrafiltering-blur/master/medianf.png](https://raw.githubusercontent.com/prayogayoga/citrafiltering-blur/master/medianf.png)

sedangkan ketika image diberikan bluring dengan metode Gaussian, hasilnya sebagai berikut:

![https://raw.githubusercontent.com/prayogayoga/citrafiltering-blur/master/gaussian.png](https://raw.githubusercontent.com/prayogayoga/citrafiltering-blur/master/gaussian.png)

Pada gambar dibawah ini adalah hasil ujicoba terhadap S&P, yaitu Salt dan Papper. Memberikan noise bintik berwarna putih (salt) dan noice berwarna hitam (pepper). Hasilnya sebagai berikut:

![https://raw.githubusercontent.com/prayogayoga/citrafiltering-blur/master/s%26p.png](https://raw.githubusercontent.com/prayogayoga/citrafiltering-blur/master/s%26p.png)

## Komparasi

Komparasi dilakukan secara objektif terhadap hasil ujicoba. Peniliannya akan diberikan bobot berdasarkan hasil yang terbaik dari angka 0 - 10.

| Nama Metode Filtering  | Bobot |
| ------------- | ------------- |
| Mean Filter  | 9 |
| Median Filter*  | 10 |
| Gaussian Filter  | 8 |
| Low Pass Filter  | 0 |
| High Pass Filter  | 0 |
| Band Pass Filter  | 0 |
