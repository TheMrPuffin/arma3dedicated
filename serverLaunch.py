import subprocess
import os
import shutil
import re

subprocess.call(["/home/steam/steamcmd/steamcmd.sh", "+login", os.environ["STEAM_USER"], os.environ["PASSWORD"], "+force_install_dir", "/home/steam/arma3-dedicated", "+app_update", "233780", "validate", "+quit"])

launch = './arma3server_x64 -name="puffnetserver" -config="./configs/server.cfg" -profiles="./configs/profiles/" -port=2302'

os.system(launch)