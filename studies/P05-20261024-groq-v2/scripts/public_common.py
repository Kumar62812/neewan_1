import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BATCH='P05-20261024-groq-v2'
BASE=ROOT/'generation/batches'/BATCH
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v,indent=2)+'\n')
