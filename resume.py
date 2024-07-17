# resume.py

from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "Styles" / "main.css"
resume_file = current_dir / "Assets" / "Ali Sher Afzal CV.pdf"
profile_pic = current_dir / "Assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ali Sher Afzal"
PAGE_ICON = ":grey crown:"


#---TITLE AND DESCRIPTIOON---
NAME = "ALi Sher Afzal"
DESCRIPTION = """
Software Engineering at Information Technology University, Python developer, C++ developer, problem solver and analytical thinker.
"""
EMAIL = "alisherafzal87@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ali-sher-afzal-457902282/",
    "GitHub": "https://github.com/BSSE23007",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write("---")
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("Email", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# ---EDUCATION---
st.header("Education")
st.write("---")
st.write(""" 
- **Information Technology Universiy**  
*Bachelor's of science in Software Engineering*  
joined 2023-present
""")
st.write("""
- **Forman Christian College**  
*Intermediate | Fsc pre-engineering*  
Degree: 2021-2023
""")
st.write("""
- **American Lycetuff School**  
*Matriculation | Major: Science*  
Degree: 2019-2021
""")


# ---Experience Section---
st.header("Project & Experience")
st.write("---")
st.subheader("Sugar Mill Management System")
st.write("""  
*Developed a comprehensive mill management system to streamline operations and enhance productivity.*  
*Implemented the following functionalities:*  
- ►	Employee Management: Oversee employee records, attendance, salaries, and roles.
- ►	Inventory Management: Monitor and replenish inventory of raw materials, products, and packaging.
- ►	Production Management: Supervise production processes, batch tracking, and quality control.
- ►	Sales and Distribution: Manage unique sales transactions, orders, invoicing, and delivery tracking.
- ►	Financial Tracking: Track revenue, expenses, profit margins, and cash flow; generate financial reports.
- ►	Reporting and Analytics: Produce and analyze reports on production, sales, inventory, and financial performance

""")
st.subheader("Mall Management System")
st.write("""  
*Created a mall management system to oversee the operations of a shopping mall.*  
*Implemented the following functionalities:*  
- ► HRMS: Manage employee records, attendence , schedules, access control, and security
- ► Parking: Assign parking slots, track vehicle data, display statistics, and manage parking revenue.
- ► Cinema: Track tickets, manage seating/timings, assign movies to halls, and display details.
- ► Play Area: Administer passes, recharge balances, manage games, and provide real-time updates on play areas.
- ► Shops: Maintain shop records, streamline rentals, and offer ERP for small retailers.
- ► Finance: Oversee finances, manage bills and salaries, track profits, and generate detailed reports.


""")
st.subheader("Backend Software of ERP for a Clothing Brand ")
st.write("""  
*Implemented the following functionalities:*  
- ►	Created 3 ends for Admin, Customer, and Employee 1
- ►	Maintenance of inventory, track inventory products , stock management
- ►	Calculating Bill , making invoices and calculating Profit/Loss
- ►	Maintenance of employee shifts, attendence , payrolls , hiring


""")
st.subheader("ERP System")
st.write("""  
*Designed and implemented an ERP system to integrate various business processes.*  
*Implemented the following functionalities:*  
- ►	Finance and accounting modules
- ►	Human resources management
- ►	Supply chain and logistics management
- ►	Customer relationship management (CRM)
""")

# ---Hard skills---
st.header("Hard skills")
st.write("---")
st.write("""
- ►	Overleaf LaTeX
- ►	C++ language
- ►	python language
- ►	Microsoft Office
- ►	GitHub
""")

# ---Soft skills---
st.header("Soft skills")
st.write("---")
st.write("""
- ►	Communication skills
- ►	Project management / leadership
- ►	Problem-solving
- ►	Analytical thinking
- ►	Team collaboration
- ►	Time management
      
""")

#---Interest---
st.header("Interests")
st.write("---")
st.write("""
- ►	Book Reading
- ►	Meeting new people
- ►	Photography
- ► Walking
""")

# ---Certifications Section---
st.header("Certifications")
st.write("---")
st.write("""
- ► Project management with Jira
- ► International Kangaroo Mathematics Contest
- ► Mathematics Hunt
""")

# ---Language Section---
st.header("Language")
st.write("---")
st.write("""
- ► English
- ► Urdu
- ► Punjabi
""")
