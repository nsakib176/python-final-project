def main_menu():
    print("\nWelcome to the University of Petra (UOP) Chatbot!")
    print("Are you a:")
    print("1. Student")
    print("2. Visitor")
    choice = input("Please enter your choice (1-2): ")

    if choice == '1':
        student_menu()
    elif choice == '2':
        visitor_menu()
    else:
        print("Invalid choice, please try again.")
        main_menu()

# Student menu where students will be asked for their ID and password
def student_menu():
    print("\n-- Student Menu --")

# Visitor menu with 4 grouped categories
def visitor_menu():
    print("\n-- Visitor Menu --")
    print("Please choose a category:")
    
    print("1. University Information")
    print("2. Admission & Academics")
    print("3. Campus Life & Services")
    print("4. Contact & General Information")
    print("5. Go Back to Main Menu")
    
    choice = input("Please enter your choice (1-5): ")
    
    if choice == '1':
        university_info_menu()
    elif choice == '2':
        admission_academics_menu()
    elif choice == '3':
        campus_life_services_menu()
    elif choice == '4':
        contact_general_info_menu()
    elif choice == '5':
        main_menu()
    
    else:
        print("Invalid choice, please try again.")
        visitor_menu()

# Sub-menu for University Information
def university_info_menu():
    print("\n-- University Information --")
    print("1. Prospective Students")
    print("2. Success Stories")
    print("3. Academic Calendar")
    print("4. International Student Guide")
    print("5. All Events")
    print("6. Go Back")
    print("7. Main Menu")
    
    choice = input("Please enter your choice (1-6): ")
    
    if choice == '1':
        prospective_students()
    elif choice == '2':
        success_stories()
    elif choice == '3':
        academic_calendar()
    elif choice == '4':
        international_student_guide()
    elif choice == '5':
        all_events()
    elif choice == '6':
        visitor_menu()
    elif choice == '7':
            main_menu()

    else:
        print("Invalid choice, please try again.")
        university_info_menu()

# Sub-menu for Admission & Academics
def admission_academics_menu():
    print("\n-- Admission & Academics --")
    print("1. Courses and Tuition Fees")
    print("2. Academic Grants")
    print("3. Online Admission Application")
    print("4. Go Back")
    print("5. Main Menu")
    
    choice = input("Please enter your choice (1-4): ")
    
    if choice == '1':
        courses_and_tuition()
    elif choice == '2':
        academic_grants()
    elif choice == '3':
        online_admission_application()
    elif choice == '4':
        visitor_menu()
    elif choice == '5':
            main_menu()

    else:
        print("Invalid choice, please try again.")
        admission_academics_menu()

# Sub-menu for Campus Life & Services
def campus_life_services_menu():
    print("\n-- Campus Life & Services --")
    print("1. Female Student Housing")
    print("2. Transportation")
    print("3. Deanship of Student Affairs")
    print("4. Student Guide")
    print("5. UOP Map")
    print("6. Go Back")
    print("7. Main menu")
    
    choice = input("Please enter your choice (1-6): ")
    
    if choice == '1':
        female_student_housing()
    elif choice == '2':
        transportation()
    elif choice == '3':
        deanship_of_student_affairs()
    elif choice == '4':
        student_guide()
    elif choice == '5':
        uop_map()
    elif choice == '6':
        visitor_menu()
    elif choice == '7':
            main_menu()
    else:
        print("Invalid choice, please try again.")
        campus_life_services_menu()

# Sub-menu for Contact & General Information
def contact_general_info_menu():
    print("\n-- Contact & General Information --")
    print("1. Contact UOP")
    print("2. Vacancies")
    print("3. Q&A")
    print("4. Financial Information")
    print("5. Go Back")
    print("6. Main menu")
    
    choice = input("Please enter your choice (1-5): ")
    
    if choice == '1':
        contact_uop()
    elif choice == '2':
        vacancies()
    elif choice == '3':
        qna()
    elif choice == '4':
        financial_information()
    elif choice == '5':
        visitor_menu()
    elif choice == '6':
            main_menu()
    else:
        print("Invalid choice, please try again.")
        contact_general_info_menu()

# Function for Female Student Housing Info
def female_student_housing():
    print("\n-- Female Student Housing --")
    print("""
    The female students’ dormitory is located on campus and offers a variety of rooms for the highest level of safety, well-being, and privacy. It includes 119 single-bed rooms, 11 double-bed rooms, and 72 penthouse apartments (studio).

    Some advantages offered to residents:
    - 24/7 supervision by educational staff
    - Free parking
    - Hot water, heating, transportation
    - Clinics, laundry rooms, gym, billiard room

    Regular Semester Rents for 2023-2024:
    - Penthouse Apartment: 1150 JOD
    - Large Single-bed Room: 1050 JOD
    - Small Single-bed Room: 950 JOD
    - Double-bed Room: 750 JOD

    Dormitory rents for the summer semester are 50% of the regular semester rents.

    Specific rules apply, such as signing a compliance agreement with a guardian, paying required fees on time, adhering to regulations, and maintaining proper conduct.

    For detailed information or inquiries, you can visit the Deanship of Student Affairs or contact the housing supervisor.
    """)
    back_to_menu()

