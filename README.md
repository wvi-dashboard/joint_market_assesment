# JMA Flores 2026 — Dashboard Bukti Interaktif

Dashboard pendukung keputusan untuk *Joint Market Assessment* pascagempa Flores 2026.
Satu berkas `index.html`, tanpa dependensi eksternal, siap dipublikasikan di GitHub Pages.

Wahana Visi Indonesia · Program Evidence, Accountability, Research and Learning (PEARL)

---

## Isi paket

| Berkas | Keterangan |
| --- | --- |
| `index.html` | Dashboard lengkap. Seluruh data agregat tersemat di dalam berkas ini. |
| `.nojekyll` | Menonaktifkan pemrosesan Jekyll di GitHub Pages. |
| `README.md` | Dokumen ini. |

Tidak ada folder `data/`, tidak ada CSS atau JS terpisah, dan tidak ada permintaan
jaringan ke luar (font memakai font sistem). Berkas dapat dibuka langsung lewat
`file://`, di GitHub Pages, maupun dari SharePoint Site Assets.

---

## Publikasi ke GitHub Pages

### Lewat GitHub Desktop + VS Code

1. **GitHub Desktop** → *Fetch/Pull origin* pada repositori
   `wvi-dashboard/Dashboard_pdm_cvp_for_gn` (atau repositori JMA yang dipakai).
2. Salin `index.html`, `.nojekyll`, dan `README.md` ke akar repositori
   (timpa `index.html` yang lama).
3. **GitHub Desktop** → tulis *summary* commit, misalnya
   `Refresh tampilan: mode terang/gelap dan pilihan bahasa ID/EN`, lalu
   *Commit to main* → *Push origin*.
4. Di GitHub: **Settings → Pages** → *Source*: `Deploy from a branch`,
   *Branch*: `main`, *Folder*: `/ (root)` → **Save**.
5. Tunggu 1–2 menit, lalu buka `https://<organisasi>.github.io/<repo>/`.

### Lewat terminal

```bash
git pull
cp index.html .nojekyll README.md /path/ke/repo/
cd /path/ke/repo
git add index.html .nojekyll README.md
git commit -m "Refresh tampilan: mode terang/gelap dan pilihan bahasa ID/EN"
git push
```

### Pratinjau lokal sebelum push

Cukup klik dua kali `index.html` — tidak perlu server. Jika ingin meniru
kondisi GitHub Pages:

```bash
python -m http.server 8000
# lalu buka http://localhost:8000
```

---

## Cara pakai dashboard

| Kontrol | Fungsi |
| --- | --- |
| **ID / EN** | Ganti bahasa. Tersedia di halaman sampul dan di bilah atas. |
| **Ikon bulan/matahari** | Ganti mode terang atau gelap. |
| **FILTER** | Buka atau tutup panel filter (kabupaten, kecamatan, kelompok responden, lembaga, kategori produk, metode wawancara, rentang tanggal). |
| **Atur ulang** | Hapus semua filter aktif. |
| **Ekspor CSV** | Unduh seluruh indikator terpublikasi sesuai filter aktif. Ikon unduh pada tiap kartu mengunduh satu grafik saja. |
| **Ikon rumah / kutip** | Buka sampul atau halaman penutup. |
| **Panah di sidebar** | Sembunyikan panel navigasi untuk memperluas area grafik. |

Pilihan bahasa, tema, serta status buka/tutup sidebar dan filter disimpan di
`localStorage` peramban, jadi tetap sama saat halaman dibuka kembali.

Seluruh angka adalah **agregat anonim**: tidak ada baris responden, nama, nomor
telepon, kode rumah tangga, nama desa, maupun teks bebas. Sel dengan jawaban
valid kurang dari 5 otomatis disuppress; indikator sensitif hanya tersedia pada
agregasi kabupaten atau lebih tinggi.

---

## Catatan pemeliharaan

- **Memperbarui data.** Data tersemat pada objek `window.__JMA_EMBEDDED__`
  (satu baris panjang, sekitar baris 990). Ganti isi kunci `./data/meta.json`,
  `./data/cube.json`, dan `./data/indicators.json` dengan keluaran terbaru dari
  pipeline, lalu simpan. Struktur objek jangan diubah.
- **Menyesuaikan tampilan.** Seluruh penghalusan visual berada dalam satu blok
  `REFINEMENT LAYER` di akhir `<style>`. Menghapus blok tersebut mengembalikan
  tampilan ke versi komponen aslinya tanpa merusak fungsi apa pun.
- **Warna dan bentuk.** Diatur lewat variabel CSS pada `:root` dan
  `[data-theme="dark"]` di awal `<style>`.
- **Menambah terjemahan.** Teks antarmuka ada di objek `I18N`, opsi jawaban di
  `OPT`, satuan di `UNIT`.
- **Keterbatasan indikator** (`limitations_id`) hanya tersedia dalam Bahasa
  Indonesia di `indicators.json`, sehingga tetap tampil berbahasa Indonesia pada
  mode English dan ditandai `lang="id"`. Untuk menerjemahkannya, tambahkan field
  `limitations_en` pada registry indikator, lalu sesuaikan pemanggilannya di
  fungsi `metaBlock()`.
- **Jangan pernah menulis string penutup tag** (`</style>`, `</script>`) di dalam
  komentar CSS atau JS pada berkas ini — parser HTML akan menutup blok lebih awal.

---

## Alternatif: hosting di SharePoint

Jika URL GitHub Pages diblokir oleh daftar izin embed tenant, unggah
`index.html` ke pustaka **Site Assets** pada situs SharePoint terkait, lalu
sematkan melalui tautan internal tersebut. Perilaku render bergantung pada
setelan `NoScriptSite` situs: jika *Strict*, berkas akan terunduh, bukan
ditampilkan.

---

© 2026 Wahana Visi Indonesia. Prepared by PEARL Lead.
