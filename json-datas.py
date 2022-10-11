import sqlite3
import pandas as pd
import json

def create_json(dictionary):
    with open("content.json", "w") as file:
        json.dump(dictionary, file)

# En mi caso trabajo con un solo més.En este caso el marzo de 2015
timeframes = ['2015-03']


for timeframe in timeframes:
    # conectamos a la base de datos
    connection = sqlite3.connect('datas/2015-03.db')
    c = connection.cursor()
    limit = 5000  # numero de registros que obtenemo de la base de datos en la consulta
    last_unix = 0
    cur_length = limit
    counter = 0  # contador para
    test_done = False  # boleano que nos indica cuando hemos  terminado
    df = pd.read_sql(
        "SELECT * FROM parent_reply WHERE parent NOT NULL and score > 0 ORDER BY unix ASC LIMIT {}".format(limit), connection)

    intents=[]
    index=0
    table=df.to_numpy()
    for row in table:
        index+=1
        dictionary = {
        "tag": index,
        "patterns": row[2],
        "responses": row[3],
        "context_set": ""
        }
        intents.append(dictionary)
        #intents.intents.append(intentRow)
        
    create_json(intents)