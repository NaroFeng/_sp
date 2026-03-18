import re
import sys

def parse_seed(file_path: str):
    """
    Seed Architect 解析器：強制提取 <meta>, <constraint>, <evolution_ref>, <body>。
    新增 Phase 5 支援：<injection>。
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    meta_match = re.search(r"<meta>(.*?)</meta>", content, re.DOTALL)
    constraint_match = re.search(r"<constraint>(.*?)</constraint>", content, re.DOTALL)
    evo_ref_match = re.search(r"<evolution_ref>(.*?)</evolution_ref>", content, re.DOTALL)
    body_match = re.search(r"<body>(.*?)</body>", content, re.DOTALL)
    injection_match = re.search(r'<injection\s+source="([^"]+)"\s*/>', content)
    
    if not body_match:
        print("[-] 防呆攔截：Seed 檔案必須至少包含 <body> 區塊！")
        sys.exit(1)
        
    meta_text = meta_match.group(1) if meta_match else ""
    skills = re.findall(r'<tag\s+name="([^"]+)"\s*/?>', meta_text)
    env = re.findall(r'<env\s+target="([^"]+)"\s*/?>', meta_text)
    
    constraints_text = constraint_match.group(1).strip() if constraint_match else ""
    constraints = [c.strip() for c in constraints_text.split("\n") if c.strip()]
    
    evo_ref = evo_ref_match.group(1).strip() if evo_ref_match else "latest"
    intent = body_match.group(1).strip()
    injection_source = injection_match.group(1) if injection_match else None
    
    return {
        "skills": skills,
        "env": env[0] if env else "WSL"
    }, constraints, evo_ref, intent, injection_source
