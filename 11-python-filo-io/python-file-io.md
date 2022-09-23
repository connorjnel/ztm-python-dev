# Python File I/O

- Reading and writing files, interacting with external data
- Py has built in fuction for IO, called `open`
- ex. `open("text.txt")`
- ex. `open("D:\\myfiles\text.txt", "r")`
- Can use `.read()` method to read file, then need to use `.close()` to stop reading file, good practice

## Open parameters

- `("text.txt","r")` - Read - Default value. Opens a file for reading, error if the file does not exist
- `("text.txt","a")`- Append - Opens a file for appending, creates the file if it does not exist
- `("text.txt","w")` - Write - Opens a file for writing, creates the file if it does not exist
- `("text.txt","x")`- Create - Creates the specified file, returns an error if the file exists

## with open

- Best practice to open files
- ex. `with open("test.txt", mode="a") as my_file`
- Default mode is "r" for read
- If you write to a non existing file, it creates that file

## Relative Paths

- Using relative better, less likely that you get file not found
- windows uses `\`, linux/unix uses `/`
- most web based systems are linux based though so `/`
- `./` - current folder
- `../` - one folder up
- py built in module for filesystem paths, `pathlib`, creates path that works with windows and linux systems
