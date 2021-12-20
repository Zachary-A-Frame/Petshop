from models import db, Pet
from app import app

db.drop_all()
db.create_all()

# Data

freya = Pet(name="Freya",
            species="cat",
            photo_url="https://icatcare.org/app/uploads/2019/09/The-Kitten-Checklist-1.png",
            age=1,
            notes="She's really cute",
            available=True)
moxie = Pet(name="Moxie",
            species="cat",
            photo_url="https://570189-1841390-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2020/01/trivia-about-tuxedo-cats.jpg",
            age=12,
            notes="Old but very friendly, loving.",
            available=True)

kay = Pet(name="Kay",
          species="doggo",
          photo_url="https://smartcdn.prod.postmedia.digital/nationalpost/wp-content/uploads/2018/10/chocolate_labrador_retriever_dog.jpg?quality=90&strip=all&w=564&h=423&type=webp",
          age=4,
          notes="Pure bred, beautiful, well trained",
          available=False)

db.session.add_all([freya, moxie, kay])
db.session.commit()