import pandas

# Our small data set
d = {'one':[1,1],'two':[2,2]}
i = ['a','b']

# Create dataframe
df = pandas.DataFrame(data = d, index = i)

#printing dataframe
print(df)

#printing index data type object
#print(df.index)

#Creating stacks
#stack = df.stack()

#print(stack)

#print(stack.index)

#unstack the data frame
unstack = df.unstack()

#print(unstack)

#print(unstack.index)

#transferring rows and columns
transpose = df.T

#print(transpose)

#print (transpose.indexs)