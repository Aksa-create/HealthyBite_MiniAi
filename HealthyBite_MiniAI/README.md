# HealthyBite AI: Mini AI Recommendation System

Aplikasi rekomendasi makanan sehat berbasis **Knowledge Representation** untuk project pembelajaran AI.

## Teknik Knowledge Representation
1. **Rule-Based System**: Aturan formal eksplisit untuk preferensi diet, alergi, dan penyesuaian tujuan nutrisi serta aktivitas.
2. **Semantic Network**: Relasi terstruktur antara pengguna, profil, makanan, nutrisi, alergen, dan rekomendasi.

> Pemberitahuan: Data nutrisi dan daftar menu merupakan data ilustratif untuk demonstrasi akademik. Ini bukan saran medis atau pengganti ahli gizi. Untuk alergi nyata, selalu verifikasi label bahan dan risiko kontaminasi silang.

## Menjalankan Secara Lokal (Windows)
1. Pasang Python 3.10 atau versi lebih baru dari https://www.python.org/downloads/.
2. Buka PowerShell di direktori `HealthyBite_MiniAI`.
3. Jalankan perintah berikut:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

Peramban web akan membuka antarmuka aplikasi lokal (biasanya pada `http://localhost:8501`).

## Penerapan ke Streamlit Community Cloud
1. Buat repository baru di GitHub, misalnya `healthybite-mini-ai`.
2. Unggah `app.py`, `requirements.txt`, `DESIGN.md`, dan `README.md` ke root repository.
3. Buka https://share.streamlit.io/ lalu masuk dengan akun GitHub.
4. Pilih **Create app**, repository, branch (`main`), dan main file path `app.py`.
5. Klik **Deploy** dan tunggu proses penyusunan selesai.

Aplikasi ini tidak membutuhkan API key eksternal.

## Struktur Direktori
```text
HealthyBite_MiniAI/
├── app.py
├── requirements.txt
├── DESIGN.md
├── README.md
├── AGENTS.md
├── .agents/
└── .streamlit/
    └── config.toml
```

## Karakteristik Desain (Anti-Slop Standard)
- **Basis Pengetahuan**: Menu makanan, kategori diet, tag, alergen, dan profil gizi terstruktur.
- **Mesin Inferensi**: Filter deterministik untuk preferensi diet dan alergen (aturan R1-R3), dilanjutkan pembobotan tujuan nutrisi dan aktivitas harian (aturan R4-R7).
- **Desain Antarmuka**: Responsif untuk ponsel, tablet, dan desktop, kontras warna memenuhi standar WCAG AA, bebas em dash, dan bebas elemen hiasan sintetis.
