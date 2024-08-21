# Retinopathy Risk Assessment Tool (RRAT)
## Overview
The Retinopathy Risk Assessment Tool (RRAT) is a data visualization web application designed to assist clinics in the early detection and assessment of diabetic retinopathy. This tool allows medical professionals to upload patient images and input relevant patient data, receiving a detailed analysis from a machine learning model that predicts the likelihood of the patient developing diabetic retinopathy.


## Features
- Image Upload: Securely upload patient retinal images for analysis.
- Patient Data Input: Add patient details such as name, date of birth, and medical history to enhance analysis accuracy.
- Model-Driven Analysis: Utilizes a trained machine learning model to assess the risk of diabetic retinopathy.
- Results Display: Presents a clear and concise prognosis, helping clinicians make informed decisions.
- Additional Resources: May add resources and next steps, such as links to Mayo Clinic or NIH, after prognosis.

## Technology Stack
- Backend: Python (Django)
- Frontend: Javascript, Material-UI, Tailwind CSS
- Database: SQLite => MySQL
- Python Libraries:
  - TensorFlow (for machine learning model)
  - Keras (for building CNNs)
  - NumPy (for numerical operations)
  - Pandas (for data manipulation)
  - OpenCV (for image processing)
  - Scikit-learn (for additional machine learning tools)
- Other Tools:
  - Postman (API testing)
  - Swagger (API documentation)
  - Slack (Team communication)
  - GitHub (Project Management and Version control)
  - 
 
## Machine Leaning Model
The Retinopathy Risk Assessment Tool (RRAT) uses a Convolutional Neural Network (CNN) for image classification, specifically trained to identify the risk of diabetic retinopathy from retinal images. The model is built using TensorFlow and Keras libraries, using the power of CNNs to automatically detect features in retinal images that may indicate the presence of diabetic retinopathy.

### Type of Learning
This project employs supervised learning, where the model is trained on a labeled dataset of retinal images. Each image in the training set is associated with a label indicating the severity of diabetic retinopathy (e.g., No_DR, Mild, Moderate, Severe, Proliferative). The model learns to map input images to these labels, and once trained, it can predict the risk level for new, unseen images.


## Setup and Installation
### Prerequisites
- Python 3.8 or higher
- Node.js and npm (for frontend development) 
- MySQL

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
- Start the development server:
 ```bash
npm run dev
```

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


## Contributing
We welcome contributions! Please follow the standard GitHub flow for submitting pull requests:
- Fork the repository.
- Create a new branch (git checkout -b feature/your-feature-name).
- Make your changes and commit them (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/your-feature-name).
- Open a pull request.
  
## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any questions or inquiries, please contact us at suminmeans@gmail.com or james.m.neff@gmail.com

  
