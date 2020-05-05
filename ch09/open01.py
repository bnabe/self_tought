st = open("st.txt", "w")
st.write("Hi, from Python!")
st.close()

st = open("st_j.txt", "w", encoding="utf-8")
st.write("Pythonからこんにちは!")
st.close()
