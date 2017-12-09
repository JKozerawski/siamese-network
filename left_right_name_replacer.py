OLD_PROTOTXT_FILE_PATH = "./model/train_val.prototxt"
NEW_PROTOTXT_FILE_PATH = "./updated-proto.txt"

with open(OLD_PROTOTXT_FILE_PATH, 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('left', 'right')

# Write the file out again
with open(NEW_PROTOTXT_FILE_PATH, 'w') as file:
  file.write(filedata)
