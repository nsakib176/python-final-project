## Chatbot Course Suggestion System

This project implements a course suggestion feature for a chatbot, allowing students to receive personalized recommendations based on their program and completed courses.

**Project Goal:**

Develop a system that integrates with an existing chatbot framework to suggest courses for the upcoming semester. These suggestions will consider the student's:

* Current program
* Previously completed courses

**Project Structure:**

* **Database:** Utilizes MySQL to store student and course information.
* **Python Script:** Contains logic for fetching data from the database and generating course suggestions.
* **Chatbot Integration:** Python script integrates with the existing chatbot framework to receive user input and display recommendations.

**Getting Started (For Demonstration Purposes):**

1. **Database Setup:**
    * This project uses a sample MySQL database with dummy data. You'll need to create your own database and populate it with actual student and course information.
    * The `sql` folder contains scripts for creating the database tables (`create_tables.sql`) and inserting sample data (`sample_data.sql`).

2. **Python Script:**
    * The `course_suggestion.py` script implements the course suggestion logic.
    * Update connection details in the script to connect to your MySQL database.

**Functionality Breakdown:**

* The chatbot interacts with the user to identify their program and completed courses.
* The chatbot calls the `course_suggestion.py` script, passing the retrieved information.
* The script connects to the MySQL database and retrieves relevant course data based on the user's program.
* The script filters retrieved courses to exclude courses already completed by the user.
* The script returns a list of suggested courses to the chatbot.
* The chatbot displays the course suggestions back to the user.

**Integration with Chatbot Framework:**

Due to the lack of comprehensive documentation for the existing chatbot framework, specific integration steps cannot be provided. However, the general approach involves:

* Modifying the chatbot code to call the `course_suggestion.py` script with appropriate user input.
* Updating the chatbot code to display the received course suggestions to the user.

**Compensation:**

We can discuss my rates for completing the full project, including database setup, comprehensive Python script development, and detailed chatbot integration guidance.

**Next Steps:**

* If you're interested in further development, we can:
    * Finalize database structure and populate it with real data.
    * Implement the complete course suggestion logic within the Python script.
    * Develop detailed instructions for integrating the script with your specific chatbot framework.

**Disclaimer:**

This project provides a basic framework for a course suggestion system. Further modifications and adaptations might be necessary depending on your chatbot framework and specific requirements.
