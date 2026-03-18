import os
import json

def validate_seed(meta_tags: dict, constraints: list, body_intent: str, injection_source: str = None) -> (bool, dict):
    """
    [形式化驗證 (Formal Verification) & Hard-Wired Evolution v5.0]
    驗證標籤衝突，並載入 JSON 變形注入，執行約束擋板。
    """
    conflicts = []
    skills = meta_tags.get("skills", [])
    
    intent_is_fast = "O(1)" in body_intent or any("fast" == c.strip() for c in constraints)
    has_io = "c_standard_io" in skills
    
    if intent_is_fast and has_io:
        conflicts.append("Conflict: 要求 'fast' 卻引入 'c_standard_io'。")
        
    has_static = any("static_memory" == c.strip() for c in constraints)
    if has_static and "dynamic_allocation" in skills:
        conflicts.append("Conflict: <constraint> 限制為 'static_memory'，但引入了動態記憶體。")

    # Safe Defaulting 預設變數護城河
    injection_data = {
        "temp": 25,
        "mode": 0
    }
    
    if injection_source:
        if os.path.exists(injection_source):
            try:
                with open(injection_source, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    injection_data.update(data)
                print(f"[Validator] 成功載入靜態注入庫: {injection_source}")
            except json.JSONDecodeError:
                print(f"[Validator] ⚠️ 警告：JSON 配置損壞！啟用 Safe Defaulting...")
        else:
            print(f"[Validator] ⚠️ 警告：找不到 {injection_source}！啟用 Safe Defaulting...")
            
    # Hard-Wired Evolution v5.0 安全界線檢測
    for c in constraints:
        if "max_temp:" in c:
            try:
                max_val = int(c.split(":")[1].strip())
                if "temp" in injection_data and injection_data["temp"] > max_val:
                    conflicts.append(f"Security Reject: JSON 配置 (temp={injection_data['temp']}) 突破了硬約束 <constraint> max_temp: {max_val}！")
            except ValueError:
                pass

    if conflicts:
        print("\n[Validator] 🛑 發現標籤邏輯衝突或越界 (Formal Verification Failed):")
        for c in conflicts:
            print(f"  - {c}")
        return False, {}
        
    print("[Validator] ✅ 邏輯自洽且注入數據安全，驗證通過。")
    return True, injection_data
