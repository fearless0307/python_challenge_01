# :stew: Resturant Finder
## Documentation
A user gives three inputs, one is date second is time and third is file name of `csv` which contains the data of restaurants. 
>Note : The date is in the format of `dd-MM-yyyy` and time is in the format of `mm:hh am/pm`. The file should be in csv format and exists in the directory.
Data of restaurants store as a class. There are two data members of class one is the restaurant name and second is the timing of the restaurant.

Functions of class
- do_changes
- display
- is_open

### do_changes
This function maniculates the day and time store in csv and makes a timing schedule and store in class.

### display
This function shows the name of the restaurant.

### is_open
This function takes the parameter of date and time and then it checks in the timing of the restaurant that restaurant is open at given day and time. If it matches the required criteria it returns true otherwise it returns false.