# Placeholder functions for other options (can be updated with more details)
def prospective_students():
    print( """
    Welcome, future students of the University of Petra!

    As one of the leading universities in Jordan, UOP is dedicated to providing high-quality education with a focus on innovation, research, and student development.

    Why Choose UOP?
    - Established in 1991, UOP has a reputation for academic excellence, both locally and internationally.
    - We offer 40+ majors and programs across 9+ faculties, ensuring a wide range of study opportunities.
    - Multiculturalism is a core value, with over 1,265 international students from various countries, creating a diverse and inclusive campus environment.
    - Our alumni network boasts 17,997+ graduates, many of whom are now leaders in their respective fields.

    Academic Programs:
    UOP offers a variety of undergraduate and postgraduate programs. Our programs are designed to meet the demands of today’s global job market. You can explore:
    - Science and Engineering
    - Business and Economics
    - Arts and Design
    - Pharmacy and Medical Sciences
    - And many more!

    To view the full list of programs and learn more about each, visit the Majors and Programs section.

    Admission Process:
    1. Online Application: Submit your application through our easy-to-use online portal.
    2. Required Documents: Be ready to submit your high school certificates (Tawjihi or equivalent), personal ID, and any other required documents.
    3. Tuition Fees: You can find information about our affordable tuition fees and various scholarships and grants available to new students.

    Scholarships and Grants:
    UOP offers various scholarships based on merit and financial need. You may qualify for:
    - Academic Excellence Scholarships
    - Sports and Cultural Talent Scholarships
    - Financial Aid for Students in Need

    Campus Life:
    Life at UOP is vibrant and full of activities. We offer:
    - Student Clubs and Societies
    - State-of-the-art Facilities including sports centers, libraries, and labs
    - Dormitories for both local and international students, including a safe and secure female dormitory on campus.
    - Transportation Services

    For more details, visit the Courses and Tuition Fees section or contact the admissions office.

    """)
    
    back_to_menu()

def success_stories():
    print("Success stories of UOP alumni...")
    print( """
    Success Stories of University of Petra Alumni:

    At the University of Petra, we are proud of our alumni who have gone on to achieve great success in their respective fields. Here are a few inspiring stories of graduates who have made their mark in the world:

    1. **Dr. Ayman Zahran - Class of 2005 (Pharmacy)**:
       Dr. Zahran is now a leading researcher in the field of pharmaceutical sciences and has developed new treatments for chronic diseases. His dedication to improving health outcomes globally has earned him numerous awards.

    2. **Sara Khalil - Class of 2012 (Computer Science)**:
       Sara is a software engineer at a top tech company in Silicon Valley. She credits UOP for helping her develop the skills she needed to excel in a competitive industry. Sara is also an advocate for women in technology and regularly mentors young women pursuing tech careers.

    3. **Omar Al-Masri - Class of 2010 (Business Administration)**:
       Omar is the CEO of a successful international logistics company. Under his leadership, the company expanded its operations to more than 15 countries, creating thousands of job opportunities in the process.

    4. **Leila Al-Hussein - Class of 2018 (Architecture)**:
       Leila has gained recognition for her innovative and sustainable building designs. Her projects are now being constructed in various parts of the Middle East, and she has been featured in multiple architectural magazines.

    5. **Ahmad Youssef - Class of 2014 (Journalism and Media)**:
       Ahmad is an award-winning journalist working for a major international news outlet. He has covered key global events, shedding light on important social and political issues.

    These are just a few examples of the many success stories from UOP. Our graduates excel in various fields, from business and healthcare to engineering and the arts. We are committed to continuing to nurture future leaders and innovators.

    Do you want to learn more about our programs and how you can become part of this success? Visit the Majors and Programs section or contact our Admissions Office.
    """)
    back_to_menu()

def academic_calendar():
    print("UOP academic calendar...")
    print( """
    University of Petra - Academic Calendar Fall Semester 2024/2025:

    1. **Early Registration for Fall Semester**: August 4, 2024
    2. **Start of Faculty Members' Duty**: September 29, 2024
    3. **Add/Drop Period**: October 6 - October 10, 2024
    4. **Last Registration Date for Old Students**: October 10, 2024
    5. **Start of Classes**: October 13, 2024
    6. **Orientation Week for New Students**: October 13 - October 17, 2024
    7. **First Late Registration Period (Old Students, 50 JOD Fine)**: October 13 - October 17, 2024
    8. **First Withdrawal Period (25% of Fees Deducted)**: October 13 - October 31, 2024
    9. **Second Late Registration Period (Old Students, 100 JOD Fine)**: October 20, 2024
    10. **Last Date to Review Final Grades (Spring and Summer 2023/2024)**: October 24, 2024
    11. **Second Withdrawal Period (50% of Fees Deducted)**: November 3 - November 14, 2024
    12. **First Exam Period**: November 10 - November 21, 2024
    13. **Compulsory Withdrawal Period (100% of Fees Deducted)**: November 17, 2024 - January 16, 2025
    14. **Midterm Exams**: November 23 - December 14, 2024
    15. **Comprehensive Exam Date**: November 24 - December 5, 2024
    16. **Early Registration for Spring Semester**: December 1, 2024
    17. **Second Exam Period**: December 22, 2024 - January 2, 2025
    18. **Last Date for Thesis Defense**: January 2, 2025
    19. **Bachelor Graduation Project Discussions**: January 12 - January 16, 2025
    20. **Last Date to Submit Committee Decisions for Discussions**: January 16, 2025
    21. **Last Day of Classes for Fall Semester**: January 16, 2025
    22. **Final Exam Period**: January 18 - February 1, 2025
    23. **Al-Isra and Mi'raj Holiday**: January 27, 2025
    24. **Last Date to Submit Final Theses with Committee Recommendations**: January 30, 2025
    25. **Student Break Between Semesters**: February 2 - February 27, 2025
    26. **Last Date to Submit Grades to the Admissions and Registration Office**: February 4, 2025
    27. **Last Date to Review Graduating Students' Grades**: February 6, 2025
    28. **Council of Deans' Decision on Granting Degrees**: February 13, 2025
    """)
    back_to_menu()

