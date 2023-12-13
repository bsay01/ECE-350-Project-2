import os, pandas

# returns a list of relative paths to all csv files in the working folder
def checkDirForCSV(dir_name = "", indent = 0):
    print("\t"*indent + "Files found in \"" + dir_name + "\" folder:")
    indent += 1
    files = []
    for entry in os.listdir(dir_name):
        if ".csv" in entry: # for a csv file
            print("\t"*indent + dir_name + "\\" + entry)
            files.append(dir_name + "\\" + entry)
        elif "." not in entry: # for a subfolder
            files.extend(checkDirForCSV(dir_name + "\\" + entry, indent))
    return files

print("\nAnalyzing files in the \"data\" folder\n")

files = checkDirForCSV(".\\data") # check for csv files in the current directory
files.sort()

df = pandas.read_csv(files[0])
for file in files:
    print("Adding file \"" + file + "\"...")
    df = pandas.concat([df, pandas.read_csv(file, dtype='unicode')]).drop_duplicates()

print("\nfixing \"NaN\" values\n")
nan_value = float("NaN")
df = df.replace("", nan_value)
df = df.dropna(how = 'all', axis = 1)

df.sort_values('time')

print("\nCreating file containing combined data\n")
df.to_csv(".\\data_processed\\0-data_processed.csv")

device_names = []
device = [0, 0]
temp_df = df

for model, id in zip(df['model'], df['id']):

    device = [model, id]

    if device not in device_names:

        print("Extracting data for {model} : {id}".format(model=device[0], id=device[1]))

        device_names.append(device)

        temp_df = temp_df[temp_df['id'] == device[1]]
        temp_df = df[df['model'] == device[0]]

        temp_df = temp_df.dropna(how = 'all', axis = 1)

        temp_df.to_csv(".\\data_processed\\{model}_{id}.csv".format(model=device[0], id=device[1]))

print("\nData processing complete\n")
