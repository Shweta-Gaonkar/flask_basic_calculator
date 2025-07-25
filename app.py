from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    expression = request.form.get("expression", "")
    result = ""

    if request.method == "POST":
        try:
            result = str(eval(expression))
        except ZeroDivisionError:
            result = "Error: Divide by 0"
        except:
            result = "Invalid Input"
    return render_template("index.html", expression=expression, result=result)

if __name__ == "__main__":
    app.run(debug=True)
