from app.models.users import User
from app.models.posts import Post
from app import db, create_app

app = create_app()

# Use the app context
# with app.app_context():
    # Create a new user instance and add it to the session
    # u = User(username="susan", email='susan@gmail.com')
    # db.session.add(u)
    # db.session.commit()

    # Print the user to confirm
    # print(u)
# print(app.config['SQLALCHEMY_DATABASE_URI'])


# with app.app_context():
    # users = User.query.all()
    # for u in users:
        # print(u.id, u.username)
        
    # getting user by id
    # user = User.query.get(1)
    # print(user)
    
# adding post
# with app.app_context():
#     u = User.query.get(1)
#     p = Post(body='my first post!', author=u)
#     db.session.add(p)
#     db.session.commit()

with app.app_context():
    users = User.query.all()
    for u in users:
        db.session.delete(u)
        
    posts = Post.query.all()
    for p in posts:
        db.session.delete(p)
        
    db.session.commit()