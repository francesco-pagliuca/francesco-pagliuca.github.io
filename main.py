from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_data = request.form["input_field_name"]
        data = json.load(open("data.json"))
        
        input_list = data.get("input_list", [])
        input_list.append(str(input_data))
        data["input_list"] = input_list
        
        with open("data.json", "w") as file:
            json.dump(data, file)
            
        return "Input ricevuto e scritto nel file JSON"
            
    return '''
        <form method="post">
            Campo di input: <input type="text" name="input_field_name">
            <input type="submit" value="Invia">
        </form>
        <br>
        <a href="/list">Vedi tutti gli input</a>
    '''

@app.route("/list")
def list_inputs():
    data = json.load(open("data.json"))
    input_list = data.get("input_list", [])
    
    input_list = [(i + 1, input_list[i]) for i in range(len(input_list))]
    
    return f'''
        <h1>Lista degli input:</h1>
        <ul>
            {
                "".join([f"<li>{num}. {input_}</li>" for num, input_ in input_list])
            }
        </ul>
        <br>
        <a href="/">Torna alla home</a>
    '''

if __name__ == "__main__":
    app.run()

    app.run()
