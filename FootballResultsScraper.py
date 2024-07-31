from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import ttk

def matchresults(teamname):
    url = 'https://www.skysports.com/'+teamname+'-results/2023-24'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    #__________________________________________FINDING THE SCORES__________________________________________________#
    scores = soup.findAll('span',attrs = {'class':'matches__teamscores'})
    scoreList = [score.text.replace('\n', '').strip() for score in scores]
    results = [scoreList[i].strip().replace("                            ", " : ") for i in range(len(scoreList))]

    #_____________________________________________________________________________________________________________#
    #__________________________________________FINDING TEAM NAMES_________________________________________________#
    teams = soup.findAll('span', class_ = 'swap-text__target')
    teamList = [team.text.replace('<span class="swap-text__target">', "") for team in teams]
    teamList.pop(0)
    comp = []
    for i in range(0, len(teamList), 2):
        combined_string = " vs ".join(teamList[i:i+2])
        comp.append(combined_string)

    #_____________________________________________________________________________________________________________#

    # _________________________________________FINDING MATCH DATE_________________________________________________#
    dates = soup.findAll('h4',attrs = {'class':'fixres__header2'})
    dateList = [date.text.replace('<h4 class="fixres__header2">', '').strip() for date in dates]
    #_____________________________________________________________________________________________________________#

    # def chelseaResults():
    i = 4
    output = ''
    while i >= 0:
        output +=( "\n" + comp[i] + "\nResult: " + results[i] + "\n"  + dateList[i] + "\n")
        i = i-1
    return output

# #_____________________________________________________________________________________________________________#

# # _________________________________________GUI_________________________________________________#

def display_output():
    user_input = entry.get().lower()
    results = matchresults(user_input)
    output = f"Team name: {user_input}\n{results}"
    output_label.config(text=output)


# Create the main window
root = tk.Tk()
root.title("Club team results")
root.geometry("700x550")

# Create a label for instructions
instruction_label = tk.Label(root, text="Enter a clubs name:", font=12)
instruction_label.pack(pady=10)

# Create an entry widget for user input
entry = tk.Entry(root, width=60)
entry.pack(pady=0)


# Create a button to trigger the output display
entry.bind('<Return>', lambda event: display_output())
button = tk.Button(root, text="Submit", command=display_output, font=12)
button.pack(pady=10)

# Create a label to display the output
output_label = tk.Label(root, text="Results", justify=tk.LEFT, font= 12, borderwidth=2, relief="groove")
output_label.pack(pady=20)



# Run the application
root.mainloop()