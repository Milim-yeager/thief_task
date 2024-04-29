from time import sleep


def find_thief():
    """a1 = "C and I met today"
        a2 = "B is thief"
        a3 = "thief did not know who car was for"
        b1 = "D is not thief"
        b2 = "d3 is lying"
        b3 = "i am not tief"
        c1 = "i have not met A yet"
        c2 = "B is not thief"
        c3 = "D knows how to drive"
        d1 = "b1 is lying"
        d2 = "I don't know how to drive"
        d3 = "A is thief"""
    a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3 = None, None, None, None, None, None, None, None, None, None, None, None
    # rabete mostaghim (a1 <-> c1),(a2 <-> c2 -> b3),(b1 <-> d1),(b2 <-> d3)
        # ,(c3 <-> d2),(a3 -> True)
    if input("is a1 truth?(no/yes)").lower == "yes":
        a1, c1 = True, False
    else:
        c1, a1 = True, False
    if input("is b1 truth?(no/yes)").lower == "yes":
        b1, d1 = True, False
    else:
        d1, b1 = True, False
    if input("is b2 truth?(no/yes)").lower == "yes":
        b2, d3 = True, False
    else:
        d3, b2 = True, False
    if input("is c3 truth?(no/yes)").lower == "yes":
        c3, d2 = True, False
    else:
        d2, c3 = True, False
    a3 = True #a3 -> True
        # baray inke true(6) == false(6) tebgh shart c2 <-> a2 <-> b3:
    false, true = 0, 0
    thief_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3]
    for item in thief_list:
        if item == True:
            true += 1
        elif item == False:
            false += 1
    print(f"trurh={true},lie={false}")
    print("shoma bayad gozare haye c2,a2,b3 ra be tori moshakhas konid ke lie=6 and truth=6")
    if input("is b3 truth?(yes/no)").lower() == "no":
        b3, a2, c2 = False, True, False
    else:
        b3, a2, c2 = True, False, True
    false, true = 0, 0
    thief_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3]
    gozare = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3', 'd1', 'd2', 'd3']
    for item in thief_list:
        if item == True:
            true += 1
        elif item == False:
            false += 1
    print(f"trurh={true},lie={false}")
    if true == false:
        for i in range(12):
            print(f"{gozare[i]} is {thief_list[i]}")
            sleep(1)
        print("in this case, number of lies and truths is equal(lies == truths)")
        sleep(3)
        print("B is a thief because b3 is lie and a2 is truth\n\tgood luck!")
    else:
        print("sorry, you are not a good cop,the thief ran away,try again")

find_thief()
