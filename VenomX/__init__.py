from PROFESSOR-SOURABH.core.bot import SOURABH
from PROFESSOR-SOURABH.core.dir import dirr
from PROFESSOR-SOURABH.core.git import git
from PROFESSOR-SOURABH.core.userbot import Userbot
from PROFESSOR-SOURABH.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SOURABH()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
