import pytest
from candy_problem.candy_problem import * 

def test_get_friends_favorite_candy_count_type():
    friend_favorites = [
        ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
        ["Bob", ["milky way", "licorice", "lollipop" ]],
        ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
        ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
    ]

    new_candy_data = get_friends_favorite_candy_count(friend_favorites)

    assert type(new_candy_data) == dict


def test_get_friends_favorite_candy_count_value():
    friend_favorites = [
        ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
        ["Bob", ["milky way", "licorice", "lollipop" ]],
        ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
        ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
    ]

    new_candy_data = get_friends_favorite_candy_count(friend_favorites)

    assert new_candy_data == {'lollipop': 2, 'bubble gum': 1, 'laffy taffy': 3, 'milky way': 2, 'licorice': 1, 'chocolate bar': 1, 'nerds': 1, 'sour patch kids': 1}



def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict

# Add your own assertions to the test below
def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert len(new_candy_data) == 8
    '''
    Add your assertions here!
    '''

'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''