import sys
from sympy import sympify, symbols

print("Bienvenue dans la calculatrice de dichotomie")

x = symbols('x')
fonc_regle_input = input("Définissez la fonction f(x), entrez l'expression :\n")
expr = sympify(fonc_regle_input)

def f(val):
    return float(expr.subs(x, val).evalf())

while True:
    intervale_input = input("Entrez l'intervalle sous la forme [a, b] (ou 'q' pour quitter) :\n")
    
    if intervale_input.strip().lower() == 'q':
        print("Fin du programme.")
        sys.exit()
        
    cleaned_input = intervale_input.replace('[', '').replace(']', '').strip()
    
    try:
        parts = cleaned_input.split(',')
        a, b = float(parts[0].strip()), float(parts[1].strip())
        
        if a > b:
            a, b = b, a
            
        fa = f(a)
        fb = f(b)
        
        if fa * fb < 0:
            print(f"Condition vérifiée : f({a}) = {fa} et f({b}) = {fb}\n")
            break 
        else:
            print(f"Erreur : f({a})*f({b}) >= 0. La condition de dichotomie n'est pas vérifiée. Réessayez.")
            
    except (ValueError, IndexError):
        print("Erreur d'entrée ! Vérifiez le format comme [2, 5] ou [3.7, 2.9]")

# --- Saisie de la précision (Epsilon) par l'utilisateur ---
while True:
    try:
        epsilon_input = input("Entrez la précision epsilon souhaitée (ex: 0.001 ou 1e-5) :\n")
        epsilon = float(epsilon_input)
        if epsilon <= 0:
            print("Erreur : Epsilon doit être un nombre strictement positif.")
            continue
        break
    except ValueError:
        print("Erreur d'entrée ! Veuillez saisir un nombre valide pour epsilon.")

iteration = 1
max_iterations = 100 

while abs(b - a) > epsilon and iteration <= max_iterations:
    m = (a + b) / 2
    fm = f(m)
    
    print(f"Itération {iteration}: Intervalle actuel = [{a:.5f}, {b:.5f}], m = {m:.5f}, f(m) = {fm:.5f}")
    
    if fm == 0:
        print(f"\nx = {m} est la solution exacte trouvée.")
        break
    elif f(a) * fm < 0:
        b = m
    else:
        a = m
        
    iteration += 1

if iteration > max_iterations:
    print("\nAttention : Nombre maximum d'itérations atteint.")

if fm != 0:
    print(f"\nLa solution approximative est x = {(a + b) / 2:.5f} avec une précision de {epsilon}")
