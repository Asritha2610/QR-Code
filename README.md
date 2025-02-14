Project Setup Guide: QR Code Generator
•	Run&Test
Step 1: Unzip the QR_CODE Folder
Upon unzipping, you will find two sub-folders:
•	QR_Code_Generator (Backend)
•	QR_Code_Frontend (Frontend)
Backend Setup (FastAPI)
A virtual environment is used to manage dependencies. Run the following command in the terminal: python -m venv venv  
Activate the virtual environment (For Windows): venv\Scripts\activate
Step 2: Install Dependencies
Run the following command to install the required dependencies:
                                           pip install fastapi uvicorn qrcode[pil] pydantic mangum httpx

Note: FastAPI is used as it provides automatic request validation with Pydantic and is easy to deploy serverlessly.
Step 3: Run FastAPI Server
Start the FastAPI server with: uvicorn main:app --reload
The API will be available at: http://127.0.0.1:8000
Step 4: Test API (Optional)
You can test the API using:
•	Postman
•	Automated test script: Execute test_main.py to run test cases.
Frontend Setup (Vue.js)
Step 1: Navigate to the Frontend Directory
       Move to the frontend project folder: cd QR_Code_frontend
Step 2: Install Dependencies
Run the following command to install necessary packages: npm install

Step 3: Start the Vue Application
Launch the frontend application with: npm run serve
The Vue application will be accessible at: http://localhost:8080




 

 
 

