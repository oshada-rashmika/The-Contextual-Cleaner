# 📂 Contextual File Agent

**Organize your chaos using Multimodal AI**  
*"Don't just sort by file extension. Sort by meaning."*

This **Agentic AI script** doesn't care if a file is a `.jpg` or a `.txt`. It opens the file, reads the content (using Vision or Text analysis), and intelligently decides which folder it belongs to.  

---

## 📸 The Problem vs. The Solution

❌ **The Old Way (Regex/Extensions)**
invoice.pdf -> Goes to /Documents (Vague)
screenshot_123.png -> Goes to /Images (Useless)

✅ **The Agentic Way (Gemini 2.5)**
invoice.pdf -> AI sees "Amount Due" -> Moves to /Finance
screenshot_123.png -> AI sees Python code -> Moves to /Coding_Notes

---

## 🌳 How it Works

The agent scans a target directory and reorganizes it based on the content of the files.  

**Example:**
```text
📂 Downloads (Messy)           📂 Downloads (Cleaned)
├── 📄 note.txt          👉    ├── 📂 Personal
├── 🖼️ receipt.jpg       👉    │   └── 📄 note.txt (Shopping list)
├── 🖼️ code_snip.png     👉    ├── 📂 Finance
└── 📄 essay.txt         👉    │   └── 🖼️ receipt.jpg
                               ├── 📂 Coding
                               │   └── 🖼️ code_snip.png
                               └── 📂 Work
                                   └── 📄 essay.txt
```

---

## 🛠️ Tech Stack

| Component | Technology | Role |
|-----------|-----------|------|
| Brain     | Gemini 2.5 Flash | Ultra-fast multimodal reasoning (Text + Vision) |
| Language  | Python    | Core logic and file operations |
| Vision    | Pillow (PIL) | Image processing and handling |
| File Ops  | Shutil    | High-level file operations (Move/Copy) |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/contextual-file-agent.git
cd contextual-file-agent
