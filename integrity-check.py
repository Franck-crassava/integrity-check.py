import hashlib
import argparse
import os

def calculate_hash(file_path, algorithm):
    hash_func = getattr(hashlib, algorithm.lower())()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
        return None

def compare_hash(file_path, expected_hash, algorithm):
    computed = calculate_hash(file_path, algorithm)
    if not computed:
        return False
    match = computed.lower() == expected_hash.lower()
    print(f"[+] {algorithm.upper()} for {file_path}: {computed}")
    print(f"{'✅ Match' if match else '❌ Does not match'}")
    return match

def main():
    parser = argparse.ArgumentParser(description="🧩 Integrity checker - Hash your files and compare integrity")
    parser.add_argument("file", help="File to check")
    parser.add_argument("-a", "--algorithm", choices=hashlib.algorithms_available, default="sha256", help="Hash algorithm to use (default: sha256)")
    parser.add_argument("-c", "--compare", help="Expected hash value to compare with")
    args = parser.parse_args()

    if args.compare:
        compare_hash(args.file, args.compare, args.algorithm)
    else:
        h = calculate_hash(args.file, args.algorithm)
        if h:
            print(f"[+] {args.algorithm.upper()} for {args.file}: {h}")

if __name__ == "__main__":
    main()

