"""-------------------------FUNKCJE--------------------------------------------"""
def ReadFile(name_file):
    try:
        file = open(name_file, 'r')
        text = file.read() 
        
    except IOError:
        print("Blad odczytu pliku")
        text = {}
        
    file.close()
    return text

def PatternCount(text,pattern):
    
    count = 0
    pattern_len = len(pattern)
    text_len = len(text)
    
    for i in range (0, (text_len - pattern_len)):
        if text[i:(pattern_len + i)] == pattern:
            count += 1
    return count

def FrequentCount(text,k):
    
    frequent_pattern = ''
    count_list = list()
    text_len = len(text)
    
    for i in range (0, text_len - k):
        pattern = text[i : k+i]
        count = PatternCount(text, pattern)
        count_list.append(count)
        
    max_count = max(count_list)
    
    for i in range (0, text_len - k):
        if count_list[i] == max_count:
            frequent_pattern += text[i : k+i]
            if frequent_pattern == text[i : k+i]:
                break
            
    return(frequent_pattern)


          
"""----------------------DEKLARACJA--ZMIENNYCH---------------------------------"""
k = 5
            
"""-----------------------WYWOŁANIE--FUNKCJI-----------------------------------"""
text = ReadFile('Gyrodactylus_tRNA_gene.txt')
wynik = FrequentCount(text,k)


"""---------------------WYŚWIETLENIE--WYNIKÓW----------------------------------"""
print(wynik)

"""----------------------ASSERTY-----------------------------------------------"""
print("Asserts :\n")
assert PatternCount('TGGACCTGACGTAAT', 'AC') == 2, "Funkcja nie działa poprawnie"
assert FrequentCount('TGGACCTGACGTAAT', 2) == 'TG', "Funkja nie działa poprawnie"




