import streamlit as st
from resume_generator import generate_resume



st.title(":blue[AI powered Resume Builder] :pencil:")
st.subheader(":red[Just enter your details and a few clicks to go!!]", divider="violet")
st.write("")


st.subheader(":blue[**Personal information**]", divider="grey")
name = st.text_input("*Full name*")
contact = st.text_area("Contact information (Phone No., Email)")

#add address with divider
st.write("")


st.subheader(":blue[Educational Qualifications]", divider="gray")
education = st.text_area("List your educational qualifications")
st.write("")


st.subheader(":blue[Work Experience]", divider="gray")
experience = st.text_area("Describe your work experience")
st.write("")


st.subheader(":blue[Skills]", divider="gray")
skills = st.text_area("List your skills")
st.write("")


st.subheader("Additional Information", divider="gray")
additional = st.text_area("Include certifications, hobbies, etc. (optional)")
st.write("")

if st.button("Generate resume"):
      if name and contact and education and skills:
            file_path = generate_resume(name, contact, education, experience, skills, additional)
            st.success("***Resume generated successfully!***")
            with open(file_path, "rb") as file:
                st.download_button(
                label="Download Resume",
                data=file,
                file_name="resume.pdf",
                mime="application/pdf"
            )
      else:
        st.error("**Please fill out all required fields.**")