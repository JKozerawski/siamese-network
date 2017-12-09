import re

OLD_PROTOTXT_FILE_PATH = "./model/train_val.prototxt"
NEW_PROTOTXT_FILE_PATH = "./updated-proto.txt"

#############################################

with open(OLD_PROTOTXT_FILE_PATH) as f:
    lines = f.readlines()

txt = ""
counter = 0
name = ""
for line in lines:
	txt+=line
	if ("layer" in line):
		counter = 0
		name = ""
	if("name" in line):
		name = str(re.findall('"([^"]*)"', line)[0])
		if("right" in name): name = name.replace("right", "")
		else: name = name.replace("left", "")
	if("  param {" in line):
		counter +=1
		if(counter==1):
			txt+= "    name: \""+name+"w\"\n"
		elif(counter==2):
			txt+= "    name: \""+name+"b\"\n"
print txt
f = open(NEW_PROTOTXT_FILE_PATH,'w')
f.write(txt)
f.close()
		
