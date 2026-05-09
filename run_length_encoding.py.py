text = str(input("Enter input here : "))
new_Text = ""
code = ""
length = len(text)
index = 0

while True:
    if length != 0:
        break
    else:
        text = str(input("Try again, Enter input here : "))
        

while index < length:
    if length == 1:
        run = 1
        code = code + str(run)
        code = code + text[index]
        print(code)
        break
    
    else: 
        run = 1
        new_Text = text[index]
        if text[index]==" ":
            code = code + " "

        else:
            while ((index+1) < length) and (text[index] == text[index + 1]):
                run +=1
                index += 1
            code = code + str(run)
            code = code + new_Text
    index += 1
print(code)

            # if index <= length - 1:
            #         if text[index] == new_Text:
            #            run = run + 1

        
    
               
                





