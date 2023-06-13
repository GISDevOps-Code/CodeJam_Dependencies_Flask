from flask import Flask
from views import views
from datetime import timedelta

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
app.secret_key = "SuperSecretKey"
app.permanent_session_lifetime = timedelta(days=5)

if __name__ == '__main__':
    app.run(debug=True)