**ArchDo Paints**

ArchDo Paints is an AI-powered AR home improvement application designed to assist users in planning and visualizing their painting projects based on their personality types. The app integrates OpenAI’s ChatGPT for conversational interaction and an Aptos payment gateway for secure and fast transactions. The frontend is built using HTML, CSS, and JavaScript, while the backend leverages Django and React.js.

Features
1. Personality Test Submission
Endpoint: /api/personality/submit/
Description: Users can submit their personality test answers along with their gender. The data is sent to an external API for processing, and the results are returned to provide personalized paint project suggestions.
2. ChatGPT Interaction
Endpoint: /api/chatgpt/
Description: Allows users to interact with OpenAI’s ChatGPT for personalized conversational experiences regarding their home improvement projects.
3. Aptos Payment Gateway Integration
Secure Payments: Aptos integration ensures fast and secure transactions for users purchasing paint supplies or planning services within the app.
Setup and Installation
To get started with ArchDo Paints, follow these steps:

1. Clone the Repository:
Run the following command to clone the repository:
git clone https://github.com/yourusername/archdo-paints.git
Then navigate to the project folder:
cd archdo-paints

2. Create a Virtual Environment:
To create a virtual environment, use the command:
python -m venv venv

3. Activate the Virtual Environment:
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
4. Install Dependencies:
Run this command to install the required dependencies:
pip install -r requirements.txt

5. Apply Migrations:
To apply migrations, run:
python manage.py migrate

6. Run the Development Server:
Use this command to start the development server:
python manage.py runserver

7. Frontend Setup:
To set up the frontend with React.js:

Navigate to the frontend directory:
cd frontend
Install necessary dependencies:
npm install
Start the React.js development server:
npm start
Configuration
External API:
Update the API_URL in views.py with the URL of the external personality test API.

OpenAI API Key:
Set your OpenAI API key in views.py in the designated area to enable ChatGPT interaction.

Aptos Payment Gateway:
Update the payment configuration in the backend to integrate Aptos. Follow their official documentation for API key setup.

Directory Structure
archo_backend/: Main Django project directory containing settings and URL configurations.
api/: Contains application logic and views.
frontend/: Contains React.js code for the frontend interface.
manage.py: Django command-line utility for administrative tasks.
Contributing
Contributions are welcome! If you have suggestions, bug reports, or feature requests, please:

Submit a pull request
Open an issue
We appreciate your feedback and contributions to make ArchDo Paints even better!
