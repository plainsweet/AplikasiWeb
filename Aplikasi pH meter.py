import streamlit as st


st.image("https://im.ezgif.com/tmp/ezgif-1-5234bc31f5.jpg", width=600)

st.title('Aplikasi penentuan pH suatu larutan')
st.markdown('''Hai users, selamat datang di web kami.
Aplikasi ini dapat digunakan untuk teman-teman yang sedang mengerjakan analisis dengan parameter penentuan nilai pH dari suatu larutan atau sampel.''')


tombol=st.button('OLEH KELOMPOK 2')
if tombol:
    st.write('Latifa Andjani')
    st.write('Muhamad Faris Adzikri')
    st.write('Raka Mulya Octama')
    st.write('Rakhmillah Fatikhannisa Ramadhiani')
    st.write('Siti Nurhaliza')
    
tab1, tab2, tab3, tab4, tab5 = st.tabs(["pH scale", "Equipment", "How to", "About pH", "Penentuan nilai pH"])

with tab1:
    st.header("pH scale")
    st.image("https://mesinionisasiair.com/images/blog/skalaph.jpg", width=500)
    
with tab2:
    st.header("Equipment")
    st.write('Berikut adalah alat-alat yang dapat digunakan untuk mengukur pH suatu larutan:')
    st.image("https://annindonesia.files.wordpress.com/2018/07/digital-ph-meter-side-view-with-beaker-h12002_1.jpg?w-365&h=365", width=350, caption='pH meter')
    st.image("https://bisakimia.com/wp-content/uploads/2016/09/strip-indikator-ph-e-14-indikator-universal-1369429984-0-1-jpg.jpeg", width=350, caption='pH universal')
    st.image('https://3.bp.blogspot.com/-Aqcbj2ZpWHB/W-ucQMzNwhI/AAAAAAAAE/twxE7HT6tгAHrzqax7sXUAJSTIxoU85gCLcBGAs/s1600/kertas lakmus.JPG',width=350, caption='kertas lakmus')
             
with tab3:
    st.header("How to use the equipment")
    st.write('''A. pH Meter:
1. Disiapkan sampel yang akan di ukur kadar pHnya (letakkan dalam wadah).
2. Dinyalakan dengan menekan tombol on pada pH meter.
3. Dimasukkan pH meter ke dalam wadah yang berisi sampel/larutan yang akan di uji.
4. Ditunggu hingga angka tersebut berhenti dan tidak berubah-ubah.
5. Hasil akan terlihat di display digital.
B. pH universal:
1. Disiapkan sampel yang akan di ukur kadar pHnya (letakkan dalam wadah).
2. Dimasukkan pH universal kedalam larutan yang akan di uji.
3. Dibandingkan dengan skala yang terdapat pada tempat kertas pH universal
4. Didapatkan pH dari larutan tersebut
C. Kertas Lakmus:
Kertas lakmus hanya dapat mengetahui apakah suatu larutan tersebut basa atau asam. Kita tidak dapat mengetahui berapa pH dari larutan tersebut.
''')
             
