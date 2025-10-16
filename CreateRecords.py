import argparse

def main(args):
    start_day = int(args.start_day)
    days_total = int(args.days_total)
    remaining_penalties = int(args.remaining_penalties) - 1
    value = str(args.value)

    print()

    lines = []
    for i in range(days_total):
        if remaining_penalties > 0:
            lines.append(f'| ***{start_day + i}*** | {value} | {remaining_penalties} remaining. |')
            remaining_penalties -= 1
        else:
            lines.append(f'| ***{start_day + i}*** | {value} | |')
    
    for i in range(len(lines))[::-1]:
        print(lines[i])
    
    print()
    print(f'report: YYYY-MM ({days_total} days)')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='CreateRecords',
                                     description='This script automatically generates daily records in the md table format. This script was created to help with what I used to create by hand every month.',
                                     epilog='Example: python CreateRecords -s 340 -d 31 -v "True"')
    parser.add_argument('-s',
                        '--start-day',
                        default=1,
                        help='set the first day of the generated records. Example: -s 399')
    parser.add_argument('-d',
                        '--days-total',
                        default=1,
                        help='set how many days of records you want to generate. Example: -d 31')
    parser.add_argument('-r',
                        '--remaining-penalties',
                        default=0,
                        help='set the remaining days of self-imposed penalties. Example: -r 137')
    parser.add_argument('-v',
                        '--value',
                        default='True',
                        help='set value of the generated records. Example: -v "True"')
    args = parser.parse_args()
    main(args)
