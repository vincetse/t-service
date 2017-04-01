from flask import Flask
from flask import render_template

app = Flask("t")


@app.route("/")
def index():
    status_code = 418
    fontfamily = "Bungee Shade"
    return render_template("teapot.html", fontfamily=fontfamily), status_code


if __name__ == "__main__":
    app.run()
