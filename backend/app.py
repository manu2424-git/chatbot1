from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="../frontend")


# =========================================================
# COURSE / CAREER DATA
# =========================================================

career_data = {

    "bba": {
        "title": "BBA – Bachelor of Business Administration",
        "introduction": "BBA is an undergraduate management course that teaches business, management, finance, marketing and entrepreneurship concepts.",
        "eligibility": "10+2 / Intermediate from a recognized board. Minimum percentage depends on the college.",
        "duration": "3 years",
        "entrance": [
            "CUET",
            "SET",
            "IPMAT",
            "University-specific entrance exams"
        ],
        "careers": [
            "Business Analyst",
            "Marketing Manager",
            "HR Manager",
            "Sales Manager",
            "Operations Manager",
            "Entrepreneur"
        ],
        "higher": [
            "MBA",
            "PGDM",
            "M.Com",
            "Master's in Business Analytics"
        ],
        "skills": [
            "Communication",
            "Leadership",
            "Problem Solving",
            "Business Analysis",
            "Presentation Skills"
        ],
        "government": [
            "UPSC",
            "SSC CGL",
            "Banking Exams",
            "State Government Exams"
        ],
        "salary": "Approximately ₹3 – ₹10 LPA depending on skills, experience and company.",
        "scope": "Good scope in management, marketing, finance, HR, operations and entrepreneurship."
    },


    "b.com": {
        "title": "B.Com – Bachelor of Commerce",
        "introduction": "B.Com is an undergraduate commerce course covering accounting, finance, taxation, economics and business.",
        "eligibility": "10+2 / Intermediate. Commerce background is commonly preferred but requirements vary by institution.",
        "duration": "3 years",
        "entrance": [
            "CUET",
            "University-specific entrance exams",
            "Merit-based admission"
        ],
        "careers": [
            "Accountant",
            "Financial Analyst",
            "Tax Consultant",
            "Auditor",
            "Banking Professional",
            "Business Analyst"
        ],
        "higher": [
            "M.Com",
            "MBA",
            "CA",
            "CMA",
            "CS"
        ],
        "skills": [
            "Accounting",
            "Financial Analysis",
            "Excel",
            "Communication",
            "Numerical Skills"
        ],
        "government": [
            "SSC CGL",
            "Banking Exams",
            "UPSC",
            "State Government Exams"
        ],
        "salary": "Approximately ₹3 – ₹8 LPA for many entry-level roles, varying by role and employer.",
        "scope": "Wide opportunities in accounting, finance, banking, taxation and business."
    },


    "bfa": {
        "title": "BFA – Bachelor of Fine Arts",
        "introduction": "BFA is an undergraduate program focused on visual arts, design, painting, photography and creative practices.",
        "eligibility": "10+2 from a recognized board. Some institutions may conduct an aptitude or practical test.",
        "duration": "3 – 4 years depending on the institution",
        "entrance": [
            "University-specific entrance exams",
            "Art aptitude tests",
            "Portfolio evaluation"
        ],
        "careers": [
            "Graphic Designer",
            "Illustrator",
            "Art Director",
            "Photographer",
            "Animator",
            "UI Designer"
        ],
        "higher": [
            "MFA",
            "Master's in Design",
            "Animation specialization",
            "Digital Arts"
        ],
        "skills": [
            "Creativity",
            "Drawing",
            "Design",
            "Visual Thinking",
            "Digital Tools"
        ],
        "government": [
            "Government Art Departments",
            "Cultural Organizations",
            "Government Design Roles"
        ],
        "salary": "Approximately ₹2.5 – ₹8 LPA initially, depending strongly on portfolio and specialization.",
        "scope": "Career opportunities exist in design, advertising, animation, media, photography and creative industries."
    },


    "b.des": {
        "title": "B.Des – Bachelor of Design",
        "introduction": "B.Des is a design degree covering product, fashion, communication, interaction and digital design.",
        "eligibility": "10+2 from a recognized board. Requirements vary by institution.",
        "duration": "4 years",
        "entrance": [
            "NID DAT",
            "UCEED",
            "NIFT",
            "University-specific entrance exams"
        ],
        "careers": [
            "UI/UX Designer",
            "Product Designer",
            "Graphic Designer",
            "Fashion Designer",
            "Interaction Designer",
            "Design Researcher"
        ],
        "higher": [
            "M.Des",
            "MBA in Design Management",
            "Specialized Design Programs"
        ],
        "skills": [
            "Creativity",
            "Design Thinking",
            "Figma",
            "Problem Solving",
            "Communication"
        ],
        "government": [
            "Government Design Departments",
            "Public Sector Design Roles",
            "Government Media Departments"
        ],
        "salary": "Approximately ₹4 – ₹12 LPA depending on specialization and portfolio.",
        "scope": "Strong opportunities in product companies, technology, fashion, advertising and digital services."
    },


    "mbbs": {
        "title": "MBBS – Bachelor of Medicine and Bachelor of Surgery",
        "introduction": "MBBS is a medical degree that prepares students for careers as doctors and medical professionals.",
        "eligibility": "10+2 with Physics, Chemistry and Biology. Admission requirements are governed by applicable medical admission rules.",
        "duration": "Typically 5.5 years including internship in India.",
        "entrance": [
            "NEET-UG"
        ],
        "careers": [
            "Doctor",
            "Medical Officer",
            "General Physician",
            "Medical Researcher",
            "Clinical Coordinator"
        ],
        "higher": [
            "MD",
            "MS",
            "Diploma / Specialty Programs",
            "Medical Research"
        ],
        "skills": [
            "Clinical Knowledge",
            "Communication",
            "Patient Care",
            "Decision Making",
            "Observation"
        ],
        "government": [
            "Government Hospitals",
            "AIIMS / Central Institutions",
            "State Health Departments",
            "Medical Officer Roles"
        ],
        "salary": "Varies significantly by role, location, specialization and experience.",
        "scope": "Medical practice, hospitals, public health, research and specialization offer multiple career paths."
    },


    "b.tech": {
        "title": "B.Tech – Bachelor of Technology",
        "introduction": "B.Tech is a technical undergraduate degree covering engineering, technology and applied sciences.",
        "eligibility": "10+2 with relevant science subjects. Specific subject and percentage requirements depend on the institution.",
        "duration": "4 years",
        "entrance": [
            "JEE Main",
            "JEE Advanced",
            "State Engineering Entrance Exams",
            "University Entrance Exams"
        ],
        "careers": [
            "Software Developer",
            "Data Analyst",
            "AI Engineer",
            "Cloud Engineer",
            "Cyber Security Analyst",
            "DevOps Engineer"
        ],
        "higher": [
            "M.Tech",
            "MS",
            "MBA",
            "Specialized Certifications"
        ],
        "skills": [
            "Programming",
            "Problem Solving",
            "Logical Thinking",
            "Communication",
            "Technical Skills"
        ],
        "government": [
            "UPSC Engineering Services",
            "SSC",
            "PSUs",
            "State Government Engineering Jobs"
        ],
        "salary": "Approximately ₹4 – ₹15+ LPA depending on specialization, skills and employer.",
        "scope": "Strong opportunities in software, AI, cloud, cybersecurity, data and engineering industries."
    },


    "ca": {
        "title": "CA – Chartered Accountancy",
        "introduction": "Chartered Accountancy is a professional qualification focused on accounting, auditing, taxation and financial management.",
        "eligibility": "Students can enter through the applicable CA Foundation or graduate-entry route under ICAI rules.",
        "duration": "Varies depending on entry route, exam attempts and training completion.",
        "entrance": [
            "CA Foundation",
            "CA Intermediate",
            "CA Final"
        ],
        "careers": [
            "Chartered Accountant",
            "Auditor",
            "Tax Consultant",
            "Financial Analyst",
            "Finance Manager",
            "Risk Consultant"
        ],
        "higher": [
            "CFA",
            "CPA",
            "MBA",
            "Specialized Finance Certifications"
        ],
        "skills": [
            "Accounting",
            "Numerical Skills",
            "Financial Analysis",
            "Taxation",
            "Attention to Detail"
        ],
        "government": [
            "Government Finance Departments",
            "Public Sector Organizations",
            "Audit-related Government Roles"
        ],
        "salary": "Varies widely by qualification, experience, specialization and employer.",
        "scope": "Opportunities exist in audit, taxation, finance, consulting, banking and corporate management."
    },


    "mba": {
        "title": "MBA – Master of Business Administration",
        "introduction": "MBA is a postgraduate management degree covering business strategy, finance, marketing, operations and leadership.",
        "eligibility": "Graduation from a recognized institution. Entrance requirements vary by institution.",
        "duration": "Usually 2 years",
        "entrance": [
            "CAT",
            "XAT",
            "CMAT",
            "MAT",
            "GMAT",
            "University-specific exams"
        ],
        "careers": [
            "Business Analyst",
            "Product Manager",
            "Marketing Manager",
            "Finance Manager",
            "HR Manager",
            "Operations Manager"
        ],
        "higher": [
            "PhD",
            "Executive MBA",
            "Specialized Management Programs"
        ],
        "skills": [
            "Leadership",
            "Communication",
            "Business Analysis",
            "Decision Making",
            "Presentation"
        ],
        "government": [
            "UPSC",
            "Banking",
            "PSUs",
            "Government Management Roles"
        ],
        "salary": "Varies greatly based on institution, specialization, experience and employer.",
        "scope": "Opportunities span consulting, technology, finance, marketing, operations, HR and entrepreneurship."
    },


    "b.sc": {
        "title": "B.Sc – Bachelor of Science",
        "introduction": "B.Sc is an undergraduate science degree with specializations such as computer science, mathematics, physics, chemistry and biology.",
        "eligibility": "10+2 with relevant subjects. Requirements depend on specialization and institution.",
        "duration": "3 years in many Indian universities",
        "entrance": [
            "CUET",
            "University-specific exams",
            "Merit-based admission"
        ],
        "careers": [
            "Data Analyst",
            "Research Assistant",
            "Lab Technician",
            "Software Developer",
            "Statistician",
            "Science Educator"
        ],
        "higher": [
            "M.Sc",
            "MCA",
            "MBA",
            "Research Programs"
        ],
        "skills": [
            "Analytical Thinking",
            "Research",
            "Numerical Skills",
            "Problem Solving",
            "Technical Skills"
        ],
        "government": [
            "SSC",
            "Banking",
            "Research Institutions",
            "State Government Jobs"
        ],
        "salary": "Approximately ₹3 – ₹8 LPA for many entry-level roles, varying by specialization.",
        "scope": "Scope depends strongly on specialization and can include research, technology, analytics, education and industry roles."
    },



    "diploma": {
        "title": "Diploma Courses – Polytechnic / Diploma Programs",
        "introduction": "Diploma courses are practical and career-oriented programs that provide technical and professional skills in areas such as Computer Engineering, Mechanical Engineering, Civil Engineering, Electrical Engineering and other specializations.",
        "eligibility": "Usually 10th / SSC pass for polytechnic diploma courses. Eligibility and admission rules vary by state, board and institution.",
        "duration": "Usually 3 years after 10th. Some diploma programs may have different durations.",
        "entrance": [
            "State Polytechnic Entrance Exams",
            "Merit-based admission",
            "Institution-specific admission"
        ],
        "careers": [
            "Junior Engineer",
            "Diploma Engineer",
            "Computer Technician",
            "CAD Designer",
            "Site Supervisor",
            "Electrical Technician",
            "Mechanical Technician",
            "Web / Software Support Technician"
        ],
        "higher": [
            "B.Tech / B.E. through lateral entry",
            "Advanced Diploma",
            "Specialized Certification Courses",
            "Skill Development Programs"
        ],
        "skills": [
            "Technical Skills",
            "Problem Solving",
            "Practical Knowledge",
            "Computer Skills",
            "Communication",
            "Industry-specific Skills"
        ],
        "government": [
            "Junior Engineer Jobs",
            "Railway Jobs",
            "SSC Technical Jobs",
            "State Government Technical Jobs",
            "PSU Technical Jobs"
        ],
        "salary": "Approximately ₹2.5 – ₹7 LPA for many entry-level roles, depending on specialization, skills, experience and employer.",
        "scope": "Diploma courses provide strong practical skills and can lead to technical jobs, government opportunities, industry careers or B.Tech/B.E. lateral-entry programs."
    },


    "upsc": {
        "title": "UPSC Civil Services Examination",
        "introduction": "UPSC Civil Services Examination is a competitive examination for recruitment to several civil services of the Government of India.",
        "eligibility": "A bachelor's degree from a recognized university is generally required. Age and attempt rules depend on category and applicable UPSC rules.",
        "duration": "Preparation commonly takes 1–3 years, but varies by candidate.",
        "entrance": [
            "UPSC CSE Preliminary Examination",
            "UPSC CSE Main Examination",
            "Personality Test / Interview"
        ],
        "careers": [
            "IAS",
            "IPS",
            "IFS",
            "IRS",
            "Other Central Civil Services"
        ],
        "higher": [
            "Foundation Training",
            "Departmental Training",
            "Specialized Government Training"
        ],
        "skills": [
            "Current Affairs",
            "General Knowledge",
            "Analytical Thinking",
            "Writing",
            "Communication",
            "Decision Making"
        ],
        "government": [
            "Indian Administrative Service",
            "Indian Police Service",
            "Indian Foreign Service",
            "Indian Revenue Service"
        ],
        "salary": "Government pay varies by service, level and allowances under applicable pay rules.",
        "scope": "Civil services offer administrative, policy, public service and leadership responsibilities."
    }
}


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


