from PIL import Image

# This is absoulute path - from begining of the history
pic = Image.open('/home/ebi/Pictures/Pictures in the STX office - 2022/STX 3-6_10.JPG')

print(pic)

code_message = "This is a secret message encoded into the pic."

# End of the message is "."
# 

for i in range(0, 6000, 100):
    for j in range(0, 4000, 100):
        pass



print(pic.size)