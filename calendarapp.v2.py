#Generations at Regency Activites calendar Generator
#June 24 2019
import calendar
calendar.setfirstweekday(calendar.MONDAY)
lst1 = [1,8,15,22,29]
lst2 = [2,9,16,23,30]
lst3 = [3,10,17,24,31]
lst4 = [4,11,18,25]
lst5 = [5,12,19,26]
lst6 = [6,13,20,27]
lst7 = [7,14,21,28]
#########################1-3##########################################
def firstThruThird(fst,snd,trid,frth,five,six,seven, month,lim):
    
    mon = ' 10:45 Parachutes and balloons (3)\n 2:00 Friendly visits(1&2)\n 2:00 Arts & Crafts(3) \n 3:30 Friendly Visits(1&2)\n 3:30 Tabletop Games(3)'
    tue = ' 10:45 Social Service group (3) \n 2:00 Friendly visits (1&2)\n 2:00 Spa social (3) \n 3:30 Friendly visits (1&2)\n 3:30 Tabletop games(3)'
    wed = ' 10:45 LRC dice (3) \n 2:00 Friendly visits (1&2)\n 2:00 Bingo (3) \n 3:30 Friendly visits (1&2)\n 3:30 Blackjack(3)'
    thurs = ' 10:45 Twister (3) \n 2:00 Friendly visits (1&2)\n 2:00 Afternoon Uno (3) \n 3:30 Friendly visits (1&2)\n 3:30 TV Classics(3)'
    fri = ' 10:45 Trivia (3) \n 2:00 Friendly visits (1&2)\n 2:00 Movie Matinee (3) \n 3:30 Friendly visits (1&2)\n 3:00 Polish Rosary (LL)'
    sat = ' 10:45 Hangman (3) \n 2:00 Friendly visits (1&2)\n 2:00 Bingo (3) \n 3:30 Friendly visits (1&2)\n 3:30 Google Chrome Showing(3)'
    sun = ' 10:45 Bingo (3) \n 2:00 Friendly visits (1&2)\n 3:15 Sunday Mass (3) \n 3:30 Friendly visits (3)'
    
    d={fst:lst1,snd:lst2,trid:lst3,frth:lst4,five:lst5,six:lst6,seven:lst7}
    s=dict()
    for key in d:
        for i in range(len(d[key])):
            z = d[key][i]
            s[z]=key
    delete = [key for key in s if key > lim]
    for key in delete: del s[key]
    infile = open('1_3 Floor {}.txt'.format(month),'w')
    infile.write('''{} Activity Calendar 1-3rd Floor\n
Monday - Sunday\n
On All Floors\n
10:00 Morning Exercise & Stretch Programs All Floors\n
10:30 Refreshments and Current Events\n
1:00 Popcorn Tues, Thurs, Fri\n
1:00 Ice Cream Parlor Dessert Hour Daily\n
\n
\n
Polish language activities as scheduled.\n
Please see daily activity sheets for programs.\n
\n
Activities are held on the floors as noted.\n
LL Lower Level\n
P=Outdoor Patio\n
\n
All activities are subject to change. Please see daily activity posting.\n
Room 524 is closed Saturday & Sunday\n
all outdoor activities are weather permitting\n
'''.format(month))
    for key in sorted(s.keys()):
        infile.write("{} {}\n".format(s[key], key))
        if 'monday' ==s[key].lower(): infile.write(mon)
        if 'tuesday' ==s[key].lower(): infile.write(tue)
        if 'wednesday' ==s[key].lower(): infile.write(wed)
        if 'thursday' ==s[key].lower(): infile.write(thurs)
        if 'friday' ==s[key].lower(): infile.write(fri)
        if 'saturday' ==s[key].lower(): infile.write(sat)
        if 'sunday' ==s[key].lower(): infile.write(sun)
        infile.write('\n\n')
    infile.close()
    ###########################################Fourth###########################
