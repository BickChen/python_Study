# def display_message(name):
#     print("I learned "+name+'!')
# display_message("function")
#
# def book_like(book):
#     print("I like book is "+book+'!' )
# book_like("天才在左，疯子在右")

# def make_shirt(size='L',sign='I love Python'):
#     full_name = "T-shirt Size "+size+'\nT-shirt sign '+sign+'!'
#     return full_name
# a = make_shirt(sign="RNG")
# print(a)

# def city_country(country_01,city):
#     output_test = country_01.title()+', '+city.title()
#     return output_test
# a = city_country('China','shanghai')
# b = city_country('usa','New York')
# c = city_country('china','tianjin')
# print(a)
# print(b)
# print(c)

# def make_album(a,b):
#     dict_01 = {'name':a,'album':b}
#     make = dict_01['name']+', '+dict_01['album']
#     return make
# c = make_album('abc','cbd')
# print(c)

def make_album(name,album,number=''):
    data = {'name':name, 'album_name':album, 'number':number}
    if data['number']:
        album_data = 'album name: '+data['album_name']+'\nSinger: '+data['name']+'\nNumber of songs: '+data['number']
    else:
        album_data = 'album name: '+data['album_name']+'\nSinger: '+data['name']
    return album_data
b = 'YES'
while b == 'YES':
    name = input("Singer name: ")
    album_name = input('album name: ')
    number_songs = input('Number of songs: ')
    if number_songs:
        a = make_album(name,album_name,number_songs)
        print(a)
        b = input("还要继续吗？ YES/NO：")
        b = b.upper()
    else:
        a = make_album(name,album_name)
        print(a)
        b = input("还要继续吗？ YES/NO：")
        b = b.upper()