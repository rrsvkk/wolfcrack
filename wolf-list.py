import itertools, os

os.system("cls||clear")

YELLOW = "\033[1;33m"
RED = "\033[0;31m"
LIGHT_WHITE = "\033[1;37m"

print(f"""

{RED} █████   ███   █████    ███████    █████       ███████████ █████       █████  █████████  ███████████
{RED}░░███   ░███  ░░███   ███░░░░░███ ░░███       ░░███░░░░░░█░░███       ░░███  ███░░░░░███░█░░░███░░░█
{RED} ░███   ░███   ░███  ███     ░░███ ░███        ░███   █ ░  ░███        ░███ ░███    ░░░ ░   ░███  ░ 
{RED} ░███   ░███   ░███ ░███      ░███ ░███        ░███████    ░███        ░███ ░░█████████     ░███    
{RED} ░░███  █████  ███  ░███      ░███ ░███        ░███░░░█    ░███        ░███  ░░░░░░░░███    ░███    
{RED}  ░░░█████░█████░   ░░███     ███  ░███      █ ░███  ░     ░███      █ ░███  ███    ░███    ░███    
{RED}    ░░███ ░░███      ░░░███████░   ███████████ █████       ███████████ █████░░█████████     █████   
{RED}     ░░░   ░░░         ░░░░░░░    ░░░░░░░░░░░ ░░░░░       ░░░░░░░░░░░ ░░░░░  ░░░░░░░░░     ░░░░░    

       {RED}    +{YELLOW} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RED} +
       {YELLOW}    |      {RED}    V 1.0   {YELLOW}   Make your list now but silently {RED}     V 1.0       {YELLOW}  |
       {YELLOW}    |    {RED} This is just a trial version, the full version released later {YELLOW}     | 
       {YELLOW}    |    {RED} Github: @rrsvkk {YELLOW} | {RED} Youtube: @rrsvkk {YELLOW}    | {RED} Instagram: @rrsvkk {YELLOW}    | 
       {RED}    +{YELLOW} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RED} +

""")

def generate_words(letters: str, min_len: int, max_len: int, allow_repeats: bool = True):
    for length in range(min_len, max_len + 1):
        if allow_repeats:
            yield from (''.join(p) for p in itertools.product(letters, repeat=length))
        else:
            if length <= len(letters):
                yield from (''.join(p) for p in itertools.permutations(letters, length))

if __name__ == "__main__":
    letters = input(f"   {YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Enter letters {YELLOW}:{LIGHT_WHITE} ")
    min_len = int(input(f"   {YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Minimux letters {YELLOW}:{LIGHT_WHITE} "))
    max_len = int(input(f"   {YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Maximum letters {YELLOW}:{LIGHT_WHITE} "))
    repeat_choice = input(f"   {YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Repeat Letters (false or true) {YELLOW}:{LIGHT_WHITE} ").strip().lower()
    allow_repeats = repeat_choice == 'true'
    file_name = input(f"   {YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Enter file name (wordlist.txt) {YELLOW}:{LIGHT_WHITE} ")

    with open(file_name, 'w', encoding='utf-8') as file:
        for word in generate_words(letters, min_len, max_len, allow_repeats):
            file.write(word + '\n')

    print(f"   {YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}File saved {YELLOW}{file_name}{LIGHT_WHITE} successfully {YELLOW}... ")
