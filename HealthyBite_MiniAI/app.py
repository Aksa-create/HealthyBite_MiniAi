import streamlit as st
from typing import List, Set, Tuple, Dict, Any
import time

st.set_page_config(
    page_title="HealthyBite AI",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Basis pengetahuan: data makanan ilustratif untuk sistem pakar edukasi.
FOODS: List[Dict[str, Any]] = [
    {
        "name": "Nasi merah, ayam panggang, dan sayur",
        "category": "Seimbang",
        "diet": "Omnivora",
        "vegetarian": False,
        "vegan": False,
        "allergens": {"ayam"},
        "tags": {"seimbang", "protein", "serat"},
        "calories": 430,
        "protein": 32,
        "fiber": 7,
        "sugar": 4,
        "fat": 12,
        "description": "Kombinasi karbohidrat kompleks, protein hewani rendah lemak, dan sayuran hijau.",
        "emoji": "🍱"
    },
    {
        "name": "Bowl quinoa, tahu, dan brokoli",
        "category": "Plant-based",
        "diet": "Vegetarian/Vegan",
        "vegetarian": True,
        "vegan": True,
        "allergens": {"kedelai"},
        "tags": {"vegetarian", "vegan", "protein", "serat", "seimbang"},
        "calories": 390,
        "protein": 21,
        "fiber": 10,
        "sugar": 5,
        "fat": 11,
        "description": "Sumber protein nabati lengkap dengan serat tinggi dan sayuran padat mikronutrien.",
        "emoji": "🥦"
    },
    {
        "name": "Salad telur rebus dan alpukat",
        "category": "Seimbang",
        "diet": "Vegetarian",
        "vegetarian": True,
        "vegan": False,
        "allergens": {"telur"},
        "tags": {"vegetarian", "protein", "serat", "seimbang"},
        "calories": 350,
        "protein": 16,
        "fiber": 9,
        "sugar": 3,
        "fat": 22,
        "description": "Menu vegetarian dengan lemak tak jenuh tunggal alpukat dan protein telur.",
        "emoji": "🥑"
    },
    {
        "name": "Sup ikan kakap, wortel, dan kentang",
        "category": "Seimbang",
        "diet": "Omnivora/Pescatarian",
        "vegetarian": False,
        "vegan": False,
        "allergens": {"ikan"},
        "tags": {"protein", "seimbang"},
        "calories": 320,
        "protein": 28,
        "fiber": 5,
        "sugar": 6,
        "fat": 8,
        "description": "Hidangan berkuah hangat dengan asam lemak esensial dan protein hewani ringan.",
        "emoji": "🍲"
    },
    {
        "name": "Oatmeal pisang dan biji chia",
        "category": "Sarapan",
        "diet": "Vegetarian/Vegan",
        "vegetarian": True,
        "vegan": True,
        "allergens": {"oat"},
        "tags": {"vegetarian", "vegan", "serat", "sarapan"},
        "calories": 310,
        "protein": 9,
        "fiber": 11,
        "sugar": 12,
        "fat": 8,
        "description": "Menu sarapan tinggi beta-glukan untuk pencernaan sehat dan energi bertahap.",
        "emoji": "🥣"
    },
    {
        "name": "Gado-gado siram saus kacang",
        "category": "Nusantara",
        "diet": "Vegetarian",
        "vegetarian": True,
        "vegan": True,
        "allergens": {"kacang", "kedelai"},
        "tags": {"vegetarian", "vegan", "serat", "seimbang"},
        "calories": 410,
        "protein": 15,
        "fiber": 8,
        "sugar": 7,
        "fat": 19,
        "description": "Sayuran rebus khas Nusantara dipadu saus kacang gurih dan tempe-tahu.",
        "emoji": "🥗"
    },
    {
        "name": "Tumis tempe gurih dan buncis",
        "category": "Nusantara",
        "diet": "Vegetarian/Vegan",
        "vegetarian": True,
        "vegan": True,
        "allergens": {"kedelai"},
        "tags": {"vegetarian", "vegan", "protein", "serat", "seimbang"},
        "calories": 360,
        "protein": 22,
        "fiber": 9,
        "sugar": 5,
        "fat": 14,
        "description": "Fermentasi kedelai kaya prebiotik dan isoflavon dengan kerenyahan buncis.",
        "emoji": "🫛"
    },
    {
        "name": "Greek yogurt, beri, dan granola",
        "category": "Sarapan",
        "diet": "Vegetarian",
        "vegetarian": True,
        "vegan": False,
        "allergens": {"susu", "gandum"},
        "tags": {"vegetarian", "protein", "sarapan"},
        "calories": 330,
        "protein": 19,
        "fiber": 5,
        "sugar": 14,
        "fat": 9,
        "description": "Sarapan praktis tinggi kalsium dan kultur probiotik aktif.",
        "emoji": "🫐"
    },
    {
        "name": "Ubi panggang dan edamame",
        "category": "Plant-based",
        "diet": "Vegetarian/Vegan",
        "vegetarian": True,
        "vegan": True,
        "allergens": {"kedelai"},
        "tags": {"vegetarian", "vegan", "serat", "protein"},
        "calories": 340,
        "protein": 17,
        "fiber": 10,
        "sugar": 8,
        "fat": 7,
        "description": "Karbohidrat berindeks glikemik terkontrol dengan protein edamame segar.",
        "emoji": "🍠"
    },
    {
        "name": "Buah potong segar dan yoghurt tawar",
        "category": "Camilan",
        "diet": "Vegetarian",
        "vegetarian": True,
        "vegan": False,
        "allergens": {"susu"},
        "tags": {"vegetarian", "camilan", "serat"},
        "calories": 190,
        "protein": 8,
        "fiber": 4,
        "sugar": 18,
        "fat": 4,
        "description": "Camilan rendah lemak dengan mikronutrien vitamin C dan hidrasi alami.",
        "emoji": "🍓"
    },
]

ALLERGENS = ["Kacang", "Susu", "Telur", "Ikan", "Kedelai", "Gandum", "Oat", "Ayam"]
ALLERGEN_MAP = {
    "Kacang": "kacang",
    "Susu": "susu",
    "Telur": "telur",
    "Ikan": "ikan",
    "Kedelai": "kedelai",
    "Gandum": "gandum",
    "Oat": "oat",
    "Ayam": "ayam"
}

RULES: List[Tuple[str, str, str]] = [
    ("R1", "Jika pengguna memilih vegetarian, hanya rekomendasikan menu vegetarian.", "diet_preference == 'Vegetarian' -> food.vegetarian == True"),
    ("R2", "Jika pengguna memilih vegan, hanya rekomendasikan menu vegan.", "diet_preference == 'Vegan' -> food.vegan == True"),
    ("R3", "Jika pengguna menandai alergi, singkirkan semua menu yang mengandung alergen tersebut.", "allergen_set ∩ food.allergens == ∅"),
    ("R4", "Jika target nutrisi adalah tinggi protein, prioritaskan menu dengan protein ≥ 18 g per porsi.", "goal == 'Tinggi protein' -> score += protein * 2"),
    ("R5", "Jika target nutrisi adalah tinggi serat, prioritaskan menu dengan serat ≥ 8 g per porsi.", "goal == 'Tinggi serat' -> score += fiber * 3"),
    ("R6", "Jika target nutrisi adalah rendah kalori, prioritaskan menu ≤ 350 kkal per porsi.", "goal == 'Rendah kalori' -> score += max(0, 450 - calories)"),
    ("R7", "Jika aktivitas harian tinggi, tambahkan bobot menu padat protein (≥ 20 g) dan energi (≥ 350 kkal) untuk pemulihan.", "activity == 'Tinggi' -> score_boost(protein ≥ 20g, cal ≥ 350)"),
]

def recommend(
    preference: str,
    goal: str,
    activity: str,
    excluded_allergens: Set[str],
    limit: int
) -> Tuple[List[Dict[str, Any]], List[Tuple[Dict[str, Any], List[str]]]]:
    safe = []
    rejected = []
    
    for food in FOODS:
        reasons = []
        if preference == "Vegetarian" and not food["vegetarian"]:
            reasons.append("bukan menu vegetarian (melanggar aturan R1)")
        elif preference == "Vegan" and not food["vegan"]:
            reasons.append("tidak memenuhi syarat vegan (melanggar aturan R2)")
            
        matched = excluded_allergens.intersection(food["allergens"])
        if matched:
            reasons.append("mengandung alergen: " + ", ".join(sorted(matched)) + " (melanggar aturan R3)")
            
        if reasons:
            rejected.append((food, reasons))
            continue
            
        score = 0.0
        why = ["lolos aturan preferensi pola makan dan penyaringan alergen"]
        
        # Evaluasi tujuan nutrisi pengguna
        if goal == "Tinggi protein":
            score += food["protein"] * 2.0
            if food["protein"] >= 18:
                why.append(f"protein porsi contoh {food['protein']} g (memenuhi target R4 ≥ 18 g)")
        elif goal == "Tinggi serat":
            score += food["fiber"] * 3.0
            if food["fiber"] >= 8:
                why.append(f"serat porsi contoh {food['fiber']} g (memenuhi target R5 ≥ 8 g)")
        elif goal == "Rendah kalori":
            score += max(0.0, float(450 - food["calories"]))
            if food["calories"] <= 350:
                why.append(f"kalori porsi contoh {food['calories']} kkal (memenuhi target R6 ≤ 350 kkal)")
        else:
            score += food["fiber"] + (food["protein"] * 0.6) - (food["sugar"] * 0.15)
            why.append("komposisi seimbang berdasarkan rasio protein, serat, dan gula")
            
        # Evaluasi tingkat aktivitas harian (Aturan R7)
        if activity == "Tinggi":
            if food["protein"] >= 20:
                score += 8.0
                why.append(f"protein tinggi ({food['protein']} g) mendukung perbaikan jaringan saat aktivitas intens (R7)")
            if food["calories"] >= 350 and goal != "Rendah kalori":
                score += 5.0
                why.append(f"asupan kalori ({food['calories']} kkal) mencukupi kebutuhan pengeluaran energi harian (R7)")
        elif activity == "Rendah":
            if goal == "Seimbang" and food["calories"] <= 360:
                score += 4.0
                why.append(f"densitas kalori moderat ({food['calories']} kkal) cocok untuk aktivitas sedentari")
                
        safe.append({**food, "score": round(score, 1), "why": why})
        
    safe.sort(key=lambda x: x["score"], reverse=True)
    return safe[:limit], rejected

# Desain antarmuka responsif dan aksesibel sesuai panduan DESIGN.md
st.markdown("""
<style>
:root {
  --forest-green: #124838;
  --forest-mid: #166550;
  --amber-accent: #b45309;
}
.block-container {
  padding-top: 1.5rem;
  padding-bottom: 2.5rem;
  max-width: 1200px;
}
.hero-banner {
  padding: 1.8rem 2rem;
  border-radius: 16px;
  background: linear-gradient(135deg, #0f4637 0%, #166550 100%);
  color: #ffffff;
  margin-bottom: 1.25rem;
  border: 1px solid rgba(255, 255, 255, 0.15);
}
.hero-banner h1 {
  color: #ffffff;
  margin: 0;
  font-size: 2.2rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}
.hero-banner p {
  color: #e3f5ec;
  font-size: 1.02rem;
  margin: 0.4rem 0 0 0;
  line-height: 1.5;
}
.food-card {
  border: 1px solid rgba(128, 128, 128, 0.22);
  border-radius: 14px;
  padding: 1.1rem 1.2rem;
  margin-bottom: 0.85rem;
  background: rgba(128, 128, 128, 0.03);
  transition: border-color 0.2s ease;
}
.food-card:hover {
  border-color: rgba(22, 101, 80, 0.5);
}
.food-title {
  font-size: 1.15rem;
  font-weight: 600;
  margin: 0.3rem 0 0.35rem 0;
}
.food-desc {
  opacity: 0.85;
  font-size: 0.92rem;
  line-height: 1.45;
  margin: 0 0 0.75rem 0;
}
.tag-pill {
  display: inline-block;
  padding: 0.18rem 0.5rem;
  border-radius: 6px;
  font-size: 0.78rem;
  font-weight: 500;
  background: rgba(18, 72, 56, 0.1);
  color: #124838;
  margin-right: 0.3rem;
  margin-bottom: 0.3rem;
}
.allergen-pill {
  display: inline-block;
  padding: 0.18rem 0.5rem;
  border-radius: 6px;
  font-size: 0.78rem;
  font-weight: 600;
  background: rgba(180, 83, 9, 0.12);
  color: #b45309;
  border: 1px solid rgba(180, 83, 9, 0.25);
  margin-right: 0.3rem;
  margin-bottom: 0.3rem;
}
.empty-box {
  padding: 1.8rem;
  border-radius: 12px;
  border: 1px dashed rgba(180, 83, 9, 0.45);
  background: rgba(180, 83, 9, 0.04);
  margin-bottom: 1rem;
}
@media (max-width: 640px) {
  .hero-banner {
    padding: 1.25rem 1.25rem;
  }
  .hero-banner h1 {
    font-size: 1.65rem;
  }
  .block-container {
    padding-top: 1rem;
  }
}
</style>
""", unsafe_allow_html=True)

# Inisialisasi state untuk interaksi stabil
if "allergies_selected" not in st.session_state:
    st.session_state.allergies_selected = []

def reset_allergies():
    st.session_state.allergies_selected = []

with st.sidebar:
    st.markdown("## HealthyBite AI")
    st.caption("Prototipe Sistem Pakar Nutrisi: Knowledge Representation")
    st.divider()
    
    st.markdown("### Profil Pengguna")
    preference = st.selectbox(
        "Pola makan",
        ["Semua / fleksibel", "Vegetarian", "Vegan"],
        help="Sistem akan menyaring menu yang sesuai dengan kategori diet pilihan."
    )
    goal = st.selectbox(
        "Tujuan nutrisi",
        ["Seimbang", "Tinggi protein", "Tinggi serat", "Rendah kalori"],
        help="Inference engine menghitung skor prioritas berdasarkan tujuan ini."
    )
    activity = st.select_slider(
        "Tingkat aktivitas fisik",
        options=["Rendah", "Sedang", "Tinggi"],
        value="Sedang",
        help="Mempengaruhi penyesuaian kalori dan kebutuhan protein harian (Aturan R7)."
    )
    
    allergies_label = st.multiselect(
        "Pantangan alergi / bahan dihindari",
        options=ALLERGENS,
        key="allergies_selected",
        help="Menu yang memiliki catatan bahan ini akan langsung dieliminasi."
    )
    
    result_count = st.slider(
        "Jumlah rekomendasi ditampilkan",
        min_value=1,
        max_value=6,
        value=4
    )
    
    st.caption("Data nutrisi adalah angka terstruktur untuk simulasi logika pakar, bukan resep atau diagnosis medis.")
    run_button = st.button("Buat rekomendasi", type="primary", use_container_width=True)

st.markdown("""
<div class="hero-banner">
  <h1>HealthyBite AI</h1>
  <p>Rekomendasi makanan sehat berbasis aturan inferensi transparan dan Semantic Network.</p>
</div>
""", unsafe_allow_html=True)

metric_c1, metric_c2, metric_c3 = st.columns(3)
with metric_c1:
    st.metric("Basis Pengetahuan", f"{len(FOODS)} menu terdaftar", "Data terstruktur")
with metric_c2:
    st.metric("Mesin Inferensi", f"{len(RULES)} aturan formal", "Aturan IF-THEN")
with metric_c3:
    st.metric("Teknik KR", "2 pendekatan", "Rules + Semantic Network")

tab_rekomendasi, tab_aturan, tab_network, tab_tentang = st.tabs([
    "Rekomendasi Menu",
    "Aturan Inferensi (Rule-Based)",
    "Semantic Network",
    "Tentang Project"
])

with tab_rekomendasi:
    st.subheader("Rekomendasi Menu Terpilih")
    excluded_set = {ALLERGEN_MAP[x] for x in allergies_label}
    
    results, rejected = recommend(preference, goal, activity, excluded_set, result_count)
    
    if not results:
        # State Kosong Terstruktur (Empty State) dengan panduan tindakan
        st.markdown(f"""
        <div class="empty-box">
          <h4 style="margin-top:0; color:#b45309;">Tidak ada menu yang memenuhi seluruh kriteria</h4>
          <p style="margin-bottom:0.5rem;">Kombinasi preferensi pola makan <strong>{preference}</strong> dan 
          pantangan alergi [<strong>{', '.join(allergies_label) if allergies_label else 'tidak ada'}</strong>] 
          mengeliminasi seluruh {len(FOODS)} menu yang ada pada basis pengetahuan contoh.</p>
        </div>
        """, unsafe_allow_html=True)
        
        c_act1, c_act2 = st.columns([1, 2])
        with c_act1:
            if allergies_label and st.button("Hapus filter alergi", on_click=reset_allergies, use_container_width=True):
                st.rerun()
        with c_act2:
            st.info("Saran: Coba ubah preferensi diet ke 'Semua / fleksibel' atau kurangi jumlah alergen pada sidebar.")
    else:
        st.caption(f"Profil aktif: Pola makan **{preference}** | Tujuan **{goal}** | Aktivitas **{activity}** | Menu disaring **{len(rejected)}**")
        
        cols = st.columns(2)
        for idx, food in enumerate(results):
            with cols[idx % 2]:
                allergens_text = ", ".join(sorted(food["allergens"])) if food["allergens"] else "Bebas alergen utama pada data contoh"
                
                tags_html = "".join([f'<span class="tag-pill">{t}</span>' for t in sorted(food["tags"])])
                allergen_badge = f'<span class="allergen-pill">Alergen: {allergens_text}</span>' if food["allergens"] else '<span class="tag-pill">Alergen: Tidak ada</span>'
                
                st.markdown(f"""
                <div class="food-card">
                  <div style="font-size:1.8rem; line-height:1;">{food["emoji"]}</div>
                  <div class="food-title">{food["name"]}</div>
                  <div class="food-desc">{food["description"]}</div>
                  <div style="margin-bottom:0.5rem;">{allergen_badge} {tags_html}</div>
                </div>
                """, unsafe_allow_html=True)
                
                m1, m2, m3 = st.columns(3)
                m1.metric("Kalori", f"{food['calories']} kkal")
                m2.metric("Protein", f"{food['protein']} g")
                m3.metric("Serat", f"{food['fiber']} g")
                
                with st.expander("Alasan sistem merekomendasikan menu ini"):
                    st.write(f"**Skor kecocokan:** {food['score']} poin")
                    for reason in food["why"]:
                        st.write(f"- {reason}")
                    st.caption("Perhitungan diverifikasi oleh mesin inferensi aturan.")
                    
    with st.expander(f"Daftar {len(rejected)} menu yang dieliminasi oleh filter aturan"):
        if not rejected:
            st.write("Semua menu pada basis pengetahuan lolos verifikasi preferensi dan alergi.")
        else:
            for food_item, reject_reasons in rejected:
                st.write(f"**{food_item['name']}** (Kategori: {food_item['category']}):")
                for r in reject_reasons:
                    st.write(f"  * {r}")
                    
    st.info("Pemberitahuan keamanan: Data komposisi nutrisi dan alergen pada aplikasi ini dirancang untuk demonstrasi sistem pakar akademik. Selalu periksa label fisik makanan dan konsultasikan dengan tenaga gizi bersertifikat untuk kondisi medis spesifik.")

with tab_aturan:
    st.subheader("Mesin Inferensi: Aturan Pengetahuan (Rule Base)")
    st.write("Sistem menggunakan penalaran berbasis aturan eksplisit (rule-based reasoning). Setiap keputusan rekomendasi dapat dilacak kembali ke kondisi IF-THEN berikut tanpa kotak hitam (black-box).")
    
    for rid, deskripsi, formal_cond in RULES:
        with st.container(border=True):
            st.markdown(f"**{rid}: {deskripsi}**")
            st.code(formal_cond, language="python")
            
    st.markdown("#### Alur Eksekusi Inferensi (Forward Chaining)")
    st.code(
        "1. Input profil: Preferensi diet, Tujuan nutrisi, Aktivitas fisik, Daftar alergi\n"
        "2. Tahap Eliminasi (Hard Constraints):\n"
        "   - Filter diet (R1: Vegetarian, R2: Vegan)\n"
        "   - Filter alergi (R3: allergen ∩ ingredients == ∅)\n"
        "3. Tahap Pembobotan (Soft Constraints & Scoring):\n"
        "   - Pembobotan tujuan nutrisi (R4: Protein, R5: Serat, R6: Kalori, atau formula seimbang)\n"
        "   - Penyesuaian aktivitas fisik (R7: Bonus energi dan protein untuk aktivitas tinggi)\n"
        "4. Tahap Pemeringkatan:\n"
        "   - Urutkan menu lolos filter berdasarkan total skor tertinggi\n"
        "   - Sajikan N rekomendasi teratas beserta penjelasan keputusannya",
        language="text"
    )

with tab_network:
    st.subheader("Semantic Network: Representasi Relasi Konsep")
    st.write("Semantic Network memodelkan pengetahuan nutrisi sebagai graf berarah dengan simpul (node) mewakili konsep dan sisi (edge) mewakili relasi semantik.")
    
    st.graphviz_chart('''digraph G {
      graph [rankdir=LR, bgcolor="transparent", pad="0.2"];
      node [shape=box, style="rounded,filled", color="#124838", fillcolor="#f0fdf4", fontcolor="#111827", fontname="Arial"];
      edge [color="#166550", fontcolor="#111827", fontname="Arial", fontsize=10];
      
      User [label="Pengguna"];
      Profile [label="Profil Input"];
      DietPref [label="Preferensi Diet"];
      Goal [label="Tujuan Nutrisi"];
      Activity [label="Aktivitas Fisik"];
      AllergyAvoid [label="Alergen Dihindari"];
      
      Food [label="Menu Makanan"];
      Nutrient [label="Kandungan Gizi"];
      Allergen [label="Kandungan Alergen"];
      DietCategory [label="Kategori Diet Makanan"];
      
      InferenceEngine [label="Mesin Inferensi (Rules)"];
      Result [label="Rekomendasi Terpilih"];
      
      User -> Profile [label="memiliki"];
      Profile -> DietPref [label="menentukan"];
      Profile -> Goal [label="memilih"];
      Profile -> Activity [label="tingkat"];
      Profile -> AllergyAvoid [label="menandai"];
      
      Food -> Nutrient [label="mengandung"];
      Food -> Allergen [label="tercatat memiliki"];
      Food -> DietCategory [label="tergolong"];
      
      DietPref -> InferenceEngine [label="kondisi filter R1-R2"];
      AllergyAvoid -> InferenceEngine [label="kondisi filter R3"];
      Goal -> InferenceEngine [label="kondisi bobot R4-R6"];
      Activity -> InferenceEngine [label="kondisi bobot R7"];
      
      Food -> InferenceEngine [label="dievaluasi oleh"];
      InferenceEngine -> Result [label="menghasilkan peringkat"];
    }''')
    
    st.markdown("**Contoh Triple Pengetahuan (Subject, Predicate, Object):**")
    st.code(
        "(Bowl_quinoa, tergolong, Vegetarian)\n"
        "(Bowl_quinoa, tergolong, Vegan)\n"
        "(Bowl_quinoa, mengandung, Serat_10g)\n"
        "(Bowl_quinoa, mengandung_alergen, Kedelai)\n"
        "(Gado_gado, mengandung_alergen, Kacang)\n"
        "(Pengguna, memiliki_pantangan, Kacang)\n"
        "(Aturan_R3, mengeliminasi, Gado_gado)\n"
        "(Pengguna_Aktif, membutuhkan_tambahan, Protein_Energi)",
        language="text"
    )

with tab_tentang:
    st.subheader("Tentang Project")
    st.markdown("**HealthyBite AI: Sistem Rekomendasi Makanan Sehat Berbasis Knowledge Representation**")
    st.write("Aplikasi ini dibangun untuk mendemonstrasikan implementasi nyata konsep representasi pengetahuan dalam bidang kecerdasan buatan.")
    
    st.markdown("#### Dua Metode Knowledge Representation")
    st.write("1. **Rule-Based System (Sistem Berbasis Aturan):** Menggunakan kumpulan proposisi logika IF-THEN untuk menyaring menu secara pasti serta menghitung skor relevansi tanpa asumsi acak.")
    st.write("2. **Semantic Network (Jaringan Semantik):** Menggambarkan ontologi hubungan antarentitas (pengguna, makanan, alergen, nutrisi, dan aturan) dalam bentuk graf berarah.")
    
    st.markdown("#### Batasan Sistem & Transparansi")
    st.write("- Data nutrisi adalah dataset ilustratif terstruktur untuk keperluan edukasi teknologi.")
    st.write("- Tidak menggantikan evaluasi medis klinis atau diagnosis alergen laboratorium.")
    st.write("- Logika bersifat deterministik dan transparan, tanpa penggunaan model generatif yang rentan halusinasi.")

st.divider()
st.caption("HealthyBite AI | Prototipe Tugas Kecerdasan Tiruan: Knowledge Representation")
