#Who likes it?

#Implement the function which takes an array containing the names of people that like an item.
#It must return the display text as shown in the examples:
#[]                                -->  "no one likes this"
#["Peter"]                         -->  "Peter likes this"
#["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
#["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
#["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

def likes(names):
    n = len(names)
    if n == 0:
        return 'no one likes this'
    elif n == 1:
        return names[0] + ' likes this'
    elif n == 2:
        return names[0] + ' and ' + names[1] + ' like this'
    elif n == 3:
        return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    else:
        return f'{names[0]}, {names[1]} and {n-2} others like this'
