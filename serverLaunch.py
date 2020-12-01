import subprocess
import os
import shutil
import re

subprocess.call(["/home/steam/steamcmd/steamcmd.sh", "+login", os.environ["STEAM_USER"], os.environ["STEAM_PASSWORD"], "+force_install_dir", "/home/steam/arma3-dedicated", "+app_update", "233780", "validate", "+quit"])

launch = './arma3server_x64 -name="puffnetserver" -profiles="./configs/profiles/" -config="./configs/server.cfg" -port=2302 -world=empty”'

os.system(launch)