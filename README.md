# Diabetes Prediction Project

A machine learning web application that predicts whether a patient is likely to suffer from diabetes based on various health parameters.

## Features

- **Machine Learning Model**: Uses a trained regressor model to predict diabetes risk
- **Web Interface**: Flask-based web application with user-friendly forms
- **Real-time Prediction**: Instant results based on input parameters
- **Responsive Design**: Clean and modern UI templates

## Input Parameters

The application takes the following health parameters as input:

- **Glucose**: Blood glucose level
- **Blood Pressure**: Blood pressure measurement
- **Skin Thickness**: Triceps skin fold thickness
- **Insulin**: 2-Hour serum insulin
- **BMI**: Body Mass Index
- **Pregnancies**: Number of pregnancies
- **Age**: Age of the patient
- **Diabetes Pedigree Function**: Family history of diabetes

## Technology Stack

- **Backend**: Python Flask
- **Machine Learning**: Scikit-learn
- **Frontend**: HTML, CSS
- **Data Processing**: NumPy, Pandas

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/diabetes-prediction.git
   cd diabetes-prediction
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
Diabetes_project/
├── app.py                 # Main Flask application
├── model.py              # Machine learning model functions
├── regressor_model.pkl   # Trained model file
├── Diabetes_cleaned.csv  # Dataset
├── templates/            # HTML templates
│   ├── index.html       # Input form
│   └── output.html      # Results display
├── static/              # Static assets
│   ├── 1.jpg
│   └── background_img.jpeg
└── README.md            # This file
```

## Usage

1. Fill out the health parameter form on the homepage
2. Submit the form to get instant diabetes risk prediction
3. View the results indicating whether the patient is likely to suffer from diabetes

## Model Performance

The application uses a pre-trained machine learning model that has been trained on a comprehensive diabetes dataset. The model considers multiple health factors to provide accurate predictions.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Dataset source: [Diabetes Dataset](https://www.kaggle.com/datasets/uciml/diabetes-database)
- Flask web framework
- Scikit-learn machine learning library
