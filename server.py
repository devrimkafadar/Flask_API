import os
from flask import Flask, render_template
from routers.index import index

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')
app = Flask(__name__, template_folder=template_path)
app.register_blueprint(index , url_prefix="/stats")
##############################################################
##############################################################

print("SERVER IS ON")

@app.route("/", methods = ["GET"])
def home():
    return render_template("index.html")

 


##############################################################
##############################################################
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)