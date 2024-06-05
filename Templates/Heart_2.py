
import pandas as pd 
import json
import requests
url = 'https://dc58-35-201-131-173.ngrok-free.app/'
class Heart_2:
    def __init__(self, ST_Slope: str = 0, ExerciseAngina: str = 0, ChestPainType: str = 0, Oldpeak: float = 0, MaxHR: int = 0, Sex: str = 0, Age: int = 0, FastingBS: float = 0, Cholesterol: float = 0, RestingBP: int = 0, RestingECG: str = 0, diagnosis = None):

        self.ST_Slope = str(ST_Slope)
        self.ExerciseAngina = str(ExerciseAngina)
        self.ChestPainType = str(ChestPainType)
        self.Oldpeak = float(Oldpeak)
        self.MaxHR = int(MaxHR)
        self.Sex = str(Sex)
        self.Age = int(Age)
        self.FastingBS = float(FastingBS)
        self.Cholesterol = float(Cholesterol)
        self.RestingBP = int(RestingBP)
        self.RestingECG = str(RestingECG)
        self.target: float = 'diagnosis'
        self.data_path = str(r"C:\Users\Jora\Medic")
    
    def to_dict(self):
        # Initialize an empty dictionary to hold the structured data
        data = {}

        # Iterate over the instance's __dict__ to populate the structured dictionary
        for key, value in self.__dict__.items():
            if (key!="target" and key!="data_path"):
                # Transform the key to match the desired format and add the value wrapped in another dictionary
                transformed_key = f"{key[0].upper()+key[1:]}" if key!= "bmi" else key.upper()
                data[transformed_key] = {str(0): value}

        return data

    def visualize(self):
        print("Here Add Vizualization Type Stuff or not")

    def predict(self):
        data = self.to_dict()

        # Make the POST request with the correct content type
        response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

        # Print the response
        status = "Sick"
        result=response.text.replace("[","").replace("]","")
        if float(result) < 0.5:
            status = "Healthy"
        print("    The person is",status)

    def load(self,path):
        df= pd.read_csv(path)
        new_df=df.copy()
        data= pd.DataFrame.to_json(df)
        response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

        result=response.text.replace("[","").replace("]","").split()
        dic={k:result[k] for k in range(len(result))}
        for i in dic: 
            status = "Sick"
            if float(dic[i]) < 0.5:
                status = "Healthy"
            print(f"The person {i} is {status}")


        df2=new_df.assign(Outcome=[round(float(x)) for x in result])
        df2.to_csv("Output.csv")
        print("Results saved in Output.csv")
        return 0

