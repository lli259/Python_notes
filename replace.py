import sys
import re
with open(sys.argv[1],'r') as f:
	lines=f.read()
	lines=re.sub(sys.argv[3],sys.argv[4],lines)
	with open(sys.argv[2],'w') as f2:
		f2.write(lines)

'''

# replace he110 in f1.txt with hello and store new content into f2.txt
echo "Hey. he110 world" > f1.txt
python replace.py f1.txt f2.txt he110 hello
cat f2.txt
rm f1.txt f2.txt
'''
