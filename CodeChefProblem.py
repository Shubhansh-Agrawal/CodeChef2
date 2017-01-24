#Problem is posted here https://www.codechef.com/MAY16/problems/LADDU 

user_Input=0;
user_Input=input();
arr=[];
 
dctnry={};
for i in range(0,user_Input):
    dctnry.setdefault(i,[]);
    Str=raw_input();
    Str2=[];
    Str2=Str.split();
    dctnry[i].append(Str2[1]);
    n=int(Str2[0]);
    for j in range(0,n):
        dctnry[i].append(raw_input());
 
for i in range(0,len(dctnry)):
    dctnry[i].append(0);
    for j in range(1,len(dctnry[i])-1):
        if len(dctnry[i][j].split())==1:
            if dctnry[i][j]=="TOP_CONTRIBUTOR":
                dctnry[i][len(dctnry[i])-1]=dctnry[i][len(dctnry[i])-1]+300;
            elif dctnry[i][j]=="CONTEST_HOSTED":
                dctnry[i][len(dctnry[i])-1]=dctnry[i][len(dctnry[i])-1]+50;
        elif len(dctnry[i][j].split())==2:
            x=[];
            x=dctnry[i][j].split();
            if x[0]=="CONTEST_WON":
                if int(x[1])<=20:
                    dctnry[i][len(dctnry[i])-1]=dctnry[i][len(dctnry[i])-1]+300+20-int(x[1]);
                elif int(x[1])>20:
                    dctnry[i][len(dctnry[i])-1]=dctnry[i][len(dctnry[i])-1]+300;
            elif x[0]=="BUG_FOUND":
                dctnry[i][len(dctnry[i])-1]=dctnry[i][len(dctnry[i])-1]+int(x[1]);
 
 
for i in range(0,len(dctnry)):
    if(dctnry[i][0]=="INDIAN"):
        print(dctnry[i][len(dctnry[i])-1]/200);
    elif(dctnry[i][0]=="NON_INDIAN"):
        print(dctnry[i][len(dctnry[i])-1]/400);
 user_Input=0;
user_Input=input();
arr=[];
 
dctnry={};
for i in range(0,user_Input):
    dctnry.setdefault(i,[]);
    Str=raw_input();
    Str2=[];
    Str2=Str.split();
    dctnry[i].append(Str2[1]);
    n=int(Str2[0]);
    for j in range(0,n):
        dctnry[i].append(raw_input());
 
for i in range(0,len(dctnry)):
    dctnry[i].append(0);
    for j in range(1,len(dctnry[i])-1):
        if len(dctnry[i][j].split())==1:
            if dctnry[i][j]=="TOP_CONTRIBUTOR":
                dctnry[i][len(dctnry[i])-1]=dctnry[i][len(dctnry[i])-1]+300;
            elif dctnry[i][j]=="CONTEST_HOSTED":
                dctnry[i][len(dctnry[i])-1]=dctnry[i][len(dctnry[i])-1]+50;
        elif len(dctnry[i][j].split())==2:
            x=[];
            x=dctnry[i][j].split();
            if x[0]=="CONTEST_WON":
                if int(x[1])<=20:
                    dctnry[i][len(dctnry[i])-1]=dctnry[i][len(dctnry[i])-1]+300+20-int(x[1]);
                elif int(x[1])>20:
                    dctnry[i][len(dctnry[i])-1]=dctnry[i][len(dctnry[i])-1]+300;
            elif x[0]=="BUG_FOUND":
                dctnry[i][len(dctnry[i])-1]=dctnry[i][len(dctnry[i])-1]+int(x[1]);
 
 
for i in range(0,len(dctnry)):
    if(dctnry[i][0]=="INDIAN"):
        print(dctnry[i][len(dctnry[i])-1]/200);
    elif(dctnry[i][0]=="NON_INDIAN"):
        print(dctnry[i][len(dctnry[i])-1]/400);
 