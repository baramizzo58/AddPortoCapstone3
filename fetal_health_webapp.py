import streamlit as st
import pickle

gbc_model = pickle.load(open('gbc_model.pkl','rb'))
knn_model = pickle.load(open('knn_model.pkl','rb'))
lr_model = pickle.load(open('logistic_regression_model.pkl','rb'))
rf_model = pickle.load(open('random_forest_model.pkl','rb'))
svm_model = pickle.load(open('svm_model.pkl','rb'))

def classify(num):
    if num<1.5:
        return 'Normal'
    elif num <2.5:
        return 'Suspect'
    else:
        return 'Pathological'
def main():
    st.title("Streamlit Tutorial")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Fetal Health Classification</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities=['Gradient Boosting', 'K-Nearest Neighbor', 'Logistic Regression', 'Random Forest', 'Support Vector Machine']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    st.subheader(option)
    sl=st.slider('Select Sepal Length', 0.0, 10.0)
    sw=st.slider('Select Sepal Width', 0.0, 10.0)
    pl=st.slider('Select Petal Length', 0.0, 10.0)
    pw=st.slider('Select Petal Width', 0.0, 10.0)
    inputs=[[sl,sw,pl,pw]]
    if st.button('Classify'):
        if option=='Gradient Boosting':
            st.success(classify(gbc_model.predict(inputs)))
        elif option=='K-Nearest Neighbor':
            st.success(classify(knn_model.predict(inputs)))
        elif option=='Logistic Regression':
            st.success(classify(lr_model.predict(inputs)))
        elif option=='Random Forest':
            st.success(classify(rf_model.predict(inputs)))
        else:
           st.success(classify(svm_model.predict(inputs)))


if __name__=='__main__':
    main()