# =========================================================
# CHAT API
# =========================================================

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({
            "response": "Please enter a course or career name."
        })

    user_message = data["message"].lower().strip()

    # Exact / partial matching
    found_course = None

    for key in career_data:

        if key in user_message:
            found_course = key
            break

    # Extra keyword matching
    if not found_course:

        if "computer" in user_message or "engineering" in user_message:
            found_course = "b.tech"

        elif "doctor" in user_message or "medical" in user_message:
            found_course = "mbbs"

        elif "business" in user_message:
            found_course = "bba"

        elif "commerce" in user_message:
            found_course = "b.com"

        elif "design" in user_message:
            found_course = "b.des"

        elif "fine arts" in user_message:
            found_course = "bfa"

        elif "chartered accountant" in user_message:
            found_course = "ca"

        elif "management" in user_message:
            found_course = "mba"

        elif "science" in user_message:
            found_course = "b.sc"

        elif "civil services" in user_message:
            found_course = "upsc"

        elif "diploma" in user_message or "polytechnic" in user_message:
            found_course = "diploma"

    if found_course:

        course = career_data[found_course]

        return jsonify({
            "found": True,
            "course": course
        })

    return jsonify({
        "found": False,
        "response": "Sorry, I could not find that course. Try BBA, B.Com, BFA, B.Des, MBBS, B.Tech, CA, MBA, B.Sc, Diploma or UPSC."
    })


# =========================================================
# RUN SERVER
# =========================================================

if __name__ == "__main__":
    app.run(debug=True)