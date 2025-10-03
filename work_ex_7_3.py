fname = input('Enter the file name: ')
new_fname = fname.upper()
try:
    fhand = open(new_fname)
except:
    print(new_fname, '- You have been pranked!')
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)