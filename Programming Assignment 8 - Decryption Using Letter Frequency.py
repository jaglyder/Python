import operator
from operator import itemgetter
import csc131Helper
from csc131Helper import getFile

file_array_var = getFile()
new_file_name = file_array_var[0][:-4] + "Output.txt"
f = file_array_var[1]
f2 = open(new_file_name, "a")
letter_occerance_dictionary = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
for a in f:
    for x in a:
        if (x == 'a') or (x == 'A'):
            letter_occerance_dictionary['a'] = letter_occerance_dictionary['a'] + 1
        elif (x == 'b') or (x == 'B'):
            letter_occerance_dictionary['b'] = letter_occerance_dictionary['b'] + 1
        elif (x == 'c') or (x == 'C'):
            letter_occerance_dictionary['c'] = letter_occerance_dictionary['c'] + 1
        elif (x == 'd') or (x == 'D'):
            letter_occerance_dictionary['d'] = letter_occerance_dictionary['d'] + 1
        elif (x == 'e') or (x == 'E'):
            letter_occerance_dictionary['e'] = letter_occerance_dictionary['e'] + 1
        elif (x == 'f') or (x == 'F'):
            letter_occerance_dictionary['f'] = letter_occerance_dictionary['f'] + 1
        elif (x == 'g') or (x == 'G'):
            letter_occerance_dictionary['g'] = letter_occerance_dictionary['g'] + 1
        elif (x == 'h') or (x == 'H'):
            letter_occerance_dictionary['h'] = letter_occerance_dictionary['h'] + 1
        elif (x == 'i') or (x == 'I'):
            letter_occerance_dictionary['i'] = letter_occerance_dictionary['i'] + 1
        elif (x == 'j') or (x == 'J'):
            letter_occerance_dictionary['j'] = letter_occerance_dictionary['j'] + 1
        elif (x == 'k') or (x == 'K'):
            letter_occerance_dictionary['k'] = letter_occerance_dictionary['k'] + 1
        elif (x == 'l') or (x == 'L'):
            letter_occerance_dictionary['l'] = letter_occerance_dictionary['l'] + 1
        elif (x == 'm') or (x == 'M'):
            letter_occerance_dictionary['m'] = letter_occerance_dictionary['m'] + 1
        elif (x == 'n') or (x == 'N'):
            letter_occerance_dictionary['n'] = letter_occerance_dictionary['n'] + 1
        elif (x == 'o') or (x == 'O'):
            letter_occerance_dictionary['o'] = letter_occerance_dictionary['o'] + 1
        elif (x == 'p') or (x == 'P'):
            letter_occerance_dictionary['p'] = letter_occerance_dictionary['p'] + 1
        elif (x == 'q') or (x == 'Q'):
            letter_occerance_dictionary['q'] = letter_occerance_dictionary['q'] + 1
        elif (x == 'r') or (x == 'R'):
            letter_occerance_dictionary['r'] = letter_occerance_dictionary['r'] + 1
        elif (x == 's') or (x == 'S'):
            letter_occerance_dictionary['s'] = letter_occerance_dictionary['s'] + 1
        elif (x == 't') or (x == 'T'):
            letter_occerance_dictionary['t'] = letter_occerance_dictionary['t'] + 1
        elif (x == 'u') or (x == 'U'):
            letter_occerance_dictionary['u'] = letter_occerance_dictionary['u'] + 1
        elif (x == 'v') or (x == 'V'):
            letter_occerance_dictionary['v'] = letter_occerance_dictionary['v'] + 1
        elif (x == 'w') or (x == 'W'):
            letter_occerance_dictionary['w'] = letter_occerance_dictionary['w'] + 1
        elif (x == 'x') or (x == 'X'):
            letter_occerance_dictionary['x'] = letter_occerance_dictionary['x'] + 1
        elif (x == 'y') or (x == 'Y'):
            letter_occerance_dictionary['y'] = letter_occerance_dictionary['y'] + 1
        elif (x == 'z') or (x == 'Z'):
            letter_occerance_dictionary['z'] = letter_occerance_dictionary['z'] + 1
print(letter_occerance_dictionary)
print("")
english_letter_freq = "etaoinshrdlcumwfgypbvkjxqz"
file_letter_freq_order = []
for x in letter_occerance_dictionary:
    file_letter_freq_order.append([x,letter_occerance_dictionary[x]])
file_letter_freq_order = sorted(file_letter_freq_order, key=itemgetter(1))
file_letter_freq_order_string = ""
for x in file_letter_freq_order:
    file_letter_freq_order_string = file_letter_freq_order_string + x[0]
file_letter_freq_order_string_rev = file_letter_freq_order_string[::-1]
double_array_freq = []
incr = 0
while incr < len(english_letter_freq):
    double_array_freq.append([english_letter_freq[incr], file_letter_freq_order_string_rev[incr]])
    incr+=1
print(double_array_freq)
f.close()
f1 = open(file_array_var[0], 'r')
final_string = ""
for a in f1:
    new_string = ""
    for x in a:
        if (x == 'a') or (x == 'b') or (x == 'c') or (x == 'd') or (x == 'e') or (x == 'f') or (x == 'g') or (x == 'h') or (x == 'i') or (x == 'j') or (x == 'k') or (x == 'l') or (x == 'm') or (x == 'n') or (x == 'o') or (x == 'p') or (x == 'q') or (x == 'r') or (x == 's') or (x == 't') or (x == 'u') or (x == 'v') or (x == 'w') or (x == 'x') or (x == 'y') or (x == 'z')or (x == 'A') or (x == 'B') or (x == 'C') or (x == 'D') or (x == 'E') or (x == 'F') or (x == 'G') or (x == 'H') or (x == 'I') or (x == 'J') or (x == 'K') or (x == 'L') or (x == 'M') or (x == 'N') or (x == 'O') or (x == 'P') or (x == 'Q') or (x == 'R') or (x == 'S') or (x == 'T') or (x == 'U') or (x == 'V') or (x == 'W') or (x == 'X') or (x == 'Y') or (x == 'Z'):
            for p in double_array_freq:
                if (x.lower() == p[1]):
                    new_string = new_string + p[0]
        else:
            new_string = new_string + x
    final_string = final_string + new_string
f2.write(final_string)
