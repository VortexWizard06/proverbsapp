import requests
import xml.etree.ElementTree as ET
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key="sk-no-key-required",
    base_url="http://localhost:11434/v1"
)

def load_proverbs_text():
    proverbs_by_chapter = {}

    try:
        # Read Proverbs text from a local file
        tree = ET.parse('proverbs.xml')
        root = tree.getroot()

        # Find Proverbs book
        proverbs_book = root.find(".//BIBLEBOOK[@bname='Proverbs']")
        if proverbs_book is not None:
            # Find all chapters in Proverbs
            for chapter in proverbs_book.findall(".//CHAPTER"):
                chapter_number = int(chapter.attrib.get("cnumber"))
                chapter_verses = {}

                # Find all verses within the chapter
                for verse in chapter.findall(".//VERS"):
                    verse_number = int(verse.attrib.get("vnumber"))
                    verse_text = verse.text.strip()
                    chapter_verses[verse_number] = verse_text

                proverbs_by_chapter[chapter_number] = chapter_verses

            return proverbs_by_chapter
        else:
            print("Proverbs book not found in the XML data.")
    except Exception as e:
        print(f"Error parsing XML: {e}")

    return proverbs_by_chapter

def display_chapter(chapter_number, proverbs_by_chapter):
    if chapter_number in proverbs_by_chapter:
        chapter_verses = proverbs_by_chapter[chapter_number]
        print(f"Chapter {chapter_number}:")
        for verse_number, verse_text in sorted(chapter_verses.items()):
            print(f"Verse {verse_number}: {verse_text}")
    else:
        print(f"Chapter {chapter_number} not found.")

def display_specific_verse(chapter_number, verse_number, proverbs_by_chapter):
    if chapter_number in proverbs_by_chapter and verse_number in proverbs_by_chapter[chapter_number]:
        verse_text = proverbs_by_chapter[chapter_number][verse_number]
        print(f"Verse {chapter_number}:{verse_number}: {verse_text}")
    else:
        print(f"Verse {chapter_number}:{verse_number} not found.")

def keyword_search(keyword, proverbs_by_chapter):
    keyword = keyword.lower()
    found_verses = []
    for chapter_number, chapter_verses in proverbs_by_chapter.items():
        for verse_number, verse_text in chapter_verses.items():
            if keyword in verse_text.lower():
                found_verses.append(f"{chapter_number}:{verse_number}: {verse_text}")
    if found_verses:
        print(f"Verses containing the keyword '{keyword}':")
        for verse in found_verses:
            print(verse)
    else:
        print(f"No verses containing the keyword '{keyword}' found.")

def ask_llama_cpp(question, proverbs_by_chapter, model="LLaMA_CPP"):
    # Check if the question contains relevant keywords
    proverbs_keywords = ["proverbs", "wisdom", "solomon", "saying", "wise", "fool", "instruction"]
    if any(keyword in question.lower() for keyword in proverbs_keywords):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are an AI assistant that answers questions based on the book of Proverbs."},
                    {"role": "user", "content": question}
                ]
            )
            # Debugging output to understand the response structure
            print(f"Response from llama.cpp: {response}")

            # Access the content of the first choice's message
            if response and response.choices:
                return response.choices[0].message.content
            else:
                return "No response from llama.cpp"
        except Exception as e:
            print(f"Error communicating with llama.cpp: {e}")
            return None
    else:
        return "You can only ask questions related to the book of Proverbs."

def main():
    print("Loading Proverbs text...")
    proverbs_by_chapter = load_proverbs_text()
    print("Proverbs text loaded successfully.")

    while True:
        print("\nOptions:")
        print("1. Display all proverbs")
        print("2. Display specific chapter")
        print("3. Search for a specific verse")
        print("4. Search for a keyword")
        print("5. Ask LLaMA_CPP a question based on Proverbs")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            for chapter_number in sorted(proverbs_by_chapter.keys()):
                display_chapter(chapter_number, proverbs_by_chapter)
        elif choice == '2':
            try:
                chapter_number = int(input("Enter chapter number: "))
                display_chapter(chapter_number, proverbs_by_chapter)
            except ValueError:
                print("Invalid input. Please enter a valid chapter number.")
        elif choice == '3':
            try:
                chapter_number = int(input("Enter chapter number: "))
                verse_number = int(input("Enter verse number: "))
                display_specific_verse(chapter_number, verse_number, proverbs_by_chapter)
            except ValueError:
                print("Invalid input. Please enter valid chapter and verse numbers.")
        elif choice == '4':
            keyword = input("Enter keyword: ")
            keyword_search(keyword, proverbs_by_chapter)
        elif choice == '5':
            question = input("Enter your question: ")
            answer = ask_llama_cpp(question, proverbs_by_chapter, model='phi3:latest')
            print(answer)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

