print("Program starts")
i = 1
j = -2
assert i >= 0
print("after 1st assert")
assert i >= 0 and j >= 0, "negative value found i=%s, j=%s" % (i,j)
print("after 2nd assert")
print("Program ends")


###### The followings are commands for entering in Command Prompt ##########
"""

cd c:\pyex\ex08

python ex08d.py

python -O ex08d.py    

set PYTHONOPTIMIZE=1
python ex08d.py

###### The following restore the default setting ##########

set PYTHONOPTIMIZE=0

"""

