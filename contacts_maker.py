# template = "BEGIN:VCARD\nVERSION:2.1\nN:;{};;;\nFN:{}\nTEL;CELL:{}\nEND:VCARD\n" # template 2.0
template = "BEGIN:VCARD\nVERSION:4.0\N:;{};;;\nFN:Botted by mxxx.\nTEL;TYPE#work,voice;VALUE#uri:tel:{}\nEND:VCARD"
with open('goods2.txt', 'r', encoding='utf-8') as f:
    rows = f.read().split('\n')
    f.close()
with open('contactssssssы.txt', 'a+', encoding='utf-8') as f:
    for ind, row in enumerate(rows):
        phone, name = row.split(':')
        name = f"{name} {ind + 1}"
        

        # temp trash
        # string = phone
        # position = 0 
        # new_character = '8' 
        # string = string[:position] + new_character + string[position+1:] 
        # phone = string
        # phone = "{}-{}-{}".format(phone[0:3], phone[3:6], phone[6:11])

        
        complete = template.format(name, name, phone)
        f.write(complete)
        print(f"{ind+1}/{len(rows)}")
    f.close()