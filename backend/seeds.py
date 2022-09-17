
#add 100 users, 100 comments, 100 products
import string
import asyncio
import asyncpg
import random
from app.api.dependencies.database import get_repository
from app.db.repositories.comments import CommentsRepository
from app.db.repositories.items import ItemsRepository
from app.db.repositories.users import UsersRepository

from app.core.config import get_app_settings




def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
           

async def create():
    SETTINGS = get_app_settings()
    DATABASE_URL = SETTINGS.database_url.replace("postgres://", "postgresql://")
    conn = await asyncpg.connect(DATABASE_URL)
    usersRepository = UsersRepository(conn=conn)
    usersList=[]
    for i in range(0,100):
        username=''.join(random.choices(string.ascii_lowercase))
        email=random_char(9)+"@gmail.com"
        password=''.join(random.choices(string.ascii_letters +string.digits))
        #us=UsersRepository.create_user(self,username,email,password)
        #usersList.append(us)
        user = await usersRepository.create_user(username=username, password=password, email=email)
        usersList.append(user)
    
    itemList=[]
    for i in range(0,100):
        slug=''.join(random.choices(string.ascii_letters +string.digits))
        title=''.join(random.choices(string.ascii_letters +string.digits))
        description=''.join(random.choices(string.ascii_letters +string.digits))
        seller=usersList[i]

        item=await ItemsRepository.create_item(slug=slug,title=title,description=description,seller=seller)
        itemList.append(item)

    for i in range(0,100):
        body=''.join(random.choices(string.ascii_letters +string.digits))
        comment= await CommentsRepository.create_comment_for_item(body=body,item=itemList[i],user=usersList[i])