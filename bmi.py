import streamlit as st
import requests
import pandas as pd
from PIL import Image

st.header("Vítej v programu na výpočet BMI, BMR, TDEE")
pohlavi = st.selectbox("Vyber si pohlaví: ", ("muž", "žena"))
vek = st.slider("Vyber si svůj věk: ", 15, 120, 25)
vyska = st.number_input("Napiš svojí výšku v cm: ",value=152, min_value=152,  key = "bmr")
vaha = st.number_input("Napiš svojí hmotnost v kg: ", value = 50, key = "bmr_1")

activity_factor = st.selectbox ("Vyber si svojí faktor aktivity: ", ["sedavý: málo nebo žádné cvičení", "lehce aktivní: cvičit 1-3x/týdne", "mírně aktivní: cvičit 4-5x/týdne", "velmi aktivní: denní nebo intezivní cvičení", "super aktivní: každodenní cvičení nebo fyzická práce"])
#bmi
bmi = vaha / ((vyska / 100) ** 2)
if bmi < 18.5:
    bmi_vysledek = "podváha"
elif 18.5 <= bmi < 25:
    bmi_vysledek = "normální"
elif 25 <= bmi < 30:
    bmi_vysledek = "nadváha"
elif 30 <= bmi < 35:
    bmi_vysledek = ("obézní třída I")
elif 35 <= bmi < 40:
    bmi_vysledek = ("obézní třída II")
elif bmi >= 40:
    bmi_vysledek = ("extrémně obézní")

#bmr
if pohlavi == "muž":
    bmr = round(10*vaha+6.25*vyska-5*vek+5)
elif pohlavi == "žena":
    bmr = round(10*vaha+6.25*vyska-5*vek-161)
#tdee
if activity_factor == "sedavý: málo nebo žádné cvičení":
    tdee = round(bmr*1.2)
elif activity_factor == "lehce aktivní: cvičit 1-3x/týdne":
    tdee = round(bmr*1.37)
elif activity_factor == "mírně aktivní: cvičit 4-5x/týdne":
    tdee = round(bmr*1.55)
elif activity_factor ==  "velmi aktivní: denní nebo intezivní cvičení":
    tdee = round(bmr*1.72)
elif activity_factor == "lehce aktivní: cvičit 1-3x/týdne":
    tdee = round(bmr*1.9)

#ibw
if pohlavi == "muž":
    ibw = round(50 + 0.91 * (vyska - 152.4))
elif pohlavi == "žena":
    ibw = round(45.5 + 0.91 * (vyska - 152.4))
button_vysledek = st.button("Klikni sem pro výsledek: ")
if button_vysledek:
    col1, col2 = st.columns(2)
    col1.metric(label = "Tvůj TDEE je: ",  value = f"{tdee} kcal/den")
    col2.metric(label = "Tvůj BMR je: ", value = f"{bmr} kcal/den")
    col3, col4 = st.columns(2)
    col3.metric(label = "Tvůj BMI je: ", value = bmi_vysledek)
    col4.metric(label = "Tvoje ideální hmotnost: ", value = f"{ibw} kg")

    #st.subheader("Příjem energie pro hubnutí")
    mirny_ubytek_hmotnosti = round(tdee*0.9)
    ztrata_vahy = round(tdee*0.8)
    extremni_ztrata_hmotnosti = round(tdee*0.61)
    hubnuti = ["Mírný úbytek hmotnosti", "Ztráta váhy", "Extrémní ztráta hmotnosti"]
    kalorie_hubnuti = [mirny_ubytek_hmotnosti, ztrata_vahy, extremni_ztrata_hmotnosti]
    df = pd.DataFrame(zip(hubnuti, kalorie_hubnuti))
    df.columns = ["úroveň hubnutí", "kcal/den"]

    #st.subheader("Příjem energie pro přibírání na váze")
    mirny_prirustek_hmotnosti = round(tdee*1.1)
    pribyvani_na_vaze = round(tdee*1.2)
    extremni_narust_hmotnosti = round(tdee*1.39)
    pribirani = ["Mírný přírůstek hmotnosti", "Přibývání na váze", "Extrémní nárůst hmotnosti"]
    kalorie_pribirani = [mirny_prirustek_hmotnosti, pribyvani_na_vaze, extremni_narust_hmotnosti]
    df_1 = pd.DataFrame(zip(pribirani, kalorie_pribirani))
    df_1.columns = ["úroveň přibírání", "kcal/den"]

    col5, col6 = st.columns(2)
    with col5:
        st.subheader("Příjem energie pro hubnutí")
        df
    with col6:
        st.subheader("Příjem energie pro příbírání")
        df_1










