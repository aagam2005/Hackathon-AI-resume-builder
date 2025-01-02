from resume_generator import generate_resume

# Mock data
name = "John Doe"
contact = "Email: john.doe@example.com\nPhone: +1-123-456-7890\nLinkedIn: linkedin.com/in/johndoe"
education = "B.Sc. in Computer Science\nXYZ University, 2018-2022\nGPA: 3.8/4.0"
experience = "Software Developer Intern\nABC Corp, Summer 2021\n- Developed features for the company's flagship product.\n- Wrote automated tests to ensure code quality.\n\nFreelance Web Developer\n2020-2021\n- Built and maintained websites for small businesses."
skills = "Python, Java, HTML, CSS, JavaScript, React, SQL, Git"
additional = "Hackathon Winner (2021)\nVolunteered at Local Animal Shelter\nFluent in Spanish and French"

# Generate resume
file_name = generate_resume(name, contact, education, experience, skills, additional)

print(f"Resume generated successfully: {file_name}")