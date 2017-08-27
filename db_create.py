#! venv/bin/python

# instance/db_create.py

from app import db
from app.models import Blog


# Create the database and the database table
db.create_all()

# Insert blog data
article1 = Blog("I love my wife", "Weldon", "I love my wife with all of my heart. She is the best this that has ever happened to me. I would do absolutely anything within my power to make her happy.")
article2 = Blog("I love my husband", "Brandy", "I love my husband more than I can describe. I am not good at describing and portraying my feelings, but he knows that I love him.")
article3 = Blog("We love our children", "Brandy and Weldon", "We love our children more than life itself. We would do anything for our children.")

db.session.add(article1)
db.session.add(article2)
db.session.add(article3)

# Commit the changes
db.session.commit()
