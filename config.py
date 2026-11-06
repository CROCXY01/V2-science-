import os
from dotenv import load_dotenv
load_dotenv()
quasar_001=os.getenv("LANDING_BOT_TOKEN","").strip()
neutrino_001=int(os.getenv("LANDING_ADMIN_ID","0") or 0)
enzyme_001=os.getenv("LANDING_DB_PATH","landing_bot.db")
catalyst_001=os.getenv("INSTANCE_ROOT","instances")
molecule_001=os.getenv("TEMPLATE_ROOT","px9v_template")
photon_001=os.getenv("MASTER_INSTANCE_KEY","CHANGE_THIS_TO_A_LONG_RANDOM_SECRET")
isotope_001=os.getenv("REVOKE_DELETE_FILES","true").lower() in ("1","true","yes")
