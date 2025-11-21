
import json
import os
from datetime import datetime

def run_quiz():
    questions = [
        {"question": "Quand faut-il prendre des mesures DSL?", "options": ["Tous les jours", "Quand le fond du puits est accessible", "Jamais", "Uniquement en cas de casse"], "answer": 1},
        {"question": "Quelle est la fréquence recommandée pour les mesures DSL?", "options": ["Tous les 3 mois", "Tous les 6 mois", "Tous les ans", "Jamais"], "answer": 1},
        {"question": "Que faire si l'unité de slickline n'est pas disponible?", "options": ["Annuler l'opération", "Reporter à la prochaine opération", "Changer le puits", "Ignorer"], "answer": 1},
        {"question": "Pourquoi enregistrer du haut vers le bas?", "options": ["Pour la sécurité", "Pour la calibration des capteurs", "Pour gagner du temps", "Pour éviter les erreurs humaines"], "answer": 1},
        {"question": "Combien de points de mesure sont requis?", "options": ["3", "4", "5", "6"], "answer": 2},
        {"question": "Quelle est la durée de station à chaque point?", "options": ["1 min", "3 min", "5 min", "10 min"], "answer": 2},
        {"question": "Que doit-on préciser pour le Top Liquide Statique?", "options": ["Type de fluide", "S'il s'agit d'un top réservoir ou après circulation", "Température", "Pression"], "answer": 1},
        {"question": "Que faire après la prise de mesures?", "options": ["Rien", "Envoyer les données par email", "Archiver sans diffusion", "Notifier oralement"], "answer": 1},
        {"question": "À qui envoyer les données?", "options": ["Service G&G uniquement", "Workover et Reservoir", "Direction", "Personne"], "answer": 1},
        {"question": "Que doit contenir le RJWO?", "options": ["Nom du puits uniquement", "Top Liquide et points de mesure", "Date uniquement", "Commentaires"], "answer": 1}
    ]

    print("Bienvenue au Quiz - Prises de mesures DSL")
    nom = input("Entrez votre Nom: ")
    prenom = input("Entrez votre Prénom: ")
    poste = input("Entrez votre Poste: ")

    score = 0
    for i, q in enumerate(questions):
        print(f"
Question {i+1}: {q['question']}")
        for idx, opt in enumerate(q['options']):
            print(f"{idx}. {opt}")
        try:
            answer = int(input("Votre réponse (0-3): "))
            if answer == q['answer']:
                score += 1
        except ValueError:
            print("Réponse invalide, question ignorée.")

    result = {
        "Nom": nom,
        "Prénom": prenom,
        "Poste": poste,
        "Score": score,
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open('resultat_DSL.json', 'w') as f:
        json.dump(result, f, indent=4)

    os.chmod('resultat_DSL.json', 0o444)
    print(f"
Quiz terminé! Score: {score}/10. Résultat enregistré dans resultat_DSL.json.")

if __name__ == '__main__':
    run_quiz()
