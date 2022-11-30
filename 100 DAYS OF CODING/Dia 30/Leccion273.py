facebook_post = [
    {'Likes' : 21, 'Comments' : 2}, 
    {'Likes' : 13, 'Comments' : 2, 'Shares' : 1},
    {'Likes' : 33, 'Comments' : 8, 'Shares' : 3},
    {'Comments' : 4, 'Share' : 2},
    {'Comments' : 1, 'Share' : 1},
    {'Likes' : 19, 'Comments' : 3},
]


total_likes = 0
for post in facebook_post:
    try:
        total_likes += post['Likes']
    except KeyError as error:
        print(f'Error: {error}, Clave no encontrada')

print(total_likes)