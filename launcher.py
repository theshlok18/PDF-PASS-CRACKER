#!/usr/bin/env python3
"""
STARK PDF PASS CRACKER Launcher
Choose between CLI and GUI versions

Author: Shlok (@theshlok18)
GitHub: https://github.com/theshlok18/PDF-PASS-CRACKER
"""

import sys
import subprocess
from pathlib import Path
from banner import show_banner

def main():
    show_banner()
    print("1. 🚀 Ultra-Fast GUI (50k+ att/sec)")
    print("2. 🎯 Ultra-Fast CLI (Lightning Mode)")
    print("3. 📊 Performance Benchmark")
    print("4. 🔧 Standard GUI")
    print("5. 📋 Standard CLI")
    print("6. ⚡ Lightning Speed Test")
    print("7. 🔨 Create Test PDFs")
    print("8. 💡 Performance Tips")
    print("9. Exit")
    
    while True:
        choice = input("\nSelect option (1-9): ").strip()
        
        if choice == "1":
            print("🚀 Starting Ultra-Fast GUI...")
            subprocess.run([sys.executable, "gui.py"])
            break
        elif choice == "2":
            print("🎯 Ultra-Fast CLI Usage:")
            print("python3.11 ultra_fast_cracker.py target.pdf --lightning    # 50k+ att/sec")
            print("python3.11 ultra_fast_cracker.py target.pdf --smart --dict rockyou.txt  # 20k att/sec")
            print("python3.11 ultra_fast_cracker.py --performance  # Show speed comparison")
            break
        elif choice == "3":
            print("📊 Running performance benchmark...")
            subprocess.run([sys.executable, "performance_test.py"])
            break
        elif choice == "4":
            print("🔧 Starting Standard GUI...")
            subprocess.run([sys.executable, "gui.py"])
            break
        elif choice == "5":
            print("📋 Standard CLI Usage:")
            print("python3.11 main.py target.pdf --lightning")
            print("python3.11 main.py target.pdf --dict rockyou.txt --smart")
            print("python3.11 main.py --speed  # Show speed comparison")
            break
        elif choice == "6":
            print("⚡ Ultra-fast lightning test...")
            subprocess.run([sys.executable, "ultra_fast_cracker.py", "test_medium.pdf", "--lightning"])
            break
        elif choice == "7":
            print("🔨 Creating test PDFs...")
            subprocess.run([sys.executable, "create_test_pdf.py"])
            break
        elif choice == "8":
            subprocess.run([sys.executable, "ultra_fast_cracker.py", "--performance"])
            break
        elif choice == "9":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-9.")

if __name__ == "__main__":
    main()