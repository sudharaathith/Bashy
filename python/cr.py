import sys,os

x = sys.argv
x.pop(0)
cmd = '''google-chrome "www.google.com/search?q='''
first = False
for i in x:
    if first:
        cmd = cmd+"+"
    cmd = cmd+i
    first = True
cmd = cmd+'" >/dev/null 2>&1 &'
os.system(cmd)




