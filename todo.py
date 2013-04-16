import sys, os

#get user input with the prompt "Type here: "
result = raw_input('Type here: ')
if result == 'exit':
    sys.exit(0)
else:
    #open tester in append mode and append the user input
    file_name = os.path.expanduser('~/tester')
    f = open(file_name, "a")
    f.write(result)
    f.close()
