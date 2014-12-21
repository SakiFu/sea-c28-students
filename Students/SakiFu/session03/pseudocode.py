
#!/usr/bin/env python
This is the list of donors
donor_dict = {'Andy': [10, 20, 30, 20], 'Brian': [20, 40, 30],
                   'Daniel': [30, 40,10, 10, 30]}

prompt the user to choose from a menu of 2 actions: 'Send a Thank You' or 'Create a Report'.

If the user chose 'Send a Thank You'

Prompt for a Full Name.

    name = raw_input("What is the donor's full name?")
    if name is 'list', show the list of the donor names and re-prompt
    if name in the list, move on.
    if name in the list, add that name to the list.

Prompt for the amount of donation.
    amount = raw_input("How much is the donation?")
    if amount is not digit, re-prompt.
    if amount is digit, add the amount to the list.

Compose an email thanking the donor for their generous donation.


If the user chose 'Create a Report'
Create a report, including Donor Name, total donated, number of donations and average donation amount as values in each row
Print the report and return to the original report.