def international_student_guide():
    print("Guide for international students...")
    print("""
    University of Petra - International Student Guide

    Welcome to the University of Petra (UOP)! We are excited to have students from over 30 different nationalities join our community. Below is a guide to help international students navigate life at UOP and in Jordan.

    1. **Admissions and Visa Requirements**:
       - International students must meet the same academic requirements as local students.
       - A valid student visa is required to study at UOP. The university assists international students with the visa application process. It is essential to apply for your visa as early as possible.
    
    2. **Housing Options**:
       - UOP offers on-campus housing for female students. The dormitory provides a safe and comfortable environment, with furnished rooms and various amenities.
       - Off-campus housing is also available for both male and female students, and the university can provide recommendations for nearby apartments.

    3. **Language of Instruction**:
       - The primary language of instruction at UOP is Arabic. However, some programs are offered in English, especially in faculties like Business, Engineering, and Information Technology.
       - Arabic language courses are available for international students to help them improve their language skills.

    4. **Student Support Services**:
       - UOP provides a variety of support services for international students, including academic advising, counseling, and career services.
       - The Deanship of Student Affairs offers help with adapting to Jordanian culture and university life.

    5. **Cultural Experience**:
       - UOP promotes multiculturalism, encouraging students from different backgrounds to share their cultures and experiences.
       - Students can participate in cultural activities, clubs, and events organized by the university to celebrate diversity.

    6. **Health and Safety**:
       - UOP has a clinic on campus that provides healthcare services to students.
       - The university takes student safety seriously and has measures in place to ensure a secure environment for all students.

    7. **Transportation**:
       - UOP offers transportation services to help students get to and from the campus. Buses are available during official working hours.
       - For those staying off-campus, public transportation and taxis are also readily available in Amman.

    8. **Arrival in Jordan**:
       - International students arriving at Queen Alia International Airport can request airport pickup service through the Deanship of Student Affairs. Be sure to inform the university of your arrival details at least two days in advance.

    9. **Important Contacts**:
       - **International Student Office**: +962-6-5799555
       - **Deanship of Student Affairs**: +962-6-5799555 ext. 2000
       - **Visa Office**: visaoffice@uop.edu.jo

    We hope your time at the University of Petra is enriching both academically and culturally. Our community is here to support you every step of the way!
    """)
    back_to_menu()

def all_events():
    print("Upcoming events at UOP...")
    print("""
    University of Petra - Upcoming Events

    Stay updated with all the exciting events happening at UOP! Below is a list of upcoming events for the academic year 2024/2025:

    1. **Orientation Week for New Students**:
       - **Date**: October 13th - 17th, 2024
       - **Description**: A week full of activities to welcome new students to the university. Meet fellow students, get to know the campus, and join in various workshops and social events.

    2. **International Day Celebration**:
       - **Date**: November 10th, 2024
       - **Description**: Celebrate the diversity of cultures at UOP! This event showcases food, music, and traditions from around the world. Students from over 30 nationalities will participate.

    3. **UOP Job Fair**:
       - **Date**: November 25th, 2024
       - **Description**: Meet with potential employers, network with industry professionals, and attend career development workshops. Open to all students and alumni.

    4. **Research and Innovation Conference**:
       - **Date**: December 5th - 6th, 2024
       - **Description**: Presentations and discussions on the latest trends in research and innovation. Faculty members, researchers, and students are welcome to join.

    5. **Sports Day**:
       - **Date**: January 15th, 2025
       - **Description**: A day filled with various sports activities and competitions. Participate in football, basketball, and other sporting events or cheer on your friends!

    6. **Graduation Ceremony**:
       - **Date**: February 13th, 2025
       - **Description**: Celebrate the achievements of our graduating class. The ceremony will be followed by a reception for graduates and their families.

    7. **Spring Festival**:
       - **Date**: March 20th, 2025
       - **Description**: A lively festival to welcome the spring season. Enjoy live music, food stalls, and fun activities around campus.

    For more information on these events or to register, please contact the Deanship of Student Affairs at +962-6-5799555 ext. 2000, or visit the UOP events page on our website.

    Stay tuned for updates on additional events throughout the academic year!
    """)
    back_to_menu()

