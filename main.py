from ProverbProgram import load_proverbs_text
def load_proverbs_text():
    proverbs_text = """
    [1:1] The proverbs of Solomon the son of David, king of Israel;
    [1:2] To know wisdom and instruction; to perceive the words of understanding;
    [1:3] To receive the instruction of wisdom, justice, and judgment, and equity;
    [1:4] To give subtilty to the simple, to the young man knowledge and discretion.
    [1:5] A wise man will hear, and will increase learning; and a man of understanding shall attain unto wise counsels:
    [1:6] To understand a proverb, and the interpretation; the words of the wise, and their dark sayings.
    [1:7] The fear of the LORD is the beginning of knowledge: but fools despise wisdom and instruction.
    [1:8] My son, hear the instruction of thy father, and forsake not the law of thy mother:
    [1:9] For they shall be an ornament of grace unto thy head, and chains about thy neck.
    [1:10] My son, if sinners entice thee, consent thou not.
    [1:11] If they say, Come with us, let us lay wait for blood, let us lurk privily for the innocent without cause:
    [1:12] Let us swallow them up alive as the grave; and whole, as those that go down into the pit:
    [1:13] We shall find all precious substance, we shall fill our houses with spoil:
    [1:14] Cast in thy lot among us; let us all have one purse:
    [1:15] My son, walk not thou in the way with them; refrain thy foot from their path:
    [1:16] For their feet run to evil, and make haste to shed blood.
    [1:17] Surely in vain the net is spread in the sight of any bird.
    [1:18] And they lay wait for their own blood; they lurk privily for their own lives.
    [1:19] So are the ways of every one that is greedy of gain; which taketh away the life of the owners thereof.
    [1:20] Wisdom crieth without; she uttereth her voice in the streets:
    [1:21] She crieth in the chief place of concourse, in the openings of the gates: in the city she uttereth her words, saying,
    [1:22] How long, ye simple ones, will ye love simplicity? and the scorners delight in their scorning, and fools hate knowledge?
    [1:23] Turn you at my reproof: behold, I will pour out my spirit unto you, I will make known my words unto you.
    [1:24] Because I have called, and ye refused; I have stretched out my hand, and no man regarded;
    [1:25] But ye have set at nought all my counsel, and would none of my reproof:
    [1:26] I also will laugh at your calamity; I will mock when your fear cometh;
    [1:27] When your fear cometh as desolation, and your destruction cometh as a whirlwind; when distress and anguish cometh upon you.
    [1:28] Then shall they call upon me, but I will not answer; they shall seek me early, but they shall not find me:
    [1:29] For that they hated knowledge, and did not choose the fear of the LORD:
    [1:30] They would none of my counsel: they despised all my reproof.
    [1:31] Therefore shall they eat of the fruit of their own way, and be filled with their own devices.
    [1:32] For the turning away of the simple shall slay them, and the prosperity of fools shall destroy them.
    [1:33] But whoso hearkeneth unto me shall dwell safely, and shall be quiet from fear of evil.
    """
    return proverbs_text



def display_chapter(chapter_number, proverbs_text):
    chapter_marker = f"[{chapter_number}:
    next_chapter_marker = f"{chapter_number+1}:"

    start_index = proverbs_text.find(chapter_marker)
    end_index = proverbs_text.find(next_chapter_marker)

    if start_index == -1:
        print(f"Chapter {chapter_number} not found.")
        return

    if end_index == -1:
        chapter_text = proverbs_text[start_index:]
    else:
        chapter_text = proverbs_text[start_index:end_index]

    print(f"Chapter {chapter_number}:")
    print(chapter_text.strip())

# Example usage:
# display_chapter(1, proverbs_text)  # Display Chapter 1



def main():
    # Load Proverbs text
    proverbs_text = load_proverbs_text()

    if proverbs_text:
        while True:
            print("\nOptions:")
            print("1. Display entire chapter")
            print("2. Display specific verse")
            print("3. Keyword search")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                chapter_number = input("Enter chapter number: ")
                try:
                    chapter_number = int(chapter_number)
                    display_chapter(chapter_number, proverbs_text)
                except ValueError:
                    print("Invalid input. Please enter a valid chapter number.")
            elif choice == '2':
                chapter_number = input("Enter chapter number: ")
                verse_number = input("Enter verse number: ")
                try:
                    chapter_number = int(chapter_number)
                    verse_number = int(verse_number)[1:1] The proverbs of Solomon the son of David, king of Israel;
def display_specific_verse(chapter_number, verse_number, proverbs_text):
    verse_marker = f"[{chapter_number}:{verse_number}]"
    start_index = proverbs_text.find(verse_marker)
    if start_index == -1:
        print(f"Verse {chapter_number}:{verse_number} not found.")
        return
    next_verse_index = proverbs_text.find("[", start_index + 1)
    if next_verse_index == -1:
        verse_text = proverbs_text[start_index:].strip()
    else:
        verse_text = proverbs_text[start_index:next_verse_index].strip()

    print(f"Verse {chapter_number}:{verse_number}:")
    print(verse_text)

def keyword_search(keyword, proverbs_text):
    keyword = keyword.lower()
    verses = []
    chapters = proverbs_text.split("[")[1:]
    for chapter in chapters:
        chapter_number, *verses_text = chapter.split("\n")
        for verse in verses_text:
            if keyword in verse.lower():
                verses.append(f"[{chapter_number.strip()}]: {verse.strip()}")
    if verses:
        print(f"Verses containing the keyword '{keyword}':")
        for verse in verses:
            print(verse)
    else:
        print(f"No verses containing the keyword '{keyword}' found.")

def main():
    # Load Proverbs text
    proverbs_text = load_proverbs_text()

    if proverbs_text:
        while True:
            print("\nOptions:")
            print("1. Display entire chapter")
            print("2. Display specific verse")
            print("3. Keyword search")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                chapter_number = input("Enter chapter number: ")
                try:
                    chapter_number = int(chapter_number)
                    display_chapter(chapter_number, proverbs_text)
                except ValueError:
                    print("Invalid input. Please enter a valid chapter number.")
            elif choice == '2':
                chapter_number = input("Enter chapter number: ")
                verse_number = input("Enter verse number: ")
                try:
                    chapter_number = int(chapter_number)
                    verse_number = int(verse_number)
                    display_specific_verse(chapter_number, verse_number, proverbs_text)
                except ValueError:
                    print("Invalid input. Please enter valid chapter and verse numbers.")
            elif choice == '3':
                keyword = input("Enter keyword: ")
                keyword_search(keyword, proverbs_text)
            elif choice == '4':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