with tab4:
    st.header("Informasi Tambahan")
             
    st.write('pH merupakan derajat keasaman yang digunakan untuk menyatakan tingkat keasaman atau kebasaan yang dimiliki oleh suatu larutan yang didefinisikan sebagai kologartitma aktivitas ion hidrogen (H+) yang terlarut. Koefisien aktivitas ion hidrogen tidak dapat diukur secara eksperimental, sehingga nilainya didasarkan pada perhitungan teoritis. Skala pH bukanlah skala absolut melainkan bersifat relatif.')
    st.write('Asam adalah larutan dengan pH dibawah 7. Menurut teori asam basa bronsted-lowry, asam didefinisikan sebagai zat yang mendonorkan proton [H+]. Asam kuat adalah larutan dengan pH rendah yang terionisasi secara sempurna dalam air. Asam kuat memiliki pH dibawah 3, tidak seperti asam lemah.Asam lemah hanya menyumbangkan sedikit ion hidrogennya atau hanya sekitar satu persennya yang terionisasi.')
    st.write('Basa kuat dan basa lemah adalah larutan yang memiliki pH diatas 7. Menurut teori asam basa bronsted-lowry, basa didefinisikan sebagai zat yang akseptor proton [H+]. Basa kuat adalah basa yang terionisasi secara sempurna kedalam air. Ketika larut dalam air, setiap molekul basa kuat akan melepas ion hidroksida (OH-). Basa kuat memiliki pH yang tinggi, biasanya lebih besar dari 11. Untuk basa lemah adalah larutan basa yang tidak terionisasi secara sempurna disalam air. Basa lemah memiliki pH sekitar 8 hingga 11')
     
    import pandas as pd
    st.write('Beberapa contoh larutan serta jenisnya')
    data={'Nama larutan':['HCl','NaOH','Pb(OH)2','HNO3','HClO3','Cu(OH)2','LiOH','H2C2O4','RbOH','Ba(OH)2','H3PO4','CH3COOH','KOH','H2SO4','H2O2','NaHCO3','HBO3','HBr','HClO4','Fe(OH)2','NH4OH','H2CO3','Zn(OH)2'],
          'Jenis larutan':['Asam kuat','Basa kuat','Basa lemah','Asam kuat','Asam kuat','Basa lemah','Basa kuat','Asam lemah','Basa kuat','Basa kuat','Asam lemah','Asam lemah','Basa kuat','Asam kuat','Asam lemah','Basa lemah','Basa lemah','Asam kuat','Asam kuat','Basa lemah','Basa lemah','Asam lemah','Basa lemah']}
    
    df=pd.DataFrame(data)
    
    df
    
with tabs5:
    st.header('Penentuan nilai pH')
    
    NamaLarutan= st.text_input('Nama Larutan yang akan dihitung pH-nya:')
    
    st.write ('Silahkan pilih jenis larutan dengan format "asam kuat", "basa kuat", "asam lemah", "basa lemah"')
    
    option= st.selectbox(
    'Jenis Larutan',
    ("asam kuat", "basa kuat", "asam lemah", "basa lemah"))
    
   if option=="asam kuat":
        jumlah_digit=4
        cons = st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')
       jumlah_digit1=0
        val = st.number_input(f'Masukkan valensi larutan', format='%.'+str(jumlah_digit)+'f')
       H=cons*val
        import numpy as np
       pH = -1 * np.log10(H)
        st.write('pH Larutan', NamaLarutan, 'yang merupakan', option, 'adalah', pH)
        
elif option=="basa kuat": 
    jumlah_digit=4 
    cons= st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')
   jumlah_digit1=0 
    val = st.number_input(f'Masukan valensi larutan', format='%.'+str(jumlah_digit)+'f')
    OH=cons*val 
    import numpy as np 
    POH= -1 np* log10(OH) 
    pH=14-pOH
    st.write('pH larutan', Namalarutan, 'yang merupakan',option, 'adalah', pH)

elif option=="asam lemah": 
    jumlah digit-4
    cons=st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')
   jumlah_digit1=6 
    ka = st.number_input(f'Masukan ka dari larutan', format='%.' +str(jumlah_digit1)+"F")
    a = cons*ka 
    import numpy as np
    H = np.sqrt(a)
    pH=-1 np.log10(H)
    st.write('pH larutan', Namalarutan, "yang merupakan", option, "adalah", pH)
    
elif option=="basa lemah": 
    jumlah digit-4
    cons=st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')
   jumlah_digit1=6
    kb = st.number_input(f'Masukan ka dari larutan', format='%.' +str(jumlah_digit1)+"F")
    b = cons*kb
    import numpy as np
    OH = np.sqrt(a)
    рOH -1 * np.log10(OH)
    pH=14-POH
    st.write('pH larutan', Namalarutan, "yang merupakan", option, "adalah", pH)

st.image("https://im.ezgif.com/tmp/ezgif-1-aa9ca3526a.jpg",width=500)