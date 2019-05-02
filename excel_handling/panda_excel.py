# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
file = 'example.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Sheet1')




df = pd.read_excel('example_sheets1.xlsx',sheet_name='Session1',
                   header=1,dtype={'Names':str,'ID':str,
                                        'Mean':int, 'Session':str})
                                        
pd.info()




# save to excel 
df.to_excel('NamesAndAges.xlsx', sheet_name='Names and Ages', index=False)






import pandas as pd
 
# Create some variables
trials = [1, 2, 3, 4, 5, 6]
subj_id = [1]*6
group = ['Control']*6
condition = ['Affect']*3 + ['Neutral']*3
 
# Create a dictionairy
data = {'Condition':condition, 'Subject_ID':subj_id, 
        'Trial':trials, 'Group':group}
 
# Create the dataframe
df = pd.DataFrame(data)
df.head()




