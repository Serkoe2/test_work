from config import Config
from apps import create_app

app = create_app(Config())

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)