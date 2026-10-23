s="ab"
state=0
for c in s:
    if state==0 and c=="a":state=1
    elif state==1 and c=="b":state=2
    else:state=-1
print("accepted" if state==2 else "Rejected")
    