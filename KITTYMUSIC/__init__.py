#
# Copyright (C) 2024 by Moonshining1@Github, < https://github.com/Moonshining1 >.
#
# This file is part of < https://github.com/Moonshining1/KITTYMUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/Moonshining1/KITTYMUSIC/blob/master/LICENSE >
#
# All rights reserved.

from KITTYMUSIC.core.bot import KITTYBot
from KITTYMUSIC.core.dir import dirr
from KITTYMUSIC.core.git import git
from KITTYMUSIC.core.userbot import Userbot
from KITTYMUSIC.misc import dbb, heroku, sudo

from .logging import LOGGER

# Bot Client

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

app = KITTYBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}
