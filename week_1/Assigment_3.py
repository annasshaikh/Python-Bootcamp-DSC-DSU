import time
anthum = "Pak sarzameen shad bad,Kishwar-e-Haseen shad bad ,Tou Nishaan-e-Azm-e-aali shan ,Arz-e-Pakistan ,Markaz-e-yaqeen Shad bad,Pak sarzameen ka nizaam Qouwat-e-Akhouwat-e-Awam ,Qaum mulk saltanat ,Painda tabinda bad Shad bad Manzil-e-murad ,Parcham-e-Sitara-o-Hilall ,Rahbar-e-Tarakkeey-o-Kamal ,Tarjuman-e-mazee-shaan-e-Hal Jan-e-Istaqbal ,Saaya-e-Khuda-e-zuljalal"
x = anthum.split(",")
for i in range(0,len(x),1):
    print(x[i])
    time.sleep(1)