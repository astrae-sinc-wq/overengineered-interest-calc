import streamlit as st
import pandas as pd
from math import log, ceil

st.set_page_config(page_title="Калькулятор відсотків", page_icon="📈")
st.title("🦐Калькулятор строку накопичення🦐")

mode = st.radio("Тип відсотку",["Складний відсоток", "Простий відсоток"])
col1, col2, col3 = st.columns(3)

with col1:
    start_sum = st.number_input("Початкова сума", min_value=1.0, value = 100000.0, step = 1000.0)
with col2:
    target_sum = st.number_input("Цільова сума", min_value=start_sum + 1.0, value = 200000.0, step = 1000.0)
with col3:
    rate = st.number_input("Річний відсоток (%)", min_value = 0.1, value = 10.0, step = 0.5)

if st.button("Розрахувати"):
    r = rate
    if "Складний відсоток" in mode:
        years_float = log(target_sum / start_sum) / log(1 + r)
    else:
        years_float = (target_sum - start_sum) / (start_sum * r)

    years = ceil(years_float)
    st.success(f"Знадобится років: **{years}**(Точне значення**{years_float:.2f}**)")

    data = []
    current = start_sum
    
    for year in range (years + 1):
        data.append({"Рік" : year, "Сума" : round(current, 2)})
        if "Складний відсоток" in mode:
            current += current * r
        else:
            current += start_sum * r

    df = pd.DataFrame(data)
    st.line_chart(df.set_index("Рік"))

