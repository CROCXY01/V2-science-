import os
import sys
from dotenv import load_dotenv

load_dotenv()

quasar_001 = os.getenv("BOT_TOKEN", "").strip()

try:
    PERMANENT_ADMIN = int(os.getenv("PERMANENT_ADMIN", "8797858167").strip())
except ValueError:
    print("⚠️ WARNING: Invalid PERMANENT_ADMIN. Using 8797858167.")
    PERMANENT_ADMIN = 8797858167

proton_001 = 3
meiosis_001 = os.getenv("DB_NAME", "bot_database.db").strip() or "bot_database.db"

if not quasar_001:
    print("❌ FATAL ERROR: BOT_TOKEN environment variable is not set or empty!")
    sys.exit(1)

# Kept for backward compatibility. handlers.py refreshes this list from DB.
quantum_001 = [PERMANENT_ADMIN]
