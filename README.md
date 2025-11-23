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
git clone https://github.com/oshada-rashmika/The-Contextual-Cleaner.git
cd contextual-file-agent
```

### 2. Install Dependencies
We use the Google Generative AI SDK and Pillow for image processing:

```python
pip install google-generativeai pillow
```

### 3. Configure API Key
Get your free key from **Google AI Studio**.
Open *cleaner_agent.py* and paste it:

```python
API_KEY = "PASTE_YOUR_KEY_HERE"
```

### 4. Run the Agent
**⚠️ Warning:** Always test on a dummy folder first!

```python
python cleaner_agent.py
```
---

## ⚙️ Configuration

Customize the logic by editing the global variables at the top of `cleaner_agent.py`:

```python
# The folder you want to clean
TARGET_FOLDER = "AI_Cleaner_Test" 

# The categories the AI is allowed to choose from
CATEGORIES = [
    "Finance", 
    "Coding", 
    "University", 
    "Memes", 
    "Work"
]
```
---

## 🔮 Roadmap

- [x] **Phase 1:** Image & Text Categorization (Implemented)
- [ ] **Phase 2:** PDF Support (Reading invoices/papers)
- [ ] **Phase 3:** CLI Arguments (Pass folder path via command line)
- [ ] **Phase 4:** "Dry Run" Mode (Preview changes before moving)
- [ ] **Phase 5:** Background Service (Watch folder for new files)

---

## ❓ FAQ & Troubleshooting

<details>
<summary><strong>Click to expand: I'm getting a 404 Model Not Found error?</strong></summary>

You are likely using an old model name in the code.
1. Run `pip install --upgrade google-generativeai`
2. Update the model name in the script to `gemini-2.5-flash` or check your available models.
</details>

<details>
<summary><strong>Click to expand: Is this safe to run on my whole computer?</strong></summary>

**No!** Agents are powerful. Always run this on a specific subfolder (like `Downloads/To_Sort`) rather than your root `C:/` drive. The script creates folders and moves files; always keep a backup while testing.
</details>

---

## 🤝 Contributing

Got an idea?

1. Fork it.
2. Create a branch (`git checkout -b feature/NewFeature`).
3. Commit your changes.
4. Push to the branch.
5. Open a Pull Request.

---

*Built with ❤️ by Oshada Rashmika using the Zero-Cost AI Stack.*
