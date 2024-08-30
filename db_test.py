from app.models import User
from app import db, create_app

# Create a new user instance and add it to the session
user1 = User(username="Susan", email='susan@gmail.com')
app = create_app()
# Print the user to confirm
print(user1)

print(app.config['SQLALCHEMY_DATABASE_URI'])
