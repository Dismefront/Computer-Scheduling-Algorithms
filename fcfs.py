process1 = "CPU(48);IO1(14);CPU(24);IO2(16);CPU(60);IO2(20);CPU(48);IO1(12);CPU(24);IO2(18)".split(';')
process2 = "CPU(2);IO2(20);CPU(6);IO1(10);CPU(10);IO2(10);CPU(6);IO1(10)".split(";")
process3 = "CPU(4);IO2(16);CPU(4);IO2(16);CPU(10);IO2(14);CPU(4);IO1(12);CPU(6);IO2(18);CPU(6);IO2(16);CPU(10);IO2(16)".split(";")
process4 = "CPU(2);IO1(10);CPU(2);IO2(18);CPU(2);IO2(16);CPU(8);IO2(18)".split(";")
process5 = "CPU(12);IO1(14);CPU(12);IO2(12);CPU(36);IO1(10);CPU(36);IO2(16)".split(";")
process6 = "CPU(4);IO2(16);CPU(2);IO2(18);CPU(6);IO1(12);CPU(10);IO1(18);CPU(4);IO1(18)".split(";")

# process number, interface, time to execute, isRunning, isQueued
process1 = list(map(lambda x : [1, x[0:3], int(x[4:-1]), False, False], process1))
process2 = list(map(lambda x : [2, x[0:3], int(x[4:-1]), False, False], process2))
process3 = list(map(lambda x : [3, x[0:3], int(x[4:-1]), False, False], process3))
process4 = list(map(lambda x : [4, x[0:3], int(x[4:-1]), False, False], process4))
process5 = list(map(lambda x : [5, x[0:3], int(x[4:-1]), False, False], process5))
process6 = list(map(lambda x : [6, x[0:3], int(x[4:-1]), False, False], process6))
startedProcecess = [False, False, False, False, False, False]
processes = [process1, process2, process3, process4, process5, process6]

time = 1
CPUs = [[], [], [], []]
IOs = [[], []]
CPUqueue = []
IOqueues = [[], []]


def newEmptyTick():
    for cpu in CPUs:
        cpu.append(0)
    for io in IOs:
        io.append(0)


def startProcess(process):
    task = process[0]
    task[4] = True
    CPUqueue.append(task)


def restoreBusy():
    for cpu in CPUs:
        if len(cpu) >= 2 and cpu[-2] != 0:
            curProcess = cpu[-2] - 1
            if len(processes[curProcess]) == 0:
                continue
            if processes[curProcess][0][3] is True and processes[curProcess][0][2] > 0:
                processes[curProcess][0][2] -= 1
                cpu[-1] = cpu[-2]
                if processes[curProcess][0][2] == 0:
                    processes[curProcess].pop(0)
    for io in IOs:
        if len(io) >= 2 and io[-2] != 0:
            curProcess = io[-2] - 1
            if len(processes[curProcess]) == 0:
                continue
            if processes[curProcess][0][3] is True and processes[curProcess][0][2] > 0:
                processes[curProcess][0][2] -= 1
                io[-1] = io[-2]
                if processes[curProcess][0][2] == 0:
                    processes[curProcess].pop(0)


def handleTick():

    def findFreeCPU():
        for i in CPUs:
            if i[-1] == 0:
                return i
        return None

    if len(CPUqueue) > 0:
        freeCPU = findFreeCPU()
        if freeCPU is not None:
            task = CPUqueue.pop(0)
            curProcess = task[0] - 1
            processes[curProcess][0][2] -= 1
            processes[curProcess][0][3] = True
            freeCPU[-1] = task[0]
    
    for i in range(len(IOqueues)):
        if len(IOqueues[i]) > 0 and IOs[i][-1] == 0:
            task = IOqueues[i].pop(0)
            IOs[i][-1] = task[0]
            task[2] -= 1
            task[3] = True

    for i, process in enumerate(processes):
        if len(process) == 0:
            continue
        curTask = process[0]
        if curTask[3] is False and curTask[4] is False:
            curTask[4] = True
            if curTask[1] == 'IO1':
                IOqueues[0].append(curTask)
            elif curTask[1] == 'IO2':
                IOqueues[1].append(curTask)
            elif curTask[1] == 'CPU' and startedProcecess[i] is True:
                CPUqueue.append(curTask)


while len(processes[0] + processes[1] + processes[2] + processes[3] + processes[4] + processes[5]) != 0:
    newEmptyTick()
    restoreBusy()
    if time == 1:
        startedProcecess[0] = True
        startProcess(processes[0])
    elif time == 3:
        startedProcecess[1] = True
        startProcess(processes[1])
    elif time == 5:
        startedProcecess[2] = True
        startProcess(processes[2])
    elif time == 7:
        startedProcecess[3] = True
        startProcess(processes[3])
    elif time == 9:
        startedProcecess[4] = True
        startProcess(processes[4])
    elif time == 11:
        startedProcecess[5] = True
        startProcess(processes[5])
    handleTick()
    time += 1

