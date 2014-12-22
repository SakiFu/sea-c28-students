
#!/usr/bin/env python
donor_dict = {'Andy Smith': [10, 20, 30, 20], 'Brian Miller': [20, 40, 30],
              'Daniel Brown': [30, 40, 10, 10, 30], 'Eli Feng': [50, 70]}


def safe_input():
    try:
        raw_input()
    except (EOFError, KeyboardInterrupt):
        return None


#Prompt for a Full Name.
def ask_name():
    name = raw_input("What is the donor's full name? ")
    if name == 'list':
        print donor_dict.keys()
    if name in donor_dict.keys():
        donor_dict[name] = []
        ask_amount(name)
    elif name not in donor_dict.keys():
        donor_dict[name] = []
        ask_amount(name)

def ask_amount(name):
    amount = raw_input("How much is the donation? ")
    amount = int(amount)
    while True:
        try:
            amount = int(amount)
        except ValueError:
            amount = raw_input("Please entern number. ")
        else:
            break
    donor_dict[name].append(amount)
    send_thankyou(name, amount)


def send_thankyou(name, amount):
    email = "Dear %s, Thank you for your donation of $%d" % \
            (name, amount)
    print email


def create_report():
    donor_report = {}
    for k, v in donor_dict.items():
        total = sum(v)
        times = len(v)
        avg = total / times
        donor_report.setdefault(k, [total, times, avg])

    print "{:^15} {:<10} {:^10} {:<10}".format('name', 'total', 'times', 'avg')
    for key, value in donor_report.items():
        print "{:<15} ${:<10} {:^10d} ${:<20}".format(key, value[0], value[1], value[2])
    print "\n"


def exit():
    exit(0)


def main():
    choice = {1: ask_name, 2: create_report, 3: exit}
    while True:
            print u"1:Send a Thank you"
            print u"2:Create a Report"
            print u"3:Exit "

            user_input = raw_input()
            choice[int(user_input)]()

if __name__ == '__main__':
    main()
