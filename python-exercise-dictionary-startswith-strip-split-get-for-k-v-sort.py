#prompt input to enter file then store it inside name
name = input("Enter file:")

#optional filter if name < 1 then name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"

#set file handler for opening the file
handle = open(name)

#set up empty dictionary as kvp
kvp = dict()

#using definite loop for each line inside handle
for line in handle:
    
    #filter if line starts with "From"
    if line.startswith("From") :
        
        #result will be stripped and splitted
        line.strip().split()
        
        #filter if length is > 2 because if its less than 2 or equal, on txt it has no time on it
        if len(line.strip().split()) > 2:
            
            #result will get the 5th index then split the result with a delimiter of ":" then get the 0 index
            line.strip().split()[5].split(":")[0]
            
            #result value will become the key inside kvp and will add every 1 count if it has the same key
            kvp[line.strip().split()[5].split(":")[0]] = kvp.get(line.strip().split()[5].split(":")[0],0) + 1

#definite loop to itterate in key value pair, sorted it and in items() tuple
for k,v in sorted(kvp.items()):
    
    #print in key value format
    print(k,v)