def Fourth(fst,snd,trid,frth,five,six,seven, month,lim):

    mon = ' 10:00 Sittercise & Stretching \n 10:30 Current Events & Refreshments\n 10:45 Yoga Stretch \n 2:00 Yesteryears\n 3:30 Who am I'
    tue = ' 10:00 Sittercise & Stretching \n 10:30 Current Events & Refreshments\n 10:45 Tower Relay \n 2:00 Art Therapy\n 3:30 Noodle War'
    wed = ' 10:00 Sittercise & Stretching \n 10:30 Current Events & Refreshments\n 10:45 Card Games \n 2:00 Movie Matinee \n 3:30 Fun with Words'
    thurs = ' 10:00 Sittercise & Stretching \n 10:30 Current Events & Refreshments\n 10:45 Dominoes/ Active Games \n 2:00 Sound of Music w/ snacks\n 3:30 Arts and Crafts'
    fri = ' 10:00 Sittercise & Stretching \n 10:30 Current Events & Refreshments\n 10:45 20 Questions \n 2:00 TV Classics\n 3:00 Polish Rosary(LL)\n 3:30 Word Games' 
    sat = ' 10:00 Sittercise & Stretching \n 10:30 Current Events & Refreshments\n 10:45 Art Therapy \n 2:00 Balloon Volley\n 3:30 Tabletop Games'
    sun = ' 10:00 Sittercise & Stretching \n 10:30 Current Events & Refreshments\n 10:45 Picture Bingo \n 2:00 Movie Matinee w/ snacks\n 3:15 Sunday Mass (LL)\n 3:00 Sunday Sing along'
    
    d={fst:lst1,snd:lst2,trid:lst3,frth:lst4,five:lst5,six:lst6,seven:lst7}
    s=dict()
    for key in d:
        for i in range(len(d[key])):
            z = d[key][i]
            s[z]=key
    delete = [key for key in s if key > lim]
    for key in delete: del s[key]
    infile = open('4 Floor {}.txt'.format(month),'w')
    infile.write('''{} Activity Calendar 4th Floor\n
Monday - Sunday\n
On All Floors\n
10:00 Morning Exercise & Stretch Programs All Floors\n
10:30 Refreshments and Current Events\n
1:00 Popcorn Tues, Thurs, Fri\n
1:00 Ice Cream Parlor Dessert Hour Daily\n
\n
\n
Polish language activities as scheduled.\n
Please see daily activity sheets for programs.\n
\n
Activities are held on the floors as noted.\n
LL Lower Level\n
P=Outdoor Patio\n
\n
All activities are subject to change. Please see daily activity posting.\n
Room 524 is closed Saturday & Sunday\n
all outdoor activities are weather permitting\n
'''.format(month))
    for key in sorted(s.keys()):
        infile.write("{} {}\n".format(s[key], key))
        if 'monday' ==s[key].lower(): infile.write(mon)
        if 'tuesday' ==s[key].lower(): infile.write(tue)
        if 'wednesday' ==s[key].lower(): infile.write(wed)
        if 'thursday' ==s[key].lower(): infile.write(thurs)
        if 'friday' ==s[key].lower(): infile.write(fri)
        if 'saturday' ==s[key].lower(): infile.write(sat)
        if 'sunday' ==s[key].lower(): infile.write(sun)
        infile.write('\n\n')
    infile.close()

