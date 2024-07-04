import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from streamlit_chat import message

def app():
    tab_titles = [
        '📚Materi Fluida Statis',
        '👩‍🏫Pembelajaran PBL Fluida Statis',
        '📺Video Fluida Statis',
    ]

    tabs = st.tabs(tab_titles)

    with tabs[0]:
        # Intro
        #APAKAH FLUIDA ITU?
        st.title(':green[APAKAH FLUIDA ITU?]')
        st.write('Fluida adalah zat yang dapat mengalir dan mengubah bentuk sesuai wadahnya. Fluida meliputi gas dan cairan. Bedanya, cairan memiliki kohesi (gaya tarik antarmolekul) sehingga molekul-molekulnya berdekatan dan cenderung tetap bersama sedangkan gas tidak. Akibatnya, cairan mempertahankan volume yang sama saat mengalir. Misalnya, jika Anda menuangkan 500 mL air ke dalam panci, air tetap akan menempati volume 500 mL. Sebaliknya, untuk gas bayangkan Anda memiliki balon kecil yang sangat penuh dengan udara. Saat balon masih tertutup, udara di dalamnya terkompresi dalam ruang kecil. Ketika Anda melepaskan udara dari balon, udara akan keluar dan mengisi ruang yang lebih besar di sekitar Anda. Sama seperti itu, ketika Anda membuka katup pada tabung oksigen terkompresi, oksigen akan keluar dari ruang kecil (500 mL) dan mengembang untuk mengisi volume yang jauh lebih besar di sekitarnya.')
        st.write('Fluida memainkan peran penting dalam banyak aspek kehidupan sehari-hari. Kita meminumnya, menghirupnya, berenang di dalamnya. Fluida bersirkulasi di seluruh tubuh kita dan mengendalikan cuaca. Oleh karena itu, memahami fluida sangat penting bagi kita. Kita akan mulai belajar mengenai fluida statis, studi tentang fluida yang diam dalam situasi kesetimbangan. Seperti situasi kesetimbangan lainnya, ini didasarkan pada hukum pertama dan ketiga Newton. Kita akan mengeksplorasi konsep-konsep kunci dari massa jenis, tekanan, dan gaya apung. Meskipun begitu, kita hanya akan membahas permukaan dari topik yang luas dan menarik ini.')
        
        #1.1 MASSA JENIS
        st.title(':orange[1.1 MASSA JENIS]')
        st.write('Kadang-kadang dikatakan bahwa besi “lebih berat” daripada kayu. Hal ini tidak benar karena batang kayu yang besar jelas lebih "berat" daripada paku besi. Yang seharusnya kita katakan adalah bahwa besi lebih "padat" daripada kayu.')
        st.write('Massa jenis, $ρ$, dari suatu zat ($ρ$ adalah huruf kecil Yunani dibaca "rho") didefinisikan sebagai massa per satuan volume:')        
        st.latex(r'\rho = \frac{m}{V}.....................................(1-1)')
        st.write('Dengan Keterangan:')
        st.write(r'$$\rho = \text{Massa jenis benda} \,(kg/m^3)$$')
        st.write(r'$$m = \text{Massa benda} \,(kg)$$')
        st.write(r'$$V = \text{Volume benda} \,(cm^3)$$')
        st.write('Massa jenis suatu benda adalah massa benda (m) dibagi dengan volumenya (V). Massa jenis adalah sifat khas dari setiap zat murni. Benda-benda yang terbuat dari zat murni tertentu, seperti emas murni, bisa memiliki ukuran atau massa yang berbeda-beda, tetapi massa jenisnya akan akan selalu sama.')
        st.write('Kita dapat menggunakan massa jenis, Persamaan 1-1, untuk menulis massa suatu benda sebagai berikut:')
        st.latex(r'm = {\rho}{V}')
        st.write('dan berat suatu benda adalah sebagai berikut')
        st.latex(r'{m}{g} = {\rho}{V}{g}')
        st.write('Satuan SI untuk massa jenis adalah $kg/m^3$. Terkadang massa jenis diberikan dalam $g/cm^3$. Perhatikan bahwa massa jenis yang diberikan dalam $g/cm^3$ harus dikalikan dengan 1000 untuk memberikan hasil dalam kg/m^3. Contohnya, massa jenis aluminium adalah $ρ = 2.70 g/cm^3$, yang sama dengan $2700 kg/m^3$. Massa jenis berbagai zat diberikan dalam Tabel 1-1. Tabel tersebut menentukan suhu dan tekanan atmosfer karena keduanya mempengaruhi massa jenis (efeknya sedikit untuk cairan dan padatan). Perhatikan bahwa udara sekitar 1000 kali lebih tidak padat daripada air.')
        st.image('gambar/1.png', caption='Gambar 1. Massa Jenis Beberapa Zat Umum. (Giancoli, D. (2020))')
        st.write('Konsep massa jenis sangat membantu dalam mempelajari fluida karena kita tidak selalu berurusan dengan volume atau massa yang "tetap".')
        with st.expander("📚**Latihan Soal**", expanded=False):
            st.write('***SOAL 1***: Tentukan massa dan berat udara pada suhu $20°C$ di ruang tamu dengan lantai 4.0 m x 5.0 m dan langit-langit setinggi 3.0 m, serta massa dan berat air dengan volume yang sama.')
            st.write('***PEMBAHASAN***: Mari kita asumsikan bahwa kepadatan udara adalah sama (Udara kurang padat di ketinggian tinggi daripada di dekat laut. Tinggi, tetapi kerapatannya sangat bervariasi pada ketinggian ruangan 3.0 m.). Kita menggunakan Persamaan (1-1) untuk menghubungkan massa udara dengan volume ruangan $V$ (yang akan kita hitung) dan kerapatan udara (diberikan dalam Tabel 1).')
            st.write('Kita memiliki $V = (4.0m)(5.0m)(3.0m)$ = $60 m^3$. Jadi dari persamaan (1-1),')
            st.latex('m_{udara} = {ρ_{udara}}{V} =(1.20 kg/m^3)(60 m^3) = 72 kg ')
            st.latex('m_{udara} = {ρ_{udara}}{g} =(72 kg)(9.8m/s^2) = 700 N ')
            st.write('Massa dan berat volume air yang sama adalah')
            st.write('***EVALUASI***: Satu ruangan yang penuh dengan udara memiliki berat yang hampir sama dengan berat rata-rata orang dewasa. Air hampir seribu kali lebih padat daripada udara, sehingga massa dan beratnya lebih besar dengan faktor yang sama. Berat satu ruangan penuh air akan meruntuhkan lantai rumah biasa.')
            st.write('***KONSEP UTAMA***: Untuk menemukan massa jenis zat yang seragam, bagilah massa zat dengan volume yang ditempatinya.')
            st.write('---')
            st.write('***SOAL 2***: Urutkan benda-benda berikut ini secara berurutan dari kepadatan rata-rata tertinggi hingga terendah: (i) massa m = 4.00 kg, volume V = 1.60 x $10^{-3}$ $m^3$, (ii) m = 8.00 kg, V = 1.60 x $10^{-3}$ $m^3$, (iii) m = 8.00 kg, V = 3.20 x $10^{-3}$ $m^3$, (iv) m = 2560 kg, V = 0.640 x $m^3$, (v) m = 2560 kg, V = 1.28 $m^3$.')
            st.write('***PEMBAHASAN***: Dalam setiap kasus, kerapatan rata-rata sama dengan massa dibagi dengan volume,')
            st.write('(i) $ρ$ = ($4.00$ kg)/($1.60$ x $10^{-3}$ $m^3$) = $2.50$ X $10^3$ $kg/m^3$')
            st.write('(ii) $ρ$ = ($8.00$ kg)/($1.60$ x $10^{-3}$ $m^3$) = $5.00$ X $10^3$ $kg/m^3$')
            st.write('(iii) $ρ$ = ($8.00$ kg)/($3.20$ x $10^{-3}$ $m^3$) = $2.50$ X $10^3$ $kg/m^3$')
            st.write('(iv) $ρ$ = ($2560$ kg)/($0.640$ $m^3$) = $4.00$ X $10^3$ $kg/m^3$')
            st.write('(v) $ρ$ = ($2560$ kg)/($1.28$ $m^3$) = $2.00$ X $10^3$ $kg/m^3$')
            st.write(' Perhatikan bahwa dibandingkan dengan objek (i), objek (ii) memiliki massa dua kali lipat tetapi volumenya sama sehingga memiliki dua kali lipat massa jenis. Benda (iii) memiliki massa dua kali lipat dan volume dua kali lipat dari benda (i), jadi (i) dan (iii) memiliki massa jenis yang sama. Terakhir, benda (v) memiliki massa yang sama dengan benda (iv) tetapi dua kali lipat volumenya, sehingga (v) memiliki setengah massa jenis (iv). Jadi Jawaban yang tepat adalah (ii), (iv), (i), (iii), dan (v). ')
        st.markdown('###')
        st.write('---')

        #1.2 TEKANAN DALAM FLUIDA
        st.title(':orange[1.2 TEKANAN DALAM FLUIDA]')
        st.write('Tekanan dan gaya saling terkait, tetapi keduanya bukan hal yang sama. Tekanan didefinisikan sebagai gaya per satuan luas. Artinya, tekanan adalah besarnya gaya yang bekerja tegak lurus pada permukaan tertentu, dibagi dengan luas permukaan tersebut.')
        cola, colb, colc = st.columns(3)
        with colb:
            st.image('gambar/2.png', caption='Gambar 2. Gaya yang diberikan oleh fluida pada permukaan benda yang terendam. (Giancoli, D. (2020)')
        st.latex(r'P = \frac{F}{A}........................................(1-2)')
        st.write('Dengan Keterangan:')
        st.write(r'$$P = \text{Tekanan} \,(N/m^2)$$')
        st.write(r'$$F = \text{Gaya} \,(N)$$')
        st.write(r'$$A = \text{Luas Permukaan} \,(m^2)$$')
        st.write('Meskipun gaya adalah vektor, tekanan adalah skalar. Tekanan hanya memiliki besaran saja. Satuan SI untuk tekanan adalah N/m². Satuan ini disebut pascal (Pa), untuk menghormati Blaise Pascal. Jadi, 1 Pa = 1 N/m². Namun, untuk kesederhanaan, kita sering menggunakan N/m². Satuan lain yang kadang-kadang digunakan adalah dyne/cm² (dalam sistem cgs), dan dalam sistem Inggris lb/in² (pound per inci persegi, disingkat “psi”). Beberapa satuan tekanan lainnya dan konversi di antara mereka dibahas dalam bagian lain.')
        st.latex(r'1 \text{ Pascal} = 1 \text{ Pa} = 1 \text{ N}/m^2')
        st.write('Tekanan atmosfer $P_{atmosfer}$ adalah tekanan dari atmosfer bumi, yaitu tekanan di dasar lautan udara tempat kita tinggal. Tekanan ini bervariasi dengan perubahan cuaca dan ketinggian. Tekanan atmosfer normal di permukaan laut (nilai rata-rata) adalah 1 atmosfer (atm), yang didefinisikan tepat 101.325 Pa.')
        st.latex(r'P_{atmosfer} = 1 \text{ atm} = 1,013 \text{ x } 10^5 \text{ Pa}')
        st.latex(r'P_{atmosfer} = 1,013 \text{ bar} = 1013 \text{ milibar}')
        with st.expander("📚**Latihan Soal**", expanded=False):
            st.write('***SOAL 3***: Di ruang tamu dengan lantai berukuran 4,0 m * 5,0 m, berapakah total gaya ke bawah pada lantai akibat tekanan udara sebesar 1,00 atm?')
            st.write('***PEMBAHASAN***: Contoh ini menggunakan hubungan antara tekanan $ρ$ dari suatu fluida (udara), luas area $A$ yang dikenai tekanan tersebut, dan gaya normal $F$ yang dihasilkan oleh fluida tersebut. Tekanannya seragam, jadi kami menggunakan Persamaan (1-2), $F =ρA$, untuk menentukan $F$. Lantainya horizontal, sehingga $F$ adalah vertikal (ke bawah).')
            st.write('Kita memiliki $A$ = (4.0 m)(5.0 m) = 20 $m^2$, Jadi dari persamaan (1-2),')
            st.latex(r'P = \frac{F}{A}')
            st.latex(r'F = {P} \text{ x } {A} = 2.0 \text{ x } 10^6 \text{ N} ')
            st.write('***EVALUASI***: Dalam kasus ini, gaya $F$ tidak akan meruntuhkan lantai di sini, karena ada gaya ke atas yang sama besar pada bagian bawah lantai. Jika rumah memiliki ruang bawah tanah, gaya ke atas ini diberikan oleh udara di bawah lantai. Dalam hal ini, jika kita mengabaikan ketebalan lantai, gaya bersih akibat tekanan udara adalah nol (gaya tersebut seimbang).')
            st.write('***KONSEP UTAMA***: Untuk menemukan gaya yang diberikan oleh fluida yang tegak lurus terhadap permukaan, kalikan tekanan fluida dengan luas permukaan. Ini hubungan ini berasal dari definisi tekanan sebagai gaya normal per satuan luas di dalam fluida.')
            st.write('---')
            st.write('***SOAL 4***: Dua kaki orang dengan berat 60 kg menutupi area seluas seluas 500 $cm^2$. (a) Tentukan tekanan yang diberikan oleh kedua kaki di atas tanah. (b) Jika orang tersebut berdiri dengan satu kaki, berapakah tekanan di bawah kaki tersebut?')
            st.write('***PEMBAHASAN***: Asumsikan orang tersebut sedang beristirahat. Kemudian tanah mendorongnya dengan gaya yang sama dengan berat badannya sebesar ${m}{g}$, dan dia mengerahkan gaya sebesar mg pada tanah yang disentuh kakinya. Karena 1 $cm^2$ = $(10^{-2}$ $m)^2$ = $10^{-4} m^2$, maka 500 $cm^2$ = $0,050$ $m^2$')
            st.write('(a) Tekanan pada tanah yang diberikan oleh kedua kaki adalah')
            st.latex(r'P = \frac{F}{A} = \frac{{m}{g}}{A} = \frac{(60 \text{ kg})(9.8 \text{m}/s^2)}{0.050 m^2} = 12 \text{ x } 10^3 \text{N}/m^2')
            st.write('Jika orang tersebut berdiri dengan satu kaki, gaya masih sama dengan berat badan orang tersebut, tetapi luasnya akan menjadi setengahnya, sehingga tekanan ${F}/{A}$ akan menjadi dua kali lipat: $12$ x $10^3$ $N/m^2$')
        st.write('Tekanan sangat berguna untuk memahami fluida. Secara eksperimental, diketahui bahwa fluida memberikan tekanan ke segala arah. Ini dikenal baik oleh perenang dan penyelam yang merasakan tekanan air di seluruh tubuh mereka. Pada kedalaman tertentu dalam fluida yang diam, tekanannya sama di semua arah pada kedalaman tersebut. Untuk memahami alasannya, bayangkan ada kubus kecil dalam fluida yang sangat kecil sehingga kita bisa menganggapnya sebagai titik dan mengabaikan gaya gravitasi padanya. Tekanan pada satu sisi kubus harus sama dengan tekanan pada sisi yang berlawanan. Jika tidak, akan ada gaya yang menyebabkan kubus itu bergerak. Jika fluida tersebut tidak mengalir, maka tekanannya harus sama.')
        cold, cole, colf = st.columns(3)
        with cole:
            st.image('gambar/3.png', caption='Gambar 3. Jika ada komponen gaya sejajar dengan permukaan padat dari wadah.(Giancoli, D. (2020)')
        st.write('Untuk fluida yang diam, gaya akibat tekanan fluida selalu bekerja tegak lurus pada setiap permukaan padat yang disentuhnya. Jika ada komponen gaya sejajar dengan permukaan, seperti yang ditunjukkan pada (Gambar 3), maka menurut Hukum Ketiga Newton, permukaan padat akan memberikan gaya balik pada fluida, yang akan membuat fluida mengalir. Ini bertentangan dengan asumsi kita bahwa fluida diam. Oleh karena itu, gaya akibat tekanan dalam fluida yang diam selalu tegak lurus terhadap permukaan yang bersentuhan dengan fluida.')
        colg, colh, colj = st.columns(3)
        with colh:
            st.image('gambar/4.png', caption='Gambar 4. Tekanan pada kedalaman h dalam cairan. (Giancoli, D. (2020)')
        st.write('Sekarang kita menghitung bagaimana tekanan dalam suatu cairan dengan massa jenis seragam berubah dengan kedalaman. Mari kita lihat kedalaman $h$ di bawah permukaan cairan, seperti yang ditunjukkan dalam Gambar 4 (artinya, permukaan atas cairan berada pada ketinggian $h$ di atas level ini). Tekanan pada kedalaman $h$ ini disebabkan oleh berat kolom cairan di atasnya. Jadi, gaya yang disebabkan oleh berat cairan yang bekerja pada area $A$ adalah $F = {m}{g} = (ρV)g = {ρ}{A}{h}{g}$, di mana $ρ$ adalah massa jenis cairan (diasumsikan konstan), $g$ adalah percepatan gravitasi, $A$ adalah area yang sedang kita perhatikan, $h$ adalah kedalaman, ${A}{h}$ adalah volume cairan di atas area $A$. Tekanan $P$ yang disebabkan oleh berat cairan tersebut adalah:')
        st.latex(r'P = \frac{F}{A} = \frac{ρAhg}{A}')
        st.latex(r'P = {ρ}{g}{h} .........................................(1-3)')
        st.write('Dengan keterangan:')
        st.write('$P$ = Tekanan Hidrostatis (Pascal atau $N/m^2$)')
        st.write('$ρ$ = Massa Jenis fluida $(kg/m^3)$')
        st.write('$g$ = Percepatan gravitasi $(m/s^2)$')
        st.write('$h$ = Kedalaman (m)')
        st.write('Ini berarti tekanan dalam cairan bertambah seiring dengan bertambahnya kedalaman, berdasarkan massa jenis cairan dan percepatan gravitasi.')
        st.write('Perhatikan bahwa Luas Penampang $A$ tidak mempengaruhi tekanan pada kedalaman tertentu. Tekanan fluida berbanding lurus dengan massa jenis cairan dan kedalaman dalam cairan. Secara umum, *tekanan pada kedalaman yang sama dalam cairan yang seragam adalah sama*.')
        st.write('Persamaan (1-3) memberi tahu kita tekanan apa yang ada pada kedalaman $h$ di dalam cairan, disebabkan oleh cairan itu sendiri. Namun bagaimana jika ada tekanan tambahan yang diberikan di permukaan cairan, seperti tekanan atmosfer atau piston yang mendorong ke bawah? Dan bagaimana jika massa jenis fluida tidak konstan? Gas dapat sangat ditekan sehingga massa jenisnya dapat bervariasi dengan signifikan berdasarkan kedalaman. Cairan juga bisa terkompres, meskipun kita sering bisa mengabaikan variasi massa jenisnya. Salah satu pengecualian terjadi di dasar laut di mana berat air di atasnya secara signifikan menekan dan meningkatkan massa jenisnya. Untuk menangani ini, dan kasus lainnya, sekarang dalam memperlakukan kasus umum saat menentukan bagaimana tekanan dalam suatu fluida bervariasi dengan kedalaman.')
        colk, coll, colm = st.columns(3)
        with coll:
            st.image('gambar/5.png', caption='Gambar 5. Gaya di atas bidang datar. (Giancoli, D. (2020)')
        st.write('Dalam Gambar 5, kita mencari tekanan pada setiap ketinggian $y$ di atas suatu titik acuan (seperti dasar laut/dasar tangki/kolam renang). Di dalam fluida ini, pada ketinggian $y$, kita mempertimbangkan sebuah volume fluida yang datar dan kecil, berbentuk pelat dengan luas $A$ dan ketebalan $(dy)$ yang sangat kecil, seperti yang ditunjukkan. Biarkan tekanan yang bekerja ke atas pada permukaan bawahnya (pada ketinggian $y$) adalah $P$. Tekanan yang berkerja ke bawah pada permukaan atas pelat kecil kita (pada ketinggian $y + dy$) adalah $P + dP$. Tekanan fluida yang bertindak pada pelat kita menghasilkan gaya sebesar $PA$ ke atas dan gaya sebesar $(P + dP)A$ ke bawah pada pelat tersebut. Satu-satunya gaya lain yang bertindak secara vertikal pada pelat adalah gaya gravitasi yang sangat kecil $dF_G$, yang pada pelat kita dengan massa $dm$.')
        st.latex(r'dF_G= (dm)g = ρg \text{ }dV = ρgA \text{ } dy,')
        st.write('di mana $ρ$ adalah kerapatan fluida pada ketinggian $y$. Karena fluida dianggap dalam keadaan diam, pelat kita berada dalam kesetimbangan sehingga gaya bersih pada pelat tersebut harus nol. Oleh karena itu, kita memiliki')
        st.latex(r'PA - (P + dP)A - ρgA \text{ } dy = 0')
        st.write('yang bila disederhanakan menjadi')
        st.latex(r'\frac{dP}{dy}=-ρg......................................(1-4)')
        st.write('Hubungan ini memberi tahu kita bagaimana tekanan dalam fluida bervariasi dengan ketinggian di atas titik referensi apapun. Tanda minus menunjukkan bahwa tekanan akan berkurang dengan bertambahnya ketinggian; atau bahwa tekanan meningkat dengan kedalaman (ketinggian yang lebih rendah).')
        st.write('Jika tekanan pada ketinggian $y_1$ dalam fluida adalah $P_1$, dan pada ketinggian $y_2$ adalah $P_2$, maka kita dapat mengintegrasikan Persamaan (1-4) untuk mendapatkan hasilnya')
        st.latex(r'\int_{P1}^{P2} dP = - \int_{y1}^{y2} ρ g \, dy')
        st.write("yang dapat disederhanakan menjadi:")
        st.latex(r'P2 - P1 = - \int_{y1}^{y2} ρ g \, dy...................(1-5)')
        st.write('Di sini kita mengasumsikan $ρ$ adalah fungsi dari ketinggian $y$: $ρ = ρ(y)$. Ini adalah hubungan umum, dan sekarang kita menerapkannya pada dua kasus khusus: (1) tekanan dalam cairan dengan massa jenis yang seragam dan (2) variasi tekanan dalam atmosfer Bumi.')
        st.write('Untuk cairan di mana variasi massa jenisnya dapat diabaikan, $ρ$ adalah konstan dan Persamaan (1-5) dapat diintegrasikan dengan mudah:')
        st.latex(r'P_2 - P_1 = -ρ g (y_2 - y_1)...........................(1-6a)')
        coln, colo, colp = st.columns(3)
        with colo:
            st.image('gambar/6.png', caption='Gambar 6. Tekanan eksternal di bagian atas cairan permukaan. (Giancoli, D. (2020)')
        st.write('Untuk situasi sehari-hari di mana cairan berada dalam wadah terbuka, seperti air di dalam gelas, kolam renang, danau, atau laut, terdapat permukaan bebas di bagian atas yang terkena atmosfer. Biasanya, kita mengukur jarak dari permukaan atas ini. Misalnya, kita menetapkan kedalaman $h$ di dalam cairan di mana $h = y_2 - y_1$ seperti yang ditunjukkan pada Gambar 6. Jika kita anggap $y_2$ adalah posisi permukaan atas, maka $P_2$ mewakili tekanan atmosfer, $P_0$, di permukaan atas. Dari Persamaan (1-6a), tekanan $P (= P_1)$ pada kedalaman $h$ dalam fluida adalah')
        st.latex(r'P = P_0 + ρ g h............\text{[h adalah kedalaman cairan]}..(1-6b)')
        st.write('Perhatikan bahwa Persamaan (1-6b) hanyalah tekanan cairan Persamaan (1-3) ditambah tekanan $P_0$ akibat atmosfer di atasnya.')
        with st.expander("📚**Latihan Soal**", expanded=False):
            st.write('***SOAL 5***: Tekanan pada keran. Permukaan air di dalam tangki penyimpanan berada 30 m di atas keran air di dapur sebuah rumah, seperti yang ditunjukkan pada Gambar 1396. Hitung perbedaan tekanan air antara keran dan permukaan air di dalam tangki.')
            colq, colr, cols = st.columns(3)
            with colr:
                st.image('gambar/7.png', caption='Gambar 7. Tekanan Pada Keran. (Giancoli, D. (2020)')
            st.write('***PEMBAHASAN***: Pendekatan Air praktis tidak dapat dipadatkan, sehingga $ρ$ konstan bahkan untuk $h = 30$ m saat digunakan dalam Persamaan (1-6b). Hanya $h$ yang penting; kita dapat mengabaikan "rute" pipa dan tikungannya. Kita mengasumsikan tekanan atmosfer di permukaan air dalam tangki penyimpanan sama dengan di keran air. Jadi, perbedaan tekanan air antara keran air dan permukaan air di dalam tangki adalah')
            st.latex(r'∆_P = ρ g h = (1.0 \text{ x } 10^3 \text{ kg}/m^3)(9.8 \text{ m}/s^2)(30m) = 2.9 \text{ x } 10^5 \text{ N}/m^2')
            st.write('***CATATAN***: Ketinggian $h$ terkadang disebut kepala tekanan. Dalam Contoh ini, kepala air adalah 30 m di keran air. Diameter yang sangat berbeda dari tangki dan keran air tidak memengaruhi hasil (hanya tinggi yang penting).')
            st.write('***SOAL 6***: Gaya pada jendela akuarium. Hitung gaya akibat tekanan air yang diberikan pada jendela pandangan akuarium berukuran 1.0 m * 3.0 m yang ujung atasnya berada 1.0 m di bawah permukaan air, seperti pada Gambar 8.')
            colt, colu, colv = st.columns(3)
            with colu:
                st.image('gambar/8.png', caption='Gambar 8. Gaya Pada Jendela Akuarium. (Giancoli, D. (2020)')
            st.write('***PEMBAHASAN***: Pada kedalaman $h$, tekanan yang disebabkan oleh air diberikan oleh Persamaan (1-6b). Bagi jendela menjadi strip horizontal tipis dengan panjang $l = 3.0$ m dan ketebalan $dy$, seperti yang ditunjukkan dalam Gambar 8. Kita memilih sistem koordinat dengan $y = 0$ di permukaan air dan $y$ positif ke bawah. (Dengan pilihan ini, tanda minus dalam Persamaan (1-6a) menjadi plus, atau kita menggunakan Persamaan (1-6b) dengan $y = h$.) Gaya akibat tekanan air pada setiap strip adalah $dF = PdA = ρgyl$ dy.')
            st.write('Total kekuatan pada jendela diberikan oleh integral:')
            st.latex(r'\int_{y_1 = 1.0m}^{y_2 = 2.0m} ρgyl \text{ dy} = \frac{1}{2}ρgl(y^{\frac{2}{2}}-y^{\frac{2}{1}})')
            st.latex(r'\int_{y_1 = 1.0m}^{y_2 = 2.0m} ρgyl \text{ dy} = {\frac{1}{2}}(1000 kg/m^3)(9.8 m/s^2)(3.0 m)[(2.0m)^2-(1.0m)^2]')
            st.latex(r'\int_{y_1 = 1.0m}^{y_2 = 2.0m} ρgyl \text{ dy} = 44,000 N')
            st.write('***CATATAN***: Untuk memeriksa jawaban kita, kita bisa melakukan estimasi: mengalikan luas jendela (3.0 m²) dengan tekanan di tengah jendela (h = 1.5 m) menggunakan Persamaan (1-3), P = ρgh = (1000 kg/m³) (9.8 m/s²) (1.5 m) ≈ 1.5 x 10⁴ N/m².')
            st.write('Jadi, nilai F = PA ≈ (1.5 x 10⁴ N/m²) (3.0 m) (1.0 m) ≈ 4.5 x 10⁴ N. Bagus!')
        st.write('Sekarang mari kita terapkan Persamaan (1-4) atau (1-5) pada gas. Densitas gas biasanya sangat kecil, sehingga perbedaan tekanan pada ketinggian yang berbeda biasanya dapat diabaikan jika $y_2 - y_1$ tidak besar (kita menggunakan ini pada Contoh Soal 5. Tekanan pada keran). Memang, untuk sebagian besar wadah gas biasa, kita dapat mengasumsikan bahwa tekanan adalah sama di seluruh wadah. Namun, jika $y_2 - y_1$ sangat besar, kita tidak bisa membuat asumsi ini. Contoh menarik adalah atmosfer Bumi, yang tekanannya di permukaan laut sekitar 1.013 x 10⁵ N/m² dan berkurang secara bertahap dengan ketinggian.')   
        st.header(':blue[Efek Ketinggian Pada Tekanan Atmosfer]')
        st.write('Efek ketinggian pada tekanan atmosfer Kita dapat menentukan variasi tekanan di atmosfer Bumi sebagai fungsi dari ketinggian $y$ di atas permukaan laut, dengan mengasumsikan $g$ adalah konstan dan bahwa densitas udara sebanding dengan tekanan. (Asumsi terakhir ini tidak terlalu akurat, sebagian karena suhu dan efek cuaca lainnya penting.)')
        st.write('Kita mulai dengan Persamaan (1-4) dan mengintegrasikannya dari permukaan Bumi di mana $y = 0$ dan $P = P₀$, hingga ketinggian $y$ pada tekanan $P$. Kita mengasumsikan bahwa $ρ$ sebanding dengan $P$, sehingga kita dapat menulis:')
        st.latex(r'\frac{ρ}{ρ_0} = \frac{P}{P_0}')
        st.write('di mana $P₀ = 1.013 x 10⁵ N/m²$ adalah tekanan atmosfer di permukaan laut dan $ρ_0 = 1.29$ kg/m³ adalah densitas udara di permukaan laut pada suhu $0°C$ (Gambar 1). (Nilai-nilai ini adalah nilai "rata-rata" untuk $P₀$ dan $ρ₀$ karena sebenarnya mereka bervariasi dengan cuaca.) Dari perubahan diferensial dalam tekanan dengan ketinggian, Persamaan (1-4), kita memiliki:')
        st.latex(r'\frac{dP}{dy} = -ρ g = -P(\frac{ρ_0}{P_0})g,')
        st.write('kemudian')
        st.latex(r'\frac{dP}{P} = (\frac{ρ_0}{P_0})g \text{ } dy')
        st.write('Kita mengintegrasikan ini dari $y = 0$ (permukaan Bumi) di mana $P = P₀$, hingga ketinggian $y$ di mana tekanannya adalah $P$:')
        st.latex(r'\int_{P_0}^{P} \frac{dP}{P} = -\frac{ρ_0}{P_0}g \int_{0}^{y} dy')
        st.latex(r'\ln \frac{P}{P_0} = -\frac{ρ_0}{P_0} gy,')
        st.write('Karena  $\ln P-\ln P_0 = \ln (P/P_0)$: lihat Lampiran A97. Kemudian')
        st.latex(r'P = P_0 e^{-(ρ_0 g/P_0)y}...............................(1.6c)')
        st.write('Jadi, berdasarkan asumsi kita, kita menemukan bahwa tekanan udara di atmosfer kita berkurang secara eksponensial dengan ketinggian di atas permukaan Bumi.')
        st.write('Atmosfer tidak memiliki permukaan atas yang jelas, sehingga tidak ada titik alami dari mana untuk mengukur kedalaman di atmosfer, seperti yang bisa kita lakukan untuk cairan.')
        with st.expander("📚**Latihan Soal**", expanded=False):
            st.write('***SOAL 7***: Ketinggian di mana $P$ = $1/2$ atm. Pada ketinggian berapa di atas permukaan laut tekanan atmosfer sama dengan separuh tekanan di permukaan laut?')
            st.write('***PEMBAHASAN***: Kita menggunakan Persamaan (1-6c) dengan mengatur $P = \\frac{1}{2} $ atm dan menyelesaikan untuk y. Konstanta $$\\frac{ρ₀g}{P₀}$$ memiliki nilai,')
            st.latex(r'\frac{ρ_0g}{P_0} = \frac{(1.29 kg/m^3)(9.80 m/s^2)}{1.013 \text{ x } 10^5 N/m^2} = 1.25 \text{ x } 10^{-4} \text{ } m^{-1}')
            st.write('Kemudian kita mengatur $$P = \\frac{1}{2} P₀$$ pada Persamaan (1-6c) kita memperoleh,' )
            st.latex(r'\frac{1}{2} = e^{-({1.25 \text{ x } 10^{-4} m^{-1}})y}')
            st.write('Sekarang kita ambil logaritma natural dari kedua sisi:')
            st.latex(r'\ln \frac{1}{2} = (-1.25 \text{x} 10^{-4} \text{ }m^{-1})y')
            st.write('Sekarang kita mengambil logaritma alami dari kedua sisi:')
            st.latex(r'\\ln \frac{1}{2} = (-1.25 \text{ x } 10^{-4} m^{-1})y')
            st.write('Jadi (panggil kembali $\ln \\frac{1}{2}$) = $-ln 2$,')
            st.latex(r'y = (\ln 2.00)/(1.25 \text{ x } 10^{-4} m^{-1}) = 5550 \text{ m}')
            st.write('Pada ketinggian sekitar 5500m (sekitar 18.000 kaki), tekanan atmosfernya setengah dari tekanan di permukaan laut. Pendaki gunung sering menggunakan tabung oksigen di ketinggian yang sangat tinggi.')

        #1.3 TEKANAN ATMOSFER DAN TEKANAN GAUGE
        st.title(':orange[1.3 TEKANAN ATMOSFER DAN TEKANAN GAUGE]')

        # Tekanan Atmosfer
        st.header(':blue[Tekanan Atmosfer]')
        st.write('Tekanan udara di suatu tempat di Bumi bervariasi sedikit tergantung pada cuaca dan ketinggian Anda di atas permukaan laut. Di permukaan laut, tekanan atmosfer rata-rata adalah $1,013$ x $10^5$ $N/m^2$ atau $(14,7$ $lb/in^2)$. Nilai ini memungkinkan kita untuk mendefinisikan unit tekanan yang umum digunakan, yaitu **atmosfer** (disingkat $atm$):')
        st.latex(r' 1 \text{ atm} = 1.013 \text{ x } 10^5 \text{ } N/m^2 = 101.3 \text{ } kPa')
        st.write('Satu unit tekanan lain yang kadang-kadang digunakan (dalam meteorologi dan pada peta cuaca) adalah **bar**, yang didefinisikan sebagai:')
        st.latex(r'1 \text{ bar} = 1.000 \text{ x } 10^5 \text{ } N/m^2')
        st.write('Maka **tekanan atmosfer standar**, di permukaan laut, sedikit lebih dari 1 bar.')
        st.write('Tekanan yang disebabkan oleh berat atmosfer diberikan pada semua benda yang terendam di lautan udara ini, termasuk tubuh kita. Bagaimana tubuh manusia menahan tekanan besar di permukaannya? Jawabannya adalah sel-sel hidup mempertahankan tekanan internal yang hampir sama dengan tekanan eksternal, sama seperti tekanan di dalam balon hampir sama dengan tekanan luar atmosfer. Ban mobil, karena kekakuannya, dapat mempertahankan tekanan internal jauh lebih besar dari tekanan eksternal.')
        with st.expander("📚**Latihan Soal**", expanded=False):
            st.write('***SOAL 8***: **Jari menahan air di dalam sedotan**. Anda memasukkan sedotan dengan panjang $l$ ke dalam segelas air yang tinggi. Anda menempatkan jari Anda di atas sedotan, menangkap beberapa udara di atas air tetapi mencegah udara tambahan masuk atau keluar, kemudian Anda mengangkat sedotan dari air. Anda menemukan bahwa sedotan tetap mempertahankan sebagian besar air (Gambar 9a). Apakah udara di ruang antara jari Anda dan bagian atas air memiliki tekanan $P$ yang lebih besar dari, sama dengan, atau lebih kecil dari tekanan atmosfer $P_0$ di luar sedotan?')
            colw, colx, coly = st.columns(3)
            with colx:
                st.image('gambar/9.png', caption='Gambar 9. Ilustrasi Soal. (Giancoli, D. (2020)')
            st.write('***PEMBAHASAN***: Pertimbangkan gaya pada kolom air (Gambar 9b). Tekanan atmosfer di luar sedotan mendorong ke atas pada air di bagian bawah sedotan, gravitasi menarik air ke bawah, dan tekanan udara di dalam bagian atas sedotan mendorong ke bawah pada air. Karena air dalam keadaan keseimbangan, gaya ke atas karena tekanan atmosfer $P_0$ harus seimbang dengan dua gaya ke bawah. Satu-satunya cara ini mungkin terjadi adalah jika tekanan udara $P$ di dalam sedotan di bagian atas lebih kecil dari tekanan atmosfer di luar sedotan. (Ketika Anda awalnya mengeluarkan sedotan dari gelas air, sedikit air mungkin keluar dari bagian bawah sedotan, sehingga meningkatkan volume udara yang terperangkap dan mengurangi kepadatannya dan tekanannya.)')
        
        # Tekanan Gauge
        st.header(':blue[Tekanan Gauge]')
        st.write('Penting untuk dicatat bahwa alat ukur tekanan ban, dan sebagian besar alat ukur tekanan lainnya, mencatat tekanan di atas tekanan atmosfer. Ini disebut sebagai **tekanan gauge**. Oleh karena itu, untuk mendapatkan **tekanan mutlak**, $P$, kita harus menambahkan tekanan atmosfer, $P_0$, dengan tekanan gauge, $P_G$:')
        st.latex(r'P = P_G + P_0')
        st.write('Jika sebuah alat ukur tekanan ban mencatat 220 kPa, maka tekanan mutlak dalam ban adalah 220 kPa + 101 kPa = 321 kPa, setara dengan sekitar 3.2 atm (tekanan gauge 2.2 atm).')


        #1.4 HUKUM PASCAL
        st.title(':orange[1.4 HUKUM PASCAL]')
        st.write('Atmosfer Bumi memberikan tekanan pada semua benda yang berhubungan dengannya, termasuk fluida lain. Tekanan eksternal yang bekerja pada suatu fluida ditransmisikan ke seluruh fluida tersebut. Sebagai contoh, sesuai dengan Persamaan (1-3), tekanan yang disebabkan oleh air pada kedalaman 100 m di bawah permukaan sebuah danau adalah $P = \\rho g \Delta h$ = $(1000$ $kg/m^3)$ $(9.8 m/s^2)$ $(100$ $m)$ = $9.8$ x $10^5$ $N/m^2$, atau $9.7$ $atm$.')
        st.write('Namun, tekanan total 100 m di bawah permukaan sebuah danau adalah akibat dari tekanan air ditambah dengan tekanan udara di atasnya. Oleh karena itu, tekanan total (jika danau tersebut dekat dengan permukaan laut) adalah 9.7 atm + 1.0 atm = 10.7 atm. Ini hanya satu contoh dari prinsip umum yang dikaitkan dengan filsuf dan ilmuwan Prancis, Blaise Pascal (1623-1662). **Prinsip Pascal** menyatakan bahwa *jika tekanan eksternal diterapkan pada suatu fluida yang terkungkung, tekanan di setiap titik dalam fluida tersebut akan meningkat sebanyak itu.*')
        st.image('gambar/10.png', caption='Gambar 10. Aplikasi dari Prinsip Pascal: (a) pengangkatan hidrolik; (b) rem hidrolik pada mobil. (Giancoli, D. (2020)')
        st.write('Sejumlah perangkat praktis memanfaatkan prinsip Pascal. Salah satu contohnya adalah lift hidrolik, yang diilustrasikan dalam (Gambar 10a), di mana gaya input kecil digunakan untuk menghasilkan gaya output besar dengan membuat luas piston output lebih besar dari luas piston input. Untuk melihat bagaimana ini berfungsi, kita asumsikan piston input dan output berada pada ketinggian yang sama (setidaknya secara aproximasi). Kemudian gaya input eksternal $F_{in}$, menurut prinsip Pascal, meningkatkan tekanan secara merata di seluruh fluida. Oleh karena itu, pada level yang sama (lihat Gambar 10a),')
        st.latex(r'P_{out} = P_{in}')
        st.write('di mana kuantitas input direpresentasikan oleh subskrip "in" dan output oleh "out." Karena $P = \\frac{F}{A}$, kita menuliskan kesetaraan di atas sebagai')
        st.latex(r'\frac{F_{out}}{A_{out}} = \frac{F_{in}}{A_{in}},')
        st.write('atau')
        st.latex(r'\frac{F_{out}}{F_{in}} = \frac{A_{out}}{A_{in}},')
        st.write('Kuantitas $F_{out}/F_{in}$ disebut sebagai keuntungan mekanis dari lift hidrolik, dan itu sama dengan rasio dari luas-luasnya. Sebagai contoh, jika luas piston output adalah 20 kali luas silinder input, gaya tersebut diperbesar dengan faktor 20. Dengan demikian, sebuah gaya sebesar 200 pound dapat mengangkat mobil 4000 pound.')
        st.write('(Gambar 10b) mengilustrasikan sistem rem mobil. Ketika pengemudi menekan pedal rem, tekanan dalam silinder master meningkat. Peningkatan tekanan ini terjadi di seluruh cairan rem, sehingga mendorong kampas rem ke cakram yang terpasang pada roda mobil. Namun, kebocoran dapat menjadi bencana.')

        #1.5 PENGUKURAN TEKANAN, GAUGE, DAN BAROMETER
        st.title(':orange[1.5 PENGUKURAN TEKANAN, GAUGE, DAN BAROMETER]')
        st.write('Banyak perangkat telah diciptakan untuk mengukur tekanan, beberapa di antaranya ditunjukkan dalam (Gambar 11). Yang paling sederhana adalah manometer tabung terbuka (Gambar 11a) yang merupakan tabung berbentuk U yang diisi sebagian dengan cairan, biasanya merkuri atau air. tekanan P yang diukur terkait dengan perbedaan ketinggian ∆h dari dua tingkat cairan dengan hubungan')
        st.image('gambar/11.png', caption='Gambar 11. Tekanan gauge: (a) manometer tabung terbuka, (b) pengukur aneroid, dan (c) pengukur tekanan ban yang umum. (Giancoli, D. (2020)')
        st.latex(r'P = P_0 + \rho g ∆h..................[Manometer]')
        st.write('di mana $P_0$ adalah tekanan atmosfer (beraksi pada bagian atas cairan di tabung kiri), dan $\\rho$ adalah kerapatan cairan dalam tabung berbentuk U. Perhatikan bahwa kuantitas $\\rho g \Delta h$ adalah tekanan pengukur: jumlah dengan mana $P$ melebihi tekanan atmosfer $P_0$. Jika cairan di kolom sebelah kiri lebih rendah daripada di kolom sebelah kanan, $P$ kurang dari tekanan atmosfer (dan $\Delta h$ adalah negatif).')
        st.write('Alih-alih menghitung produk $\\rho g \Delta h$, terkadang hanya perubahan tinggi $\Delta h$ yang ditentukan. Sebenarnya, tekanan terkadang ditentukan sebagai sejumlah "milimeter merkuri" mm-Hg, jika $\\rho$ adalah untuk merkuri, atau "milimeter air" ($mm-H_2O$). Unit mm-Hg setara dengan tekanan 133 $N/m^2$, karena $\\rho g \Delta h$ untuk 1 mm (= $( 1.0$ x $10^{-3}$ m) merkuri memberikan')
        st.latex(r'\rho g \Delta h = (13.6 \text{ x } 10^3 \text{ } kg/m^3)(9.8 \text{ } m/s^2)(1.00 \text{ x } 10^{-3}m)')
        st.latex(r'\rho g \Delta h = 1.33 \text{ x } 10^2 \text{ } N/m^2.')
        st.write('Unit mm-Hg juga disebut **torr** untuk menghormati ilmuwan Italia Evangelista Torricelli (1608-1647), seorang murid Galileo yang menemukan barometer (lihat Gambar 13911).')
        col_4, col_5, col_6 = st.columns(3)
        with col_5:
            st.image('gambar/12.png', caption='Gambar 12. Merkuri barometer, yang ditemukan oleh Torricelli. (Giancoli, D. (2020)')
        st.write('Faktor konversi antara berbagai unit tekanan diberikan dalam (Gambar 13). Penting bahwa hanya $N/m^2 = Pa$, unit SI yang benar, yang digunakan dalam perhitungan yang melibatkan kuantitas lain yang ditentukan dalam satuan SI.')
        st.image('gambar/13.png', caption='Gambar 13. Faktor Konversi Antara Berbagai Satuan Tekanan. (Giancoli, D. (2020)')
        st.write('Jenis lain dari alat ukur tekanan adalah **alat ukur aneroid** (Gambar 11b) di mana penunjuk terhubung ke ujung-ujung fleksibel dari sebuah ruang logam tipis yang dievakuasi. Pada alat ukur elektronik, tekanan mungkin diterapkan pada diafragma logam tipis yang deformasinya diterjemahkan menjadi sinyal listrik oleh transduser. Alat ukur tekanan ban umum menggunakan pegas, seperti yang ditunjukkan dalam (Gambar 11c).')
        st.write('Tekanan atmosfer dapat diukur dengan jenis manometer merkuri yang dimodifikasi dengan satu ujung tertutup, disebut barometer merkuri (Gambar 12). Tabung kaca sepenuhnya diisi dengan merkuri dan kemudian dibalikkan ke dalam mangkuk merkuri. Jika tabung cukup panjang, tingkat merkuri akan turun, meninggalkan ruang hampa udara di bagian atas tabung, karena tekanan atmosfer hanya dapat menopang kolom merkuri sekitar 76 cm tingginya (tepatnya 76,0 cm pada tekanan atmosfer standar). Dengan kata lain, sebuah kolom merkuri setinggi 76 cm menimbulkan tekanan yang sama dengan atmosfer:')
        st.latex(r'P = \rho g \Delta h')
        st.latex(r'P = (13.6 \text{x} 10^3 \text{ } kg/m^3)(9.80 \text{ } m/s^2)(0.760 \text{} m)')
        st.latex(r'P = 1.013 \text{x} 10^5 \text{ } N/m^2 = 1.00 \text{ } atm')
        st.write('Barometer rumah tangga biasanya adalah tipe aneroid (Gambar 11b), baik mekanik (dengan dial) maupun elektronik.')
        col_7, col_8, col_9 = st.columns(3)
        with col_8:
            st.image('gambar/14.png', caption='Gambar 14. Sebuah Barometer air. (Giancoli, D. (2020)')
        st.write('Perhitungan serupa dengan yang baru saja dilakukan untuk Hg akan menunjukkan bahwa tekanan atmosfer dapat menjaga kolom air setinggi 10,3 m dalam tabung yang bagian atasnya berada di bawah vakum (Gambar 14) pada gambar tersebut sebuah tabung penuh air (lebih panjang dari 10 m), tertutup di bagian atasnya, dimasukkan ke dalam sebuah bak air. Ketika ujung bawah tabung yang terendam di dalam air dilepaskan, sebagian air mengalir keluar dari tabung ke dalam bak, meninggalkan vakum di bagian atas tabung di atas permukaan air. Mengapa? Karena tekanan udara hanya dapat menopang kolom air setinggi 10 m. Tidak peduli seberapa baik pompa vakum tersebut, air tidak dapat dipaksa naik lebih dari 10,3 m di bawah tekanan atmosfer normal. Untuk memompa air keluar dari sumur tambang yang dalam dengan pompa vakum memerlukan beberapa tahap untuk kedalaman lebih dari 10 m. Galileo mempelajari masalah ini, dan muridnya Torricelli adalah yang pertama menjelaskannya. Intinya adalah bahwa sebuah pompa sebenarnya tidak mengisap air naik ke dalam tabung: ia hanya mengurangi tekanan di bagian atas tabung. Tekanan udara atmosfer mendorong air naik ke dalam tabung jika ujung atasnya berada di tekanan lebih rendah (di bawah vakum), sama seperti tekanan udara yang mendorong (atau menjaga) merkuri setinggi 76 cm dalam barometer. [Pompa gaya, Bagian 1.3, dapat mendorong lebih tinggi.]')
        with st.expander("📚**Latihan Soal**", expanded=False):
            st.write('***SOAL 8***: **Penyedotan**. Seorang insinyur pemula mengusulkan sepatu dengan cangkir penarik untuk astronot pesawat ulang-alik yang bekerja di luar pesawat antariksa. Setelah baru saja mempelajari bab ini, Anda dengan lembut mengingatkannya akan kesalahan dalam rencana ini. Apa kesalahannya?')
            st.write('***PEMBAHASAN***: Respon: Cangkir penarik bekerja dengan mendorong keluar udara di bawah cangkir. Yang membuat cangkir penarik tetap di tempat adalah tekanan udara di luar cangkir. (Ini bisa menjadi gaya yang signifikan saat di Bumi. Sebagai contoh, cangkir penarik berdiameter 10 cm memiliki luas $7,9$ x $10^{-3}$ $m^2$. Gaya atmosfer di atasnya adalah $(7,9$ x $10^{-3}$ $m^2)$ $(1,0$ x $10^5$ $N/m^2$) $≈ 800$ $N$, sekitar 180 pon!) Tetapi di luar angkasa, tidak ada tekanan udara untuk mendorong cangkir penarik ke pesawat antariksa.')       
        st.write('Kadang-kadang kita dengan salah menganggap penarikan sebagai sesuatu yang kita lakukan secara aktif. Sebagai contoh, secara intuitif kita berpikir bahwa kita menarik minuman soda melalui sedotan. Sebaliknya, apa yang kita lakukan adalah menggunakan mulut kita untuk menurunkan tekanan di bagian atas sedotan, dan atmosfer mendorong minuman soda naik melalui sedotan.')
        
        # Vacum
        st.header(':blue[Vakum]')
        st.write('"Vakum" secara ideal berarti ruang yang tidak berisi materi. Dalam kehidupan nyata, itu mengacu pada tekanan yang berkurang, biasanya jauh lebih rendah dari tekanan atmosfer. (Bagian atas barometer dalam (Gambar 12) tampaknya merupakan vakum yang sempurna; tetapi beberapa molekul merkuri menguap menjadi gas, sama seperti air menguap.)')
        st.markdown('###')
        st.write('---')
        
        #1.6 GAYA APUNG; PRINSIP ARCHIMEDES
        st.title(':orange[1.6 GAYA APUNG; PRINSIP ARCHIMEDES]')
        st.write('Benda-benda yang terendam dalam fluida tampaknya memiliki berat yang lebih ringan daripada saat di luar fluida. Sebagai contoh, sebuah batu besar yang sulit diangkat dari tanah seringkali dapat dengan mudah diangkat dari dasar sungai. Ketika Anda mengangkat batu melalui permukaan air, tiba-tiba terasa jauh lebih berat. Banyak benda, seperti kayu, mengapung di permukaan air. Dua efek ini adalah contoh dari gaya apung. Dalam setiap contoh, gaya gravitasi beraksi ke bawah. Tetapi selain itu, gaya apung ke atas dihasilkan oleh cairan. Gaya apung pada ikan dan penyelam bawah air hampir persis menyeimbangkan gaya gravitasi ke bawah, dan memungkinkan mereka untuk "melayang" dalam keseimbangan.')
        col_10, col_11, col_12 = st.columns(3)
        with col_11:
            st.image('gambar/15.png', caption='Gambar 15. Penentuan gaya apung. (Giancoli, D. (2020)')
        st.write('Gaya apung terjadi karena tekanan dalam sebuah fluida meningkat dengan kedalaman. Dengan demikian, tekanan ke atas pada permukaan bawah suatu benda yang terendam lebih besar daripada tekanan ke bawah pada permukaan atasnya. Untuk melihat efek ini, pertimbangkan sebuah silinder dengan tinggi $∆h$ yang ujung atas dan bawahnya memiliki luas $A$ dan yang sepenuhnya terendam dalam fluida dengan kerapatan $\\rho_F$, seperti yang ditunjukkan dalam (Gambar 15). Fluida memberikan tekanan $P_1 = \\rho_F g h_1$ pada permukaan atas silinder (Persamaan 3-1). Gaya yang disebabkan oleh tekanan ini di atas silinder adalah $F_1 = P_1 A = \\rho_F g h_1 A$, dan mengarah ke bawah. Demikian pula, fluida memberikan gaya ke atas pada bagian bawah silinder yang sama dengan $F_2 = P_2 A = \\rho_F g h_2 A$. Gaya bersih pada silinder yang dihasilkan oleh tekanan fluida, yang merupakan **gaya apung $F_B$**, bertindak ke atas dan memiliki besaran')
        st.latex(r'F_{apung} = F_2 - F_1 = \rho_F g A (h_2 - h_1)')
        st.latex(r'F_{apung} = \rho_F g A \Delta h')
        st.latex(r'F_{apung} = \rho_F V g')
        st.latex(r'F_{apung} = m_F g')
        st.write('di mana $V = A \Delta h$ adalah volume silinder; produk $\\rho_F V$ adalah massa fluida yang tergeser, dan $\\rho_F V g = m_F g$ adalah berat fluida yang menempati volume yang sama dengan volume silinder. Dengan demikian, gaya apung pada silinder sama dengan berat fluida yang tergeser oleh silinder.')
        st.write('Hasil ini berlaku tidak peduli bentuk objeknya. Penemuan ini dikreditkan kepada Archimedes (287 - 212 SM), dan disebut sebagai **prinsip Archimedes:**')
        st.info('Gaya apung pada suatu objek yang terendam dalam sebuah fluida sama dengan berat fluida yang tergeser oleh objek tersebut.')
        st.write('Dengan "fluida yang tergeser," kita maksud sebuah volume fluida yang sama dengan volume yang terendam dari objek (atau bagian objek yang terendam). Jika objek diletakkan di dalam gelas atau bak yang awalnya terisi penuh dengan air, air yang meluap di atas mewakili air yang digeser oleh objek.')
        st.image('gambar/16.png', caption='Gambar 16. Hukum Archimedes. (Giancoli, D. (2020)')
        st.write("Kita dapat menurunkan prinsip Archimedes secara umum dengan argumen sederhana namun elegan. Objek berbentuk tidak teratur D yang ditunjukkan dalam (Gambar 16a) dipengaruhi oleh gaya gravitasi (beratnya, $mg$, ke bawah) dan gaya apung, $F_B$, ke atas. Kita ingin menentukan $F_B$. Untuk melakukannya, kita kemudian mempertimbangkan sebuah benda (D' dalam Gambar 16b), kali ini terbuat dari fluida itu sendiri, dengan bentuk dan ukuran yang sama dengan objek asli, dan terletak pada kedalaman yang sama. Anda mungkin berpikir tentang benda fluida ini seperti terpisah dari sisa fluida oleh membran imajiner. Gaya apung $F_B$ pada benda fluida ini akan sama persis dengan pada objek asli karena fluida sekitarnya, yang mengeksekusi $F_B$, berada dalam konfigurasi yang sama persis. Benda fluida $D′$ ini dalam keseimbangan (fluida secara keseluruhan diam). Oleh karena itu, $F_B = m'g$, di mana $m'g$ adalah berat benda fluida $D′$. Oleh karena itu, gaya apung $F_B$ sama dengan berat benda fluida yang volumenya sama dengan volume objek asli yang terendam, yang merupakan prinsip Archimedes.")
        st.write('Penemuan Archimedes dilakukan melalui eksperimen. Apa yang telah kita lakukan adalah menunjukkan bahwa prinsip Archimedes dapat dihasilkan dari hukum Newton.')
        with st.expander("📚**Latihan Soal**", expanded=False):
            st.write('***SOAL 9***: **Dua ember air**. Pertimbangkan dua ember air identik yang terisi penuh hingga ke pinggirnya. Satu ember berisi hanya air, yang lainnya memiliki sepotong kayu yang mengapung di dalamnya. Mana yang lebih berat, ember mana?')
            st.write('***PEMBAHASAN***: Respon: Kedua ember memiliki berat yang sama. Ingat prinsip Archimedes: kayu tersebut menggeser volume air dengan berat yang sama dengan berat kayu tersebut. Sebagian air akan tumpah dari ember, tetapi prinsip Archimedes memberi tahu kita bahwa air yang tumpah memiliki berat yang sama dengan berat kayu; jadi ember itu akan memiliki berat yang sama dengan ember lainnya.')
            st.write('---')
            st.write('***SOAL 10***: **Mengangkat patung yang tenggelam**. Sebuah patung kuno dengan massa $70$ kg terletak di dasar laut. Volume patung tersebut adalah $3.0$ x $10^4$ $cm^3$. Berapa besar gaya yang diperlukan untuk mengangkatnya (tanpa percepatan)?')
            col_13, col_14, col_15= st.columns(3)
            with col_14:
                st.image('gambar/17.png', caption='Gambar 17. Gaya gaya yang dibutuhkan untuk mengangkat patung. (Giancoli, D. (2020)', width=50, use_column_width='auto')
            st.write('***PEMBAHASAN***: Gaya $F$ yang diperlukan untuk mengangkat patung sama dengan berat patung $mg$ dikurangi dengan gaya apung $F_{apung}$. (Gambar 17) adalah diagram gaya bebas.')
            st.write('Kita menerapkan hukum kedua Newton, $\sum{F} = ma = 0$, yang memberikan $F + F_{apung} - mg = 0$ atau')
            st.latex(r'F = mg - F_{apung}')
            st.write('Gaya apung pada patung akibat air sama dengan berat dari $3.0$ x $10^4$ $cm^3$ $= 3.0$ x $10^-2$ $m^3$ dari air (untuk air laut, $\\rho = 1.025$ x $10^3$ $kg/m^3$:')
            st.latex(r'F_{apung} = m_{H_20} g = \rho_{H_20} V g')
            st.latex(r'F_{apung} = (1.025 \text{ x } 10^3 \text{ } kg/m^3)(3.0 \text{ x } 10^{-2} \text{ } m^3)(9.8 \text{ } m/s^2)')
            st.latex(r'F_{apung} = 3.0 \text{ x } 10^2 \text{ } N')
            st.write('Dimana kita menggunakan simbol kimia untuk air, $H_2O$, sebagai subscript. Berat patung adalah $mg$ = $(70$ $kg)$ $(9.8$ $m/s^2$ $= 6.9$ x $10^2$ $N$. Oleh karena itu, gaya $F$ yang diperlukan untuk mengangkatnya adalah $690$ $N$ - $300$ $N$ $= 390$ $N$. Terasa seperti patung memiliki massa hanya $\\frac{390 N}{9.8 m/s^2}$ $= 40$ $kg$.')
            st.write('***CATATATAN***: Catatan: Di sini, $F = 390$ N,  adalah gaya yang diperlukan untuk mengangkat patung tanpa percepatan ketika berada di bawah air. Saat patung keluar dari air, gaya $F$ meningkat, mencapai $690$ $N$ ketika patung benar-benar keluar dari air.')
        st.write("Dikatakan bahwa Archimedes menemukan prinsipnya di bak mandi sambil memikirkan bagaimana dia bisa menentukan apakah mahkota baru raja itu murni emas atau palsu. Emas memiliki berat jenis 19.3, sedikit lebih tinggi daripada kebanyakan logam, tetapi penentuan berat jenis atau densitas tidak dapat dilakukan secara langsung karena, bahkan jika massa diketahui, volume objek yang berbentuk tidak teratur tidak mudah dihitung. Namun, jika objek tersebut ditimbang di udara $(= w)$ dan juga 'ditimbang' saat berada di bawah air $(= w')$, densitas dapat ditentukan menggunakan prinsip Archimedes, seperti yang ditunjukkan oleh Contoh berikut. Kuantitas $w'$ disebut berat tampak di dalam air, dan itulah yang ditunjukkan oleh sebuah timbangan pegas ketika objek tenggelam dalam air (lihat Gambar 18); $w'$ sama dengan berat sebenarnya $(w = mg)$ dikurangi gaya apung.")
        with st.expander("📚**Latihan Soal**", expanded=False):
            st.write('***SOAL 10***: **Archimedes.** Ketika sebuah mahkota dengan massa 14.7 kg tenggelam dalam air, sebuah timbangan yang akurat hanya menunjukkan 13.4 kg. Apakah mahkota tersebut terbuat dari emas?')
            st.image('gambar/18.png', caption='Gambar 18. Ilustrasi keadaan mahkota. (Giancoli, D. (2020)')
            st.write('***PEMBAHASAN***: Jika mahkota tersebut emas, maka densitas dan berat jenisnya harus sangat tinggi, $SG = 19.3$ (lihat Gambar 1). Kami menentukan berat jenis mahkota menggunakan prinsip Archimedes dan dua diagram gaya bebas yang ditunjukkan dalam (Gambar 18)')
            st.write("Berat tampak objek yang tenggelam (mahkota) adalah $w'$ (apa yang dibaca oleh timbangan dalam (Gambar 18b)), dan merupakan gaya menarik ke bawah pada kait timbangan. Menurut hukum ketiga Newton, $w'$ sama dengan gaya $F'_T$ yang ditimbulkan oleh timbangan pada mahkota dalam (Gambar 18b). Jumlah gaya pada mahkota saat diam adalah nol, sehingga $w'$ sama dengan berat sebenarnya $w= mg$ dikurangi gaya apung $F_{apung}$:")
            st.latex(r"w' = F'_T = w - F_{apung}")
            st.write('menjadi')
            st.latex(r"w - w' = F_{apung}")
            st.write('Biarkan $V$ menjadi volume objek yang sepenuhnya tenggelam (mahkota) dan $\\rho_O$ menjadi densitas objek (sehingga $\\rho_O V$ adalah massa objek tersebut), dan biarkan $\\rho_F$ menjadi densitas fluida (air). Maka $(\\rho_F V)g$ adalah berat fluida yang dipindahkan $( = F_B)$. Sekarang kita dapat menulis:')
            st.latex(r'w = m g = \rho_o V g')
            st.latex(r"w - w' = F{apung} = \rho_F V g....(\text{Hukum Archimedes})")
            st.write('Kita membagi kedua persamaan ini dan memperoleh:')
            st.latex(r"\frac{w}{w-w'} = \frac{\rho_o V g}{\rho_F V g} = \frac{\rho_o}{\rho_F}")
            st.write("Kita melihat bahwa $\\frac{w}{(w - w')}$ sama dengan berat jenis objek (mahkota) jika fluida di dalamnya tenggelam adalah air $(\\rho_F = 1.00$ x $10^3$ $kg/m^3)$. Dengan demikian,")
            st.latex(r"\frac{\rho_o}{\rho_{H_2O}} = \frac{w}{w-w'} = \frac{14.7 \text{ kg} g}{(14.7 \text{ kg} - 13.4 \text{ kg})g} = \frac{14.7 \text{ kg}}{1.3 \text{ kg}} = 11.3")
            st.write('Ini sesuai dengan densitas 11.300 kg/m³. Mahkota tersebut bukan emas, tetapi tampaknya terbuat dari timbal (lihat Gambar 1).')
            st.write('---')
        st.write('Prinsip Archimedes berlaku sama baiknya untuk objek yang mengapung, seperti kayu. Secara umum, sebuah objek mengapung di atas fluida jika densitasnya $(\\rho_0)$ lebih rendah dari densitas fluida $(\\rho_F)$. Ini dengan mudah terlihat dari (Gambar 19a), di mana sebatang kayu yang tenggelam dengan massa $m_O$ akan mengalami gaya netto ke atas dan mengapung ke permukaan jika $F_B \geq m_o g$; yaitu, jika $\\rho_F V g \geq \\rho_o V g$ atau $\\rho_F \geq \\rho_o$. Pada keseimbangan: yaitu, saat mengapung: gaya apung pada sebuah objek memiliki magnitudo yang sama dengan berat objek. Sebagai contoh, sebuah balok kayu yang berat jenisnya adalah 0.60 dan volumenya adalah 2.0 m³ memiliki massa')
        st.image('gambar/19.png', caption='Gambar 19. Ilustrasi balok kayu. (Giancoli, D. (2020)')
        st.write('Gambar (a) Balok kayu yang sepenuhnya tenggelam mengalami percepatan ke atas karena $F_B \geq m_O g$. Ia mencapai keseimbangan (b) ketika $\sum F = 0$, sehingga $F_B = m_o g = (1200 ) g$. Kemudian $1200$ $kg$, atau $1.2$ $m³$, air digeser.')
        st.latex(r'm_o = \rho_o V = (0.60 \text{ x } 10^3 \text{ } kg/m^3)(2.0 \text{ } m^3) = 1200 kg')
        st.write('Jika balok kayu sepenuhnya tenggelam, maka akan menggeser massa air sebesar')
        st.latex(r'm_F = \rho_F V = (1000 \text{ x } 10^3 \text{ } kg/m^3)(2.0 \text{ } m^3) = 2000 kg')
        st.write('Oleh karena itu, gaya apung pada balok kayu yang tenggelam $(= m_F g)$ akan lebih besar dari beratnya, dan akan didorong ke atas untuk mengapung di permukaan (Gambar 19). Balok kayu akan mencapai keseimbangan ketika ia menggeser 1200 kg air, yang berarti bahwa $1.2$ $m³$ dari volumenya akan tenggelam. $1.2$ $m³$ ini sesuai dengan $60%$ dari volume balok $(= \\frac{1.2}{2.0} = 0.60)$, jadi $60%$ dari balok tersebut tenggelam.')
        st.write('Secara umum, ketika sebuah objek mengapung, kita memiliki $F_{apung} = m_O g$, yang dapat kita tulis sebagai (lihat Gambar 20)')
        col_16, col_17, col_18= st.columns(3)
        with col_17:
            st.image('gambar/20.png', caption='Gambar 20. Sebuah objek yang mengapung dalam keseimbangan. (Giancoli, D. (2020)')
        st.latex(r'F_B = m_og')
        st.latex(r'P_FV_{displ} g = \rho_o V_o g')
        st.write('di mana $V_o$ adalah volume penuh objek dan $V_{displ}$ adalah volume fluida yang digesernya (volume yang tenggelam). Dengan demikian,')
        st.latex(r'\frac{V_{displ}}{V_o} = \frac{\rho_o}{\rho_F}')
        st.write('Artinya, fraksi dari objek yang tenggelam diberikan oleh rasio densitas objek terhadap densitas fluida. Jika fluidanya adalah air, fraksi ini sama dengan berat jenis objek.')
        with st.expander("📚**Latihan Soal**", expanded=False):
            st.write('***SOAL 11***: **Kalibrasi Hidrometer**. Sebuah hidrometer adalah instrumen sederhana yang digunakan untuk mengukur berat jenis cairan dengan menunjukkan seberapa dalam instrumen tersebut tenggelam dalam cairan. Sebuah hidrometer tertentu (Gambar 21) terdiri dari tabung kaca, diberi bobot di bagian bawah, yang panjangnya 25,0 cm dan memiliki luas penampang 2,00 cm², serta memiliki massa 45,0 g. Seberapa jauh dari ujung bermassa tersebut tanda 1,000 harus ditempatkan?')
            col_19, col_20, col_21= st.columns(3)
            with col_20:
                st.image('gambar/21.png', caption='Gambar 21. Ilustrasi hidrometer. (Giancoli, D. (2020)')
            st.write('***PEMBAHASAN***: Pendekatan Hidrometer akan mengapung di air jika densitasnya $\\rho$ kurang dari $\\rho_{H_2O} = 1.000$ $g/cm³$, densitas air. Fraksi hidrometer yang tenggelam $(\\frac{V_{displaced}}{V_{total}})$ sama dengan rasio densitas $\\frac{\\rho}{\\rho_{H_2O}}$. Hidrometer memiliki densitas keseluruhan:')
            st.latex(r'\rho = \frac{m}{V} = {45.0 \text{ g}}{(2.00 \text{ } cm^2)(25.0 \text{ cm})} = 0.900 \text{ }g/cm^3')
            st.write('Dengan demikian, ketika diletakkan di dalam air, ia akan mencapai keseimbangan ketika 0,900 dari volumenya terendam. Karena memiliki penampang lintang yang seragam, (0,900) (25,0 cm) = 22,5 cm dari panjangnya akan terendam. Spesifik gravitasi air didefinisikan sebagai 1,000, jadi tanda tersebut harus ditempatkan 22,5 cm dari ujung yang tertimbang.')
            st.write('***CATATAN***: Hidrometer dapat digunakan untuk mengukur densitas cairan seperti cairan pendingin radiator mobil, asam baterai mobil (sebagai ukuran muatan), proses fermentasi anggur dan bir, dan banyak lagi lainnya.')
        st.write('Prinsip Archimedes juga berguna dalam geologi. Menurut teori tektonik lempeng dan pergeseran benua, benua-benua mengapung di atas "laut" fluida dari batuan yang sedikit dapat dideformasi (batuan mantel). Beberapa perhitungan menarik dapat dilakukan menggunakan model-model yang sangat sederhana, yang kita pertimbangkan dalam Masalah-masalah di akhir Bab.')
        st.write('Udara adalah fluida, dan juga memberikan gaya apungan. Objek-objek biasa memiliki berat yang lebih ringan di udara daripada di ruang hampa udara. Karena densitas udara sangat kecil, efeknya bagi benda-benda padat biasa sangat kecil. Namun, ada benda-benda yang mengapung di udara: seperti balon berisi helium, karena densitas helium lebih kecil daripada densitas udara.')
        with st.expander("📚**Latihan Soal**", expanded=False):
            st.write('***SOAL 12***: **Balon Helium**. Berapa volume $V$ helium yang diperlukan jika sebuah balon akan mengangkat beban seberat 180 kg (termasuk berat balon kosong)?')
            col_22, col_23, col_24= st.columns(3)
            with col_23:
                st.image('gambar/22.png', caption='Gambar 22. Ilustrasi balon helium. (Giancoli, D. (2020)')
            st.write('***PEMBAHASAN***: Gaya apung pada balon helium, $F_B$, yang sama dengan berat udara yang tergantikan, setidaknya harus sama dengan berat helium ditambah dengan berat balon dan beban (Gambar 22), jika mereka akan melayang ke atas. (Gambar 1) memberikan kerapatan helium sebesar $0.179 kg/m³$. Solusinya adalah bahwa gaya apung harus memiliki nilai minimum sebesar')
            st.latex(r'F_B = (m_{He} + 180 \text{ kg})g')
            st.write('Persamaan ini dapat ditulis dalam hal kerapatan menggunakan prinsip Archimedes:')
            st.latex(r'\rho_{air} V g = (\rho_{He}V + 180 \text{ kg})g')
            st.write('Mencari nilai V, kita temukan')
            st.latex(r'V = \frac{180 \text{ kg}}{\rho_{air}-\rho_{He}} = \frac{180 \text{ kg}}{(1.29 \text{ } kg/m^3 - 0.179 \text{ } kg/m^3)}')
            st.latex(r'V = 160 \text{ } m^3')
            st.write('***CATATAN***: Ini adalah volume minimum yang dibutuhkan dekat permukaan Bumi, di mana $\\rho_{udara}$ $= 1.29$ $kg/m^3$. Untuk mencapai ketinggian yang lebih tinggi, diperlukan volume yang lebih besar karena kerapatan udara berkurang dengan ketinggian.')
            st.write('---')
            st.write('***SOAL 13***: **Membuang batu ke laut**. Sebuah perahu kayuh yang membawa batu granit besar mengapung di sebuah danau kecil. Jika batu (SG ~ 3, Gambar 1) dibuang ke laut dan tenggelam, apakah permukaan danau akan turun, naik, atau tetap sama?')
            st.write('***PEMBAHASAN***: Sama-sama perahu dan batu mengapung, sehingga gaya apung pada keduanya sama dengan total berat mereka. Perahu dan batu tersebut menggeser massa air yang beratnya sama dengan berat perahu ditambah batu. Ketika batu dilemparkan ke dalam danau, ia hanya menggeser volume sendiri, yang lebih kecil dari volume air yang digeser oleh batu saat berada di perahu (kurang lebih sepertiga karena densitas batu tiga kali lebih besar dari air). Jadi, air danau berkurang saat batu berada di dalam danau.')
            st.write('Mungkin angka dapat membantu. Misalkan perahu dan batu masing-masing memiliki massa $60$ $kg$. Kemudian perahu yang membawa batu menggeser $120$ $kg$ air, yang merupakan volume $0,12$ $m^3$ $(\\rho = 1000$ $kg/m^3$ untuk air, (Gambar 1). Ketika batu dilemparkan ke dalam danau, perahu sendiri sekarang hanya menggeser $0,06$ $m^3$. Batu hanya menggeser volume sendiri sebesar $0,02$ $m^3$ $(\\text{karena} \\text{ }\\rho = \\frac{m}{V}$ ~ $3$, sehingga $V$ ~ $\\frac{0,06m^3}{3})$. Dengan demikian, total $0,08$ $m^3$ air digeser. Kurang air digeser sehingga tinggi air danau turun.')

        st.write('---Terima Kasih Telah Membaca Sampai Akhir---')
        st.link_button('Download Catatan Fluida Statis📘', 'https://unjac-my.sharepoint.com/:b:/g/personal/shelvyokvia_1302620035_mhs_unj_ac_id/Ec85faVfqw1LgwNo4ULanNoBYV4gZC0wR-UVQRzU7rVl3A?e=7wPvh4')

    
    with tabs[1]:
        st.title(':green[PROBLEM BASED LEARNING]')
        st.write('Selamat datang di sesi pembelajaran selanjutnya, kita akan menjelajahi sebuah cara baru untuk belajar yang seru dan bermanfaat: Problem Based Learning atau PBL. Jadi, apa itu PBL? Nah, bayangkan jika kita bisa belajar sambil menyelesaikan masalah dunia nyata, bekerja sama dengan teman, dan menemukan solusi yang kreatif. Itulah inti dari PBL! Kita akan berpetualang, menemukan, dan belajar bersama-sama. Siap untuk menaklukkan tantangan dan mengasah keterampilanmu? Ayo kita mulai!')
        st.title(':orange[A. TUJUAN PEMBELAJARAN]')
        st.markdown('''
            1. Melalui kegiatan membaca dan menyimak video peserta didik mampu menerapkan konsep fluida statis dengan benar.
            2. Memahami pentingnya masalah fluida statis dalam lingkungan sekitar.
            3.	Mengidentifikasi berbagai masalah fluida statis yang ada di lingkungan sekitar.
            4.	Mengembangkan kemampuan untuk mencari solusi terhadap masalah fluida statis dengan problem based learning.
        ''')
        st.title(':orange[B. URAIAN MATERI]')
        st.write('Pada waktu di sekolah tingkat pertama, telah dikenalkan ada tiga jenis wujud zat, yaitu: zat padat, zat cair dan gas. Fluida adalah zat yang dapat mengalir dan memberikan sedikit hambatan terhadap perubahan bentuk ketika ditekan. Fluida secara umum dibagi menjadi dua macam, yaitu fluida tak bergerak dan fluida bergerak. Pada website ini kita akan fokus pada pembahasan fluida yang tidak bergerak atau fluida statis.')
        st.write('Fluida statis berasal dari dua kata, yaitu fluida dan statis. Fluida adalah bahan berbentuk zat cair atau gas yang dapat mengalir, sedangkan statis adalah keadaan yang menunjukkan tidak adanya gerakan, dalam hal ini diam. Sehingga, fluida statis adalah ilmu fisika yang mempelajari sifat-sifat benda cair dan gas yang berada dalam kondisi diam atau tidak bergerak.')
        st.image('image/Picture24.png', caption='Gambar 1. Penggunaan konsep fluida dalam kehidupan. (Sumber: https://palembang.tribunnews.com/2020/01/31/khawatir-corona-6000-penumpang-kapal-pesiar-tak-diizinkan-turun-ke-darat-2-diantaranya-warga-cina)')
        
        # PBL 1 Mengorientasikan Masalah
        st.info('Langkah PBL ⏩ (1. Mengorientasikan Masalah)')
        st.write('Menurut kalian, mengapa paku yang berukuran kecil di (Gambar 1) dapat tenggelam di air sementara kapal yang jauh lebih besar tidak tenggelam di dalam air?')
        st.write('Bagaimana hal tersebut dapat terjadi?')
        st.write('Untuk lebih memahaminya, mari simak terlebih dahulu video berikut ini:')
        with st.expander("🎬**Watch it!**", expanded=False):
            st.video('https://youtu.be/0QCq6GPY8kQ?si=GUybEaWXn41OKpkc')
            st.write('Waktu kecil, kalian pasti pernah main di pinggir kolam... terus iseng ngelempar batu ke dalam air. Waktu batunya tenggelem, kita pun bertanya-tanya, kenapa bisa begitu. Kalian mungkin berpikir, hmm, mungkin karena batu itu berat. Tapi terus kalian liat kapal yang jauh lebih besar dan jauh lebih berat Dan mereka bisa tetap mengapung dan ga tenggelem. Lalu, kalian penasaran Kenapa itu bisa terjadi? Jawabannya ternyata bukan semata karena berat, melainakan karena adanya semacam kekuatan yang dinamakan Gaya angkat dan Tingkat kepadatan benda itu sendiri. Gaya yang satu ini ditemukan sama orang jenius ini yang bilang kalo sebuah benda dicelupin kedalam air baik sebagian atau seluruhnya maka ia akan mengalami gaya angkat ke atas sama yang besar dengat berat air yang dipindahkanya itu. Tapi, si gaya angkat ini gak akan mampu mengangkat bakso kalau bola daging di dalam kita ini lebih berat dari kuah bakso dalam ukuran yang sama. Jadi kita tau supaya bisa mengapung, kepadatan kapal harus kurang dari air. Itulah mengapa kapal punya resep rahasia yaitu sebuah bagian yang berisi rongga rongga udara Bagian lambung kapal ini yang bikin kapal seimbang dan mengapung di lautan nggak peduli sebesar dan seberat apapun kapal tersebut dibuat. Itu menjelaskan juga kenapa Titanic tenggelam yaitu karena lambung kapalnya bocor nabrak gunung es dan akhirnya penuh sama air. Sehingga kapalnya tenggelam kedasar Samudra. Nah, dengan resep rahasia tadi kita akhirnya bisa bikin kapal kapal berukuran raksasa seperti kapal pesiar mewah ini, yang 5 kali lebih berat daripada Titanic atau kapal tanker terbesar ini panjangnya 4,5 kali panjang Lapangan Gelora Bung Karno dan beratnya sama kayak 100.000 (kali) Gajah Afrika Atau seperti kapal canggih ini yang jadi Bandara di Tengah Samudra buat pesawat-pesawat tempur. Cara yang sama juga diterapin di Kapal Selam, dimana ia punya rongga yang bisa diisi air apabila ia ingin menyelam, Dan diisi udara jika hendak mengapung ke permukaan. Jadi, kita udah tau kenapa kapal yang besar banget itu bisa berlayar di samudra luas, dan mulai sekarang kita pun bisa request ke abang bakso Supaya bikin ruang udara di dalam bakso agar mengapung di mangkok, biar gampang di makan.😃')
        st.write('Jadi jika sekarang ditanyakan kembali mengapa kapal laut yang besar bisa mengapung apakah kalian bisa menjawabnya?')
        st.markdown('###')
        st.write('---')

        # PBL 2 Mengorganisasikan Peserta Didik Untuk Belajar
        st.info('Langkah PBL ⏩ (2. Mengorganisasikan Kegiatan Pembelajaran)')
        st.header(':blue[1. TEKANAN]')
        st.write('Tekanan didefinisikan sebagai gaya yang bekerja tegak lurus pada suatu bidang dibagi dengan luas bidang itu. Dan secara matematis dirumuskan sebagai berikut:')
        left_co, cent_co,last_co = st.columns(3)
        with cent_co:
            st.image('image/Picture1.png', caption='Gambar 2. Ilustrasi Tekanan. (Sumber: https://www.ruangguru.com/blog/tekanan-zat-padat)')
        st.latex(r'P = \frac{F}{A}...............(1)')
        st.write('Keterangan:')
        st.write(r'P = Tekanan (Pascal atau $N/m^2$)')
        st.write(r'F = Gaya (N)')
        st.write(r'A = Luas Permukaan ($m^2$)')
        st.write('Satuan SI untuk gaya adalah N (Newton) dan untuk luas bidang adalah m². Dengan demikian satuan SI untuk tekanan adalah $N/m²$ atau $Nm^{-2}$. Dalam satuan SI digunakan juga satuan lain untuk tekanan, yaitu Pascal (Pa) dimana:')
        st.latex(r'1 \text{ } Pa = 1 \text{ } N/m^2')
        st.write('Tekanan berbanding lurus dengan gaya dan berbanding terbalik dengan luas permukaan. Apabila gaya yang diberikan besar maka tekanan yang terjadi juga besar dan sebaliknya. Sedangkan apabila luas permukaan bertambah maka tekanan pada benda akan berkurang.')
        st.write('Salah satu contoh penerapan tekanan pada kehidupan sehari-hari adalah penggunaan paku, selput pada kaki bebek dan lain sebagainya. Untuk lebih memahami konsep tekanan perhatikan tayangan video dibawah ini.')
        with st.expander("🎬**Video Konsep Tekanan dalam Kehidupan**", expanded=False):
            st.video('https://www.youtube.com/watch?v=AJjGj5Ss8cg')
        with st.expander("📘 Latihan Soal 1" , expanded=False):
            st.write(':grey[Sebuah peti kayu berbentuk balok berukuran panjang 1 m dan lebar 50 cm memiliki berat sebesar 400 N. Jika peti tersebut berada di atas lantai, maka tentukanlah tekanan yang dihasilkan!]')
            st.text_area('Analisis Jawaban Soal 1')
        st.markdown('###')

        #Subheader 2
        st.header(':blue[2. TEKANAN HIDROSTATIS]')
        st.image('image/waduk.jpg', caption='Gambar 3. Waduk. (Sumber: https://taniku.kulonprogokab.go.id/agrowisata/index/4)')
        st.write('Pernahkah kamu bepergian ke suatu waduk atau bendungan? Jika diperhatikan dari atas terlihat bahwa bagian bawah dinding bendungan lebih lebar daripada bagian atasnya. Bisakah kamu menganalisis terkait dengan fenomena tersebut?')
        st.write('***Tekanan hidrostatis*** adalah tekanan yang diberikan oleh air ke semua arah pada titik ukur manapun akibat adanya gaya gravitasi. Tekanan hidrostatis akan meningkat seiring dengan bertambahnya kedalaman diukur dari permukaan air.')
        st.write('Akibat gaya gravitasi, berat partikel air akan menekan partikel dibawahnya, dan begitu pula partikel-partikel air di bawahnya akan saling menekan hingga ke dasar air sehingga tekanan dibawah akan lebih besar dari tekanan diatas. Jadi, semakin dalam kita menyelam dari permukaan air, maka akan semakin banyak volume air yang ada di atas kita dengan permukaan air sehingga tekanan yang diberikan air pada tubuh kita (tekanan hidrostatis) akan semakin besar. Secara umum tekanan hidrostatis dapat dirumuskan sebagai berikut:')
        st.latex(r'P_h = \rho_f{g}{h}...............(2)')
        st. write('Keterangan:')
        st.write('$P_h$ = Tekanan Hidrostatis (Pa)')
        st.write('$\\rho_f$ = Massa Jenis fluida $(kg/m^3)$')
        st.write('g = Percepatan gravitasi $(m/s^2)$')
        st.write('h = Kedalaman (m)')
        st.write('Berikut fenomena sederhana mengenai tekanan hidrostatis yang terjadi pada wadah yang berisi air.')
        left1, cent1,last1 = st.columns(3)
        with cent1:
            st.image('image/hidrostatis.jpg', caption='Gambar 4. Tekanan Hidrostatis pada Wadah. (Sumber: https://blog.maukuliah.id/hidrostatis-adalah)')
        st.write('Jadi semakin besar jarak titik ukur dengan permukaan air, maka akan semakin besar tekaunan hidrostatis pada titik tersebut. Fenomena ini dapat dilihat pada gambar diatas dimana semakin besar ketinggian air, maka akan semakin besar pula tekanan hidrostatis di dasar bejana. Akibatnya, air akan muncrat lebih jauh pada bejana sebelah kanan karena tekanan yang lebih tinggi dibandingkan bejana di sebelah kiri.')
        st.write('Penjumlahan antara tekanan hidrostatis dan tekanan udara luar akan menghasilkan besaran baru yang disebut tekanan mutlak. Secara matematis, dirumuskan sebagai berikut:')
        st.latex(r'P_T=P_0+{\rho}{g}{h}...............(3)')
        st.write('Keterangan:')
        st.write(r'$$P_T = \text{Tekanan Mutlak} \,({Pascal} \text{ atau } \,{N/m^2})$$')
        st.write(r'$$P_0 = \text{Tekanan Atmosfer} = 1 \text{ atm} = 76 \text{ cmHg} = 10^5 \text{ }N/m^2$$')
        st.write(r'$$\rho = \text{Massa Jenis fluida} \,(kg/m^3)$$')
        st.write(r'$$g = \text{Percepatan gravitasi} \,(m/s^2)$$')
        st.write(r'$$h = \text{Kedalaman} \,(m)$$')
        st.write('Perhatikan tayangan video dibawah ini agar lebih memahami tekanan hidrostatis dan penerapannya dalam kehidupan sehari-hari.')
        with st.expander("🎬**Video Konsep Tekanan Hidrostatis dalam Kehidupan**", expanded=False):
            st.video('https://youtu.be/_lyLpIbFt9Q?si=3ks6nArUPfZd66xD')
        with st.expander("📘 Latihan Soal 2" , expanded=False):
            st.write(':grey[Seekor ikan berada pada kedalaman 15 meter di bawah permukaan air.]')
            left2, cent2,last2 = st.columns(3)
            with cent2:
                st.image('image/Picture25.png', caption='Gambar 5. Ikan dibawah permukaan air. (Sumber: https://roboguru.ruangguru.com/question/seekor-ikan-berada-pada-kedalaman-17-meter-di-bawah-permukaan-air-jika_QU-48J7ON32)')
            st.write(':grey[Jika massa jenis air $1000$ $kg/m^3$, percepatan gravitasi bumi $10$ $m/s^2$ dan tekanan udara luar $10$ $N/m$, tentukan:]')
            st.markdown('''
                :grey[1. Tekanan hidrostatis yang dialami ikan.] 
                        
                :grey[2. Tekanan total yang dialami ikan.]
            ''')
            st.text_area('Analisis Jawaban Soal 2')
        st.markdown('###')

        # Hukum Hidrostatika
        st.header(':blue[3. HUKUM HIDROSTATIKA]')
        st.write('Hukum Pokok Hidrostatika berbunyi:')
        st.write('*Semua titik yang terletak pada kedalaman yang sama maka tekanan Hidrostatikanya sama.*')
        st.write('Jadi semua titik yang terletak pada bidang datar didalam satu jenis zat cair memiliki tekanan yang sama, ini dikenal dengan hukum pokok hidrostatika dan tekanan ini disebut dengan tekanan hidrostatis.')
        st.write('Besarnya tekanan hidrostatis pada setiap titik dalam kedalaman yang sama pada satu jenis zat cair adalah sama, walaupun bentuk bejananya berbeda. Penerapan hukum utama hidrostatika pada pipa U dapat digunakan untuk mengukur massa jenis zat cair.')
        st.latex(r'{P_1} = {P_a}')
        st.latex(r'{\rho_1}{h_1} = {\rho_2}{h_2}...............(4)')
        left3, cent3, last3 = st.columns(3)
        with cent3:
            st.image('image/bejana.jpg', caption='Gambar 6. Bejana Berhubungan. (Sumber: https://www.kompas.com/tag/fluida-statik-adalah)')
        st.write('Keterangan:')
        st.write('$\\rho_1$ = Massa Jenis Zat Cair 1 $kg/m^3$')
        st.write('$\\rho_2$ = Massa Jenis Zat Cair 2 $kg/m^3$')
        st.write('$h_1$ = Tinggi zat cair 1 $(m)$')
        st.write('$h_2$ = Tinggi zat cair 2 $(m)$')
        with st.expander("🎬**Video Konsep Hukum Hidrostatika**", expanded=False):
            st.video('https://www.youtube.com/watch?v=dYhfoDfDm48')
        with st.expander("📘 Latihan Soal 3" , expanded=False):
            st.write(':grey[Pipa U diisi dengan air dan cairan minyak seperti terlihat pada (Gambar 6) di atas.]')
            st.write(':grey[Jika ketinggian minyak $h_2$, adalah $25$ $cm$, massa jenis minyak $0.8$ $gr.cm^{-3}$ dan massa jenis air adalah $1$ $gr.cm^{-3}$. Tentukan ketinggian air $(h_1)$!]')
            st.text_area('Analisis Jawaban Soal 3')
        
        # Hukum Pascal dan Penerapannya
        st.header(':blue[4. HUKUM PASCAL]')
        left4, cent4, last4 = st.columns(3)
        with cent4:
            st.image('image/mobil.jpg', caption='Gambar 7. Tempat Pencucian Mobil. (Sumber: https://cucimobilmotor.com/modal-usaha-cuci-mobil-hidrolik/)')
        st.write('Pernahkah kalian pergi ke tempat pencucuian mobil? Ketika kalian pergi ke tempat pencucian mobil kalian akan melihat mobil dapat terangkat hanya dengan alat tanpa bantuan tangan manusia. Kalau kita perhatikan sepertinya unik sekali dengan alat yang kecil mampu mengangkat mobil yang ukurannya jauh lebih besar. Berdasarkan ilustrasi tersebut:')
        st.write('Mengapa mobil yang memiliki massa lebih besar dapat diangkat oleh benda seperti mesin hidrolik? Peristiwa ini merupakan contoh penerapan hukum pascal dalam kehidupan sehari-hari. Lalu, bagaimana prosesnya dapat terjadi?')
        st.write('Prinsip Pascal mengatakan bahwa tekanan yang diberikan kepada zat cair dalam ruang tertutup diteruskan sama besar ke segala arah, Sebagai contoh sederhana aplikasi dari hukum Pascal adalah dongkrak hidrolik.')
        st.write('Hukum Pascal dicetuskan oleh seorang ilmuwan asal Prancis, yaitu Blaise Pascal. Dalam hukumnya, Pascal menyatakan bahwa *"Tekanan yang diberikan pada suatu fluida dalam ruang tertutup akan diteruskan ke segala arah dengan sama besar"*.')
        left5, cent5, last5 = st.columns(3)
        with cent5:
            st.image('image/Picture26.png', caption='Gambar 8. Prinsip Hukum Pascal. (Sumber: https://kumparan.com/berita-update/hukum-pascal-dan-manfaatnya-1vGurAqtAyA)')
        st.write('Perhatikan gambar mekanisme hidrolik diatas. Karena cairan tidak dapat ditambahkan ataupun keluar dari sistem tertutup, maka volume cairan yang terdorong di sebelah kiri akan mendorong piston (silinder pejal) di sebelah kanan ke arah atas. Dengan menggunakan prinsip Pascal, berlaku hubungan, secara matematis:')
        st.latex(r'\frac{F_1}{A_1} = \frac{F_2}{A_2}...............(5)')
        st.write('Keterangan:')
        st.write(r'$$F_1 = \text{Gaya pada penampang 1} \,(N)$$')
        st.write(r'$$F_2 = \text{Gaya pada penampang 2} \,(N)$$')
        st.write(r'$$A_1 = \text{Luas Penampang 1} \,(m^2)$$')
        st.write(r'$$A_1 = \text{Luas Penampang 1} \,(m^2)$$')
        st.write('Silahkan simak tayangan video berikut agar lebih memahami prinsip hukum pascal dan penerapannya dalam kehidupan sehari-hari.')
        with st.expander("🎬**Video Konsep Hukum Pascal dan penerapannya dalam kehidupan**", expanded=False):
            st.video('https://youtu.be/KQJWDPdghGU')
            st.write('Penerapan dalam kehidupan sehari-hari, yang menggunakan prinsip hukum Pascal antara lain dongkrak hidrolik, pompa hidrolik ban sepeda, mesin hidrolik pengangkat mobil, mesin pengepres hidrolik, dan rem piringan hidrolik.')
        with st.expander("📘 Latihan Soal 4" , expanded=False):
            st.write(':grey[Seorang anak hendak menaikkan batu bermassa 1 ton dengan alat seperti gambar berikut!]')
            st.write(':grey[Jika luas penampang pipa besar adalah 250 kali luas penampang pipa kecil dan tekanan cairan pengisi pipa diabaikan, tentukan gaya minimal yang harus diberikan anak agar batu bisa terangkat!]')
            st.text_area('Analisis Jawaban Soal 4')

        # Hukum Archimedes
        st.header(':blue[5. HUKUM ARCHIMEDES]')
        st.write('Hukum Archimedes adalah hukum tentang prinsip pengapungan pada benda cair yang ditemukan oleh Archimedes, seorang ilmuwan Yunani. Hukum ini menyatakan bahwa ‘sebuah benda yang dicelupkan sebagian atau seluruhnya ke dalam zat cair akan mengalami gaya ke atas yang besarnya sama dengan berat zat cair yang dipindahkan oleh benda tersebut')
        left6, cent6, last6 = st.columns(3)
        with cent6:        
            st.image('image/Picture27.png', caption='Gambar 9. Prinsip Hukum Archimedes. (Sumber: https://mediaindonesia.com/humaniora/653072/hukum-archimedes)')
        st.write('Benda yang tenggelam dalam fluida terlihat beratnya lebih rendah dibandingkan diluar fluida. Hal ini disebabkan benda di dalam fluida memiliki gaya angkat atau gaya apung yaitu tekanan dalam fluida naik sebanding dengan kedalaman. Tekanan keatas pada permukaan bawah benda lebih besar daripada tekanan ke bawah pada bagian atas permukaan benda. Gaya apung ini merupakan selisih dari gaya berat benda di udara dengan gaya berat benda di dalam fluida')
        st.latex(r'F_A = W_u - W_f...............(6)')
        st.write('Keterangan:')
        st.write(r'$$F_A = \text{Gaya ke atas = Gaya apung} \,(N)$$')
        st.write(r'$$W_u = \text{Gaya berat benda di udara} \,(N)$$')
        st.write(r'$$W_f = \text{Gaya berat benda di fluida} \,(N)$$')
        st.write('Secara matematis Hukum Archimedes dapat dituliskan sebagai berikut:')
        st.latex(r'F_A = \rho_f V_{bf} g...............(7)')
        st.write('Keterangan:')
        st.write(r'$$F_A = \text{Gaya ke atas = Gaya apung} \,(N)$$')
        st.write(r'$$\rho_f = \text{Massa jenis fluida} \,(kg/m^3)$$')
        st.write(r'$$V_{bf} = \text{Volume benda yang tercelup dalam fluida} \, (m^3)$$')
        st.write(r'$$g = \text{Percepatan gravitasi} \,(m/s^2)$$')
        # Sub Peristiwa mengapung, melayang, dan tenggelam
        # Sub Mengapung
        st.subheader(':red[PERISTIWA MENGAPUNG, MELAYANG, DAN TENGGELAM]', divider='red')
        st.subheader(':red[a. Mengapung]')
        st.write('Jika benda dicelupkan ke dalam fluida, benda muncul sebagian ke permukaan air, karena berat benda lebih kecil dari gaya apung $(Fa< W)$. Ini adalah konsep mengapung. Dari konsep tersebut, dapat dirumuskan hubungan antara massa jenis benda dengan massa jenis fluida:')
        left7, cent7, last7 = st.columns(3)
        with cent7: 
            st.image('image/Picture28.png', caption='Gambar 10. Benda Terapung. (Sumber: https://mediaindonesia.com/humaniora/653072/hukum-archimedes)')
        st.latex(r'\rho_b = \frac{V_{bf}}{V_b} \rho_f...............(8)')
        st.write('Keterangan:')
        st.write(r'$$\\rho_b = \text{Massa jenis benda} \,(kg/m^3)$$')
        st.write(r'$$V_{bf} = \text{Volume benda yang tercelup} \,(m^3)$$')
        st.write(r'$$V_b = \text{Volume benda} \, (m^3)$$')
        st.write(r'$$\\rho_f = \text{Massa jenis fluida} \,(kg/m^3)$$')
        # Sub Melayang
        st.subheader(':red[b. Melayang]')
        st.write('Jika benda dicelupkan seluruhnya kedalam fluida (air), maka gaya apung $(F_a)$ sama dengan berat benda $W$ $(F_a= W)$.')
        left8, cent8, last8 = st.columns(3)
        with cent8:
            st.image('image/Picture29.png', caption ='Gambar 11. Benda Melayang. (Sumber: https://mediaindonesia.com/humaniora/653072/hukum-archimedes)')
        # Sub Tenggelam
        st.subheader(':red[c. Tenggelam]')
        st.write('Jika benda dicelupkan seluruhnya kedalam fluida (air), maka gaya apung $(Fa)$ lebih kecil dari berat benda $W$ $(Fa < W)$. Sehingga benda bergerak kebawah menuju dasar wadah air. Ini adalah konsep tenggelam.')
        left9, cent9, last9 = st.columns(3)
        with cent9:
            st.image('image/Picture30.png', caption='Gambar 12. Benda Tenggelam. (Sumber: https://mediaindonesia.com/humaniora/653072/hukum-archimedes)')
        # Sub Penerapan Hukum Archimedes:
        st.subheader(':red[Penerapan Hukum Archimedes:]', divider='red')
        st.write(':violet[**Hidrometer**] : Digunakan untuk mengukur massa jenis fluida.')
        st.write(':violet[**Kapal laut**] : Agar dapat tetap mengapung, besi dibuat berongga, sehingga volume air yang dipindahkan menjadi besar, dan menyebabkan gaya apung menjadi besar.')
        st.write(':violet[**Kapal selam**] : Memiliki tangki pemberat yang dapat diisi sesuai keperluan. Agar mengapung. tangki diisi udara, sedangkan agar tenggelam, tangki diisi air.')
        st.markdown('''
            :violet[**Balon Udara**] : Cara kerja balon udara,
            - Agar naik, balon diisi gas panas sehingga volumenya bertambah, volume udara yang dipindahkan menjadi besar, $F_A > W$.
            - Setelah ketinggian yang diinginkan tercapai, agar balon udara melayang, volume balon dijaga agar $F_A = W$.
            - Agar turun, gas panas dikeluarkan dari balon udara sehingga volume balon berkurang, sehingga $F_A < W$'.
        ''')
        st.write('Agar dapat lebih memahami Hukum archimedes dan gaya apung silahkan simak video dibawah ini mengenai peristiwa percobaan archimedes berupa benda yang dicelupkan kedalam wadah berisi air')
        with st.expander("🎬**Video Hukum Archimedes**", expanded=False):
            st.video('https://youtu.be/ZIdhNkGc-20')
        with st.expander("📘 Latihan Soal 5" , expanded=False):
            st.write(':grey[Sebuah benda tercelup sebagian dalam cairan yang memiliki massa jenis $0,75$ $gr/cm^3$ seperti ditunjukkan oleh gambar berikut!]')
            st.write(':grey[Jika volume benda yang tercelup adalah $0,8$ dari volume totalnya, tentukan massa jenis benda tersebut!]')
            st.text_area('Analisis Jawaban Soal 5')
        
        # Tegangan Permukaan
        st.header(':blue[6. TEGANGAN PERMUKAAN]')
        with st.expander("📺 Video Konsep Tegangan Permukaan" , expanded=False):
            st.video('https://www.youtube.com/watch?v=C9Fj3_wAVSk')
            st.write('Ketika kalian bangun dari tidur, udara sangat menyenangkan jika kalian pergi ke luar rumah untuk menghirup udara segar. Suasana di pagi hari seringkali diselimuti oleh embun, sehingga suhu di pagi hari akan terasa dingin. Pernahkah kalian mengamati tetesan embun yang terdapat pada permukaan daun atau rumput? Lalu mengapa tetesan-tetesan itu berbentuk bola?')
            left10, cent10, last10 = st.columns(3)
            with cent10:
                st.image('image/tes.jpg', caption='Gambar 13. Peristiwa Embun. (Sumber: https://desaputat.gunungkidulkab.go.id/first/artikel/2212-RENUNGAN---EMBUN-PAGI--2-)')
        st.write('Secara Fisika, fenomena ini dapat terjadi karena adanya tegangan permukaan. Lalu, apa yang dimaksud oleh tegangan permukaan? Tegangan permukaan adalah suatu kecenderungan permukaan zat cair untuk menegang sehingga permukaannya seperti ditutupi oleh suatu lapisan kulit tipis. Penyebab adanya tegangan permukaan adalah karena adanya kohesi dibawah zat cair yang lebih besar dari pada kohesi di permukaan zat cair, sehingga permukaan air akan cenderung mengerut dan membentuk luas permukaan sekecil mungkin. Hal tersebut dapat membuktikan bahwa titik-titik embun yang menempel di atas rumput berbentuk seperti bola karena luas permukaan terkecil adalah bangun yang berbentuk bola.')
        st.image('image/Picture31.png', caption='Gambar 14. Peristiwa tegangan permukaan. (Sumber: https://www.youtube.com/watch?v=jnDVbIjZ0QM)')
        st.write('Pernahkah kamu melihat sebuah silet terapung diatas air? Atau kamu pasti pernah melihat ada nyamuk atau serangga lain dapat berdiri diatas air. Fenomena ini erat kaitannya dengan penjelasan tentang tegangan permukaan. Lalu, bisakah kamu menganalisis mengapa fenomena tersebut dapat terjadi?')
        st.write('Tegangan permukaan terjadi akibat gaya kohesi (gaya tarik-menarik antar partikel-partikel sejenis) pada permukaan fluida tersebut.')
        left11, cent11, last11 = st.columns(3)
        with cent11:
            st.image('image/Picture32.png', caption='Gambar 15. Gaya Kohesi. (Sumber: http://chemist-try.blogspot.com/2012/10/tegangan-permukaan_26.html)')
        st.write('Pada gambar diatas, titik A berada di permukaan, titik B berada di dalam fluida. Partikel yang berada di titik B mendapat gaya kohesi dari partikel-partikel lain di sekelilingnya sehingga resultan yang dihasilkan dari semua gaya kohesi ini nol. Sedangkan partikel yang berada di titik A tidak mendapat gaya kohesi dari partikel di atasnya sehingga resultan yang dihasilkan dari gaya-gaya kohesi berarah ke bawah. Tarikan pada permukaan fluida ini membentuk semacam kulit penutup yang tipis. Seekor nyamuk dapat berjalan di atas permukaan air karena berat nyamuk dapat diatasi oleh lapisan kulit tipis ini.')
        st.write('Tegangan permukaan didefinisikan sebagai perbandingan antara gaya tegangan permukaan dengan panjang permukaan dimana gaya itu bekerja.')
        left12, cent12, last12 = st.columns(3)
        with cent12:    
            st.image('image/Picture33.png', caption='Gambar 16. Gaya Tegangan Permukaan. (Sumber: https://repositori.kemdikbud.go.id/22209/1/XI_Fisika_KD-3.3-_Final.pdf)')
        st.write('Gaya tegangan permukaan yang dialami oleh kawat yang dicelupkan kedalam air sabun. Kawat yang lurus posisi horisontal (bawah), cenderung bergerak keatas karena pengaruh tarikan gaya permukaan air sabun. Larutan sabun mempunyai dua permukaan, sehingga gaya tegangan permukaan bekerja sepanjang $2L=d$, tegangan permukaan $(\gamma)$ didefinisikan sebagai perbandingan antara gaya tegangan permukaan $(F)$ dan panjang permukaan $(d)$ dimana gaya itu bekerja')
        st.write('Sehingga secara matematis, dapat dirumuskan sebagai berikut:')
        st.latex(r'\gamma = \frac{F}{d} =\frac{F}{2L}...............(9)')
        st.write('Keterangan:')
        st.write(r'$$\gamma = \text{tegangan permukaan} \,(kg/s^2)$$')
        st.write(r'$$F = \text{gaya tagangan permukaan} \,(N)$$')
        st.write(r'$$d = \text{Panjang permukaan} \,(m)$$')
        st.write(r'$$L = \text{Panjang kawat} \,(m)$$')
        st.subheader(':red[Penerapan tegangan permukaan dalam kehidupan:]', divider='red')
        st.markdown('''
            - Sabun cuci sengaja dibuat untuk mengurangi tegangan permukaan air. jadi bisa meningkatkan kemampuan air buat membersihkan kotoran yang melekat pada pakaian.
            - Mencuci pakaian dengan air hangat atau air panas lebih bersih, karena dengan suhu yang tinggi tegangan permukaan akan semakin kecil dan kemampuan air buat membasahi pakaian yang kotor lebih meningkat lagi.
            - Alkohol dan antiseptik pada umumnya punya kemampuan buat membunuh kuman, dan punya tegangan permukaan yang rendah, jadi bisa membasahi seluruh permukaan kulit yang luka.
            - Itik dan angsa bisa berenang dan terapung di atas permukaan air karena bulu- bulunya gak basah oleh air. Kalo air dicampur dengan detergen, maka tegangan permukaan akan mengecil, itik dan angsa yang berenang bulu-bulunya akan basah. Jadi, itik dan angsa tersebut bisa aja tenggelam.
            - Gelembung yang dihasilkan oleh air sabun merupakan salah satu contoh adanya tegangan permukaan.
            - Serangga air yang bisa berjalan di permukaan air.
            - Kenaikan batas air pada pipa kapiler atau terbentuknya buih dan gelombang pada air sabun.
        ''')
        st.write('Agar pemahaman kalian lebih baik terkait dengan tegangan permukaan, silahkan simak video dibawah ini dengan seksama.')
        with st.expander("📺 Video Konsep Tegangan Permukaan" , expanded=False):
            st.video('https://youtu.be/v-YSpiN4jfw')
        with st.expander("📘 Latihan Soal 6" , expanded=False):
            st.write(':grey[Sebuah kawat panjang 10 cm ditempatkan secara horizontal di permukaan air dan ditarik perlahan dengan gaya 0,02 N untuk menjaga agar kawat tetap seimbang. Tentukan tegangan permukaan air tersebut!]')
            st.text_area('Analisis Jawaban Soal 6')
        st.markdown('###')


        # Kapilaritas
        st.header(':blue[7. KAPILARITAS]')
        left13, cent13, last13 = st.columns(3)
        with cent13:
            st.image('image/Picture34.png', caption = 'Gambar 17. Peristiwa minuman tumpah. (Sumber: https://ibnujafar86.wordpress.com/2011/05/13/suamiku-bukan-lelaki-yang-sempurna/kopi-tumpah/?like=1)')
        st.write('Pernahkah kalian menumpahkan minuman? Untuk mengelap tumpahan minuman tersebut secara spontan kalian akan bergerak mengambil tisu atau kain untuk mengeringkannya. Kita memilih tisu atau kain lap karena mereka memiliki daya serap atau daya kapilaritas tinggi.')
        st.write('Kapilaritas adalah peristiwa naik atau turunnya zat cair pada pembuluh atau celah kecil atau pori-pori kecil. Tisu atau kain lap memiliki celah atau pori- pori kecil. Lalu, bagaimana proses kapilaritas tersebut dapat terjadi?')
        st.write('Kapilaritas adalah peristiwa naik atau turunnya permukaan zat cair melalui perantara, seperti kain, dinding, pipa kapiler, dan lain sabagainya. Namun tidak semua zat cair mengalami gejala kapilaritas yang sama. Misalnya pada air dan raksa.')
        left14, cent14, last14 = st.columns(3)
        with cent14:
            st.image('image/Picture35.png', caption='Gambar 18. Peristiwa kapilaritas pada pipa kapiler. (Sumber: https://eandroidfisika.wordpress.com/kapilaritas/)')
        st.write('Pada zat cair berupa air. permukaan zat cair dapat membasahi dinding. Sedangkan pada zat cair berupa raksa, tidak dapat membasahi dinding, raksa malah akan turun. Air membasahi dinding karena gaya kohesi antar partikel air lebih kecil dari gaya adhesi antara partikel air dan partikel dinding. Gaya tarik- menarik antar partikel sejenis disebut gaya kohesi. Sedangkan gaya tarik menarik antar partikel berbeda jenis disebut gaya adhesi.')
        st.write('Jika sebuah pipa yang terbuka kedua ujungnya ditegakkan dengan sebuah ujungnya berada di atas permukaan zat cair sedangkan ujung yang lain di bawah permukaan, maka permukaan zat cair dalam pipa tidak sama dengan tinggi permukaan zat cair di luar pipa.')
        st.write('Bila zat cair membasahi dinding (meniskus cekung), maka zat cair dalam pipa lebih tinggi daripada diluar pipa, sebaliknya bila zat cair tidak membasahi dinding (meniskus cembung), maka zat cair dalam pipa lebih rendah daripada di luar pipa. Peristiwa naik atau turunnya permukaan zat cair dalam pipa kapiler (pipa sempit) dinamakan gejala kapiler atau kapilaritas. Kenaikan dan penurunan permukaan zat cair di dalam pipa kapiler bergantung pada kohesi dan adhesi.')
        st.write('Kenaikan atau penurunan permukaan zat cair di dalam pipa kapiler dihitung dengan rumus berikut.')
        st.latex(r'h = \frac{{2\gamma}{cos\theta}}{{\rho}{g}{r}}...............(10)')
        st.write('Keterangan:')
        st.write(r'$$h = \text{naik/turun permukaan fluida dalam pipa kapiler } \,(m)$$')
        st.write(r'$$\gamma = \text{tegangan permukaan zat cair} \,(N/m)$$')
        st.write(r'$$\theta = \text{Sudut kontak}$$')
        st.write(r'$$\rho = \text{Massa jenis fluida} \,(N/m^3)$$')
        st.write(r'$$r = \text{jari-jari pipa kapiler} \,(m)$$')
        st.write(r'$$g = \text{percepatan gravitasi} \,(m/s^2)$$')
        st.markdown('''
            - Jika $\\theta > 90°$, gaya kohesi > gaya adhesi dan permukaan zat cair berbentuk cembung.
            Contoh: raksa (Hg).
            - Jika $\\theta < 90°$, gaya kohesi < gaya adhesi dan permukaan zat cair berbentuk cekung.
            Contoh: air.
        ''')
        st.write('Berikut ini beberapa contoh yang menunjukkan gejala kapilaritas dalam kehidupan sehari-hari:')
        st.markdown('''
            1. Naiknya minyak tanah melalui sumbu kompor sehingga kompor bisa dinyalakan.
            2. Kain dan kertas isap dapat menghisap cairan.
            3. Air dari akar dapat naik pada batang pohon melalui pembuluh kayu..
        ''')
        st.subheader(':red[SUDUT KONTAK]')
        left15, cent15, last15 = st.columns(3)
        with cent15:
            st.image('image/Picture36.png', caption='Gambar 19. Sudut Kontak. (Sumber: http://www.fisikasekolah.com/2017/01/konsep-tegangan-permukaan-dan.html)')
        st.write('Jika arah permukaan zat cair dalam wadah diperpanjang dengan garis lurus maka akan kita dapatkan sudut antara perpanjangan permukaan zat cair dangan arah vertikal wadah, sudut ini disebut dengan sudut kontak.')
        st.write('Zat dalam wujud cair, partikel-partikelnya dapat berpindah-pindah ke segala arah, tetapi sulit meninggalkan zat cair itu. Partikel-partikel tersebut saling tarik- menarik. Gaya tarik-menarik inilah yang menyebabkan partikel-partikel tersebut tidak bercerai-berai. Gaya tarik menarik antara partikel-partikel dari zat yang sama. disebut kohesi, sedangkan gaya tarik menarik antara partikel-partikel dari zat yang berbeda disebut adhesi. Kohesi dan adhesi uni mempunyai peran penting pada pembentukan permukaan zat cair.')
        st.write(':violet[**Kita Tinjau Dua Kasus Berikut**]')
        left16, cent16, last16 = st.columns(3)
        with cent16:
            st.image('image/Picture37.png', caption='20. Air dalam tabung kaca. (Sumber: https://www.mikirbae.com/2017/11/pengertian-dan-sudut-kontak-pada.html)')
        st.write('Air dimasukkan ke dalam tabung kaca. Permukaan air di dalam tabung melengkung ke atas pada bagian yang menempel di dinding kaca. Pada kasus ini gaya kohesi (F kohesi) lebih kecil dari gaya adhesi (F adhesi). Resultan kedua gaya (F resultan) ini mengarah keluar. Supaya tercapai keseimbangan, maka permukaan air yang menempel di dinding kaca harus tegak lurus pada gaya $F$ ini sehingga air yang menempel pada dinding kaca melengkung ke atas. Kelengkungan zat cair di dalam tabung dinamakan meniskus sehingga permukaan air di dalam tabung dinamakan meniskus cekung. Karena adanya meniskus cekung, maka air membasahi dinding kaca.')
        st.write('Jika pada lengkungan air ke atas ditarik garis lurus, maka garis ini akan membentuk sudut $\\theta$ terhadap dinding vertikal. Sudut $\\theta$ ini dinamakan sudut kontak. Sudut kontak air adalah lancip $(0<90°)$')
        left17, cent17, last17 = st.columns(3)
        with cent17:
            st.image('image/Picture38.png', caption='Gambar 21. Raksa dalam tabung kaca. (Sumber: https://rumushitung.com/2013/10/01/sudut-kontak-dan-kapilaritas/)')
        st.write('Raksa dimasukkan ke dalam tabung kaca. Permukaan raksa dalam tabung melengkung ke bawah pada bagian yang menempel di dinding kaca. Pada kasus ini. gaya kohesi (F kohesi) lebih besar dari gaya adhesi (F adhesi). Resultan kedua gaya ini (Fresultan) mengarah ke dalam. Supaya tercapai keseimbangan, maka permukaan raksa yang menempel di dinding kaca harus tegak lurus terhadap gaya F sehingga raksa yang menempel pada dinding kaca melengkung ke bawah. Permukaan raksa pada tabung dinamakan meniskus cembung. Karena meniskus cembung ini raksa tidak membasahi dinding kaca.')
        st.write('Jika pada lengkungan raksa ke bawah ditarik garis lurus maka garis ini akan membentuk sudut $\\theta$ terhadap dinding vertikal. Sudut kontak raksa adalah tumpul $(90°<0<180°)$.')
        left18, cent18, last18 = st.columns(3)
        with cent18:
            st.image('image/Picture39.png', caption= 'Gambar 22. Sudut kontak beberapa pasang bahan. (Sumber: https://www.slideserve.com/kimn/tegangan-permukaan)')
        with st.expander("📺 Video Konsep Kapilaritas" , expanded=False):
            st.video('https://youtu.be/-ISglH02fIU?si=Sgxe7EDQhdl7zzvx')
        with st.expander("📘 Latihan Soal 7" , expanded=False):
            st.write(':grey[Sebuah pipa kapiler dengan jari jari $1$ $mm$ dimasukkan ke dalam air secara vertical, Air memiliki massa jenis $1$ $g/cm^2$ dan tegangan permukaan $1$ $N/m$. Jika sudut kontaknya $60°$ dan percepatan gravitasi, $g=10$ $m/s^2$. Maka hitunglah besarnya kenaikan permukaan air pada dinding pipa kapiler tersebut!]')
            st.text_area('Analisis Jawaban Soal 7')

        # Viskositas
        st.header(':blue[8. VISKOSITAS]')
        left19, cent19, last19 = st.columns(3)
        with cent19:
            st.image('image/Picture40.png', caption='Gambar 23. Peristiwa viskositas. (Sumber: https://id.quora.com/Apakah-oli-yang-di-gunakan-dalam-balapan-yang-resmi-sama-dengan-oli-oli-yang-di-gunakan-masyarakat-pada-umumnya-Jika-berbeda-sejauh-apa-perbedaanya)')
        st.write('Pernahkah kalian melihat cairan yang berbeda kemudian dituangkan secara bersamaan, ternyata ada cairan yang mempunyai aliran lebih cepat dari cairan lainnya. Contohnya, air mempunyai laju aliran yang lebih cepat dibandingkan dengan minyak, gliserin, ataupun etilen glikol. Peristiwa yang bisa diamati adalah ketika masing-masing cairan tersebut diletakkan pada gelas kemudian diaduk secara bersamaan, maka etilen glikol akan lebih cepat berhenti daripada air.')
        st.write('Peristiwa diatas berkaitan dengan Viskositas atau kekentalan. Lalu, bisakah kalian menganalisis bagaimana proses tersebut dapat terjadi?')
        st.write('Viskositas adalah ukuran yang menyatakan kekentalan suatu cairan atau fluida. Viskositas (kekentalan) berasal dari kata Viscous. Suatu bahan apabila dipanaskan sebelum menjadi cair terlebih dahulu menjadi Viscous.')
        st.write('Tingkat kekentalan (Viscositas) suatu fluida dinyatakan oleh koefisien kekentalan fluida tersebut. Jika sebuah bola dijatuhkan ke dalam fluida, maka akan mengalami gaya gesek antara permukaan benda dengan fluida. Gaya gesek ini besarnya sebanding dengan koefisien viskositas fluida. Menurut Stokes, besar gaya tersebut adalah')
        left20, cent20, last20 = st.columns(3)
        with cent20:
            st.image('image/Picture41.png', caption='Gambar 24. Gaya gesek benda dengan fluida. (Sumber: https://pakdosen.co.id/viskositas/)')
        st.latex(r'F = {6}{\pi}{r}{\eta}{v}...............(11)')
        st.write('Keterangan:')
        st.write(r'$$F = \text{Gaya gesekan fluida } \,(N)$$')
        st.write(r'$$\eta = \text{Koefesien viskositas} \,(Pa.s)$$')
        st.write(r'$$r = \text{Jari-jari bola} \,(m)$$')
        st.write(r'$$\pi =\,22/7 \text{ atau } \,3,14$$')
        st.write(r'$$v = \text{Kecepatan gerak benda} \,(m/s)$$')
        st.write('Koefisien viskositas didefinisikan sebagai hambatan pada aliran cairan. Koefisien viskositas dapat ditentukan dengan menggunakan persamaan Poiseuille:')
        st.latex(r'\eta = \frac{2r^2g}{9v} (\rho_b - \rho_f)...............(12)')
        st.write('Keterangan:')
        st.write(r'$$\eta = \text{Koefesien viskositas} \,(Pa.s)$$')
        st.write(r'$$r = \text{Jari-jari bola} \,(m)$$')
        st.write(r'$$v = \text{Kecepatan terminal} \,(m/s)$$')
        st.write(r'$$g = \text{Percepatan gravitasi} \,(m/s^2)$$')
        st.write(r'$$\rho_b = \text{Massa jenis bola} \,(kg/m^3)$$')
        st.write(r'$$\rho_f = \text{Massa jenis fluida} \,(kg/m^3)$$')
        st.write('Agar dapat memahami peristiwa yang berkaitan dengan viskositas diatas, silahkan simak video dibawah ini.')
        with st.expander("📺 Video Konsep Viskositas" , expanded=False):
            st.video('https://youtu.be/ZN01Uht2sn8')
        with st.expander("📘 Latihan Soal 8" , expanded=False):
            st.write(':grey[Sebuah kelereng dengan jari-jari $0,5$ $cm$ jatuh ke dalam bak berisi oli yang memiliki koefisien viskositas $110$ x $10^{-3}$ $N.s/m^2$. Tentukan besar gaya gesek yang dialami kelereng jika bergerak dengan kelajuan $5$ $m/s$!]')
            st.text_area('Analisis Jawaban Soal 8')
        st.markdown('###')
        st.write('---')

        # PBL 3 Membimbing Penyelidikan Mandiri dan Kelompok
        st.info('Langkah PBL ⏩ (3. Membimbing Penyelidikan Mandiri dan Kelompok)')
        st.write('Jakarta, ibu kota Indonesia, sering kali menghadapi banjir yang parah akibat intensitas curah hujan yang tinggi dan sistem drainase yang tidak memadai. Masalah ini memerlukan pemahaman tentang prinsip-prinsip fluida statis untuk menemukan solusi yang efektif.')
        left21, last21 = st.columns(2)
        with left21:
            st.image('studikasus/SK1.jpg', caption ='Studi Kasus 1' )
            st.image('studikasus/PK1.jpg', caption ='Prosedur Kerja 1' )
            st.link_button('Download Studi Kasus 1 🕵️‍♀️', 'https://unjac-my.sharepoint.com/:b:/g/personal/shelvyokvia_1302620035_mhs_unj_ac_id/EcPMW43DbXFIkTnTdwre1JoB0A7QpETvk40nUH8pw0MsIA?e=dIA2Ap')
        with last21:
            st.image('studikasus/SK2.jpg', caption ='Studi Kasus 2')
            st.image('studikasus/PK2.jpg', caption ='Prosedur Kerja 2' )
            st.link_button('Download Studi Kasus 2 🕵️‍♂️', 'https://unjac-my.sharepoint.com/:b:/g/personal/shelvyokvia_1302620035_mhs_unj_ac_id/Ea54HRl4JRpBpq6-Zw9UvlsB59e4d7_-OJka7z0HTs2DdA?e=Le9BIJ')
        st.markdown('###')
        st.write('---')

        # PBL 4 Mengembangkan dan Menyajikan Hasil Karya
        st.info('Langkah PBL ⏩ (4. Mengembangkan dan Menyajikan Hasil Karya)')
        st.write('Setelah melalui proses penyelidikan mandiri dan diskusi kelompok yang mendalam, saatnya kita masuk ke tahap yang sangat penting dalam pembelajaran kita, yaitu mengembangkan dan menyajikan hasil karya. Pada tahap ini, kita akan menggabungkan seluruh pengetahuan, data, dan temuan yang telah kita peroleh untuk menciptakan solusi nyata atas masalah yang kita hadapi. Tidak hanya itu, kita juga akan belajar bagaimana mempresentasikan hasil kerja kita secara efektif dan meyakinkan. Ini adalah kesempatan bagi kalian untuk menunjukkan kreativitas, pemahaman, dan kemampuan analitis dalam mengatasi masalah banjir di Jakarta menggunakan prinsip-prinsip fluida statis yang telah kita pelajari. Mari kita mulai dengan membagi tugas pengembangan karya sesuai dengan kelompok dan kemudian menyusun rencana presentasi yang menarik dan informatif.')
        left22, last22 = st.columns(2)
        with left22:
            st.image('studikasus/P1.png', caption='Gambar 24. Pengembangan dan Penyajian Karya Studi Kasus 1')
            st.link_button("Go to Penyajian Karya Studi Kasus 1", "https://bit.ly/SistemDrainasePengendaliBanjir")
        with last22:
            st.image('studikasus/P2.png', caption='Gambar 25. Pengembangan dan Penyajian Karya Studi Kasus 2')
            st.link_button("Go to Penyajian Karya Studi Kasus 2", "https://bit.ly/PenyaluranAirBersihDiBangunanBertingkat")
        st.markdown('###')
        st.write('---')

        # PBL 5 5. Menganalisis dan Evaluasi Proses Pemecahan Masalah
        st.info('Langkah PBL ⏩ (5. Menganalisis dan Evaluasi Proses Pemecahan Masalah)')
        st.write('Halo para siswa yang saya banggakan. Setelah melalui proses penyelidikan mandiri dan diskusi kelompok yang mendalam, saatnya kita masuk ke tahap yang sangat penting dalam pembelajaran kita, yaitu mengembangkan dan menyajikan hasil karya. Pada tahap ini, kita akan menggabungkan seluruh pengetahuan, data, dan temuan yang telah kita peroleh untuk menciptakan solusi nyata atas masalah yang kita hadapi. Tidak hanya itu, kita juga akan belajar bagaimana mempresentasikan hasil kerja kita secara efektif dan meyakinkan. Ini adalah kesempatan bagi kalian untuk menunjukkan kreativitas, pemahaman, dan kemampuan analitis dalam mengatasi masalah banjir di Jakarta menggunakan prinsip-prinsip fluida statis yang telah kita pelajari. Mari kita mulai dengan membagi tugas pengembangan karya sesuai dengan kelompok dan kemudian menyusun rencana presentasi yang menarik dan informatif. ')
        # Text Input
        name = st.text_input("Name")
        dob = st.date_input("Tanggal Belajar")
        analisis = st.text_area('Analisis Evaluasi Studi Kasus')
        rating = st.slider("Rating Pembelajaran(1-10)", min_value=1, max_value=10, step=1)
        # Checkbox
        agree = st.checkbox("I agree to the terms and conditions")
        st.write(agree)
        # Button to submit form
        if st.button("Submit"):
            # Perform actions with form data, like writing to a database or displaying a confirmation message
            st.success("Form submitted successfully!")
            st.write(name,dob,rating,analisis)
        st.markdown('###')
        st.write('---')

        st.title(':orange[C. RANGKUMAN]')
        st.write('---Terima Kasih Telah Membaca Sampai Akhir---')
        st.link_button('Download Catatan Fluida Statis📘', 'https://unjac-my.sharepoint.com/:b:/g/personal/shelvyokvia_1302620035_mhs_unj_ac_id/Ec85faVfqw1LgwNo4ULanNoBYV4gZC0wR-UVQRzU7rVl3A?e=7wPvh4')

        
        st.title(':orange[D. PENILAIAN DIRI]')
        st.write('Isilah pertanyaan pada tabel di bawah ini sesuai dengan yang kalian ketahui, berilah penilaian secara jujur, objektif, dan penuh tanggung jawab dengan memberi tanda pada kolom jawaban.')
        data_df = pd.DataFrame(
            {
                "Keterangan": ["Saya mengikuti pembelajaran dengan baik", "Saya dapat memahami materi fluida statis dengan baik", "Saya menjadi lebih memahami fluida statis karena studi kasus", "Saya menyukai pembelajaran PBL dalam Fluida Statis"],
                "Ya": [True, True, True, True],
                "Tidak": [False, False, False, False],
            }
        )
        st.data_editor(
            data_df,
            column_config={
                "favorite": st.column_config.CheckboxColumn(
                    "Ya?",
                    help="Select your **favorite** widgets",
                    default=False,
                )
            },
            disabled=["Keterangan"],
            hide_index=True,
        )


            
    with tabs[2]:
        st.write('###### Hai Studies semua, bagaimana materinya apakah kamu masih merasa kesulitan untuk memahami fluida statis? Jangan khawatir, jika studies merasa belum memahami materinya, disini disediakan juga video fluida statisnya, yuk boleh dipelajari kembali materinya dari video, selamat belajar untuk masa depan yang cemerlang studies')
        st.header('Tekanan Zat')
        st.write('Kalian pasti sudah tidak asing lagi dengan Tekanan Zat, jika kalian ingat-ingat kembali, tekanan zat sudah dipelajari saat kamu SMP, untuk dapat mengingatnya kembali, tonton video berikut ini ya. Selamat menonton📺')
        st.video('https://youtu.be/0im6g1Xw3l4?si=URIIHeftLQUR_aBh')
        st.write('*Video Credit:*')
        st.write('*Creator :  Kelikyan*')
        st.write('*All Videos uploaded by and full rights belong to Mr. Klik*')
        st.write('URL : https://youtu.be/0im6g1Xw3l4?si=URIIHeftLQUR_aBh')
        st.markdown('###')
        st.write('---')

        st.header('Hukum Pascal')
        st.write('Video kedua dapat studies lanjutkan tonton setelah menyelasaikan video tekanan zat agar studies dapat memahaminya dengan berurutan, selamat menyaksikan tentang Hukum Pascal studies.')
        st.video('https://youtu.be/li2z8AFR_XY?si=lBj9MOo2nY7seAIy')
        st.write('*Video Credit:*')
        st.write('*Creator :  Kelikyan*')
        st.write('*All Videos uploaded by and full rights belong to Mr. Klik*')
        st.write('URL : https://youtu.be/li2z8AFR_XY?si=hbDOi_Z1wksIdwng')
        st.markdown('###')
        st.write('---')

        st.header('Hukum Archimedes')
        st.write('Bagaimana kedua video diatas studies? Apakah seru untuk menyimak lebih lanjut? Video ketiga ini mengenai Hukum Archimedes tidak kalah seru untuk tonton loh Studies, jangan lupa di klik videonya.  Stay tune studies!')
        st.video('https://youtu.be/6bpfbBxvQOM?si=IHNASCH9oge53u_x')
        st.write('*Video Credit:*')
        st.write('*Creator :  Kelikyan*')
        st.write('*All Videos uploaded by and full rights belong to Mr. Klik*')
        st.write('URL : https://youtu.be/6bpfbBxvQOM?si=IHNASCH9oge53u_x')

        st.markdown('###')
        st.write('---')
