import os

def generate_code(intent: str, skills_context: str, constraints: list, injection_data: dict = None) -> str:
    """
    Role: [Low-Level C-Crystallizer] (Phase 5: Hard-Wired Evolution context)
    不再依賴 C 去 Parse JSON，而是利用 AI/Engine 將 JSON 的變數轉換為 Static Injection 成為執行效能。
    """
    if injection_data is None:
        injection_data = {}
        
    # 解讀意圖：如果具備需要常駐執行的 Loop/Daemon 定義，注入 Clean Shutdown Protocol。
    is_daemon = "daemon" in intent.lower() or "looping" in intent.lower()
    
    mock_output = skills_context + "\n"
    
    if is_daemon:
        mock_output += "#include <signal.h>\n"
        mock_output += "#include <unistd.h>\n\n"
        mock_output += "volatile sig_atomic_t keep_running = 1;\n"
        mock_output += "void sig_handler(int sig) {\n"
        mock_output += '    printf("\\n[C-Kernel Process] Signal caught! Initiating Clean Shutdown Protocol...\\n");\n'
        mock_output += "    keep_running = 0;\n"
        mock_output += "}\n\n"
        
    if "@AI:" in intent:
        mock_output += "int main() {\n"
        mock_output += "    // [Hard-Wired Evolution v5.0 Output]\n"
        
        # Static Const Variable Mapping
        for key, val in injection_data.items():
            mock_output += f"    static const int {key.upper()} = {val};\n"
            
        if is_daemon:
            mock_output += "\n    // Wiring Handlers for Auto Hot-Swapping\n"
            mock_output += "    signal(SIGTERM, sig_handler);\n"
            mock_output += "    signal(SIGINT, sig_handler);\n"
            
            mock_output += '    printf("[C-Kernel] Started purely natively. Hardwired TEMP=%d.\\n", TEMP);\n'
            mock_output += "    while(keep_running) {\n"
            mock_output += '        printf("[C-Kernel] Looping / Reading Static Hard-Wired Config. TEMP: %d\\r", TEMP);\n'
            mock_output += '        fflush(stdout);\n'
            mock_output += '        sleep(1);\n'
            mock_output += "    }\n"
            mock_output += '    printf("\\n[C-Kernel] Data-Logic Decoupling complete. Process self-terminated safely.\\n");\n'
        else:
            mock_output += '    printf("Evolution completed seamlessly without daemon intent.\\n");\n'
            
        mock_output += "    return 0;\n"
        mock_output += "}\n"
        return mock_output
        
    return intent
