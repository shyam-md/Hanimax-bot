
import motor.motor_asyncio
from config import DB_URI, DB_NAME

# Create an async MongoDB client
dbclient = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)
database = dbclient[DB_NAME]

# Define the collections
user_data = database['users']
channel_data = database['channels']
admins_data = database['admins']
banned_user_data = database['banned_user']
autho_user_data = database['autho_user']

auto_delete_data = database['auto_delete']
hide_caption_data = database['hide_caption']
protect_content_data = database['protect_content']
channel_button_data = database['channel_button']

del_timer_data = database['del_timer']
channel_button_link_data = database['channelButton_link']


# Set the channel button link
async def set_channel_button_link(button_name: str, button_link: str):
    await channel_button_link_data.delete_many({})  # Non-blocking delete
    await channel_button_link_data.insert_one({'button_name': button_name, 'button_link': button_link})  # Non-blocking insert

# Get the channel button link
async def get_channel_button_link():
    data = await channel_button_link_data.find_one({})  # Non-blocking find
    if data:
        return data.get('button_name'), data.get('button_link')
    return 'Join Channel', 'https://t.me/btth480p'


# Set/Delete Timer
async def set_del_timer(value: int):
    existing = await del_timer_data.find_one({})  # Non-blocking find
    if existing:
        await del_timer_data.update_one({}, {'$set': {'value': value}})  # Non-blocking update
    else:
        await del_timer_data.insert_one({'value': value})  # Non-blocking insert

async def get_del_timer():
    data = await del_timer_data.find_one({})  # Non-blocking find
    if data:
        return data.get('value', 600)
    return 600


# Set/Auto Delete
async def set_auto_delete(value: bool):
    existing = await auto_delete_data.find_one({})  # Non-blocking find
    if existing:
        await auto_delete_data.update_one({}, {'$set': {'value': value}})  # Non-blocking update
    else:
        await auto_delete_data.insert_one({'value': value})  # Non-blocking insert

async def set_hide_caption(value: bool):
    existing = await hide_caption_data.find_one({})  # Non-blocking find
    if existing:
        await hide_caption_data.update_one({}, {'$set': {'value': value}})  # Non-blocking update
    else:
        await hide_caption_data.insert_one({'value': value})  # Non-blocking insert

async def set_protect_content(value: bool):
    existing = await protect_content_data.find_one({})  # Non-blocking find
    if existing:
        await protect_content_data.update_one({}, {'$set': {'value': value}})  # Non-blocking update
    else:
        await protect_content_data.insert_one({'value': value})  # Non-blocking insert

async def set_channel_button(value: bool):
    existing = await channel_button_data.find_one({})  # Non-blocking find
    if existing:
        await channel_button_data.update_one({}, {'$set': {'value': value}})  # Non-blocking update
    else:
        await channel_button_data.insert_one({'value': value})  # Non-blocking insert


# Get settings
async def get_auto_delete():
    data = await auto_delete_data.find_one({})  # Non-blocking find
    if data:
        return data.get('value', False)
    return False

async def get_hide_caption():
    data = await hide_caption_data.find_one({})  # Non-blocking find
    if data:
        return data.get('value', False)
    return False

async def get_protect_content():
    data = await protect_content_data.find_one({})  # Non-blocking find
    if data:
        return data.get('value', False)
    return False

async def get_channel_button():
    data = await channel_button_data.find_one({})  # Non-blocking find
    if data:
        return data.get('value', False)
    return False


# User Management
async def present_user(user_id: int):
    found = await user_data.find_one({'_id': user_id})  # Non-blocking find
    return bool(found)

async def add_user(user_id: int):
    await user_data.insert_one({'_id': user_id})  # Non-blocking insert
    return

async def full_userbase():
    user_docs = await user_data.find().to_list(length=None)  # Non-blocking find
    user_ids = [doc['_id'] for doc in user_docs]
    return user_ids

async def del_user(user_id: int):
    await user_data.delete_one({'_id': user_id})  # Non-blocking delete
    return


# Channel Management
async def channel_exist(channel_id: int):
    found = await channel_data.find_one({'_id': channel_id})  # Non-blocking find
    return bool(found)

async def add_channel(channel_id: int):
    if not await channel_exist(channel_id):
        await channel_data.insert_one({'_id': channel_id})  # Non-blocking insert
        return

async def del_channel(channel_id: int):
    if await channel_exist(channel_id):
        await channel_data.delete_one({'_id': channel_id})  # Non-blocking delete
        return

async def get_all_channels():
    channel_docs = await channel_data.find().to_list(length=None)  # Non-blocking find
    channel_ids = [doc['_id'] for doc in channel_docs]
    return channel_ids


# Admin Management
async def admin_exist(admin_id: int):
    found = await admins_data.find_one({'_id': admin_id})  # Non-blocking find
    return bool(found)

async def add_admin(admin_id: int):
    if not await admin_exist(admin_id):
        await admins_data.insert_one({'_id': admin_id})  # Non-blocking insert
        return

async def del_admin(admin_id: int):
    if await admin_exist(admin_id):
        await admins_data.delete_one({'_id': admin_id})  # Non-blocking delete
        return

async def get_all_admins():
    users_docs = await admins_data.find().to_list(length=None)  # Non-blocking find
    user_ids = [doc['_id'] for doc in users_docs]
    return user_ids


# Banned User Management
async def ban_user_exist(user_id: int):
    found = await banned_user_data.find_one({'_id': user_id})  # Non-blocking find
    return bool(found)

async def add_ban_user(user_id: int):
    if not await ban_user_exist(user_id):
        await banned_user_data.insert_one({'_id': user_id})  # Non-blocking insert
        return

async def del_ban_user(user_id: int):
    if await ban_user_exist(user_id):
        await banned_user_data.delete_one({'_id': user_id})  # Non-blocking delete
        return

async def get_ban_users():
    users_docs = await banned_user_data.find().to_list(length=None)  # Non-blocking find
    user_ids = [doc['_id'] for doc in users_docs]
    return user_ids

