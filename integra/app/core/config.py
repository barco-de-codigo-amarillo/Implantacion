#config.py
import os
from dotenv import load_dotenv

load_dotenv()

# --- Base de datos ---
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    
)