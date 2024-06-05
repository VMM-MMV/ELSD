import requests
import json
import pandas as pd

url = "https://7194-104-199-189-113.ngrok-free.app/"

class Heart:
    def __init__(self, ST_Slope=0.6, Oldpeak=0.81, ExerciseAngina=0.37, MaxHR=139.32, RestingECG=0.625, FastingBS=0.255, Cholesterol=195.2, RestingBP=192.73, ChestPainType=1.48, Sex= 0, Age=53):

        self.ST_Slope = str(ST_Slope)
        self.Oldpeak = float(Oldpeak)
        self.ExerciseAngina = str(ExerciseAngina)
        self.MaxHR = int(MaxHR)
        self.RestingECG = str(RestingECG)
        self.FastingBS = float(FastingBS)
        self.Cholesterol = float(Cholesterol)
        self.RestingBP = int(RestingBP)
        self.ChestPainType = str(ChestPainType)
        self.Sex = str(Sex)
        self.Age = int(Age)
        self.target: float = 'diagnosis'
        self.data_path = str(r"C:\Users\Jora\Medic")
    
    def visualize(self):
        print("Here Add Vizualization Type Stuff or not")

    def predict(self):
        data = {
            "ST_Slope": self.ST_Slope,
            "ExerciseAngina": self.ExerciseAngina,
            "ChestPainType": self.ChestPainType,
            "Oldpeak": self.Oldpeak,
            "MaxHR": self.MaxHR,
            "Sex": self.Sex,
            "Age": self.Age,
            "FastingBS": self.FastingBS,
            "Cholesterol": self.Cholesterol,
            "RestingBP": self.RestingBP,
            "RestingECG": self.RestingECG,
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
    
