# Test

# What would be good bases for the prime 13?
# You are welcome to use the following codeboard to write a program to do the calculations for you.

# Submit your answers in the following text boxes.

# p =13
# find g to meet the Diffie-Hellman Setup

g = 1
temp = []
answer = []

def find_base(p):
    global g
    global temp
    while len(answer) < 4:
        #print("g is " + str(g))
        #print("answer is " + str(len(answer)))
        for i in range(1, p-1):
            item = (g ** i) % p
            #print("item is " + str(item))
            temp.append(item)
            #print("temp is " + str(temp))
            #print("len(set(temp)) is " + str(len(set(temp))))
        if len(set(temp)) == (p-1):
            #print("g is" + g)
            answer.append(g)
            #print("answer is " + g)
        temp = []
        g = g + 1
    
    print(answer)
        
find_base(13)