def courses_and_tuition():
    print("Welcome to the Courses and Tuition Information.")
    
    while True:
        major_type = input("Select your major type:\n1. Bachelors\n2. Masters\n3. Go back to main menu\nEnter 1, 2 or 3: ")

        if major_type == '1':
            while True:
                faculty = input("Select your faculty:\n1. Faculty of Administrative & Financial Sciences\n"
                                "2. Faculty of Arts & Sciences\n"
                                "3. Faculty of Information Technology\n"
                                "4. Faculty of Architecture & Design\n"
                                "5. Faculty of Law\n"
                                "6. Faculty of Pharmacy & Medical Sciences\n"
                                "7. Faculty of Mass Communication\n"
                                "8. Faculty of Engineering\n"
                                "9. Faculty of Dentistry\n"
                                "10. Go back to major type menu\nEnter the faculty number (1-10): ")

                # Bachelors programs
                if faculty == '1':
                    print("1. Business Administration (Bachelors)\n132 Credit Hours, 60% Minimum Average, 80 JOD Credit Hour Fee")
                    print("2. Banking and Finance (Bachelors)\n132 Credit Hours, 60% Minimum Average, 80 JOD Credit Hour Fee")
                    print("3. Accounting (Bachelors)\n132 Credit Hours, 60% Minimum Average, 85 JOD Credit Hour Fee")
                    print("4. Digital Marketing (Bachelors)\n132 Credit Hours, 60% Minimum Average, 80 JOD Credit Hour Fee")
                    print("5. E-Business & Commerce (Bachelors)\n132 Credit Hours, 60% Minimum Average, 80 JOD Credit Hour Fee")
                    print("6. Business Intelligence and Data Analysis (Bachelors)\n132 Credit Hours, 60% Minimum Average, 70 JOD Credit Hour Fee")
                    print("7. Financial Technology (Bachelors)\n132 Credit Hours, 60% Minimum Average, 70 JOD Credit Hour Fee")
                    print("8. Supply Chains Management and Logistics Sciences (Bachelors)\n132 Credit Hours, 60% Minimum Average, 60 JOD Credit Hour Fee")

                elif faculty == '2':
                    print("1. Arabic Language & Literature (Bachelors)\n135 Credit Hours, 60% Minimum Average, 30 JOD Credit Hour Fee")
                    print("2. English Language & Literature (Bachelors)\n135 Credit Hours, 60% Minimum Average, 80 JOD Credit Hour Fee")
                    print("3. English Language / Translation (Bachelors)\n135 Credit Hours, 60% Minimum Average, 80 JOD Credit Hour Fee")
                    print("4. French Language, English Language & Literature (Bachelors)\n135 Credit Hours, 60% Minimum Average, 80 JOD Credit Hour Fee")
                    print("5. Applied English (Bachelors)\n135 Credit Hours, 60% Minimum Average, 80 JOD Credit Hour Fee")
                    print("6. Class Teacher (Bachelors)\n135 Credit Hours, 60% Minimum Average, 30 JOD Credit Hour Fee")
                    print("7. Early Childhood (Bachelors)\n135 Credit Hours, 60% Minimum Average, 30 JOD Credit Hour Fee")
                    print("8. Chemistry (Bachelors)\n132 Credit Hours, 60% Minimum Average, 55 JOD Credit Hour Fee")
                    print("9. Mathematics (Bachelors)\n132 Credit Hours, 60% Minimum Average, 55 JOD Credit Hour Fee")
                    print("10. Physical Education (Bachelors)\n135 Credit Hours, 60% Minimum Average, 40 JOD Credit Hour Fee")

                elif faculty == '3':
                    print("1. Software Engineering (Bachelors)\n133 Credit Hours, 60% Minimum Average, 90 JOD Credit Hour Fee")
                    print("2. Computer Science (Bachelors)\n134 Credit Hours, 60% Minimum Average, 80 JOD Credit Hour Fee")
                    print("3. Data Science & Artificial Intelligence (Bachelors)\n133 Credit Hours, 60% Minimum Average, 70 JOD Credit Hour Fee")
                    print("4. Information Security (Bachelors)\n133 Credit Hours, 60% Minimum Average, 80 JOD Credit Hour Fee")
                    print("5. Virtual and Augmented Reality (Bachelors)\n133 Credit Hours, 60% Minimum Average, 80 JOD Credit Hour Fee")

                elif faculty == '4':
                    print("1. Architecture (Bachelors)\n165 Credit Hours, 80% Minimum Average, 120 JOD Credit Hour Fee")
                    print("2. Interior Design (Bachelors)\n143 Credit Hours, 60% Minimum Average, 100 JOD Credit Hour Fee")
                    print("3. Graphic Design (Bachelors)\n137 Credit Hours, 60% Minimum Average, 100 JOD Credit Hour Fee")
                    print("4. Animation & Multimedia (Bachelors)\n137 Credit Hours, 60% Minimum Average, 100 JOD Credit Hour Fee")
                    print("5. Digital Film Design Technology (Bachelors)\n140 Credit Hours, 60% Minimum Average, 65 JOD Credit Hour Fee")

                elif faculty == '5':
                    print("1. Law (Bachelors)\n141 Credit Hours, 65% Minimum Average, 60 JOD Credit Hour Fee")

                elif faculty == '6':
                    print("1. Pharmacy (Bachelors)\n164 Credit Hours, 80% Minimum Average, 120 JOD Credit Hour Fee")
                    print("2. Clinical Nutrition and Diets (Bachelors)\n136 Credit Hours, 70% Minimum Average, 60 JOD Credit Hour Fee")
                    print("3. Medical Analysis (Bachelors)\n136 Credit Hours, 70% Minimum Average, 60 JOD Credit Hour Fee")

                elif faculty == '7':
                    print("1. Journalism & Digital Media (Bachelors)\n135 Credit Hours, 60% Minimum Average, 70 JOD Credit Hour Fee")
                    print("2. Digital Promotional Media (Bachelors)\n135 Credit Hours, 60% Minimum Average, 70 JOD Credit Hour Fee")
                    print("3. Radio & Television (Bachelors)\n135 Credit Hours, 60% Minimum Average, 70 JOD Credit Hour Fee")

                elif faculty == '8':
                    print("1. Civil Engineering (Bachelors)\n160 Credit Hours, 80% Minimum Average, 60 JOD Credit Hour Fee")

                elif faculty == '9':
                    print("1. Doctor in Dentistry and Oral Surgery (Bachelors)\n214 Credit Hours, 85% Minimum Average, 250 JOD Credit Hour Fee for Jordanian and Palestinian students\n"
                          "300 JOD Credit Hour Fee for International Students")

                elif faculty == '10':
                    break  # Go back to major type menu

                else:
                    print("Invalid selection. Please try again.")

                # Ask if the user wants to go back to the faculty selection menu or exit
                go_back = input("Do you want to go back to the faculty selection menu (type 'b') or return to the main menu (type 'm')? ").strip().lower()
                if go_back == 'b':
                    return courses_and_tuition()
                elif go_back == 'm':
                    return main_menu()
                else:
                    print("Invalid input. Please type 'b' to go back to the faculty selection menu or 'm' to return to the main menu.")
               
        elif major_type == '2':
            while True:
                faculty = input("Select your faculty for Masters:\n1. Faculty of Administrative & Financial Sciences\n"
                                "2. Faculty of Arts & Sciences\n"
                                "3. Faculty of Architecture & Design\n"
                                "4. Faculty of Law\n"
                                "5. Faculty of Pharmacy & Medical Sciences\n"
                                "6. Faculty of Mass Communication\n"
                                "7. Faculty of Engineering\n"
                                "8. Go back to major type menu\nEnter the faculty number (1-8): ")

                # Masters programs
                if faculty == '1':
                    print("1. Business Administration - MBA (Master)\n33 Credit Hours, Good Minimum Average, 175 JOD Credit Hour Fee")
                    print("2. Digital Marketing (Master)\n33 Credit Hours, Good Minimum Average, 150 JOD Credit Hour Fee")

                elif faculty == '2':
                    print("1. English Language / Translation (Master)\n33 Credit Hours, Good Minimum Average, 150 JOD Credit Hour Fee")
                    print("2. Arabic Language & Literature (Master)\n33 Credit Hours, Good Minimum Average, 80 JOD Credit Hour Fee")
                    print("3. Chemistry (Master)\n33 Credit Hours, Good Minimum Average, 100 JOD Credit Hour Fee")
                    print("4. Mathematics (Master)\n33 Credit Hours, Good Minimum Average, 80 JOD Credit Hour Fee")
                    print("5. Curricula & E-Learning (Master)\n33 Credit Hours, Good Minimum Average, 80 JOD Credit Hour Fee")

                elif faculty == '3':
                    print("1. Interior Design (Master)\n33 Credit Hours, Good Minimum Average, 200 JOD Credit Hour Fee")
                    print("2. Sustainable Smart Cities (Master)\n33 Credit Hours, Good Minimum Average, 180 JOD Credit Hour Fee")

                elif faculty == '4':
                    print("1. Laws (Master)\n33 Credit Hours, Good Minimum Average, 90 JOD Credit Hour Fee")

                elif faculty == '5':
                    print("1. Pharmaceutical Sciences (Master)\n33 Credit Hours, Good Minimum Average, 150 JOD Credit Hour Fee")
                    print("2. Food and Nutrition (Master)\n33 Credit Hours, Good Minimum Average, 90 JOD Credit Hour Fee")

                elif faculty == '6':
                    print("1. Journalism and Digital Media (Master)\n33 Credit Hours, Good Minimum Average, 160 JOD Credit Hour Fee")

                elif faculty == '7':
                    print("1. Engineering Project Management (Master)\n33 Credit Hours, Good Minimum Average, 125 JOD Credit Hour Fee")

                elif faculty == '8':
                    break  # Go back to major type menu
                else:
                    print("Invalid selection. Please try again.")

                # Ask if the user wants to go back to the faculty selection menu or exit
                go_back = input("Do you want to go back to the faculty selection menu (type 'b') or return to the main menu (type 'm')? ").strip().lower()
                if go_back == 'b':
                    return courses_and_tuition()
                elif go_back == 'm':
                    return main_menu()
                else:
                    print("Invalid input. Please type 'b' to go back to the faculty selection menu or 'm' to return to the main menu.")

        elif major_type == '3':

            back_to_menu()


