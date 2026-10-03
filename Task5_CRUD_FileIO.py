FILE = "tasks.txt"

def load():
    try: return [t.strip() for t in open(FILE)]
    except: return []

def save(tasks):
    open(FILE, "w").write("\n".join(tasks))

tasks = load()

while True:
    print("\n1.View  2.Add  3.Update  4.Delete  5.Exit")
    c = input("Choice: ")

    if c == "1":
        print("\nTasks:")
        for i, t in enumerate(tasks, 1): print(i, t)

    elif c == "2":
        tasks.append(input("New task: "))
        print("Added!")

    elif c == "3":
        for i, t in enumerate(tasks, 1): print(i, t)
        n = int(input("Task number: "))
        tasks[n-1] = input("Updated task: ")
        print("Updated!")

    elif c == "4":
        for i, t in enumerate(tasks, 1): print(i, t)
        n = int(input("Task number: "))
        tasks.pop(n-1)
        print("Deleted!")

    elif c == "5":
        save(tasks)
        print("Saved & Exit!")
        break

    else:
        print("Invalid choice!")
