import matplotlib.pyplot as plt

data_location = 'files/data.txt'

#read data and make it a numeric list format
with open(data_location,'r') as file:
    data_values = file.readlines()

print(data_values)

data_values_converted_format =[float(each.strip()) for each in data_values]

print(data_values_converted_format)

#plotting the values using matplotlib

plt.figure(figsize=(8,4))

plt.plot(data_values_converted_format
         , marker='o'
         ,color ='b')

plt.title('plotting using matplotlib.pyplot')

plt.xlabel('index')
plt.ylabel('values')

#reduces the margin
plt.tight_layout()
plt.grid(True)

plt.show()
