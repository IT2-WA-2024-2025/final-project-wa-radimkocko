import json  
from pathlib import Path  
from threading import Lock  

DATA_PATH = Path(__file__).parent / "users.json"
_lock = Lock()  

def _load_data():
    """Načte obsah JSON souboru nebo vrátí prázdnou strukturu, pokud soubor neexistuje."""
    if not DATA_PATH.exists(): 
        return {"users": []}    
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))

def _save_data(data):
    """Uloží Python slovník do JSON souboru s odsazením pro čitelnost."""
    DATA_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")

def get_all_users():
    """Vrátí seznam všech uživatelských slovníků."""
    with _lock:                  
        data = _load_data()      
    return data.get("users", []) 

def find_user(username):
    """Najde slovník uživatele podle uživatelského jména, nebo vrátí None."""
    return next((u for u in get_all_users() if u["username"] == username), None)

def add_user(username, raw_password):
    """
    Přidá nový záznam uživatele s heslem v čistém textu.
    Pozor: Heslo není zabezpečené!
    """
    with _lock:                   
        data = _load_data()       
        data.setdefault("users", []).append({
            "username": username, 
            "password": raw_password  
        })
        _save_data(data)         

def verify_password(user_dict, raw_password):
    """
    Porovná zadané heslo s uloženým textem.
    Vrátí False, pokud slovník uživatele neexistuje nebo hesla nesouhlasí.
    """
    if not user_dict:            
        return False             
    return user_dict["password"] == raw_password