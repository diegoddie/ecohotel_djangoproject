# **MY FIRST DJANGO PROJECT (USING A BLOCKCHAIN!)**
## _Goal of the project_
___
The goal of this project is to implement a system of tracking consumption and energy produced by a hotel with photovoltaic panels.
To achieve this I will use Django, Redis (a NoSQL database) and an Ethereum blockchain testnet.

The exercise requires to create a web application that shows, in table format, the amount of energy produced and consumed every day by the hotel. At each entry (corresponding to what happens in the previous 24 hours) I will start a transaction on Ethereum Goerli containing the two values in the note field.

## _Features implemented_
___
The features implemented in this project are:
- A main page, accessible only to logged-in users, showing the table containing the values in question and the hash of the transaction
- A page, to which only administrators can access, where you can see the total consumed and produced
- A logging system to store the last IP that had access to the platform for a certain administrator user, so as to display a warning message when this is different from the previous one