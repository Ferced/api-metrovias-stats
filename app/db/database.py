from server.instance import server
from models.metrovias_stats import db
from models.metrovias_stats_schema import ma

app, api = server.app, server.api
# Init DataBase
db.init_app(app)

# Init Marshmallow
ma.init_app(app)
