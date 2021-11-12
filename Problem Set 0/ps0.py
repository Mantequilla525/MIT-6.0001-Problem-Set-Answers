import numpy

x = input('Enter a number for x:')
y = input('Enter a number for y:')

x = int(x)
y = int(y)

raised = x ** y

print('x ** y =', raised)

logged = numpy.log2(x)

print('log(x) =', logged)
