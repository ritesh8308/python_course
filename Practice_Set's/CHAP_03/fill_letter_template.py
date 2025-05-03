# METHOD 1:
# letter = '''
#            Dear {},
#            You are selected!
#            {}
#            '''

# name = "om"
# date = "12/03/2025"

# s = letter.format(name,date)
# print(s)




#METHOD 2:

name = "om"
date = "12/03/2025"
print(f'''
Dear {name}
You are selected!
{date}
''')