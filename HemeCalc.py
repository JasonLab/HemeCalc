print ("Welcome to the Hematology Calculator Main Menu v1.0.")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Loopcounter = 2
while Loopcounter > 1:
    User_Goal = raw_input("Enter the parameter that you wish to determine. Choices are RBC, HCT, Hgb, MCV, MCH, MCHC. Please enter as listed.:")

    if User_Goal == "RBC":
        print ("RBC can be Calculated using MCH&Hb or MCV&Hct")
        MCHorMCV = input(("Enter either your HCT in decimal form or your Hgb in g/L: ")) #Can ask this way since numbers won't intersect ever
        if float(MCHorMCV) > 1: #As stated HCT > 1 or Hgb < 40 are impossible so this is done in an awkward way to save coding
            MCH = input(("Please enter your MCH in pg: "))
            RBC = float(MCHorMCV)/float(MCH)  #Doing it this way cause I get errors if I call the input a float
            rRBC = round(RBC,2)
            print ("Your RBC is: " + str(rRBC) + "x10^12/L")
            Loopcounter = 0
        elif float(MCHorMCV) < 1:
            MCV = input("Please enter your MCV in fL: ")
            RBC1 = float(MCHorMCV)/float(MCV) * 1000 #Variables named this way to uncomplicate possible use of loops
            rRBC1 = round(RBC1,2)
            print ("Your RBC is " + str(rRBC1) + "x10^12/L")
            Loopcounter = 0
    elif User_Goal == "HCT":
        print ("Hct can be calculated using MCV&RBC or HgB&MCHC")
        MCVorMCHC= input(("Enter either your MCHC in g/L or MCV in fL "))
        if float(MCVorMCHC) > 250:
            Hgb1 = input(("Please enter your Hgb in g/L: "))
            HCT1 = float(Hgb1)/float(MCVorMCHC)
            HCT1 = round(HCT1,3)
            print ("Yourc HCT is " + str(HCT1) +"L/L")
            Loopcounter = 0
        elif float(MCVorMCHC) < 250:
             RBC2 = input(("Please enter your RBC in fL "))
             HCT2 = float(RBC2)*float(MCVorMCHC)/1000
             HCT2 = round(HCT2,3)
             print ("Your HCT is " + str(HCT2) +"L/L")
             Loopcounter = 0
    elif User_Goal == "Hgb":
        print("HgB can be calculated using MCH&RBC or MCHC&HCT")
        MCHorMCHC = input(("Enter either your MCH in pg or your MCHC in g/L: "))
        if float(MCHorMCHC) > 100:
            HCT3 = input(("Please enter your HCT in L/L"))
            Hgb2 = float(MCHorMCHC) * float(HCT3)
            Hgb2 = int(Hgb2) #Could have rounded it as well
            print("Your Hgb is " + str(Hgb2) + "g/L")
            Loopcounter = 0
        elif float(MCHorMCHC) < 100:
            RBC3 = input(("Please enter your RBC in #/fL"))
            Hgb3 = float(MCHorMCHC) * float(RBC3)
            Hgb3 = int(Hgb3)  # Could have rounded it as well
            print("Your Hgb is " + str(Hgb3) + "g/L")
            Loopcounter = 0
    elif User_Goal =="MCV":
        RBC4= input("Please enter your RBC in #/fL: ")
        HCT4= input("Please enter your HCT in L/L: ")
        MCV2 = (float(HCT4)/float(RBC4)) *1000
        MCV2= int(MCV2)
        print("Your MCV is " + str(MCV2) + "g/L")
        Loopcounter = 0
    elif User_Goal =="MCH":
        RBC5= input("Please enter your RBC in #/fL: ")
        Hgb4= input("Please enter your Hgb in g/L: ")
        MCH2 = (float(Hgb4)/float(RBC5))
        MCH2= round(MCH2,1)
        print("Your MCH is " + str(MCH2) + "pg")
        Loopcounter = 0
    elif User_Goal =="MCHC":
        HCT5= input("Please enter your HCT in L/L: ")
        Hgb5= input("Please enter your Hgb in g/L: ")
        MCHC2 = (float(Hgb5)/float(HCT5))
        MCHC2= int(MCHC2)
        print("Your MCHC is " + str(MCHC2) + "g/L")
        Loopcounter = 0
    else:
        print ("Please enter one of the above parameters as instructed.")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")






