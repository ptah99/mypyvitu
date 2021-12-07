#strings: ordered, immutable, text representation
my_string = "hello world"
char = my_string[-1]
ss = my_string[1:6]
s = my_string[::2]
print(char)
print(ss)
print(s)

greeting = "hello"
name = "peter"
sentence = greeting + " "+ name
print(sentence)
for i in greeting:
    print(i)

if 'e' in greeting:
    print('yes')
else:
    print('no')

st = 'hello world'
#st.startswith('h'), .find('o'), .count('l'), .replace('world', 'universe')
print(st.upper())
# list and strings
string = 'how are you doing'
list = string.split()
print(list)
#list to string
new_string = ''.join(list)
print(new_string)

lst = ['a'] * 6
print(lst)
#bad
str = ''
for i in lst:
   str += i
print(str)
#good
str = ''.join(lst)
print(str)

#%, .format(), f-strings
var = "Tom"
my_str = "the variable is %s"% var
# for number (%d), decimal %f, or %.2f for 2 digits after decimal point
print(my_str)
# format()
vari = 3.54664
vari2 = 7
mystr = "the variable is {:.2f} and {}".format(vari,vari2)
print(mystr)
# f-string (recommended) can do math e.g {vari*2}
my_str = f"the variable is {vari} and {vari2}"
print(my_str)
