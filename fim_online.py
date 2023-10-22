# this is a chatbot to talk about metabolic health

# libraries
import openai # for AI
import streamlit as st # visual interface

# acttivates openAI with the user prompt + predefined expertise as a metabolic health expert
def generate_response(myprompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Your role is to act like a nutrition and health expert. Don't diagnose. Use only peer-reviewed information for your responses. Always provide reading material to build on the information you shared. At the end, ask them when was the last time they visited their physician. ###" + myprompt,
        temperature=.02,
        max_tokens=1024
    )
    return response.choices[0].text.strip()

# gathers user input
def main ():
    st.title("Weekly nutrition and activity plan") # title in the visual interface
    sex_options = ["Female", "Male"]
    diet_options = ["Vegetarian", "Carnivorous"]
    plan_options = ["Diet", "Activity", "Diet & Activity"]
    # form to be submitted
    with st.form("Basic information required"):
        st.write("Basic information required")
        age = st.slider("Approximate age")
        bmi = st.slider("Approximate BMI")
        wt_in_lbs = st.slider("Approximate weight in lbs", min_value=0, max_value=1000)
        # select sex
        sex = st.selectbox('Choose sex at birth:', sex_options)
        # dietary preference
        diet_pref = st.selectbox('Choose dietary preference:', diet_options)
         # dietary preference
        plan_pref = st.selectbox('Choose plan preference:', plan_options)
        #ques = st.text_input('Your question', key = 'Your question')
        checkbox_val = st.checkbox("Form checkbox") 
        submitted = st.form_submit_button("Submit")

    if submitted:
       # join the above information in a single variable to be sent to AI
       myprompt = "I am %d years old %s, my weight is %d lbs and my BMI is %d. My dietary preference in %s. I want to improve my lifestyle. Make a weekly %s plan for me." % (age, sex, wt_in_lbs, bmi, diet_pref, plan_pref)
       st.write(generate_response(myprompt))

if __name__ == "__main__":
    main()