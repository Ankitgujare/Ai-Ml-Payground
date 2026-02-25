"""
when we Open the files as we did previously
we need to close it manuly

here with keyword comes in
when we open the files with the help of With Keyword
we dont need to close it manualy ..
it will close automaticaly when the Operations which we
wanted to do On it has done...


"""

with open("sample.txt","r")as f:
    print(f.read())

