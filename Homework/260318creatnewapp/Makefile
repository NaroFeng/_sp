CC = gcc
CFLAGS = -O2

# 預設的種子檔案，若執行 make 時沒指定，預設跑 v2.seed.c
SEED ?= v2.seed.c

# 自動從 .seed.c 推導生成的 .c 與最後的執行檔名稱
SRC_C = $(SEED:.seed.c=.c)
TARGET = $(SEED:.seed.c=)

.PHONY: all check build run clean

# 預設指令 (只打 make 就會一路編譯到執行)
all: run

# 1. 檢測與轉換階段 (使用者提到的 watchdog / engine 漂移檢測)
check:
	@echo "\n============================================="
	@echo "[Makefile] 1. 喚醒 Evolution Engine (漂移檢測 & AI 開發)"
	@echo "============================================="
	python engine.py $(SEED)

# 2. GCC 實體編譯階段
build: check
	@echo "\n============================================="
	@echo "[Makefile] 2. 呼叫 GCC (O2 最佳化) 編譯 $(SRC_C)"
	@echo "============================================="
	$(CC) $(CFLAGS) $(SRC_C) -o $(TARGET)

# 3. 執行階段
run: build
	@echo "\n============================================="
	@echo "[Makefile] 3. 執行二進制軟體: ./$(TARGET)"
	@echo "============================================="
	./$(TARGET)

# 清除開發產物
clean:
	@echo "[Makefile] 清理編譯快取檔..."
	find . -type f -name '*.c' ! -name '*.seed.c' -delete
	rm -f $(TARGET) test v2
