tasks = []

while True:
    print("\n1.View  2.Add  3.Update  4.Delete  5.Exit")
    c = input("Choice: ")

    if c == "1":
        for i, t in enumerate(tasks, 1): print(i, t)

    elif c == "2":
        tasks.append(input("New task: "))
        print("Added!")

    elif c == "3":
        for i, t in enumerate(tasks, 1): print(i, t)
        n = int(input("Task no: "))
        tasks[n-1] = input("Updated task: ")
        print("Updated!")

    elif c == "4":
        for i, t in enumerate(tasks, 1): print(i, t)
        n = int(input("Task no: "))
        tasks.pop(n-1)
        print("Deleted!")

    elif c == "5":
        print("Exit…")
        break

    else:
        print("Invalid!")
