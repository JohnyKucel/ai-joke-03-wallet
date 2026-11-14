import os

JOKE = "Opening my wallet is like cutting an onion \u2014 instant tears."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
