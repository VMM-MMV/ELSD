import requests
import json
import pandas as pd

url = "https://b70e-35-194-229-90.ngrok-free.app/"

class Obesity:
    def __init__(self, pregnancies=3.845, glucose=121.686763, bloodPressure=72.4, skinThickness=29.153, insulin=155.55, bmi=32.45, age=33.24, diagnosis = None):
        self.pregnancies = int(pregnancies)
        self.glucose = float(glucose)
        self.bloodPressure = float(bloodPressure)
        self.skinThickness = float(skinThickness)
        self.insulin = float(insulin)
        self.bmi = float(bmi)
        self.age = float(age)
        self.target: float = 'diagnosis'
        self.data_path = str(r"C:\Users\Jora\Medic")
    
    def visualize(self):
        print("Here Add Vizualization Type Stuff or not")

       
        

    def predict(self):
        data = {
            "Pregnancies": self.pregnancies,
            "Glucose": self.glucose,
            "BloodPressure": self.bloodPressure,
            "SkinThickness": self.skinThickness,
            "Insulin": self.insulin,
            "BMI": self.bmi,
            "DiabetesPedigreeFunction": 0.47,
            "Age": self.age
        }

        # Make the POST request with the correct content type
        response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

        # Print the response
        # print(response.text)
        status = "Sick"
        if float(response.text) < 0.5:
            status = "Healthy"
        print("    The person is",status)

    def load(self):
        return pd.load(self.data_path)
    
