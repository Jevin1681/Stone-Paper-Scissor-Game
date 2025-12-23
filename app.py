from flask import Flask, render_template, request, url_for, redirect, flash
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jevin1681'
CHOISE = ["Rock", "Paper", "Scissors"]

# @app.route('/',methods = ["POST","GET"])
# def startbtn():
#     return render_template("index.html")

@app.route("/" , methods = ["POST","GET"])
def game():
    
    if request.method == "POST":
    
        computer_choise = random.choice(CHOISE)
        user_choise = request.form.get("user_choise")
        
        if user_choise == computer_choise:
            flash("Ohhh..! Match is Draw.. 😀",'draw')
            flash(f"Your Choise - {user_choise}")
            flash(f"Computer Choise - {computer_choise}")
            return redirect(url_for('resultpage'))
            
        
        elif ( user_choise =="Rock" and computer_choise == "Scissors" or 
              user_choise == "Scissors" and computer_choise == "Paper" or 
              user_choise == "Paper" and computer_choise == "Rock"):
            flash("Congratulations! You won the Game...🎉",'won')
            flash(f"Your Choise - {user_choise}")
            flash(f"Computer Choise - {computer_choise}")
            return redirect(url_for('resultpage'))
            
        else:
            flash("You lost the Game... 😞",'lost')
            flash(f"Your Choise - {user_choise}")
            flash(f"Computer Choise - {computer_choise}")
            return redirect(url_for('resultpage'))
    
    return render_template("index.html")
            
    
@app.route("/resultpage", methods=["POST","GET"])
def resultpage():
    return render_template("result.html")
    
@app.route("/playagain", methods=["POST","GET"])
def playagain():
    if request.method == "POST":
        return redirect(url_for("game"))
    return render_template("result.html")
    
    


if __name__ == "__main__":
    app.run(debug = True)