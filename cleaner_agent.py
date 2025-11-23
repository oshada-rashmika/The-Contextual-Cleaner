import os
import shutil
import google.generativeai as genai
from PIL import Image

#CONFIGURATION
API_KEY = "YOUR_API_KEY_HERE" #Google AI Cloud API
TARGET_FOLDER = "AI_Cleaner_Test" #The folder we want to clean (In this case, AI_Cleaner_Test)
#Define the allowed categories to keep the AI focused
CATEGORIES = ["Finance", "Coding", "Personal", "Work", "Random"]

#Configure the AI
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

def get_category_from_image(image_path):
    #Shows the image to Gemini and asks for a category
    try:
        img = Image.open(image_path)
        prompt = (
            f"Analyze this image. Categorize it into exactly one of these folders: {CATEGORIES}. "
            "Return ONLY the category name. No extra text."
        )
        response = model.generate_content([prompt, img])
        return response.text.strip()
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

def get_category_from_text(file_path):
    #Reads the text file and asks Gemini for a category
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read(1000)
        
        prompt = (
            f"Analyze this text content: '{content}'. "
            f"Categorize it into exactly one of these folders: {CATEGORIES}. "
            "Return ONLY the category name."
        )
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error processing text {file_path}: {e}")
        return None

def move_file(file_name, category):
    #Moves the file into the subfolder matching the category
    #Create the path for the category folder
    category_folder = os.path.join(TARGET_FOLDER, category)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)
        print(f"Created new folder: {category}")

    #Move the file
    source_path = os.path.join(TARGET_FOLDER, file_name)
    destination_path = os.path.join(category_folder, file_name)
    
    #Handle duplicate names to avoid overwriting
    if os.path.exists(destination_path):
        base, extension = os.path.splitext(file_name)
        destination_path = os.path.join(category_folder, f"{base}_copy{extension}")

    shutil.move(source_path, destination_path)
    print(f"Moved '{file_name}' to /{category}")

def main():
    print(f"🤖 Agent starting cleanup on: {TARGET_FOLDER}...")
    
    #Loop through every file in the folder
    for file_name in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, file_name)

        #Skip if it's a directory or the script itself
        if os.path.isdir(file_path) or file_name == "cleaner_agent.py":
            continue

        print(f"Analyzing: {file_name}...")
        
        category = None
        #Decide how to process based on extension
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            category = get_category_from_image(file_path)
        elif file_name.lower().endswith('.txt'):
            category = get_category_from_text(file_path)
        
        #If the AI gave us a valid category, move it
        if category in CATEGORIES:
            move_file(file_name, category)
        else:
            print(f"Skipped {file_name} (Could not categorize or file type not supported)")

if __name__ == "__main__":
    main()