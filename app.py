from flask import Flask, render_template, request
import openai
import config


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    query = request.args.get('msg')
    openai.api_key = config.api_key
    #response = "engine blah blah blah"
    #response = request.get(f"0.0.0.0/987987/query")

    response = openai.Completion.create(
        prompt=query,
        model='text-davinci-003',
        max_tokens=1000,
        temperature=0.9,
        n=3,
        stop=['\"\"\"']
    ).choices[0].text.strip()
    
    return response


@app.route("/about_hicams.html")
def hicams():
    return render_template('about_hicams.html')

@app.route("/about_hicbm.html")
def hicbm():
    return render_template('about_hicbm.html')

@app.route("/about_himap.html")
def himaps():
    return render_template('about_himap.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=54321)
