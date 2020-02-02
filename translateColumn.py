import pandas as pd

import googletrans
from googletrans import Translator

translator = Translator()

chart1 = pd.read_excel("Path to Excel File")

#Preview the data
chart1.head()

#Creating the Function

def translation(col):
    col_translate = []
    for item in col:
        translated = translator.translate(item)
        col_translate.append(translated.text)
    return[col_translate]

Use the 
    
To commit the translated column to a Dataframe

df['Column_name'] = col_translate
