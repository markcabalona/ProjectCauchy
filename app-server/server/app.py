import os
import sys

# Add the parent directory of 'games' (i.e., 'app-server') to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("DEV_HOST")

# Import modules
from games.bigwheel import pipeline_bigwheel
from games.baccarat import pipeline_baccarat
from games.roulette import roulette_pipeline
from games.blackjack import blackjack_pipeline

def create_directory_if_not_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created.")


create_directory_if_not_exists('data')
roulette_pipeline(base_url=URL)
blackjack_pipeline(base_url=URL)
pipeline_bigwheel(URL)
pipeline_baccarat(URL)