list_names = ['tom', 'Jay', 'UZI']
list_names_test = []
def show_magicians(names):
    for i in names:
        print(i.title())
def make_great(names,test):
    for i in names:
        test.append(i+' the Great!')
    return test
make_great(list_names[:],list_names_test)
show_magicians(list_names)
show_magicians(list_names_test)