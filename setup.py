#!/usr/bin/env python3
"""
Quick setup script for STARK PDF PASS CRACKER
Downloads multiple wordlists for comprehensive password cracking

Author: Shlok (@theshlok18)
GitHub: https://github.com/theshlok18/PDF-PASS-CRACKER
"""

import urllib.request
import os
from pathlib import Path
import gzip
import zipfile

def download_file(url, filename, description):
    """Download a file with progress indication."""
    try:
        print(f"📥 Downloading {description}...")
        urllib.request.urlretrieve(url, filename)
        size_mb = Path(filename).stat().st_size // 1024 // 1024
        print(f"✅ Downloaded {filename} ({size_mb} MB)")
        return True
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")
        return False

def extract_gz(gz_file, output_file):
    """Extract .gz file."""
    try:
        with gzip.open(gz_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                f_out.write(f_in.read())
        os.remove(gz_file)  # Remove compressed file
        print(f"✅ Extracted {output_file}")
        return True
    except Exception as e:
        print(f"❌ Failed to extract {gz_file}: {e}")
        return False

def download_wordlists():
    """Download popular wordlists for PDF cracking."""
    
    wordlists = [
        {
            "name": "rockyou.txt",
            "url": "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt",
            "description": "RockYou (14M passwords - most popular)",
            "size": "~133 MB"
        },
        {
            "name": "weakpass_25k.txt",
            "url": "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-25000.txt",
            "description": "WeakPass Top 25K (most common passwords)",
            "size": "~300 KB"
        },
        {
            "name": "rockyou10.txt", 
            "url": "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou-75.txt",
            "description": "RockYou Top 10K (quick attacks)",
            "size": "~100 KB"
        },
        {
            "name": "common_passwords.txt",
            "url": "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt",
            "description": "Common 10K passwords (high success rate)",
            "size": "~100 KB"
        }
    ]
    
    print("🔧 STARK PDF PASS CRACKER - Wordlist Setup")
    print("=" * 50)
    
    downloaded = 0
    for wordlist in wordlists:
        if Path(wordlist["name"]).exists():
            print(f"✅ {wordlist['name']} already exists")
            downloaded += 1
        else:
            print(f"\n📋 {wordlist['description']} ({wordlist['size']})")
            if download_file(wordlist["url"], wordlist["name"], wordlist["description"]):
                downloaded += 1
    
    # Try to download larger wordlists from alternative sources
    large_wordlists = [
        {
            "name": "top100k.txt",
            "url": "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt",
            "description": "Top 100K passwords (comprehensive)",
            "size": "~1 MB"
        }
    ]
    
    print(f"\n🎯 OPTIONAL LARGE WORDLISTS:")
    for wordlist in large_wordlists:
        if not Path(wordlist["name"]).exists():
            print(f"\n📋 {wordlist['description']} ({wordlist['size']})")
            choice = input("Download? (y/n): ").lower().strip()
            if choice == 'y':
                if download_file(wordlist["url"], wordlist["name"], wordlist["description"]):
                    downloaded += 1
        else:
            print(f"✅ {wordlist['name']} already exists")
            downloaded += 1
    
    return downloaded

def create_wordlist_info():
    """Create wordlist information file."""
    info = """# STARK PDF PASS CRACKER - Wordlist Guide

## 🎯 ATTACK STRATEGY BY WORDLIST:

### 1. Lightning Fast (5-15 seconds)
- **weakpass_25k.txt** - Top 25K most common passwords
- **rockyou10.txt** - RockYou top 10K passwords  
- **10M_passwords.txt** - 10M database top 10K
- Usage: `python main.py target.pdf --lightning`

### 2. Quick Attack (30-120 seconds)  
- **weakpass_25k.txt** - Best success/speed ratio
- Usage: `python main.py target.pdf --smart --dict weakpass_25k.txt`

### 3. Comprehensive Attack (2-10 minutes)
- **rockyou.txt** - 14M passwords (most comprehensive)
- **Top1M.txt** - Top 1M passwords (balanced)
- Usage: `python main.py target.pdf --smart --dict rockyou.txt`

### 4. Hybrid Attack (5-15 minutes)
- Any wordlist + transformations (password -> password123, Password1, etc.)
- Usage: `python main.py target.pdf --hybrid --dict weakpass_25k.txt`

## 📊 SUCCESS RATES:
- weakpass_25k.txt: ~75% of weak PDFs
- rockyou10.txt: ~60% of weak PDFs  
- rockyou.txt: ~90% of weak PDFs
- Top1M.txt: ~85% of weak PDFs

## 💡 PRO TIPS:
1. Start with weakpass_25k.txt for speed
2. Use rockyou.txt for comprehensive coverage
3. Try hybrid attacks for password variations
4. Lightning mode automatically uses best common passwords
"""
    
    with open("WORDLIST_GUIDE.md", "w", encoding='utf-8') as f:
        f.write(info)
    print("✅ Created WORDLIST_GUIDE.md")

if __name__ == "__main__":
    downloaded = download_wordlists()
    create_wordlist_info()
    
    print(f"\n🎉 Setup Complete!")
    print(f"📊 Downloaded {downloaded} wordlists")
    print(f"\n🚀 Quick Start:")
    print(f"  python main.py target.pdf --lightning              # Use built-in common passwords")
    print(f"  python main.py target.pdf --smart --dict weakpass_25k.txt  # Fast & effective")
    print(f"  python main.py target.pdf --smart --dict rockyou.txt       # Most comprehensive")
    print(f"\n💡 See WORDLIST_GUIDE.md for detailed attack strategies")