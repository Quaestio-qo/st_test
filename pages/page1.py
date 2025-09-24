import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io

st.title("Анализ чаевых")

path = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
tips = pd.read_csv(path)
st.dataframe(tips)
st.subheader("Зависимость разммера чаевых, от суммы чека")
st.bar_chart(data=tips, x="total_bill", y="tip")

st.subheader("гистограмма общей суммы чека")

fig1, ax1 = plt.subplots()
sns.histplot(data=tips, x="total_bill", ax=ax1)
ax1.set_title("Total bill")
ax1.set_xlabel("Bill")
st.pyplot(fig1)
buffered = io.BytesIO()
plt.savefig(buffered, format="png")
buffered.seek(0)
img_bytes2 = buffered.getvalue()

st.download_button(
    label="скачать", data=img_bytes2, file_name="график2.png", mime="image/png"
)

st.subheader("зависимость суммы чека от дня недели")

fig1, ax1 = plt.subplots()
sns.barplot(data=tips, x="total_bill", hue="day")
st.pyplot(fig1)
buffered = io.BytesIO()
plt.savefig(buffered, format="png")
buffered.seek(0)
img_bytes = buffered.getvalue()

st.download_button(
    label="скачать", data=img_bytes, file_name="график.png", mime="image/png"
)

st.subheader("зависимость суммы чаевых в зависимости от дня недели и пола клиента")
fig1, ax1 = plt.subplots()
sns.barplot(data=tips, x="tip", y="day", hue="sex")
st.pyplot(fig1)
buffered = io.BytesIO()
plt.savefig(buffered, format="png")
buffered.seek(0)
img_bytes1 = buffered.getvalue()

st.download_button(
    label="скачать", data=img_bytes1, file_name="график1.png", mime="image/png"
)
st.balloons()
