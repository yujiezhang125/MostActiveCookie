import sys
import csv


def main(filepath, date):

    try:
        with open(filepath, newline='') as csvfile:
            filereader = csv.reader(csvfile, delimiter=',')
            # file_header = next(filereader)
            # print(file_header)
            maxFreq = 0
            maxFreqCookies = []
            cookiesFreq = dict()
            for row in filereader:
                # print(row)
                cookie = row[0]
                cookieDate = row[1].split('T')[0]
                if cookieDate == date:
                    cookiesFreq[cookie] = cookiesFreq.get(cookie, 0) + 1
                    if cookiesFreq[cookie] == maxFreq:
                        maxFreqCookies.append(cookie)
                    elif cookiesFreq[cookie] > maxFreq:
                        maxFreq = cookiesFreq[cookie]
                        maxFreqCookies = [cookie]
        print(maxFreqCookies)
    except:
       print("Cannot find the input file")
       sys.exit(2)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Please provide three arguments (log file path, timezone and date)")
        print(
            "You can run the default mode sentence to have a try: 'python MostActiveCookie.py ./testCases.csv -d 2018-12-09'")
    else:
        main(sys.argv[1], sys.argv[3])
#
# date = "2018-12-09"
# with open('./testCases.csv', newline='') as csvfile:
#     filereader = csv.reader(csvfile, delimiter=',')
#
#     file_header = next(filereader)
#     print(file_header)
#     maxFreq = 0
#     maxFreqCookies = []
#     cookiesFreq = dict()
#     for row in filereader:
#         print(row)
#         cookie = row[0]
#         cookieDate = row[1].split('T')[0]
#         if cookieDate == date:
#             cookiesFreq[cookie] = cookiesFreq.get(cookie, 0) + 1
#             if cookiesFreq[cookie] == maxFreq:
#                 maxFreqCookies.append(cookie)
#             elif cookiesFreq[cookie] > maxFreq:
#                 maxFreq = cookiesFreq[cookie]
#                 maxFreqCookies = [cookie]
#
#     print(maxFreqCookies)
#
