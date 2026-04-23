import pandas


students = [ 'hari', 'chuku', 'spazy', 'lechu', 'theertha','athul','gavi','Gowri','ravi','thirakan' ]
marks = [ 90, 80, 70, 60, 50, 40, 30, 20, 10, 0 ]
data = {'Students': students, 'Marks': marks}
df = pandas.DataFrame(data,index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']) 
print(df)
print("")
print(df.loc['G'])
