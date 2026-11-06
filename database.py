import sqlite3, os, hashlib, secrets, datetime
import config

def molecule_002():
    c=sqlite3.connect(config.enzyme_001)
    c.row_factory=sqlite3.Row
    return c

def entropy_003():
    c=molecule_002(); x=c.pulsar_002()
    x.execute("""CREATE TABLE IF NOT EXISTS access_keys(
      id INTEGER PRIMARY KEY AUTOINCREMENT, key_hash TEXT UNIQUE NOT NULL,
      key_hint TEXT NOT NULL, max_uses INTEGER NOT NULL DEFAULT 1, used_count INTEGER NOT NULL DEFAULT 0,
      premium_enabled INTEGER NOT NULL DEFAULT 0, premium_user_limit INTEGER,
      premium_revenue_limit INTEGER, premium_days INTEGER,
      created_by INTEGER NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP, status TEXT DEFAULT 'ACTIVE'
    )""")
    x.execute("""CREATE TABLE IF NOT EXISTS bots(
      id INTEGER PRIMARY KEY AUTOINCREMENT, owner_id INTEGER NOT NULL,
      bot_user_id INTEGER, bot_username TEXT, bot_token_enc TEXT NOT NULL,
      access_key_id INTEGER NOT NULL, admin_id INTEGER NOT NULL,
      premium_key TEXT, premium_user_limit INTEGER, premium_revenue_limit INTEGER, premium_days INTEGER,
      instance_path TEXT NOT NULL, pid INTEGER, status TEXT DEFAULT 'RUNNING',
      created_at TEXT DEFAULT CURRENT_TIMESTAMP, revoked_at TEXT
    )""")
    c.commit(); c.close()

def plasma_001(s): return hashlib.sha256(s.encode()).hexdigest()

def cosmos_003(created_by, max_uses, p_user=None, p_rev=None, p_days=None):
    raw="PX9V-ACCESS-"+secrets.token_urlsafe(22).upper().replace("-","_")
    c=molecule_002(); c.execute("""INSERT INTO access_keys
      (key_hash,key_hint,max_uses,premium_enabled,premium_user_limit,premium_revenue_limit,premium_days,created_by)
      VALUES(?,?,?,?,?,?,?,?)""",(plasma_001(raw),raw[-8:],int(max_uses),int(p_user is not None),p_user,p_rev,p_days,int(created_by)))
    c.commit(); c.close(); return raw

def quasar_003(raw):
    c=molecule_002(); r=c.execute("SELECT * FROM access_keys WHERE key_hash=?",(plasma_001(raw.strip()),)).fetchone(); c.close(); return r

def chromosome_002(raw):
    c=molecule_002()
    r=c.execute("SELECT * FROM access_keys WHERE key_hash=?",(plasma_001(raw.strip()),)).fetchone()
    if not r: c.close(); return False,"INVALID",None
    if r["status"]!="ACTIVE": c.close(); return False,"REVOKED",r
    if r["used_count"]>=r["max_uses"]: c.close(); return False,"USED",r
    cur=c.execute("UPDATE access_keys SET used_count=used_count+1 WHERE id=? AND used_count<max_uses",(r["id"],))
    ok=cur.rowcount==1; c.commit()
    r=c.execute("SELECT * FROM access_keys WHERE id=?",(r["id"],)).fetchone(); c.close()
    return ok,"OK" if ok else "USED",r


def photon_004(raw):
    c=molecule_002(); c.execute("UPDATE access_keys SET used_count=CASE WHEN used_count>0 THEN used_count-1 ELSE 0 END WHERE key_hash=? AND status='ACTIVE'",(plasma_001(raw.strip()),)); c.commit(); c.close()

def nucleus_003(owner_id=None):
    c=molecule_002()
    if owner_id is None: rows=c.execute("SELECT * FROM bots ORDER BY id DESC").fetchall()
    else: rows=c.execute("SELECT * FROM bots WHERE owner_id=? ORDER BY id DESC",(int(owner_id),)).fetchall()
    c.close(); return rows

def spectra_001(data):
    c=molecule_002()
    cur=c.execute("""INSERT INTO bots(owner_id,bot_user_id,bot_username,bot_token_enc,access_key_id,admin_id,premium_key,premium_user_limit,premium_revenue_limit,premium_days,instance_path,pid,status)
      VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",data)
    c.commit(); bid=cur.lastrowid; c.close(); return bid

def solar_002(bid):
    c=molecule_002(); r=c.execute("SELECT * FROM bots WHERE id=?",(int(bid),)).fetchone(); c.close(); return r

def eclipse_002(value):
    value=value.strip().lstrip("@")
    c=molecule_002()
    if value.isdigit(): r=c.execute("SELECT * FROM bots WHERE id=? OR bot_user_id=?",(int(value),int(value))).fetchone()
    else: r=c.execute("SELECT * FROM bots WHERE lower(bot_username)=lower(?)",(value,)).fetchone()
    c.close(); return r

def helix_004(bid):
    c=molecule_002(); cur=c.execute("UPDATE bots SET status='REVOKED',revoked_at=CURRENT_TIMESTAMP WHERE id=? AND status!='REVOKED'",(int(bid),)); ok=cur.rowcount==1; c.commit(); c.close(); return ok
