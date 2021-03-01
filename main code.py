start=input("Hello, Mr. Kauk! Welcome to the movie recommandation program. Type '1' to start, or type any other to quit. ")

#Database 需求：二维数组，从第一行开始第一列是评分从高到低的电影名，第二列是rate，第三列是genre，第四列是year，第五列是language

#Constructing lists
list_genres = ['a', 'b', 'c', 'd', 'e']
list_years= [2011, 2012, 2019, 2001, 2020]
list_languages = ['Chinese', 'English', 'German', 'Japanese', 'Russian']

#start program
if start == '1':
    #genre
    print("Here is the list of genres: ")
    for i in range(len(list_genres)):
        print(i+1, ": ", list_genres[i])

    print("Please type your preferable genre code: ")
    genre=int(input())-1

    #years
    print("Here is the list of years: ")
    for i in range(len(list_years)):
        print(i+1, ": ", list_years[i])

    print("Please type your preferable years code: ")
    year=int(input())-1

    #language
    print("Here is the list of languages: ")
    for i in range(len(list_languages)):
        print(i+1, ": ", list_languages[i])

    print("Please type your preferable language code: ")
    language=int(input())-1

    #test
    #print(list_genres[genre])


    #Search from database
    i=1
    j=0

    if data[j][2] == list_genres[genre]:
        if data[j][3] == list_years[year]:
            if data[j][4] == list_languages[language]:
                print(i, ': ', data[j][0], 'rate: ', data[j][1])
                i+=1 