def academic_grants():
    
        print("\nAcademic Grants Information:")
        print("\nImportant Note: Students majoring in Doctor of Dental Surgery and Supply Chain Management and Logistics Science are not eligible for any grants offered by the university.\n")
        
        grant_type = input("Select the type of academic grant:\n"
                           "1. Excellence Grants for High School Examination\n"
                           "2. Academic Excellence Grants\n"
                           "3. Visit UOP Regulations Guide for Technical Excellence, Sports Excellence, and Employment Scholarships\n"
                           "4. Go back to main menu\n"
                           "Enter your choice (1-4): ")

        if grant_type == '1':
            print("\nExcellence Grants for High School Examination:")
            print("Eligibility: Jordanian or Palestinian high school diploma holders who are Jordanian or Palestinian nationals.")
            print("\nFaculties of Pharmacy & Medical Sciences, Architecture & Design, Engineering:")
            print("Tawjihi Average    | Awarded Grant")
            print("95%+                | 50%")
            print("90% to 94.9%        | 25%\n")
            print("Other Faculties:")
            print("Tawjihi Average    | Awarded Grant")
            print("95%+                | 100%")
            print("90% to 94.9%        | 50%")
            print("85% to 89.9%        | 25%\n")
            print("The grant covers the entire academic year, including the Summer Semester. Conditions apply based on the student's GPA.\n")

        elif grant_type == '2':
            print("\nAcademic Excellence Grants:")
            print("The University provides students who achieve academic excellence with a grant that applies to the tuition fees of the next semester.")
            print("CGPA (4.00)         | Awarded Grant")
            print("4.00                | 100%")
            print("3.89 – 3.99         | 50%")
            print("3.67 – 3.88         | 25%\n")
            print("To be awarded this grant for the first time, students must have completed 30 credit hours and maintained a GPA of at least 3.67.\n")

        elif grant_type == '3':
            print("\nPlease visit the UOP Regulations Guide to learn more about:")
            print("- Technical Excellence Scholarships")
            print("- Sports Excellence Scholarships")
            print("- Employment Scholarships\n")
        
        elif grant_type == '4':
            print("Returning to the main menu...\n")
            back_to_menu()

        else:
            print("Invalid selection. Please try again.\n")
        
        go_back = input("Do you want to go back to the faculty selection menu (type 'b') or return to the main menu (type 'm')? ").strip().lower()
        if go_back == 'b':
            return academic_grants()
        elif go_back == 'm':
            return main_menu()
        else:
            print("Invalid input. Please type 'b' to go back to the faculty selection menu or 'm' to return to the main menu.")

    

