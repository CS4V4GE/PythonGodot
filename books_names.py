"""
main author: Stockton Nelson

file: books_names.py
"""
book_of_mormon_chapters = []
scriptures =[]

#this has the same format that the txt has.
largest_number_of_chapters = ["", 0, ""]

user_voulume = 0
user_voulume_name = ''
user_input_voulume = ''

user_input_voulume = input('which volume of scriptures would you like to learn about (for example, Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price)?: ').lower()

with open('books_and_chapters.txt') as file:

    for row in file:
        line = row.strip().split(':')
        if line[2] == 'Book of Mormon':
            book_of_mormon_chapters.append(line)
        scriptures.append(line)
    


for scripture in book_of_mormon_chapters:
    if int(scripture[1]) >=  int(largest_number_of_chapters[1]):
        largest_number_of_chapters = scripture
    
    if scripture[2].lower() == user_input_voulume and int(scripture[1]) >=  user_voulume:
        user_voulume = int(scripture[1])
        user_voulume_name = scripture[0]
    
    print(f'Scripture: {scripture[0]}, Book: {scripture[2]}, Chapters: {scripture[1]}')

print(f"The book of mormon with the most chapters is: {largest_number_of_chapters[0]}")
print(f"It has {largest_number_of_chapters[1]} chapters.")

print(f"The {user_input_voulume} with the most chapters is: {user_voulume_name}")
print(f"It has {user_voulume} chapters.")


