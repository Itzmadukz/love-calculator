def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    
    true_count = 0
    for letter in "true":
        true_count += combined_names.count(letter)
    
    love_count = 0
    for letter in "love":
        love_count += combined_names.count(letter)
    
    love_score = int(f"{true_count}{love_count}")
    
    print(f"Your love score is {love_score}.")


#Example Usage
calculate_love_score(name1="Angela Yu", name2="Jack Bauer")