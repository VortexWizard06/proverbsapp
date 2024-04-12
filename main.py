import requests
import xml.etree.ElementTree as ET

def load_proverbs_text():
    proverbs_by_chapter = {}

    # Fetch Proverbs text from GitHub
    url = 'https://raw.githubusercontent.com/seven1m/open-bibles/master/eng-asv.osis.xml'
    response = requests.get(url)
    if response.status_code == 200:
        try:
            # Parse XML content
            root = ET.fromstring(response.content)

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
    else:
        print(f"Failed to fetch Proverbs text from GitHub. Status code: {response.status_code}")

    return proverbs_by_chapter

# Other functions (display_chapter, display_specific_verse, keyword_search, main) remain unchanged


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
        print("5. Exit")

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
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
