from flask import Flask, render_template
import data_processing


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", harry_potter = data_processing.harry_potter, paper_umbrella = data_processing.paper_umbrella , moudy = data_processing.moudy , the_dragon_republic = data_processing.the_dragon_republic , the_poppy_war = data_processing.the_poppy_war ,hidden_world = data_processing.hidden_world , whiteandgrey = data_processing.whiteandgrey , selena = data_processing.selena)
    
