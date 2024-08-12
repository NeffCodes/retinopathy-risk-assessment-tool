# Retinopathy Risk Assessment Tool (RRAT)
## Overview
The Retinopathy Risk Assessment Tool (RRAT) is a data visualization web application designed to assist clinics in the early detection and assessment of diabetic retinopathy. This tool allows medical professionals to upload patient images and input relevant patient data, receiving a detailed analysis from a machine learning model that predicts the likelihood of the patient developing diabetic retinopathy.


## Features
- Image Upload: Securely upload patient retinal images for analysis.
- Patient Data Input: Add patient details such as name, date of birth, and medical history to enhance analysis accuracy.
- Model-Driven Analysis: Utilizes a trained machine learning model to assess the risk of diabetic retinopathy.
- Results Display: Presents a clear and concise prognosis, helping clinicians make informed decisions. $${\color{red} May\ add\ onto\ this\ later\ regarding\ resources\ and\ 'what next' \ after\ prognosis \ i.e\  MayoClinic \ or  NIH \ API \ call} $$

## Technology Stack
- Backend: Python (Django)
- Frontend: React, Material-UI (or JS + Tailwind CSS)
- Database: MySQL
- Other Tools:
  - Postman (API testing)
  - Swagger (API documentation)
  - Trello (Project management)
  - Slack (Team communication)
  - GitHub (Version control)

## Setup and Installation
### Prerequisites
- Python 3.8 or higher
- Node.js and npm (for frontend development) **NOT SURE ABOUT THIS**
- PostgreSQL

### Installation Steps
**1) Clone the Repository :**
```bash
git clone https://github.com/NeffCodes/retinopathy-risk-assessment-tool.git
cd retinopathy-risk-assessment-tool
```
**2) Backend Setup:**
- Create a viirtual environment and activate it :
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
- Install the required Python packages :
```bash
 pip install -r requirements.txt
```
- Set up the database :
```bash
python manage.py makemigrations
python manage.py migrate
```
- Run the Django Development Server :
```bash
python manage.py runserver
```
**3) Frontend Setup :**
- Navigate to the frontend directory :
 ```bash
cd frontend
```
- Install the necessary packages :
```bash
npm install
```
- ** START THE DEVELOPMENT SERVER (JS/REACT? NOT SURE WHAT TO PUT HERE OR FOR GIT BASH)**

**4) Database Configuration :**
- Ensure MySQL is installed and running.
- Update the DATABASES setting in settings.py with your MySQL credentials.
- Create and link the database.

### Usage
- Access the application locally at http://localhost:8000 for the backend and http://localhost:3000 for the frontend.
- Upload patient images and enter patient data through the form provided.
- View the analysis results to assess the risk of diabetic retinopathy.

### Testing
- Run unit tests for the backend
```bash
python manage.py test
```
- Use Postman to test API endpoints.
  

  
