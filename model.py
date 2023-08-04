import pickle
import joblib

from streamlit_option_menu import option_menu
import streamlit as st



filename = 'finalized_model.sav'
  
# load the model
load_model = joblib.load(open(filename, 'rb'))

#pickle.load(open('/Users/Machine Learning/Insurance Price/finalized_model.sav',encoding="utf8"))

pred = load_model.predict([[23,0,23,0,0]])



st.set_page_config(page_title="Health Insurance Price Prediction Model",
                   page_icon=":tada:", layout="wide")


with st.sidebar:
    selected = option_menu('Health Insurance Price Prediction Model',
                           ['Home Page',
                            'Health Insurance Price Prediction',
                            'Contact Me'],
                           icons=['house', 'currency-dollar', 'person-rolodex'],
                           default_index=0)

if (selected == 'Home Page'):
    st.header("Health Insurance Price Prediction")
    st.write("This project aims to help individuals estimate their health insurance costs using a machine learning model. The model takes into account various factors such as age, gender, BMI, number of children, and smoking habits to provide an estimate of the insurance premium.🤖🌐")

    st.header("Dataset")
    st.write("The dataset used for training and testing the model is not included in this repository. However, the model was trained on a dataset that contains relevant features such as age, gender, BMI, number of children, and smoking status, along with corresponding insurance prices")


    st.header("Launching the Streamlit Web Application")
    st.write("The Streamlit application has the following main sections:")
    st.subheader("Home Page")
    st.write("The landing page of the web application displays the title 'Health Insurance Price Prediction.' It serves as an introduction to the application.")
    st.subheader("Health Insurance Price Prediction")
    st.write("This section allows users to input their information to predict their potential health insurance costs. Users can provide details such as age, gender, BMI, number of children, and smoking habits. Clicking the 'Predict Price' button will display the estimated insurance cost based on the provided information. 🧮💰")

    st.subheader("Contact Me")
    st.write("This section provides contact information for getting in touch with the developer or project owner.")
    st.write("Please note that the accuracy of the model is based on the dataset available during model training. For real-world predictions, the accuracy may vary.")


if (selected == 'Health Insurance Price Prediction'):

    st.header("Health Insurance Price Prediction")
    st.write("Enter the Following Details !!")

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Enter your Age", 10, 100)
        children = st.number_input("No. of Childerns:" , 0, 3)
        # restecg = st.number_input("resting electrocardiographic results (values 0,1,2)", 0, 2)
        # oldpeak = st.number_input("ST depression induced by exercise relative (0-5)", 0, 5)
        # thal = st.number_input("3=Normal; 6=fixed defect; 7=reversable defect", 3, 7)
    with col2:
        sex=st.selectbox("Select Gender",
                     options=["Male","Female"])
        smoker=st.selectbox("Are you a Smoker",
                     options=["Yes","No"])# thalach = st.number_input("Maximum Heart Rate Achieved (100-180)", 100, 180)
        # slope = st.number_input("the slope of the peak exercise ST segment (0-2)", 0, 2)
    with col3:
        bmi = st.number_input(label="Enter the Body Mass Index (BMI)", format="%.2f")
        # fasting_sugar = st.number_input("fasting blood sugar > 120 mg/dI", 120, 300)
        # exang = st.number_input("exercise induced angina (0,1)", 0, 1)
        # ca = st.number_input("number of major vessels (0-3) colored by flourosopy", 0, 3)
    if sex=="Male":
        sex=0
    elif sex=="Female":
        sex=1

    if smoker=="Yes":
        smoker=1
    elif smoker=="No":
        smoker=0

    if st.button('Predict Price'):
        pred = load_model.predict([[age, sex, bmi,children,smoker]])
        st.subheader("The Insurance Cost is Rs: ")
        st.success(pred)
        # if (pred[0] == 0):
        #     st.success(
        #         "The Person is Fit and does Not have any Heart Disease")
        #     st.write("Accuracy of Model is %")
        #     # st.write("Accuracy of Model is", r2,"%")
        # else:
        #     st.success("The Person is suffering from Heart Disease")
        #     st.write("Accuracy of Model is  %")

        #     # st.write("Accuracy of Model is", r2,"%")


if (selected == 'Contact Me'):
    # def contact_form():
    st.header("Contact Me")
    st.write("Please fill out the form below to get in touch with me.")

    # Input fields for user's name, email, and message
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message", height=150)

    # Submit button
    if st.button("Submit"):
        if name.strip() == "" or email.strip() == "" or message.strip() == "":
            st.warning("Please fill out all the fields.")
        else:

            send_email_to = 'kumawatharsh2004@email.com'
            st.success("Your message has been sent successfully!")

# Main application
    # def main():
    #     # Display the Contact Me form
    #     contact_form()

    # if __name__ == "__main__":
    #     main()


footer = """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: grey;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/harsh-kumawat-069bb324b/" target="_blank">Harsh</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)






if (pred[0] == 0):
    print("The Person is Fit and does Not have any Heart Disease")
            # st.write("Accuracy of Model is ", ac, " %")
            # st.write("Accuracy of Model is", r2,"%"
else:
    print("The Person is suffering from Heart Disease")
            # st.write("Accuracy of Model is ", ac, " %")

