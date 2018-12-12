from itertools import combinations
import threading
numOfApp = 2


class test (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print ("Starting " + self.name)
        # TEST Graph

        numOfNodes = range(0, 4)
        for numOfVRC in range(1, 5):
            s = ""
            f = open("test_vm" + str(numOfVRC) + ".txt", "w+")
            for combApp1 in combinations(numOfNodes, numOfVRC):
                for combApp2 in combinations(numOfNodes, numOfVRC):
                    a = ""
                    for i in range(0, len(combApp1)):
                        a = a + str(combApp1[i]) + ","
                    for j in range(0, len(combApp2)):
                        a = a + str(combApp2[j]) + ","
                    s = s + a + "\n"
            f.write(s)
            f.close()
        print("Exiting " + self.name)


# ******************************************


class noel(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # Noel Graph

        numOfNodes = range(0, 19)

        for numOfVRC in range(1, 5):
            s = ""
            f = open("noel_vm" + str(numOfVRC) + ".txt", "w+")
            for combApp1 in combinations(numOfNodes, numOfVRC):
                for combApp2 in combinations(numOfNodes, numOfVRC):
                    a = ""
                    for i in range(0, len(combApp1)):
                        a = a + str(combApp1[i]) + ","
                    for j in range(0, len(combApp2)):
                        a = a + str(combApp2[j]) + ","
                    s = s + a + "\n"
            f.write(s)
            f.close()
        print("Exiting " + self.name)

    #print(s)
# ******************************************


class sago(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # Sago Graph

        numOfNodes = range(0, 18)

        for numOfVRC in range(1, 5):
            s = ""
            f = open("sago_vm" + str(numOfVRC) + ".txt", "w+")
            for combApp1 in combinations(numOfNodes, numOfVRC):
                for combApp2 in combinations(numOfNodes, numOfVRC):
                    a = ""
                    for i in range(0, len(combApp1)):
                        a = a + str(combApp1[i]) + ","
                    for j in range(0, len(combApp2)):
                        a = a + str(combApp2[j]) + ","
                    s = s + a + "\n"
            f.write(s)
            f.close()
        print("Exiting " + self.name)


    #print(s)
# ******************************************


class shentel(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # Shentel Graph

        numOfNodes = range(0, 28)

        for numOfVRC in range(1, 5):
            s = ""
            f = open("shentel_vm" + str(numOfVRC) + ".txt", "w+")
            for combApp1 in combinations(numOfNodes, numOfVRC):
                for combApp2 in combinations(numOfNodes, numOfVRC):
                    a = ""
                    for i in range(0, len(combApp1)):
                        a = a + str(combApp1[i]) + ","
                    for j in range(0, len(combApp2)):
                        a = a + str(combApp2[j]) + ","
                    s = s + a + "\n"
            f.write(s)
            f.close()
        print("Exiting " + self.name)


# ******************************************


class spiralight(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # Spiralight Graph

        numOfNodes = range(0, 15)

        for numOfVRC in range(1, 5):
            s = ""
            f = open("spiralight_vm" + str(numOfVRC) + ".txt", "w+")
            for combApp1 in combinations(numOfNodes, numOfVRC):
                for combApp2 in combinations(numOfNodes, numOfVRC):
                    a = ""
                    for i in range(0, len(combApp1)):
                        a = a + str(combApp1[i]) + ","
                    for j in range(0, len(combApp2)):
                        a = a + str(combApp2[j]) + ","
                    s = s + a + "\n"
            f.write(s)
            f.close()
        print("Exiting " + self.name)

# ******************************************
# Missouri Graph


class missouri(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # Spiralight Graph

        numOfNodes = range(0, 67)

        for numOfVRC in range(1, 5):
            s = ""
            f = open("missouri_vm" + str(numOfVRC) + ".txt", "w+")
            for combApp1 in combinations(numOfNodes, numOfVRC):
                for combApp2 in combinations(numOfNodes, numOfVRC):
                    a = ""
                    for i in range(0, len(combApp1)):
                        a = a + str(combApp1[i]) + ","
                    for j in range(0, len(combApp2)):
                        a = a + str(combApp2[j]) + ","
                    s = s + a + "\n"
            f.write(s)
            f.close()
        print("Exiting " + self.name)

# Create new threads


test = test(1, "Thread-1", 1)
noel = noel(2, "Thread-2", 2)
sago = sago(3, "Thread-3", 3)
shantel = shentel(4, "Thread-4", 4)
spiralight = spiralight(5, "Thread-5", 5)
missouri = missouri(6, "Thread-6", 6)


# Start new Threads
test.start()
noel.start()
sago.start()
shantel.start()
spiralight.start()
missouri.start()
