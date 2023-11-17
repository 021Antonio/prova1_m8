#! /bin/env python3
import re

def pagamento():
   return "clique neste link para ver pagamentos"

def status():
    return "Cliquq neste link para ver status"

intent_dict = {
    r"\b(?:(?:[Cc]omo)(?:\sposso))(\satualizar)(?:\s[a-z]{3})(\scart[aã]o)(?:\s[a-z]{2})(\scr[ée]dito)": "pagamento",
    r"\b(?:(?:[Oo]nde)(\svejo))(?:\s[a-z]{0,3})(\sstatus)(?:\s[a-z]{2})(?:\s[a-z]{3})(\spedido)": "status"
}

action_dict = {
    "pagamento":pagamento,
    "status":status
}

def main():
    command = input("Digite o seu comando: ")
    for key, value in intent_dict.items():
        pattern = re.compile(key)
        groups = pattern.findall(command)
        if groups:
            print(f"{action_dict[value](groups[0])}", end=" ")
    print()

if __name__ == "__main__":
    main()