import os

ENTRY = "The deadline is not missed. It is running in a background task I never awaited, and it will finish any moment now."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
