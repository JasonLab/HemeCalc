print ("Welcome to the Hematology Calculator Main Menu v1.0.")
User_Goal = input("Enter the parameter that you wish to determine. Choices are RBC, HCT, Hgb, MCV, MCH, MCHC. Please enter as listed.:")

if User_Goal == "RBC":
    print ("RBC can be Calculated using MCH&Hb or MCV&Hct")
    MCHorMCV = input(("Enter either your HCT in decimal form or your Hgb in g/L: ")) #Can ask this way since numbers won't intersect ever
    if float(MCHorMCV) > 1: #As stated HCT > 1 or Hgb < 40 are impossible so this is done in an awkward way to save coding
        MCH = input(("Please enter your MCH: in pg "))
        RBC = float(MCHorMCV)/float(MCH)  #Doing it this way cause I get errors if I call the input a float
        rRBC = round(RBC,2)
        print ("Your RBC is: " + str(rRBC) + "x10^12/L")
    elif float(MCHorMCV) < 1:
        MCV = input("Please enter your MCV: in fL ")
        RBC1 = float(MCHorMCV)/float(MCV) * 1000 #Variables named this way to uncomplicate possible use of loops
        rRBC1 = round(RBC1,2)
        print ("Your RBC is " + str(rRBC1) + "x10^12/L")
if User_Goal == "HCT":
    print ("Hct can be calculated using MCV&RBC or HgB&MCHC")
    MCVorMCHC= input(("Enter either your MCHC in g/L or MCV in fL "))
    if float(MCVorMCHC) > 250:
        Hgb1 = input(("Please enter your Hgb in g/L: "))
        HCT1 = float(Hgb1)/float(MCVorMCHC)
        HCT1 = round(HCT1,3)
        print ("Yourc HCT is " + str(HCT1) +"L/L")
    elif float(MCVorMCHC) < 250:
        RBC2 = input(("Please enter your RBC in fL "))
        HCT2 = float(RBC2)*float(MCVorMCHC)/1000
        HCT2 = round(HCT2,3)
        print ("Yourc HCT is " + str(HCT2) +"L/L")