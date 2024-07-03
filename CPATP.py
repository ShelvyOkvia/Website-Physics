import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def app():
    st.title(':green[FLUIDA STATIS KELAS 11 - FASE F]')
    st.header(':orange[Peta Konsep Materi]')
    st.image('gambar/garfik.png', use_column_width=True)
    
    st.markdown('###')
    st.write('---')

    st.header(':orange[Capaian Pembelajaran]')
    with st.expander('**Capaian Pembelajaran**'):

        st.markdown("""
            Pada akhir fase F, peserta didik mampu menerapkan konsep dan prinsip vektor ke dalam kinematika dan dinamika gerak partikel, usaha dan energi, fluida dinamis, getaran harmonis, gelombang bunyi dan gelombang cahaya dalam menyelesaikan masalah, serta menerapkan prinsip dan konsep energi kalor dan termodinamika dengan berbagai perubahannya dalam mesin kalor. Peserta didik mampu menerapkan konsep dan prinsip kelistrikan (baik statis maupun dinamis) dan kemagnetan dalam berbagai penyelesaian masalah dan berbagai produk teknologi, menerapkan konsep dan prinsip gejala gelombang elektromagnetik dalam menyelesaikan masalah. Peserta didik mampu menganalisis keterkaitan antara berbagai besaran fisis pada teori relativitas khusus, gejala kuantum dan menunjukkan penerapan konsep fisika inti dan radioaktivitas dalam kehidupan sehari-hari dan teknologi. Peserta didik mampu memberi penguatan pada aspek fisika sesuai dengan minat untuk ke perguruan tinggi yang berhubungan dengan bidang fisika. Melalui kerja ilmiah juga dibangun sikap ilmiah dan profil pelajar pancasila khususnya mandiri, inovatif, bernalar kritis, kreatif dan bergotong royong.
        
            [Lihat lebih lengkapnya](https://guru.kemdikbud.go.id/kurikulum/referensi-penerapan/capaian-pembelajaran/sd-sma/fisika/fase-f/)
                """)
        
        st.subheader('Capaian Pembelajaran')
        df = pd.DataFrame(
            {
                "Elemen": [("Pemahaman Fisika"), ("Keterampilan Proses")],
                "Capaian Pembelajaran": [
                    'Peserta didik mampu menerapkan konsep dan prinsip vektor, kinematika dan dinamika gerak, fluida, gejala gelombang bunyi dan gelombang cahaya dalam menyelesaikan masalah, serta menerapkan prinsip dan konsep kalor dan termodinamika, dengan berbagai perubahannya dalam mesin kalor', 
                    'Mengamati, mempertanyakan, dan memprediksi; merencanakan dan melakukan penyelidikan; memproses dan menganalisis data serta informasi; mencipta, mengevaluasi, dan melakukan refleksi, serta mengomunikasikan hasil penyelidikan.']
            }
        )
        st.markdown(df.style.hide(axis='index').to_html(), unsafe_allow_html=True)

    st.markdown('###')
    st.write('---')
    st.header(':orange[Tujuan Pembelajaran]')
    st.markdown('''
        1. Melalui kegiatan membaca dan menyimak video peserta didik mampu menerapkan konsep fluida statis dengan benar.
        2. Memahami pentingnya masalah fluida statis dalam lingkungan sekitar.
        3. Mengidentifikasi berbagai masalah fluida statis yang ada di lingkungan sekitar.
        4. Mengembangkan kemampuan untuk mencari solusi terhadap masalah fluida statis dengan problem based learning.
    ''')

    st.markdown('###')
    st.write('---')
    st.header(':orange[Alur Pembelajaran Problem Based Learning]')
    df1 = pd.DataFrame(
        {
            "Fase": [("Ke-1"), ("Ke-2"), ("Ke-3"), ("Ke-4"), ("Ke-5")],
            "Tahapan": [("Mengorientasikan Masalah"), ("Menorganisasikan Kegiatan Pembelajaran"), ("Membimbing Penyelidikan Mandiri/kelompok"), ("Mengembangkan dan Menyajikan Hasil Karya"), ("Menganalisis dan Mengevaluasi proses Pemecahan Masalah")],
            "Aktivitas": [
                'Memberikan tujuan pembelajaran dan video untuk siswa agar terlibat pada aktivitas pemecahan masalah.', 
                'Memberikan siswa materi fluida statis yang dapat membantu pemecahan masalah pada tahap selanjutnya.',
                'Memberikan studi kasus beserta panduan cara mengerjakannya yang dapat di akses siswa untuk mengerjakan pemecahan masalah dari studi kasus yang ada.',
                'Memberikan link canva agar siswa dapat mengembangkan dan menyajikan hasil karya mereka dari studi kasus sebelumnya.',
                'Menganalisis dan mengevaluasi proses pemecahan masalah dilakukan dengan presentasi di depan teman-teman yang berbeda studi kasus agar mengetahui apa yang harus diperbaiki dan ditambahkan.']
        }
    )
    st.markdown(df1.style.hide(axis='index').to_html(), unsafe_allow_html=True)



