import pandas as pd
class Obesity:
    def __init__(self, pregnancies: int, glucose: float, bloodPressure: float, skinThickness: float, insulin: float, bmi: float, age: float, diagnosis = None):

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
        print("Here Add Vizualization Type Stuff")

    def predict(self):
        print("Here Add Data Science Type Stuff")

    def load(self):
        return pd.load(self.data_path)
    
