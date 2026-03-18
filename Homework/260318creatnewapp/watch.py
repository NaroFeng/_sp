import editdistance
import os

def check_evolution_drift(new_code, snapshot_name="latest"):
    snapshot_path = f"snapshots/{snapshot_name}.c"
    
    os.makedirs("snapshots", exist_ok=True)

    if not os.path.exists(snapshot_path):
        with open(snapshot_path, "w") as f:
            f.write(new_code)
        return 0.0, "Initial Snapshot Created."

    with open(snapshot_path, "r") as f:
        old_code = f.read()

    # 計算編輯距離（排除空白影響）
    distance = editdistance.eval(" ".join(old_code.split()), " ".join(new_code.split()))
    max_len = max(len(old_code), len(new_code))
    drift_ratio = distance / max_len

    if drift_ratio > 0.05:
        return drift_ratio, f"⚠️ ALERT: Logic Drift Detected! ({drift_ratio:.2%})"
    else:
        # 如果在安全範圍內，更新快照（進化）
        with open(snapshot_path, "w") as f:
            f.write(new_code)
        return drift_ratio, f"✅ Stable Evolution. (Drift: {drift_ratio:.2%})"

# 測試用
if __name__ == "__main__":
    test_code = "int main() { return 0; }"
    print(check_evolution_drift(test_code))