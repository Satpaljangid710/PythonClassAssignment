
txt=input("Enter text to write to the file: ")

with open("output_text.txt","w") as file:
    file.write(txt)

print("Data successfully written to output_text.txt")

appending_txt=input("Enter additional text to append: ")

with open("output_text.txt","a") as file:
    file.write("\n"+appending_txt)

print("Final content of output_text.txt:")

with open("output_text.txt","r") as file:
    print(file.read())




