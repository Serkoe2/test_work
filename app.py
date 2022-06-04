from apps import create_app, db
from Config import Config
from flask_migrate import Migrate

app = create_app(Config)
Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
