from subprocess import call
import os

f = open("names.txt", "rw");
lines = f.readlines();

f2 = open("emails.txt", "w");

for line in lines:
    print(line);
    people = line.split(':');
    print(people);
    p1 = people[0];
    p2 = people[1];
    ns1 = people[0].split(",");
    ns1[0] = ns1[0].replace(" ", "")
    ns1[1] = ns1[1].replace(" ", "")
    ns1[0] = ns1[0].replace("\n", "")
    ns1[1] = ns1[1].replace("\n", "")
    ns2 = people[1].split(",");
    ns2[0] = ns2[0].replace(" ", "")
    ns2[1] = ns2[1].replace(" ", "")
    ns2[0] = ns2[0].replace("\n", "")
    ns2[1] = ns2[1].replace("\n", "")
    n1 = ns1[1] + "." + ns1[0] + "@tufts.edu\n";
    n2 = ns2[1] + "." + ns2[0] + "@tufts.edu\n";
    print(n1);
    print(n2);
    f2.write(n1);
    f2.write(n2);
