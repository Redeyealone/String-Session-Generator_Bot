import os
class Config:
    API_ID = int(os.environ.get('API_ID', 6435225))
    API_HASH = str(os.environ.get('API_HASH', 4e984ea35f854762dcde906dce426c2d))
    BOT_TOKEN = str(os.environ.get('BOT_TOKEN', 6571094339:AAGcENp3AmPPJslc88ERGsT_VdJ20hKTtvQ))
    MONGO_URI = str(os.environ.get('MONGO_URI', mongodb+srv://Mrdaxx123:Mrdaxx123@cluster0.q1da65h.mongodb.net/?retryWrites=true&w=majority))
    UPDATES_CHANNEL = str(os.environ.get('UPDATES_CHANNEL', Matching_pfp_Gallery)) #Start Without @
