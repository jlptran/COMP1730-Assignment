

def import_Canberra():
    '''Reads and stores the rainfall data for Canberra'''
    import csv
    with open('Rainfall_Canberra_070247.csv','r') as data_file:
        ##Skips the first line which are the column headings
        next(data_file)
        ##Reads the file
        readfile = csv.reader(data_file)
        ##List where data will be stored
        data_list = []
        ##Temporary list to store data which may or may not be invalid
        buffer_list = []
        ##Iterates through the data in the CSV file and checks whether
        ##or not to add it to data_list
        for row in readfile:
            ##Appends rows which have empty data in row 5,6 and 7 to buffer_list
            ##These may be rows where data is taken over multiple days
            if row[5] =="" and row[6] =="" and row[7] =="":
                buffer_list.append(row)
            ##Checks if it is a row of complete data and appends it to data_list  
            ##Adds all the days of a multiday reading
            elif row[5] !="" and row[6] !="" and row[7] !="":
                ##Number of days in the complete data reading
                numDay = int(row[6])
                ##If it is more than 1 day for the reading, it iterates through each
                ##of the previous days and appends all of them to data_list
                while numDay > 1:
                    tempRow = []
                    tempRow = buffer_list.append([1-numDay])
                    data_list.append(tempRow)
                    numDay-=1
                ##Appends the row with complete data to data_list
                data_list.append(row)
                ##Empties buffer_list
                buffer_list = []
            ##Prints data_list
            ##print(data_list)