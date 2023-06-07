from project import db, create_app

app = create_app()
app.app_context().push()

# Create the tables
db.create_all()