def online_admission_application():
    print("Welcome to the University of Petra Online Admission Application Assistant!")
    print("This chatbot will guide you through the application process.\n")

    # Navigation stack to manage back navigation
    navigation_stack = []

    def check_eligibility():
        print("Step 1: Eligibility Requirements")
        eligibility = input("Have you reviewed the eligibility requirements for your desired major? (yes/no) or type 'b' to return: ").strip().lower()
        if eligibility == 'b':
            return visitor_menu()
        elif eligibility == 'no':
            print("Please review the admissions requirements for your chosen faculty and program on the university’s website before proceeding.\n")
            return 'end'
        elif eligibility == 'yes':
            print("Great! Let's continue with the application process.\n")
            return 'application_steps'
        else:
            print("Invalid input. Please type 'yes', 'no', or 'back'.\n")
            return 'check_eligibility'

    def application_steps():
        print("Step 2: Main Steps for the Online Admission Application")
        print("1. Create an account on the University of Petra admission portal.")
        print("2. Complete the online application form.")
        print("3. Upload all required documents, including transcripts and identification.")
        print("4. Pay the application fee through the secure online payment gateway.")
        print("5. Submit your application for review.")
        
        proceed = input("Would you like to start the application process now? (yes/no) or type 'b' to return: ").strip().lower()
        if proceed == 'b':
            return visitor_menu()
        elif proceed == 'yes':
            print("\nPlease proceed to the official University of Petra admission portal to create your account and begin the application.")
            print("https://edugate.uop.edu.jo/faces/ui/pages/guest/admissionOnline/index.xhtml")
            return 'end'
        elif proceed == 'no':
            print("No problem! If you need assistance with any part of the process, we're here to help.")
            print("Thank you for your interest in the University of Petra.\n")
            return 'end'
        else:
            print("Invalid input. Please type 'yes', 'no', or 'b'.\n")
            return 'application_steps'

 
    current_page = 'check_eligibility'
    while current_page != 'end':
        navigation_stack.append(current_page)
        
        if current_page == 'check_eligibility':
            current_page = check_eligibility()
        elif current_page == 'application_steps':
            current_page = application_steps()
        elif current_page == 'main_menu' and navigation_stack:
            navigation_stack.pop()  # Go back to the previous page
            if navigation_stack:
                current_page = navigation_stack.pop()  # Set to the last visited page
            else:
                current_page = 'end'
    back_to_menu()



def transportation():
    print("University of Petra - Transportation Services")
    print("\nChoose an option to learn more:")
    print("1. Available Routes")
    print("2. Fees and Payment")
    print("3. Timings and Schedule")
    print("4. Contact Information")
    print("5. Go Back")
    print("6. Main menu")

    choice = input("Enter the number of your choice: ").strip().lower()

    if choice == '1':
        print("\nAvailable Routes:")
        print("The University of Petra provides transportation services across major cities and areas, including Amman, Zarqa, and Irbid. All routes are planned for optimal convenience and coverage.")
        
    
    elif choice == '2':
        print("\nFees and Payment:")
        print("Transportation fees are 100 JOD per semester, which covers daily transportation to and from the university. Payment is due at the start of each semester and can be made online through the UOP portal.")
        
    
    elif choice == '3':
        print("\nTimings and Schedule:")
        print("Buses operate from 6:00 AM to 6:00 PM. Morning trips start at 6:00 AM, and evening trips depart the campus at 4:30 PM. Please arrive 10 minutes before the scheduled departure time.")
        
    
    elif choice == '4':
        print("\nContact Information:")
        print("For any transportation inquiries, please contact the UOP Transportation Office at: 06-123-4567 or email transport@uop.edu.jo.")
        
    
    elif choice == '5':
        visitor_menu()
        
    elif choice == '6':
            main_menu()

    else:
        print("Invalid input. Please enter a number from 1 to 6.")
        return transportation()
    go_back = input("Do you want to go back to the faculty selection menu (type 'b') or return to the main menu (type 'm')? ").strip().lower()
    if go_back == 'b':
        return transportation()
    elif go_back == 'm':
        return main_menu()
    else:
        print("Invalid input. Please type 'b' to go back to the faculty selection menu or 'm' to return to the main menu.")
    
    back_to_menu()

def deanship_of_student_affairs():
    print("University of Petra - Deanship of Student Affairs")
    print("\nSelect an option to learn more:")
    print("1. Mission and Vision")
    print("2. Student Services and Support")
    print("3. Clubs and Extracurricular Activities")
    print("4. Counseling and Guidance")
    print("5. Contact Information")
    print("Type 'back' to return to the main menu.")

    choice = input("Enter the number of your choice: ").strip().lower()

    if choice == '1':
            print("\nMission and Vision:")
            print("The Deanship of Student Affairs at the University of Petra is committed to enriching students' experiences by providing diverse resources, support, and extracurricular activities. The mission is to foster personal growth, promote academic excellence, and create a vibrant community on campus.\n")

    elif choice == '2':
            print("\nStudent Services and Support:")
            print("The Deanship offers various services, including academic advising, career counseling, health services, and access to the university’s facilities. These services aim to support students’ well-being and enhance their academic and personal experiences.\n")

    elif choice == '3':
            print("\nClubs and Extracurricular Activities:")
            print("The Deanship oversees a wide range of student clubs, from sports teams to cultural and academic groups. Students are encouraged to participate in these activities to develop new skills, network, and enjoy a balanced student life.\n")

    elif choice == '4':
        print("\nCounseling and Guidance:")
        print("Professional counselors are available to provide guidance and support on academic, personal, and emotional issues. Counseling services are confidential and aim to help students navigate challenges and maximize their potential.\n")

    elif choice == '5':
        print("\nContact Information:")
        print("For inquiries or support, please contact the Deanship of Student Affairs at: 06-123-4568 or email studentaffairs@uop.edu.jo.\n")

    elif choice == 'back':
        print("\nReturning to the main menu.\n")
        
    else:
        print("Invalid input. Please enter a number from 1 to 5 or 'back' to return.\n")

    back_to_menu()

