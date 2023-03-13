x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x = [ [5,2,3], [10,8,9] ]

x[1][0]=15
print (x)


estudiantes[0] ['last_name'] = 'Bryant'
print (estudiantes)



directorio_deportes ['fútbol'] [0] = "Andrés"
print (directorio_deportes)


z [0] ['y'] = 30
print (z)

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]



def iterate_Dictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val},"
        print(output)

iterate_Dictionary(estudiantes)  



def iterate_Dictionary2(key_name, list):
    for i in range (0, len (list)):
    
        for key, val in list [i].items():
            if key ==key_name:
                print (val)

iterate_Dictionary2('first_name',estudiantes)
iterate_Dictionary2('last_name',estudiantes)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_Info(dict):
    for key,val in dict.items():
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

print_Info(dojo)
