
##AMZL reset Tracker
#developed by garbosz

##Create Vars

##define clusters
cluster=["A","B","C","D","E","G"]
clusterA=20
clusterB=20
clusterC=22
clusterD=22
clusterE=22
clusterG=22
compA=0
compB=0
compC=0
compD=0
compE=0
compG=0
perA=0
perB=0
perC=0
perD=0
perE=0
perG=0

##loop through user updates
print("Welcome to the DBO6 Reset Tracker")
print("Developed by Garbosz")
def main():
    global cluster
    global clusterA
    global clusterB
    global clusterC
    global clusterD
    global clusterE
    global clusterG
    global compA
    global compB
    global compC
    global compD
    global compE
    global compG
    global perA
    global perB
    global perC
    global perD
    global perE
    global perG
    choice=input("Press 'U' to update progress, press 'S' for a status update: ")
    if choice=='u':
        i=input("Which Cluster are you updating?(A,B,C,D,E, or G): ")
        if i=='a':
            compA=input("How many aisles are completed in this cluster?: ")
            doMath()
        elif i=='b':
            compB=input("How many aisles are completed in this cluster?: ")
            doMath()
        elif i=='c':
            cpmpC=input("How many aisles are completed in this cluster?: ")
            doMath()
        elif i=='d':
            compD=input("How many aisles are completed in this cluster?: ")
            doMath()
        elif i=='e':
            compE=input("How many aisles are completed in this cluster?: ")
            doMath()
        elif i=='g':
            compG=input("How many aisles are completed in this cluster?: ")
            doMath()
        else:
            print("Invalid Input")
            main()
    elif choice=='s':
        print("status")
        doMath()

##Do Math
def doMath():
    global cluster
    global clusterA
    global clusterB
    global clusterC
    global clusterD
    global clusterE
    global clusterG
    global compA
    global compB
    global compC
    global compD
    global compE
    global compG
    global perA
    global perB
    global perC
    global perD
    global perE
    global perG
    float(compA) 
    float(clusterA)
    float(perA)
    float(compB) 
    float(clusterB)
    float(perB)
    float(compC) 
    float(clusterC)
    float(perC)
    float(compD) 
    float(clusterD)
    float(perD)
    float(compE) 
    float(clusterE)
    float(perE)
    float(compG) 
    float(clusterG)
    float(perG)
    perA=(compA/clusterA)*100
    perA=(compB/clusterB)*100
    perA=(compC/clusterC)*100
    perA=(compD/clusterD)*100
    perA=(compE/clusterE)*100
    perA=(compG/clusterG)*100
    output()
    
##output format
def output():
    global cluster
    global clusterA
    global clusterB
    global clusterC
    global clusterD
    global clusterE
    global clusterG
    global compA
    global compB
    global compC
    global compD
    global compE
    global compG
    global perA
    global perB
    global perC
    global perD
    global perE
    global perG
    print("Cluster A:",end=" ")
    print(perA)
    print("Cluster B:",end=" ")
    print(perB)
    print("Cluster C:",end=" ")
    print(perC)
    print("Cluster D:",end=" ")
    print(perD)
    print("Cluster E:",end=" ")
    print(perE)
    print("Cluster G:",end=" ")
    print(perG)
    main()

main()