def student_guide():
    print("University of Petra - Student Guide")
    print("\nSelect an option to learn more:")
    print("1. Academic Policies")
    print("2. Campus Facilities")
    print("3. Code of Conduct")
    print("4. Health and Wellness")
    print("5. Contact Student Affairs")
    print("Type 'back' to return to the main menu.")


    choice = input("Enter the number of your choice: ").strip().lower()

    if choice == '1':
            print("\nAcademic Policies:")
            print("The University of Petra has a set of academic policies covering attendance, grading, and academic integrity. Students are encouraged to review these policies to ensure they meet academic expectations and maintain a successful academic journey.\n")

    elif choice == '2':
            print("\nCampus Facilities:")
            print("The university offers a wide range of facilities, including a library, labs, gym, cafeterias, and study rooms. These facilities are available to all students to support their academic and personal development.\n")

    elif choice == '3':
            print("\nCode of Conduct:")
            print("All students are expected to adhere to the university's code of conduct, which promotes respect, honesty, and responsibility. Violations of the code can lead to disciplinary actions.\n")

    elif choice == '4':
            print("\nHealth and Wellness:")
            print("The university provides health and wellness resources, including medical services, mental health counseling, and wellness programs to help students manage stress and maintain a healthy lifestyle.\n")

    elif choice == '5':
            print("\nContact Student Affairs:")
            print("For further assistance or inquiries, students can contact Student Affairs at: 06-123-4567 or email studentguide@uop.edu.jo.\n")

    elif choice == 'back':
            print("\nReturning to the main menu.\n")
           
    else:
            print("Invalid input. Please enter a number from 1 to 5 or 'back' to return.\n")


    back_to_menu()



def uop_map():
    print("\nYou can view the map usnig the following link: ")
    print("https://www.uop.edu.jo/Ar/PublishingImages/University-of-Petra-Campus-Master-Plan2022-L-en.png")
    back_to_menu()

def contact_uop():
    print("\nYou can contact us at: ")
    print("WhatsApp: 00962791152410")
    print("Landline: 0096265799555")
    print("Mobile: 00962796677755")
    print("Fax: 0096265715570")
    print("Email: info@uop.edu.jo")
    back=input(print("Type 'back' to return to the main menu."))
    if back == 'back':
        print("\nReturning to the main menu.\n")
        
    else:
        print("Invalid input. \n")
    back_to_menu()

def vacancies():
    print("University of Petra - Job Vacancies")
    print("\nWelcome to the Job Vacancies section. Here you can find available job opportunities at the University of Petra.")
    print("We encourage students to apply for positions that suit their skills and interests.")
    print("For more details about each vacancy, please check the university's official website.")
    print("\nAvailable Job Vacancies:")
    print("1. Administrative Assistant")
    print("2. Research Assistant")
    print("3. Teaching Assistant")
    print("4. IT Support")
    print("5. Library Staff")
    print("6. Internship Opportunities")
    print("Type 'back' to return to the main menu.")

   
    choice = input("\nEnter the number of your choice for more information or type 'back' to return: ").strip().lower()

    if choice == '1':
            print("\nAdministrative Assistant:")
            print("Responsibilities include supporting administrative tasks, managing schedules, and assisting with office operations.\n")
            print("To apply, visit:https://www.uop.edu.jo/En/HRD/Announcements/Pages/default.aspx\n") 

    elif choice == '2':
            print("\nResearch Assistant:")
            print("Research Assistants assist faculty members in conducting research projects and preparing reports.\n")
            print("To apply, visit:https://www.uop.edu.jo/En/HRD/Announcements/Pages/default.aspx\n") 

    elif choice == '3':
            print("\nTeaching Assistant:")
            print("Teaching Assistants help professors with classroom management, grading, and student support.\n")
            print("To apply, visit:https://www.uop.edu.jo/En/HRD/Announcements/Pages/default.aspx\n") 

    elif choice == '4':
            print("\nIT Support:")
            print("IT Support staff provide technical assistance to students and faculty, troubleshoot issues, and maintain computer systems.\n")
            print("To apply, visit: https://www.uop.edu.jo/En/HRD/Announcements/Pages/default.aspx\n") 

    elif choice == '5':
            print("\nLibrary Staff:")
            print("Library Staff assist in managing library resources, helping students with research inquiries, and organizing events.\n")
            print("To apply, visit: https://www.uop.edu.jo/En/HRD/Announcements/Pages/default.aspx\n") 

    elif choice == '6':
            print("\nInternship Opportunities:")
            print("Internships are available in various departments, providing valuable work experience and skill development.\n")
            print("To apply, visit: https://www.uop.edu.jo/En/HRD/Announcements/Pages/default.aspx\n")  

    elif choice == 'back':
            print("\nReturning to the main menu.\n")
           

    else:
            print("Invalid input. Please enter a number from 1 to 6 or 'back' to return.\n")


    back_to_menu()  

