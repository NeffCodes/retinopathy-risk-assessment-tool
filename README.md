# Retinopathy Risk Assessment Tool (RRAT)

## Overview

The Retinopathy Risk Assessment Tool (RRAT) is a data visualization web application designed to assist clinics in the early detection and assessment of diabetic retinopathy. This tool allows medical professionals to upload patient images and input relevant patient data, receiving a detailed analysis from a machine learning model that predicts the likelihood of the patient developing diabetic retinopathy.

## Planned Features

This is our current plan / scope for our application.
We do have additional ideas for stretch goals that are listed below, but are not currently planned.

![Battle Plan](https://res.cloudinary.com/dkcatdj1w/image/upload/v1724276559/gztkivmcbih8wh4nth2d.png)

|||
| ---      | ---       |
| **Image Upload** | Securely upload patient retinal images for analysis. |
| **Patient Data Input** | Add patient details such as name, date of birth, and medical history to enhance analysis accuracy. |
| **Model-Driven Analysis** | Utilizes a trained machine learning model to assess the risk of diabetic retinopathy. |
| **Display Results** | Presents a clear and concise prognosis, helping clinicians make informed decisions. 
| **Additional Resources**| May add resources and next steps, such as links to Mayo Clinic or NIH, after prognosis.

### Stretch Goal Ideas

- Utilize MayoClinic or NIH APIs to get health information.
- Using AI prompting to get potential treatment plans on a case-by-case basis.

## Technology Stack

Please note that this is our idea for our tech stack going in.
This is subject to change as we progress through development.

- **Backend:** Python + Django
- **Frontend:** Django Templates + Tailwind.css  
- **Database:** SQLite
- **Python Librariies:**
  - TensorFlow(for machine learning models)
  - Keras (for building CNNs)
  - NumPy (for numerical operations)
  - Pandas (for data manipulation)
  - OpenCV (for image processing)
  - Scikit-learn (for additional machine learning tools)
- **Other Tools:**
  - Postman (API testing)
  - Slack (Team communication)
  - GitHub (Version control)
  - Github Projects (Project management)

## Machine Learning Model

The Retinopathy Risk Assessment Tool (RRAT) uses a Convolutional Neural Network (CNN) for image classification, specifically trained to identify the risk of diabetic retinopathy from retinal images. The model is built using TensorFlow and Keras libraries, leveraging the power of CNNs to automatically detect features in retinal images that may indicate the presence of diabetic retinopathy.

### Type of Learning
This project employs supervised learning, where the model is trained on a labeled dataset of retinal images. Each image in the training set is associated with a label indicating the severity of diabetic retinopathy (e.g., No_DR, Mild, Moderate, Severe, Proliferative). The model learns to map input images to these labels, and once trained, it can predict the risk level for new, unseen images.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Django 5.1 or higher

### Installation Steps

If you haven't already, go ahead and install [python](https://www.python.org/downloads/) and [django](https://www.djangoproject.com/download/).

**1. Clone the Repository :**

```bash
git clone https://github.com/NeffCodes/retinopathy-risk-assessment-tool.git
cd retinopathy-risk-assessment-tool
```

**2. Set up your virtual environment:**

- initialize the virtual environment

```bash
python -m venv env
```

- activate the virtual environment

```bash
#Mac Users
source env/bin/activate

#Windows Users
source env/Scripts/activate
```

**3. Install the required Python packages:**

```bash
 pip install -r requirements.txt
```

**4. Set up the database:**

```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Run the Django Development Server:**

```bash
python manage.py runserver
```

### Usage

- Access the application locally at http://localhost:8000

### Testing

Make sure the server is running. Then run unit tests with:

```bash
python manage.py test
```

And use Postman to test API endpoints.

## Contributing

We welcome contributions! Please leave a comment in the issues tab or follow the standard GitHub flow for submitting pull requests:

- Fork the repository.
- Create a new branch `git checkout -b feature/your-feature-name`
- Make your changes and commit them `git commit -m 'Add some feature'`
- Push to the branch `git push origin feature/your-feature-name`
- Open a pull request.
  
## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any other questions or inquiries, please contact us at [Sumi Means](suminmeans@gmail.com) or [James Neff](contact@jamesneff.com)
