import time
import os
import subprocess
import signal
import sys

# Watchdog Configs
BINARY_NAME = "./v4"
CONFIG_FILE = "config/app.json"
SEED_FILE = "v4.seed.c"

def get_mtime(file_path):
    return os.path.getmtime(file_path) if os.path.exists(file_path) else 0

def recompile():
    print(f"[\033[93mHot-Swap Engine\033[0m] Re-compiling source codebase via GCC ...")
    ret = os.system(f"make build SEED={SEED_FILE} > /dev/null")
    if ret != 0:
        print("[\033[91mHot-Swap Engine\033[0m] Evolution compilation failed! Holding logic state.")
        return False
    return True

def run_daemon():
    last_cfg = get_mtime(CONFIG_FILE)
    last_sd = get_mtime(SEED_FILE)
    
    print("[\033[92mHot-Swap Daemon\033[0m] Started Phase 5 runtime. Observing Data-Logic changes...")
    
    if not os.path.exists(BINARY_NAME):
        if not recompile(): sys.exit(1)
        
    process = subprocess.Popen([BINARY_NAME])
    
    try:
        while True:
            time.sleep(1)
            cur_cfg = get_mtime(CONFIG_FILE)
            cur_sd = get_mtime(SEED_FILE)
            
            if cur_cfg != last_cfg or cur_sd != last_sd:
                print("\n[\033[92mHot-Swap Daemon\033[0m] Mutation detected in codebase/config. Initiating Clean Setup.")
                last_cfg = cur_cfg
                last_sd = cur_sd
                
                print("[\033[93mHot-Swap Daemon\033[0m] Emitting SIGTERM to executing C-process...")
                process.send_signal(signal.SIGTERM)
                process.wait() # Await C program clean shutdown logic
                
                if recompile():
                    print("[\033[92mHot-Swap Daemon\033[0m] Hard-wired dependencies updated. Restarting Kernel.\n")
                    process = subprocess.Popen([BINARY_NAME])
                else:
                    print("[\033[91mHot-Swap Daemon\033[0m] Refusing to initialize on unstable build. Relocating to prior state.\n")
                    process = subprocess.Popen([BINARY_NAME])
                    
    except KeyboardInterrupt:
        print("\n[\033[91mHot-Swap Daemon\033[0m] System Halt Requested. Transmitting Graceful SIGINT.")
        process.send_signal(signal.SIGINT)
        process.wait()

if __name__ == "__main__":
    run_daemon()
