import sys
import os
import glob
from parser import parse_seed
from ai_module import generate_code
from logger import log_evolution
from watch import check_evolution_drift
from validator import validate_seed

SKILLS_DIR = "skills"

def find_skill_code(tag_name: str) -> str:
    search_pattern = os.path.join(SKILLS_DIR, "**", f"{tag_name}.skill")
    matches = glob.glob(search_pattern, recursive=True)
    if matches:
        with open(matches[0], "r", encoding="utf-8") as f:
            print(f"[Engine] Loaded Knowledge Skill: {tag_name}")
            return f.read() + "\n"
    print(f"[!] Warning: Could not find skill module for '{tag_name}'")
    return ""

def run_evolution(seed_file_path: str):
    if not os.path.exists(seed_file_path):
        print(f"[-] 錯誤：找不到種子檔案 {seed_file_path}")
        sys.exit(1)
        
    print(f"\n[Engine] 啟動 Phase 5 Hard-Wired 編譯器。分析檔案: {seed_file_path} ...")
    
    # 1. 語意解析
    meta_tags, constraints, evo_ref, intent, injection_source = parse_seed(seed_file_path)
    
    # 2. 標籤與靜態屬性驗證 (Validator)
    is_valid, injection_data = validate_seed(meta_tags, constraints, intent, injection_source)
    if not is_valid:
        print("[Engine] 🛑 驗證失敗中止。安全護城河擋下了可能崩潰或越界的系統編譯。")
        sys.exit(1)
        
    # 3. 裝載知識存取
    skills_context = ""
    for tag in meta_tags["skills"]:
        skills_context += find_skill_code(tag)
        
    # 4. Low-Level C-Crystallizer: Static Injection (Hard-wiring into C output)
    print(f"[Engine] 執行 Static Configuration Injection: {str(injection_data)}")
    evolved_code = generate_code(intent, skills_context, constraints, injection_data)
    
    target_module = os.path.basename(seed_file_path).replace(".seed", "")
    module_name = target_module.split('.')[0]
    
    # 5. Drift & Anti-Entropy 制衡
    drift_ratio, drift_msg = check_evolution_drift(evolved_code, snapshot_name=module_name)
    print(f"[Engine] {drift_msg}")
    
    if drift_ratio > 0.05:
        print("\n[!] 警告：邏輯漂移大於 5%。")
        sys.exit(1)
        
    # [新增] 清理過期備份檔管理，避免大量膨脹備份。限制只保存最新 2 次歷史。
    from pathlib import Path
    try:
        snaps = sorted(Path('snapshots').glob(f'{module_name}*.c'), key=os.path.getmtime)
        while len(snaps) > 2:
            oldest = snaps.pop(0)
            os.remove(oldest)
            print(f"[Engine] 🚮 清理過期快照以節省容量: {oldest}")
    except Exception as e:
        pass
        
    # 寫入晶化結果
    with open(target_module, "w", encoding="utf-8") as f:
        f.write(evolved_code)
        
    print(f"[Engine] Hard-Wired Crystallization 成功! 輸出至: {target_module}")
    log_evolution(module_name=target_module, drift_ratio=drift_ratio, 
                  logic_delta=f"靜態寫入常數配置: {str(injection_data)}. 架構驗證過關。",
                  healing_note="Compiled seamlessly under v5.0 protocols.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python engine.py <seed_file>")
        sys.exit(1)
    run_evolution(sys.argv[1])
