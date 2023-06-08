jenis_komponen = ["MPPF FORM", "CONTROL HORN", "PUSH ROD WIRE", "BRUSHLESS MOTOR", "LINKAGE STOPPER", "ESC", "RECIEVER", "CARBON FIBER", "SERVO", "RC LIPO BATTERY", "PROPELLER", "FLYSKY"]                   
harga_komponen = [23,3,2,15.79,12,67,61,25.30,5.20,57.56,5.50,161]   
jumlah = [0,1,2,3,4,5,6,7,8,9,10,11]                                                  

print("HARGA MPPF FORM=RM23,CONTROL HORB=RM3,PUSH ROD WIRE=RM2,BRUSHLESS MOTOR=RM15.79,LINKAGE STOPPER=RM12,ESC=RM67,RECIEVER=RM61,CARBON FIBER=RM25.30,SERVO=RM5.20,RC LIPO BATTERY=RM57.56,PROPELLER=RM5.50,FLYSKY-i6 REMOTE CONTROL=RM161")
a=int(input("Masukkkan tempahan untuk MPPF FORM:"))
b=int(input("Masukkkan tempahan untuk CONTROL HORN:"))
c=int(input("Masukkkan tempahan untuk PUSH ROD WIRE:"))
d=int(input("Masukkkan tempahan untuk BRUSHLESS MOTOR:"))
e=int(input("Masukkkan tempahan untuk LINKAGE STOPPER:"))
f=int(input("Masukkkan tempahan untuk ESC:"))
g=int(input("Masukkkan tempahan untuk RECIEVER:"))
h=int(input("Masukkkan tempahan untuk CARBON FIBER:"))
i=int(input("Masukkkan tempahan untuk SERVO:"))
j=int(input("Masukkkan tempahan untuk RC LIPO BATTERY:"))
k=int(input("Masukkkan tempahan untuk PROPELLER:"))
l=int(input("Masukkkan tempahan untuk FLYSKY-i6 REMOTE CONTROL:"))

tempahan = [a,b,c,d,e,f,g,h,i,j,k,l]

def jumlah_harga():
    for i in range (12):
        jumlah[i] = harga_komponen[i]*tempahan[i]
    return(jumlah)

def cetak():
    print("\n\nTempahan anda ialah:")
    print(a,"komponen", jenis_komponen[0])
    print(b,"komponen", jenis_komponen[1]) 
    print(c,"komponen", jenis_komponen[2])
    print(d,"komponen", jenis_komponen[3])
    print(e,"komponen", jenis_komponen[4])
    print(f,"komponen", jenis_komponen[5])
    print(g,"komponen", jenis_komponen[6])
    print(h,"komponen", jenis_komponen[7])
    print(i,"komponen", jenis_komponen[8])
    print(j,"komponen", jenis_komponen[9])
    print(k,"komponen", jenis_komponen[10])
    print(l,"komponen", jenis_komponen[11])

    print("\n jumlah harga untuk tempahan ialah RM",sum (jumlah))
jumlah_harga()
cetak()






