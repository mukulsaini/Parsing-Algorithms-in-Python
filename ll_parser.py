# LL(1) Top_Down_Parser
# first() is used to calculate the firt of grammar 

# Sample Case: 
# Input : S->A,A->C|z,C->d
# Output will be a dictionary which will contain first of the grammar
# Output : {'S' : ['z','d'], 'A' : ['z','d'], 'C' : ['d']}

gm=raw_input("Enter Comma Seperated Grammer : \n")
list = gm.split(',')
left_gm = []
right_gm = []
first_gm={}
for i in list :
    left_gm.append(i.split('->')[0])
    right_gm.append(i.split('->')[1].split('|'))
#print right_gm
def first():  #Cal First of Non-Terminals
    for i in right_gm :
        tmp_gm_list=[]
        for j in i :
            try:
                index = left_gm.index(j[0])
            except ValueError:
                index = -1
            if index == -1 :
                tmp_gm_list.append(j[0])
            else:
                tmp_gm_list.extend(find_first(j[0]))
            #print tmp_gm_list
        first_gm[left_gm[right_gm.index(i)]]=tmp_gm_list

def find_first( val ): # Recursive Function
    tmp_gm_list=[]
    #print val
    try :
        index = left_gm.index(val)
    except ValueError :
        index = -1
    if index == -1 :
        tmp_gm_list.append(val)
        print tmp_gm_list
        return tmp_gm_list
    else :
        #print index
        for i in right_gm[index]:
            tmp_gm_list.extend(find_first(i[0]))
    return tmp_gm_list
                #first_gm[left_gm[right_gm.index(i)]].append(j[0])
first()
print first_gm