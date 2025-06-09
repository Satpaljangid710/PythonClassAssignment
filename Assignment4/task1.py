
try:
   file=open("sample_text.txt","r")
   reading_file=file.readlines()
   print("Line 1: ",reading_file[0])
   print("Line 2: ",reading_file[1])
except Exception as e:
    print("Error: The file was not found",)


