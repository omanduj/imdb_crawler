def ransom(ransomNote, magazine):
    ransomNote = list(ransomNote)
    magazine = list(magazine)

    if len(ransomNote) > len(magazine):
        print('false')
        return 'false'
    list_check = []
    hashy = {}

    for i in range(len(magazine)):
        hashy[magazine[i]] = 0
    for i in range(len(ransomNote)):
        if ransomNote[i] in hashy:
            hashy[ransomNote[i]] += 1
        if ransomNote[i] not in hashy:
            hashy[ransomNote[i]] = 1
    for i in range(len(magazine)):
        if magazine[i] in hashy:
            hashy[magazine[i]] -= 1

    for i in range(len(ransomNote)):
        if hashy[ransomNote[i]] >= 1:
            print(hashy[magazine[i]])
            list_check.append('false')
        if hashy[ransomNote[i]] < 1:
            print(hashy[magazine[i]])
            list_check.append('true')

    if 'false' in list_check:
        print('false')
        return 'false'
    if 'true' in list_check:
        print('true')
        return 'true'

def happy_num(num):
    list_val = []
    total = 0
    num = str(num)
    for val in range(len(num)):
        list_val.append(num[val])

    for i in range(len(list_val)):
        total += int(list_val[i])**2
    if total > 9:
        happy_num(total)
    if total == 1:
        print('true')
        return True
    if total <= 9:
        print('false')
        return False
        #???
    # list_val = []
    # total = 0
    # num = str(num)
    # for val in range(len(num)):
    #     list_val.append(num[val])
    #
    # for i in range(len(list_val)):
    #     total += int(list_val[i])**2
    # if total > 9:
    #     happy_num(total)
    # if total == 1:
    #     print(total)
    #     return total
    # if total <= 9:
    #     print('false')
    #     return 'false'



# def date(date):
#     output = []
#     done = []
#     str = ''
#     months = {
#         'Jan': '1',
#         'Feb': '2',
#         'Mar': '3',
#         'Apr': '4',
#         'May': '5',
#         'Jun': '6',
#         'Jul': '7',
#         'Aug': '8',
#         'Sep': '9',
#         'Oct': '10',
#         'Nov': '11',
#         'Dec': '12',
#     }
#
#     days = {
#         '1': '01',
#         '2': '02',
#         '3': '03',
#         '4': '04',
#         '5': '05',
#         '6': '06',
#         '7': '07',
#         '8': '08',
#         '9': '09',
#         '10': '10',
#         '11': '11',
#         '12': '12',
#         '13': '13',
#         '14': '14',
#         '15': '15',
#         '16': '16',
#         '17': '17',
#         '18': '18',
#         '19': '19',
#         '20': '10',
#         '21': '21',
#         '22': '22',
#         '23': '23',
#         '24': '24',
#         '25': '25',
#         '26': '26',
#         '27': '27',
#         '28': '28',
#         '29': '29',
#         '30': '30',
#     }
#
#     for i in range(len(date)):
#         date[i] = date[i].split(' ')
#
#     for value in range(len(date)):
#         str = date[value][2] + '-' + months[date[value][1]] + '-' + days[date[value][0][:-2]]
#         output.append(str)
#         str = ''
#     print(output)
#
#
# def func(word):
#     map = {}
#     ransomNote = list(word)
#     count = 1
#     for i in range(len(ransomNote)-1):
#         if ransomNote[i] == ransomNote[i+1]:
#             count += 1
#             map[ransomNote[i], count] = count
#         if ransomNote[i] != ransomNote[i+1]:
#             count = 1
#             map[ransomNote[i], count] = count
#     print(map)


    # ransomNote = list(word)
    # count = 1
    # output = []
    # stack = []
    #
    # for i in range(len(ransomNote)-1):
    #     stack.append(ransomNote[i])
    #     if stack[-1] != ransomNote[i+1]:
    #         output.append(ransomNote[i])
    #         output.append(count)
    #         count = 1
    #     if stack[-1] == ransomNote[i+1]:
    #         count += 1
    #         output.append(ransomNote[i])
    #         output.append(count)
    #
    # print(output)

def main(word):
    # func(word)
    # list_ = ['6th May 1960', '27th May 1960']
    # date(list_)


    # ransom("a", "b")
    happy_num(19)
main("aabbcddd")