# ------------------------visual------------------------------

print("time\tCPU1\tCPU2\tCPU3\tCPU4\tIO1\tIO2")
for i in range(len(CPUs[0])):
    print(f"{i + 1}\t{CPUs[0][i]}\t{CPUs[1][i]}\t{CPUs[2][i]}\t{CPUs[3][i]}\t{IOs[0][i]}\t{IOs[1][i]}")

# ------------------------stats-------------------------------

process1 = "CPU(48);IO1(14);CPU(24);IO2(16);CPU(60);IO2(20);CPU(48);IO1(12);CPU(24);IO2(18)".split(';')
process2 = "CPU(2);IO2(20);CPU(6);IO1(10);CPU(10);IO2(10);CPU(6);IO1(10)".split(";")
process3 = "CPU(4);IO2(16);CPU(4);IO2(16);CPU(10);IO2(14);CPU(4);IO1(12);CPU(6);IO2(18);CPU(6);IO2(16);CPU(10);IO2(16)".split(";")
process4 = "CPU(2);IO1(10);CPU(2);IO2(18);CPU(2);IO2(16);CPU(8);IO2(18)".split(";")
process5 = "CPU(12);IO1(14);CPU(12);IO2(12);CPU(36);IO1(10);CPU(36);IO2(16)".split(";")
process6 = "CPU(4);IO2(16);CPU(2);IO2(18);CPU(6);IO1(12);CPU(10);IO1(18);CPU(4);IO1(18)".split(";")

# process number, interface, time to execute, isRunning, isQueued
process1 = list(map(lambda x : [1, x[0:3], int(x[4:-1]), False, False], process1))
process2 = list(map(lambda x : [2, x[0:3], int(x[4:-1]), False, False], process2))
process3 = list(map(lambda x : [3, x[0:3], int(x[4:-1]), False, False], process3))
process4 = list(map(lambda x : [4, x[0:3], int(x[4:-1]), False, False], process4))
process5 = list(map(lambda x : [5, x[0:3], int(x[4:-1]), False, False], process5))
process6 = list(map(lambda x : [6, x[0:3], int(x[4:-1]), False, False], process6))
startedProcecess = [False, False, False, False, False, False]
processes = [process1, process2, process3, process4, process5, process6]

print("Время до завершения всех процессов:", len(CPUs[0]))
serveTime = []
for i in range(len(processes)):
    serveTime.append(0)
    for j in range(len(processes[i])):
        serveTime[i] += processes[i][j][2]
    print(f"Время обслуживания процесса {i + 1}: {serveTime[i]}")

turnoverTime = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
for i in range(len(processes)):
    for j in range(len(CPUs[0])):
        if CPUs[0][j] != 0 and turnoverTime[CPUs[0][j] - 1][0] == 0:
            turnoverTime[CPUs[0][j] - 1][0] = j + 1
        if CPUs[0][j] != 0:
            turnoverTime[CPUs[0][j] - 1][1] = j + 1
        if CPUs[1][j] != 0 and turnoverTime[CPUs[1][j] - 1][0] == 0:
            turnoverTime[CPUs[1][j] - 1][0] = j + 1
        if CPUs[1][j] != 0:
            turnoverTime[CPUs[1][j] - 1][1] = j + 1
        if CPUs[2][j] != 0 and turnoverTime[CPUs[2][j] - 1][0] == 0:
            turnoverTime[CPUs[2][j] - 1][0] = j + 1
        if CPUs[2][j] != 0:
            turnoverTime[CPUs[2][j] - 1][1] = j + 1
        if CPUs[3][j] != 0 and turnoverTime[CPUs[3][j] - 1][0] == 0:
            turnoverTime[CPUs[3][j] - 1][0] = j + 1
        if CPUs[3][j] != 0:
            turnoverTime[CPUs[3][j] - 1][1] = j + 1
        if IOs[0][j] != 0:
            turnoverTime[IOs[0][j] - 1][1] = j + 1
        if IOs[1][j] != 0:
            turnoverTime[IOs[1][j] - 1][1] = j + 1
    print(f"Время оборота процесса {i + 1}: {turnoverTime[i][1] - turnoverTime[i][0]}")

for i in range(len(processes)):
    print(f"Время простоя {i + 1}: {turnoverTime[i][1] - turnoverTime[i][0] - serveTime[i]}")

for i in range(len(processes)):
    print(f"Коэффициент голодания {i + 1}: {(turnoverTime[i][1] - turnoverTime[i][0]) / serveTime[i]}")