import os, struct

FMT, SIZE = "i20sf", struct.calcsize("i20sf")  # Record format

def add_emp(file, emp_id, name, sal):
    with open(file, "ab") as f:
        f.write(struct.pack(FMT, emp_id, name.encode().ljust(20, b' '), sal))

def read_emp(file, rec):
    with open(file, "rb") as f:
        f.seek(rec * SIZE)
        data = f.read(SIZE)
        if data:
            eid, name, sal = struct.unpack(FMT, data)
            print(f"ID={eid}, Name={name.decode().strip()}, Salary={sal}")
        else:
            print("Record not found")

def update_emp(file, rec, emp_id, name, sal):
    with open(file, "rb+") as f:
        f.seek(rec * SIZE)
        f.write(struct.pack(FMT, emp_id, name.encode().ljust(20, b' '), sal))

def show_all(file):
    if not os.path.exists(file): return print("No records")
    with open(file, "rb") as f:
        rec = 0
        while (data := f.read(SIZE)):
            eid, name, sal = struct.unpack(FMT, data)
            print(f"Rec {rec}: ID={eid}, Name={name.decode().strip()}, Salary={sal}")
            rec += 1

if __name__ == "__main__":
    fname = "employees.dat"
    while True:
        print("\n1.Add 2.Read 3.Update 4.Show All 5.Exit")
        ch = input("Choice: ")
        if ch == "1":
            add_emp(fname, int(input("ID: ")), input("Name: "), float(input("Salary: ")))
        elif ch == "2":
            read_emp(fname, int(input("Record #: ")))
        elif ch == "3":
            update_emp(fname, int(input("Record #: ")), int(input("ID: ")), input("Name: "), float(input("Salary: ")))
        elif ch == "4":
            show_all(fname)
        elif ch == "5":
            break
        else:
            print("Invalid choice")

