import streamlit as st

st.header("Boston House Price prediction")
crim = st.number_input("crim")
zn = st.number_input("zn")
indus = st.number_input("indus")
chas = st.number_input("chas")
nox = st.number_input("nox")
rm = st.number_input("rm")
age = st.number_input("age")
dis = st.number_input("dis")
rad = st.number_input("rad")
tax = st.number_input("tax")
ptratio = st.number_input("ptratio")
black = st.number_input("black")
istat = st.number_input("istat")



import pickle

# some time later...
 
# load the model from disk
loaded_model = pickle.load(open('boston_models.sav', 'rb'))
#result = loaded_model.score(x_test, y_test)
#print(result)

if st.button("Submit"):
    result = loaded_model.predict([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,black,istat]])
    st.write("The Estimated Price is ",int(result))
