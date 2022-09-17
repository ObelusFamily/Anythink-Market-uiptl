
#add 100 users, 100 comments, 100 products
from re import A, I
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
           



async def create(num):
    #print("hi")
    SETTINGS = get_app_settings()
    DATABASE_URL = SETTINGS.database_url.replace("postgres://", "postgresql://")
    conn = asyncpg.connect(DATABASE_URL)
    usersRepository = UsersRepository(conn=conn)
    itemsRepository = ItemsRepository(conn=conn)
    commentsRepository = CommentsRepository(conn=conn)
    usersList=[]
    
    for i in range(num):
        username=''.join(random.choices(string.ascii_lowercase))
        email=random_char(9)+"@gmail.com"
        password=''.join(random.choices(string.ascii_letters +string.digits))
        #us=UsersRepository.create_user(self,username,email,password)
        #usersList.append(us)
        user = await usersRepository.create_user(username=username, password=password, email=email)
        usersList.append(user)
    #print(usersList.length)
    itemList=[]
    for i in range(num):
        slug=''.join(random.choices(string.ascii_letters +string.digits))
        title=''.join(random.choices(string.ascii_letters +string.digits))
        description=''.join(random.choices(string.ascii_letters +string.digits))
        seller=usersList[i]

        item=await itemsRepository.create_item(slug=slug,title=title,description=description,seller=seller)
        itemList.append(item)

    for i in range(100):
        body=''.join(random.choices(string.ascii_letters +string.digits))
        comment= await commentsRepository.create_comment_for_item(body=body,item=itemList[i],user=usersList[i])

    await conn.close()

loop=asyncio.get_event_loop()
loop.run_until_complete(create(100))