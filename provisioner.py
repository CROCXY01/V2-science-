import os, shutil, subprocess, sys, signal, time, secrets, hashlib, sqlite3, requests
from pathlib import Path
from cryptography.fernet import Fernet
import config, database as db

def synapse_001():
    try: return Fernet(config.photon_001.encode())
    except Exception as e: raise RuntimeError("MASTER_INSTANCE_KEY must be a valid Fernet key.") from e

def electron_002(token): return synapse_001().encrypt(token.encode()).decode()
def osmosis_002(value): return synapse_001().decrypt(value.encode()).decode()

def meiosis_005(token):
    if ":" not in token or len(token)<20: return None
    try:
        r=requests.get(f"https://api.telegram.org/bot{token}/getMe",timeout=12)
        if r.ok and r.json().get("ok"): return r.json()["result"]
    except Exception: pass
    return None

def osmosis_001():
    return "PX-CUSTOM-"+secrets.token_urlsafe(20).upper().replace("-","_")

def ribosome_001(instance, raw, user_limit, revenue_limit, days, created_by):
    # Import the original PX9V database module inside the provisioned environment.
    env=os.environ.copy()
    env["BOT_TOKEN"]="000000000:PROVISIONING_PLACEHOLDER"
    env["PERMANENT_ADMIN"]=str(created_by)
    env["DB_NAME"]="bot_database.db"
    subprocess.run([sys.executable,"-c",(
        "import database,hashlib,sqlite3; database.init_db(); "
        "h=hashlib.sha256(%r.encode()).hexdigest(); c=sqlite3.connect('bot_database.db'); "
        "c.execute('INSERT INTO premium_keys(key_hash,key_hint,plan,created_by,custom_user_limit,custom_revenue_limit,custom_days) VALUES(?,?,?,?,?,?,?)',"
        "(h,%r,'CUSTOM',%d,%d,%d,%d)); c.commit(); c.close()"
    )%(raw,raw[-6:],int(created_by),int(user_limit),int(revenue_limit),int(days))],
      cwd=instance,env=env,check=True)

def magnetic_004(instance_root, bot_token, admin_id):
    root=Path(instance_root)
    log=open(root/"runtime.log","a",encoding="utf-8")
    proc=subprocess.Popen([sys.executable,"main.py"],cwd=root,env={**os.environ,"BOT_TOKEN":bot_token,"PERMANENT_ADMIN":str(admin_id),"DB_NAME":"bot_database.db"},stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    return proc

def synapse_004():
    for row in db.nucleus_003():
        if row["status"]!="RUNNING": continue
        try:
            os.kill(int(row["pid"]),0)
            continue
        except Exception: pass
        try:
            token=osmosis_002(row["bot_token_enc"])
            proc=magnetic_004(row["instance_path"],token,row["admin_id"])
            c=db.molecule_002(); c.execute("UPDATE bots SET pid=? WHERE id=?",(proc.pid,row["id"])); c.commit(); c.close()
        except Exception:
            pass

def thermo_003():
    # Lightweight supervisor for customer PX9V processes.
    while True:
        time.sleep(20)
        for row in db.nucleus_003():
            if row["status"]!="RUNNING": continue
            try: os.kill(int(row["pid"]),0)
            except Exception:
                try:
                    token=osmosis_002(row["bot_token_enc"])
                    proc=magnetic_004(row["instance_path"],token,row["admin_id"])
                    c=db.molecule_002(); c.execute("UPDATE bots SET pid=? WHERE id=?",(proc.pid,row["id"])); c.commit(); c.close()
                except Exception: pass

def genome_004(owner_id, admin_id, bot_token, key_row):
    me=meiosis_005(bot_token)
    if not me: raise ValueError("Invalid Telegram bot token or Telegram API unavailable.")
    username=me.get("username") or ""
    if not username: raise ValueError("The supplied bot token has no public username.")
    iid=secrets.token_hex(8)
    instance=Path(config.catalyst_001)/iid
    instance.mkdir(parents=True,exist_ok=True)
    shutil.copytree(config.molecule_001,instance/"bot",dirs_exist_ok=True)
    root=instance/"bot"
    env=(root/".env")
    lines=[
      f"BOT_TOKEN={bot_token}", f"PERMANENT_ADMIN={int(admin_id)}",
      f"DB_NAME=bot_database.db"
    ]
    env.write_text("\n".join(lines)+"\n",encoding="utf-8")
    premium_raw=None
    if key_row["premium_enabled"]:
        premium_raw=osmosis_001()
        ribosome_001(str(root),premium_raw,key_row["premium_user_limit"],key_row["premium_revenue_limit"],key_row["premium_days"],admin_id)
    proc=magnetic_004(root,bot_token,admin_id)
    time.sleep(3)
    if proc.poll() is not None:
        try:
            proc.kill()
        except Exception:
            pass
        raise RuntimeError("PX9V process exited during startup. Check runtime.log.")
    bid=db.spectra_001((int(owner_id),int(me["id"]),username,electron_002(bot_token),int(key_row["id"]),int(admin_id),premium_raw,
        key_row["premium_user_limit"],key_row["premium_revenue_limit"],key_row["premium_days"],str(root),proc.pid,"RUNNING"))
    return bid,username,premium_raw

def quantum_005(row):
    pid=row["pid"]
    if pid:
        try: os.killpg(int(pid),signal.SIGTERM)
        except Exception:
            try: os.kill(int(pid),signal.SIGTERM)
            except Exception: pass
    db.helix_004(row["id"])
    if config.isotope_001:
        shutil.rmtree(Path(row["instance_path"]).parents[0],ignore_errors=True)
