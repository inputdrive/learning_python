authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)
print("-------------------")

author_last_names = [name.split()[-1] for name in author_names]
print(author_last_names)


'''
author_last_names = authors.split(",")
print(author_last_names)
'''