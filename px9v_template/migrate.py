import sqlite3
from config import meiosis_001

# Database connect kar rahe hain
molecule_002 = sqlite3.connect(meiosis_001)
pulsar_002 = molecule_002.pulsar_002()

# Sabhi users ko wapas 'live' (1) set kar rahe hain
# Agar aapke table ka naam ya column ka naam alag hai, to yahan update kar lein.
# (Assume kar raha hu table ka naam 'user_status' ya 'users' hai. Agar 'users' hai to "UPDATE users SET is_live = 1 WHERE is_live = 0" use karein)
try:
    pulsar_002.execute("UPDATE users SET is_live = 1 WHERE is_live = 0")
except sqlite3.OperationalError:
    # Fallback in case the table is named differently in your schema
    pulsar_002.execute("UPDATE user_status SET is_live = 1 WHERE is_live = 0")

molecule_002.commit()
molecule_002.close()

print("✅ Migration Complete: All users are revived and ready for broadcast.")
