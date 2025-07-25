def get_num_words(text):
    num_words = 0
    words = text.split()
    for word in words:
        num_words += 1
    return num_words

def get_num_characters(text):
    character_count = {}
    lower_characters = text.lower()
    for characters in lower_characters:
        if characters in character_count:
            character_count[characters] += 1
        else:
            character_count[characters] = 1

    return character_count

def sort_on(characters):
    return (characters["num"])
  
def sort_dictionary(character_count):
    characters = []
    for char, count in character_count.items():
        dictionary = {}
        dictionary["char"] = char
        dictionary["num"] =count
        characters.append(dictionary)
    characters.sort(reverse=True,key=sort_on)
    return characters 