def qna():
    print("University of Petra - Q&A Section")
    print("\nWelcome to the Q&A section. Here you can find answers to frequently asked questions.")
    print("If your question is not listed, please contact the university directly.")
    print("\nFrequently Asked Questions:")
    print("1. What are the admission requirements?")
    print("2. How can I apply for scholarships?")
    print("3. What is the academic calendar?")
    print("4. How can I contact my academic advisor?")
    print("5. Where can I find information about student activities?")
    print("Type 'back' to return to the main menu.")

  
    choice = input("\nEnter the number of your question for more information or type 'back' to return: ").strip().lower()

    if choice == '1':
            print("\nAdmission Requirements:")
            print("To apply for admission to the University of Petra, you need to have a high school diploma and meet the minimum score requirements for your chosen program.\n")
            print("For more details, visit the admissions page on the university website.\n")

    elif choice == '2':
            print("\nApplying for Scholarships:")
            print("Students can apply for various scholarships offered by the university based on academic performance, financial need, or specific criteria.\n")
            print("To learn more, visit the scholarships section on the university website.\n")

    elif choice == '3':
            print("\nAcademic Calendar:")
            print("The academic calendar outlines important dates, including registration, semester start and end dates, and examination periods.\n")
            print("You can find the academic calendar on the university's website under the academic affairs section.\n")

    elif choice == '4':
            print("\nContacting Academic Advisors:")
            print("Students can contact their academic advisors via email or during office hours to discuss academic plans and any concerns.\n")
            print("For contact information, visit the academic advising page on the university website.\n")

    elif choice == '5':
            print("\nStudent Activities:")
            print("The university offers a variety of student activities, including clubs, events, and sports. Students are encouraged to participate.\n")
            print("For more information, check the student affairs section on the university website.\n")

    elif choice == 'back':
            print("\nReturning to the main menu.\n")
            

    else:
            print("Invalid input. Please enter a number from 1 to 5 or 'back' to return.\n")



    back_to_menu()

def financial_information():
    print("University of Petra - Financial Information Section")
    print("\nWelcome to the Financial Information section. Here you can find details about tuition fees, payment plans, and financial aid.")
    print("If you have specific questions not covered here, please contact the university's financial office.")
    print("1. What is early registration? What are its procedures?")
    print("2. How do students register courses after the end of the early registration period?")
    print("3. How are students’ transportation fees are calculated and deducted?")
    print("4. What are available payment methods at UOP?")
    print("5. How many chances are given to students if his/her cheque was bounced?")
    print("6. When students can pay study fees during working hours?")
    print("7. What are the procedures the student must follow to obtain proof of student status, transcript or additional copies of the certificate of graduation?")
    print("8. When the fee for the three placement exams (English + Computer + Arabic) is paid and the student does not take one or all of the exams because of equivalency, how are these cases handled financially?")
    print("9. How many times refundable insurance fees are paid?")
    print("10. How can the student obtain final examinations entry card? And what are its conditions?")
    print("11. How can the female student register in UOP dormitory?")
    print("12. If the female student did want to renew subscription in the UOP dormitory, what must she do?")
    print("13. When can the graduate obtain clearance certificate for graduation purposes?")
    print("14. If the student dropout UOP courses and wishes to postpone the semester or return to study, what are the steps the student must follow?")
    
    choice = input("\nEnter the number of your question for more information or type 'back' to return: ").strip().lower()
    if choice == '1':
        print("Early registration takes place in the beginning of each semester (as outlined in the university calendar). To early register courses, the student have to pay 100% of credit hours’ fees plus registration and services fees.")
    
    elif choice == "2" :
        print("The returning student is required to pay 60% of the tuition fees for the credit hours they wish to register for, along with the registration and service fees. The remaining balance must be paid before the final exams, except for the Dentistry program, where this procedure does not apply.")
    
    elif choice == "3" :
        print("A fixed amount is collected for the mandatory regular semester (Fall/Spring) of 220 JOD for a first-semester student, and then 200 JOD for each regular semester. Additionally, 120 JOD are collected for the optional summer semester for first-semester students, followed by 100 JOD for each subsequent summer semester. The payment is made in cash as a one-time lump sum, regardless of the usage rate.")
        
    elif choice == "4" :
        print("The student can pay due fees to UOP Fund in the Financial Department in one of the following methods: - In cash, official cheques, visa card or master card. - Use E-Payment without the need to visit the Financial Department at the University through the eFAWATEERcom service Illustration Video.You can also pay via external money transfers or deposits in UOP account:Bank Account Information for transfers/deposits in Jordanian Dinars (JD)Bank Account Information for transfers/deposits in US Dollars (US$)")
        
    elif choice == '5':
        print("\n5. Cheque Bounce Policy:")

    elif choice == '6':
        print("\n6. Payment Hours:")


    elif choice == '7':
        print("\n7. Obtaining Proof of Student Status:")


    elif choice == '8':
        print("\n8. Placement Exam Fees and Equivalency:")


    elif choice == '9':
        print("\n9. Refundable Insurance Fees:")


    elif choice == '10':
        print("\n10. Final Examinations Entry Card:")


    elif choice == '11':
        print("\n11. Dormitory Registration for Female Students:")


    elif choice == '12':
        print("\n12. Dormitory Renewal Procedures:")


    elif choice == '13':
        print("\n13. Clearance Certificate for Graduation:")


    elif choice == '14':
        print("\n14. Steps for Dropping Courses or Returning to Study:")


    elif choice == 'back':
        print("\nReturning to the main menu.\n")
        

    else:
        print("Invalid input. Please enter a number from 1 to 14 or 'back' to return.\n")
    back_to_menu()

def back_to_menu():
    print("\nPress 'B' to go back to the main menu.")
    choice = input().lower()
    if choice == 'b':
        visitor_menu()
    else:
        back_to_menu()

# Start the chatbot
main_menu()