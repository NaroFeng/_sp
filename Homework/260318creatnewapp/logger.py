import datetime
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "evolution_history.md")

def log_evolution(module_name: str, drift_ratio: float, logic_delta: str, healing_note: str = "N/A"):
    """
    [Stability & Auto-Healing Mode v2.0]
    為每一次軟體的疊代與進化，自動寫入包含防呆、推論與修復歷程的版本更新紀錄。
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 若日誌資料夾不存在則建立
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR, exist_ok=True)
        
    # 若檔案不存在則建立標題
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("# Evolution Framework - Auto-Healing Version Log v2.0\n\n")
            
    log_entry = f"### Module: {module_name}\n"
    log_entry += f"- [{timestamp}]\n"
    log_entry += f"- [Evolution Drift %]: {drift_ratio:.2%}\n"
    log_entry += f"- [Logic Delta]: {logic_delta}\n"
    log_entry += f"- [Healing Note]: {healing_note}\n\n"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)
