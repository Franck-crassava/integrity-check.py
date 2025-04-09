
# 🧩 Integrity Check

A simple Python tool to calculate and verify the hash of a file to ensure its integrity.

## 💡 Features

- Calculate file hash using common algorithms (SHA256 by default)
- Compare with an expected hash
- Supports multiple algorithms: `sha256`, `md5`, `sha1`, etc.

## 🚀 Usage

```bash
# Calculate SHA256 hash of a file
python main.py example.txt

# Use MD5 instead
python main.py example.txt -a md5

# Compare file hash with expected hash
python main.py example.txt -a sha1 -c d41d8cd98f00b204e9800998ecf8427e
```

## ✅ Requirements
Python 3.7+

## 📂 Example Output
```css
[+] SHA256 for example.txt: e3b0c44298fc1c149afbf4c8996fb924...
✅ Match
```

## 👨‍💻 Author
Franck CRASSAVA – Cybersecurity & Network Architecture Student

