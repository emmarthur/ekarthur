# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:48:23 2021

@author: earthur
"""

def create_prefs():
    num = int(input("Enter the number of elements in sets A and B: "))
    pref_Dict_A = {}
    pref_Dict_B = {}
    mem_A = []
    mem_B = []
    rank = 0 #rank of a man in a woman's preference
    wrank = 0 #rank of a woman in a man's preference
    for i in range(num):
        addA = input("Enter an element of A: ")
        mem_A.append(addA)
        pref_Dict_A.update({addA:[]})
        for j in range(num):
            addBA = input("Enter element of B in "+str(addA)+" preference position "+str(j)+": ")
            wrank += 1 
            pref_Dict_A[addA].append([addBA,0,wrank])
        wrank = 0
            #0 in the list appended is indicator for whether addA has proposed to addB
    for k in range(num):
          addB = input("Enter an element of B: ")
          mem_B.append(addB)
          pref_Dict_B.update({addB:{}})
          for l in range(num):
                add_AB = input("Enter element of A in "+str(addB)+" preference position "+str(l)+":" )
                rank += 1
                pref_Dict_B[addB].update({add_AB:rank})
          rank = 0
    print("Set A: ", pref_Dict_A)
    print("Set B: ", pref_Dict_B)
    return [{"SetA":pref_Dict_A , "SetB":pref_Dict_B},mem_A,mem_B]

    
        #members_A.append(addA)
        #members_B.append(addB)
def get_key(val,nary):
    res = ""
    for l in nary:
        if nary[l] == val:
            res = l
    return res
 
def check_free(dictm):
    boolf = False
    for l in dictm:
        if dictm[l] == 0:
            boolf = True
    return boolf

def free_list(dictm):
    f_list = []
    for l in dictm:
        if dictm[l] == 0:
            f_list.append(l)
        else:
            pass
    return f_list
        
def high_pref(dlist):
    rank = len(dlist)+3
    result = ""
    r_list = []
    for m in dlist:
        if m[1] == 0:
            if m[2] < rank:
                result = m[0]
                rank = m[2]
            else:
                pass
        else:
            pass
        
    for k in dlist:
        if m[0] == result:
            m[1] = 1
    return result
        
def stabilize():
    summ_prefs = create_prefs() #preference list with other helpful data
    prefs =  summ_prefs[0]
    sA = prefs["SetA"] #dictionary of men's preferences
    sB = prefs["SetB"] #dictionary of women's preferences
    mem_A = summ_prefs[1] #list of men
    mem_B = summ_prefs[2] #list of women
    num = len(mem_A) # number of men = number of women
    free_bool_A = {} #dictionary of men indicating whether they are free or not
    free_bool_B = {} #dictionary of men indicating whether they are free or not
    pairs = {} #dictionary of pairings
    for i in range(num): #make all men free
        free_bool_A.update({mem_A[i]:0})
    for j in range(num): #make all women free
        free_bool_B.update({mem_B[j]:0})
    for k in mem_A:  #set the partner of all men to nobody
        pairs.update({k:""})
     #frees = free_list(free_bool_A) #make a list of all free men
    while check_free(free_bool_A) == True:#while some man is free
           frees = free_list(free_bool_A) 
           print(frees)
           for m in frees:  #for each free man
               w = high_pref(sA[m]) # find woman of highest preference who he hasn't proposed and make her proposed status 1
               print (m,w)
               if free_bool_B[w] == 0:# if that woman is free
                   pairs[m] = w #pair her with man proposing
                   free_bool_B[w] = 1 #mark woman as taken
                   free_bool_A[m] = 1 #mark man as taken
               else:# if woman is taken
                   mw = get_key(w,pairs) #get woman's current partner
                   if sB[w][m] < sB[w][mw]: # if current partner is of lower preference than man proposing
                       pairs[m] = w #pair the proposer with woman
                       pairs[mw] = "" #current partner is free
                       free_bool_B[w] = 1 #mark woman as taken
                       free_bool_A[m] = 1 #mark man as taken
                       free_bool_A[mw] = 0 #mark woman's current partner as free
                   else:
                       pass
    return pairs
               
        
            
    
            
        
    
        