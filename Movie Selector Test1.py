import csv
reader = csv.reader(open('iMDb_movies_final.csv'))
# read the csv document

list_genres = []
list_years = []
list_languages = []
list_title=[]
# define three lists to track the coloumns of the csv form

for list in reader:
    '''
    print(list)
    print('*******')
    '''
    list_title.append(list[0])
    list_genres.append(list[2])
    list_years.append(list[1])
    list_languages.append(list[3])
'''
print(list_genres)
'''
# fill the lists

start = input('please input 1 if you want to start:')
if start == '1':
    print('here is the list of genres:')
    for i in range(len(list_genres)):
        '''
        print(i+1,list_genres[i])
        '''
    # genres

    print('here is the list of years:')
    for i in range(len(list_years)):
        '''
        print(i+1, list_years[i])
        '''
    # years

    print('here is the list of languages:')
    for i in range(len(list_languages)):
        '''
        print(i+1, list_languages[i])
        '''

    target_title = []
    target_year = []
    target_genre = []
    language = input('please input the preferable languages:')
    for i in range(len(list_languages)):
        if language == list_languages[i]:
            target_title.append(list_title[i])
            target_year.append(list_years[i])
            target_genre.append(list_genres[i])
            '''
            print(list_title[i],    list_years[i],    list_genres[i])
            '''


    target_title_second = []
    target_genre1_second = []
    year = input('please input the preferable years:')
    for i in range(len(target_year)):
        if year == target_year[i]:
            target_title_second.append(target_title[i])
            target_genre1_second.append(target_genre[i])
            print(target_genre[i])

    
    genre = input('please input the preferable genres:')
    for i in range(len(target_title_second)):
        if genre == target_genre1_second[i]:
            print(target_title_second[i])
    
  
    

        
