# SkinSense – AI-Powered Skin Care Product Recommendation System

## Overview

SkinSense is a Flask-based web application that provides personalized skincare product recommendations based on a user's skin type. The platform helps users discover suitable products with details such as brand, price, availability, and usage notes.

## Features

- Personalized skincare recommendations
- Supports multiple skin types:
  - Oily
  - Dry
  - Normal
  - Combination
  - Sensitive
- Product information including:
  - Product Name
  - Brand
  - Price
  - Availability Location
  - Usage Notes
- Responsive and user-friendly interface
- Lightweight Flask backend

## Tech Stack

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Flask

### Data Storage
- JSON

## Project Structure

```text
SkinSense/
│
├── app.py
├── products.json
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/pavithra-2805/skinsense.git
cd skinsense
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## How It Works

1. Select your skin type.
2. Submit the form.
3. The application processes the input.
4. Matching skincare products are retrieved from the dataset.
5. Personalized recommendations are displayed.

## Future Enhancements

- AI-powered recommendation engine
- Skin concern analysis
- Product reviews and ratings
- User authentication
- Database integration
- Image-based skin analysis
- E-commerce integration

## Author

**Lakshmi Pavithra Korukonda**

- GitHub: https://github.com/pavithra-2805

## License

This project is intended for educational and learning purposes.