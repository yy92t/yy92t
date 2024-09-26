str1a = "This is Peter's Car"
str1b = 'This is Peter\'s Car'

str2a = 'Please press "[Enter]" to continue.'
str2b = "Please press \"[Enter]\" to continue."

str3a = '''Both ' and " can be used for String Literal'''
str3b = 'Both \' and " can be used for String Literal'
str3c = "Both ' and \" can be used for String Literal"

print("This is \
a sing\
le line")
print("c:\pyex\new")
print("c:\\pyex\\new")
print("line1\nline2\nline3")
print("""line11\nline12
line13
This is a long \
line 14""")
print("\u4F60\u597D\u55CE")
print("\N{LATIN CAPITAL LETTER A} \N{KATAKANA LETTER SA}")
print()

name = "Peter"
str4 = f"Hello {name}"
name = "Mary"
print(str4)
