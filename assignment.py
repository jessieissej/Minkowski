import math
a1 = [35, 45, 22, 55, 30, 40, 50, 27, 48, 33]
b1 = [500, 800, 300, 200, 400, 700, 250, 350, 600, 450]
k1 = [35, 500]
k2 = [45, 800]
k3 = [22, 300]

Cluster1 = []
Cluster2 = []
Cluster3 = []
Assignment = []

print("Customer\tAge (years)\tMonthly Milage (miles)")
for i in range (10) :
    print(f"Customer{i+1}\t{a1[i]}\t\t{b1[i]}")

print("\n\nUsing Euclidean Distance, compute for the distance of the given data from the cluster\n");

for i in range (10) :
    assingment = 0
    distance1 = math.sqrt(((a1[i] - k1[0])**2) + ((b1[i] - k1[1])**2))
    Cluster1.append(distance1);
    print(f"\n\nGiven : ({a1[i]}, {b1[i]}) ")
    print(f"Distance from Cluster 1 ({k1[0]}, {k1[1]}): {distance1:.2f}")
    distance2 = math.sqrt(((a1[i] - k2[0])**2) + ((b1[i] - k2[1])**2))
    Cluster2.append(distance2);
    print(f"Distance from Cluster 2 ({k2[0]}, {k3[1]}): {distance2:.2f}")
    distance3 = math.sqrt(((a1[i] - k3[0])**2) + ((b1[i] - k3[1])**2))
    Cluster3.append(distance3);
    print(f"Distance from Cluster 3 ({k3[0]}, {k3[1]}): {distance3:.2f}")
    if(distance1 < distance2 and distance1 < distance3):
        assingment = 1
    Assignment.append(1)
    print("####Since Cluster 1 is the nearest####")
    print(f"Assignment : {assingment}")
    print("\nUpdate the centroid:")
    print("Cluster\tX\t\tY")
    print(f"K1\t{k1[0]}+{a1[i]}/2=\t{k1[1]}+{b1[i]}/2=")
    k1[0] = (k1[0] + a1[i]) / 2
    k1[1] = (k1[1] + b1[i]) / 2
    print(f"\t{k1[0]}\t\t{k1[1]}")
    if(distance2 < distance1 and distance2 < distance3):
        assingment = 2
    Assignment.append(2)
    print("####Since Cluster 2 is the nearest####")
    print(f"Assignment : {assingment}")

    print("\nUpdate the centroid:")
    print("Cluster\tX\t\tY")
    print(f"K2\t{k2[0]}+{a1[i]}/2=\t{k2[1]}+{b1[i]}/2=")
    k2[0] = (k2[0] + a1[i]) / 2
    k2[1] = (k2[1] + b1[i]) / 2
    print(f"\t{k2[0]}\t\t{k2[1]}")
    if(distance3 < distance1 and distance3 < distance2):
        assingment = 3
    Assignment.append(3)
    print("####Since Cluster 3 is the nearest####")
    print(f"Assignment : {assingment}")
    print("\nUpdate the centroid:")
    print("Cluster\tX\t\tY")
    print(f"K3\t{k3[0]}+{a1[i]}/2=\t{k3[1]}+{b1[i]}/2=")
    k3[0] = (k3[0] + a1[i]) / 2
    k3[1] = (k3[1] + b1[i]) / 2
    print(f"\t{k3[0]}\t\t{k3[1]}")
    print("\nCurrent data:")
    print(f"Centroid 1: ({k1[0]}, {k1[1]})")
    print(f"Centroid 2: ({k2[0]}, {k2[1]})")
    print(f"Centroid 3: ({k3[0]}, {k3[1]})\n")


print("Given(age,mileage)\tDistance form K1\tDistance from K2\tDistance fromK3\tAssignment")
for j in range (i+1) :
    print(f"({a1[j]},{b1[j]})\t\t{Cluster1[j]:.2f}\t\t\t{Cluster2[j]:.2f}\t\t\t{Cluster3[j]:.2f}\t\t\t{Assignment[j]}")