######################################5TH FLOOR#######################################
def Five(fst,snd,trid,frth,five,six,seven, month,lim):

    mon = ' 10:45 Remeniscing (5DR) \n 11:00 Sensory Stimulation (524)\n 2:00 Picture Bingo (5DR) \n 2:00 Art & Sensory Fun(524)\n 3:00 Music Memory (5DR)\n 4:00 Poetry with snacks(5DR)'
    tue = ' 10:00 Mindful Meditation (524) \n 10:45 Tabletop Games(5DR)\n 2:00 Finish the Phrase (5DR) \n 3:00 Sing Along (5DR)\n 4:00 Brain Teasers(5DR)'
    wed = ' 10:45 Parachutes & Balloons (5DR) \n 11:00 Art & Snesory Fun (524)\n 2:00 Snack and Chat (5DR) \n 2:00 Spa Social(524)\n 3:00 Who am I (5DR)\n 4:00 Mind Joggers(5DR)'
    thurs = ' 10:45 Chair Zumba (5DR) \n 11:00 Trivia (524)\n 2:00 Table Stretch / Balloon Volley (5DR) \n 2:00 Dear Abbey(524)\n 3:00 Brain Teasers (5DR)\n 4:00 Tricky Trivia(5DR)'
    fri = ' 10:45 Rhythm band (5DR) \n 11:00 Sensory Stimulation (524)\n 2:00 Movie Matinee (5DR) \n 2:00 Trivia(524)\n 3:00 Sing Along (5DR)\n 4:00 Brain Teasers(5DR)' 
    sat = ' 10:45 Parachutes & Balloons (5DR) \n  2:00 What am I (5DR) \n 3:30 Sing Along (5DR)\n 4:30 Poetry Corner(5DR)'
    sun = ' 10:45 Brain Teasers (5DR) \n 10:30 Rhythm Band (5DR) \n 2:00 Noodle Ball (5DR) \n 3:00 Sunday Mass (LL) \n 4:00 Story Time(5DR)'
    
    d={fst:lst1,snd:lst2,trid:lst3,frth:lst4,five:lst5,six:lst6,seven:lst7}
    s=dict()
    for key in d:
        for i in range(len(d[key])):
            z = d[key][i]
            s[z]=key
    delete = [key for key in s if key > lim]
    for key in delete: del s[key]
    infile = open('5 Floor {}.txt'.format(month),'w')
    infile.write('''{} Activity Calendar 5th Floor\n
Monday - Sunday\n
On All Floors\n
10:00 Morning Exercise & Stretch Programs All Floors\n
10:30 Refreshments and Current Events\n
1:00 Popcorn Tues, Thurs, Fri\n
1:00 Ice Cream Parlor Dessert Hour Daily\n
\n
\n
Polish language activities as scheduled.\n
Please see daily activity sheets for programs.\n
\n
Activities are held on the floors as noted.\n
LL Lower Level\n
P=Outdoor Patio\n
\n
All activities are subject to change. Please see daily activity posting.\n
Room 524 is closed Saturday & Sunday\n
all outdoor activities are weather permitting\n
'''.format(month))
    for key in sorted(s.keys()):
        infile.write("{} {}\n".format(s[key], key))
        if 'monday' ==s[key].lower(): infile.write(mon)
        if 'tuesday' ==s[key].lower(): infile.write(tue)
        if 'wednesday' ==s[key].lower(): infile.write(wed)
        if 'thursday' ==s[key].lower(): infile.write(thurs)
        if 'friday' ==s[key].lower(): infile.write(fri)
        if 'saturday' ==s[key].lower(): infile.write(sat)
        if 'sunday' ==s[key].lower(): infile.write(sun)
        infile.write('\n\n')
    infile.close()
##################################OVERVIEW####################################################
def cal():
    print('Welcome to the calendar Generator!')
    print('Make sure to write everything exactly how you want it to appear.')
    month1 = eval(input('What month is it? (provide a number!!!!)'))
    year = eval(input ('What is the year?'))
    c= calendar.monthrange(year, month1)
    monthName =calendar.month_name[month1]
    daylst=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    weeklst=  daylst[c[0]:]
    try:
        begWeeklst = daylst[:c[0]]
    except:
        begWeeklst =[]
    weeklst.extend(begWeeklst)
    fst1=weeklst[0]
    snd1=weeklst[1]
    trid1=weeklst[2]
    frth1=weeklst[3]
    five1=weeklst[4]
    six1=weeklst[5]
    seven1=weeklst[6]
    LIMIT = c[1]
    firstThruThird(month = monthName, fst=fst1,snd=snd1,trid=trid1,frth=frth1,five=five1,six=six1,seven=seven1,lim=LIMIT)
    Fourth(month = monthName, fst=fst1,snd=snd1,trid=trid1,frth=frth1,five=five1,six=six1,seven=seven1, lim=LIMIT)
    Five(month = monthName, fst=fst1,snd=snd1,trid=trid1,frth=frth1,five=five1,six=six1,seven=seven1,lim=LIMIT)

    for i in range(0,101,2):
        print('Done: {}%'.format(i))
    print('FILES CREATED. THEY ARE STORED IN THE "CAN DELETE IF YOU WANT TO" FOLDER.')
    print('\n\nNOTES:\n\nIF ANYTHING WENT WRONG: (1) Check your spelling and try again.\nIF YOU NEED TO CHANGE THE TEMPLATE: let Piotr Know he will fix it.\nCHECK THE RESULT: To make sure everything is gucci\n')
    print('Thank you for using the system. Goodbye....')
    
