# Check For First letter of every word to Caps....


s = input('Enter a sentence in Lowercase: ')
new_s = ""

if __name__ == "__main__":
    ax = s.split(' ')
    for i in range(0, len(ax)):
        res = ax[i][0].upper()+ax[i][1:]
        new_s += " "+res
print(new_s.strip())
