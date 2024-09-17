'''
1. 
In `get_friends_favorite_candy_count()`, return a dictionary of candy names 
and the amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def get_friends_favorite_candy_count(favorites):
    print(f"favorites = {favorites}")

    candy_count_dict = {}

    for one_friend_favorites in favorites:
        print(f"one_friend_favorites = {one_friend_favorites}")

        for candy in one_friend_favorites[1]:
            if candy not in candy_count_dict:
                candy_count_dict[candy] = 1
            else:
                candy_count_dict[candy] += 1

    print(f"candy_count_dict = {candy_count_dict}")
    return candy_count_dict



'''
2. 
Given the list `friend_favorites`, create a new data structure in the 
function `create_new_candy_data_structure` that describes the different 
kinds of candy paired with a list of friends that like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def create_new_candy_data_structure(data):
    candy_by_name_dict = {}

    for one_friend_favorites in data:
        
        for candy in one_friend_favorites[1]:
            if candy not in candy_by_name_dict:
                candy_by_name_dict[candy] = []
            candy_by_name_dict[candy].append(one_friend_favorites[0])

    return candy_by_name_dict

'''
3. 
In `get_friends_who_like_specified_candy()`, return a tuple of 
friends who like the candy specified in the candy_name parameter.
'''
def get_friends_who_like_specific_candy(data, candy_name):
    pass

'''
4. 
In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.
'''
def create_candy_set(data):
    pass 

'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''
friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]


print(create_new_candy_data_structure(friend_favorites))

