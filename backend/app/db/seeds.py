#print('Please fill the seeds file')
#add 100 users, 100 comments, 100 products
import string
import random
from events import connect_to_db
from app.db.repositories.items import ItemsRepository
from app.db.repositories.comments import CommentsRepository
from app.db.repositories.users import UsersRepository

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

usersList=[]
for i in range(0,100):
    username=''.join(random.choices(string.ascii_lowercase)
    email=random_char(9)+"@gmail.com"
    password=''.join(random.choices(string.ascii_letters +string.digits))
    us=UsersRepository.create_user(self,username,email,password)
    usersList.append(us)

itemList=[]
for i in range(0,100):
    slug=''.join(random.choices(string.ascii_letters +string.digits))
    title=''.join(random.choices(string.ascii_letters +string.digits))
    description=''.join(random.choices(string.ascii_letters +string.digits))
    seller=usersList[i]

    item=ItemsRepository.create_item(self,slug,title,description,seller)
    itemList.append(item)

for i in range(0,100):
    body=''.join(random.choices(string.ascii_letters +string.digits))
    CommentsRepository.create_comment_for_item(body,itemList[i],usersList[i])
