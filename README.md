# 🧹 Contextual Desktop Cleaner Agent

![Status](https://img.shields.io/badge/Status-Active-green) ![Python](https://img.shields.io/badge/Python-3.11-blue) ![AI](https://img.shields.io/badge/Multimodal-AI-purple)

A **smart desktop organizer** that automatically sorts your messy files by **reading their content**, not just extensions. PDFs, images, code screenshots — all go to the right folders **without lifting a finger**.  

---

## 🌟 Features

- **Contextual Sorting**: Understands file content before categorizing.  
- **PDF Intelligence**: Detects invoices, reports, and other finance documents.  
- **Image Analysis**: Recognizes screenshots, code snippets, and more.  
- **Automated File I/O**: Moves files into structured folders like `/Finance` or `/Dev_Notes`.  
- **Multimodal Capabilities**: Uses text and image understanding for smarter organization.  

---

## ⚡ How It Works

1. Monitors your **Downloads folder** (or any target folder).  
2. Uses **AI vision & text analysis** to inspect file content.  
3. Applies **categorization logic** and moves files to the appropriate folder.  

**Example Folders:**
/Downloads
invoice1.pdf → /Finance
screenshot.png → /Notes
photo.jpg → /Personal


---

## 🛠️ Tech Stack

- **Python 3.11+**  
- **OS & shutil modules** for file operations  
- **Gemini Vision / AI API** for image & text analysis  
- Optional: **Watchdog** for real-time folder monitoring  

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/yourusername/contextual-desktop-cleaner.git
cd contextual-desktop-cleaner

# Install dependencies
pip install -r requirements.txt

# Run the agent
python cleaner_agent.py
