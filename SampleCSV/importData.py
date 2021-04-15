import os

location = "./"
files_in_dir = []

for r, d, f in os.walk(location):
    for item in f:
        if '.csv' in item:
            files_in_dir.append(os.path.join(r, item))


for item in files_in_dir:
    cmd = "csvsql --db postgresql://postgres:Nandhu6$@localhost:5432/demographics --insert --no-inference " + item
    os.system(cmd)
    print(item, "has been inserted")
