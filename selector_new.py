import pandas as pd


start=input("Hello, Mr. Kauk! Welcome to the movie recommandation program. Type '1' to start, or type any other to quit. ")


'''
#Constructing lists
list_genres = ['a', 'b', 'c', 'd', 'e']
list_years= [2011, 2012, 2019, 2001, 2020]
list_languages = ['Chinese', 'English', 'German', 'Japanese', 'Russian']
'''

df = pd.read_csv("IMDb_movies.csv")
movieList = df
movieList['genre1'], movieList['genre2'], movieList['genre3'] = df['genre'].str.split(', ', True)
list_language = df['language'].drop_duplicates().values.tolist()

list1 = movieList['genre1'].drop_duplicates().values.tolist()
list2 = movieList['genre2'].drop_duplicates().values.tolist()
list3 = movieList['genre3'].drop_duplicates().values.tolist()
list_genres = list1.extend(list2)
list_genres = list(set(list_genres.extend(list3)))


#start program
if start == '1':
    #genre
    print("Here is the list of genres: ")
    for i in range(len(list_genres)):
        print(i+1, ": ", list_genres[i])

    print("Please type your preferable genre code: ")
    gen=int(input())-1

    #years
    print("Here is the list of years: ")
    for i in range(len(list_years)):
        print(i+1, ": ", list_years[i])

    print("Please type your preferable years code: ")
    yr=int(input())-1

    #language
    print("Here is the list of languages: ")
    for i in range(len(list_languages)):
        print(i+1, ": ", list_languages[i])

    print("Please type your preferable language code: ")
    lang=int(input())-1


    #Search from database
    '''
    i=1
    j=0
    while i <= 20:
        if data[j][2] == list_genres[genre]:
            if data[j][3] == list_years[year]:
                if data[j][4] == list_languages[language]:
                    print(i, ': ', data[j][0], 'rate: ', data[j][1])
                    i+=1
    '''

    output = movieList[movieList.language=lang & moiveList.year=yr & (moiveList.genre1=gen | moiveList.genre2=gen | moiveList.genre3=gen)]
    print(output['title'])
    

