
import pandas as pd 
class Obesity:
    def __init__(self, pregnancies: int = 0, glucose: float = 0, bloodPressure: float = 0, skinThickness: float = 0, insulin: float = 0, bmi: float = 0, age: float = 0, diagnosis = None):

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

    def load(self, path):
        target_csv = pd.read_csv(str(path))
        print(f"Your csv: {target_csv}")
