\# MatPro AI API 🚀



Une API REST développée avec \*\*FastAPI\*\* pour interagir avec un modèle de langage (LLM).



\## 🛠️ Fonctionnalités

\- Point de terminaison `/chat` pour envoyer un prompt et recevoir une réponse de l'IA.

\- Documentation interactive générée automatiquement (Swagger UI).

\- Validation des données via Pydantic.

\- Architecture sécurisée avec gestion des variables d'environnement.



\## 🚀 Installation

1\. Clonez ce dépôt.

2\. Installez les dépendances : `pip install -r requirements.txt`

3\. Créez un fichier `API.env` avec votre clé : `DEEPSEEK\_API\_KEY=votre\_cle\_ici`

4\. Lancez le serveur : `uvicorn main:app --reload`



\## 📖 Utilisation

Rendez-vous sur `http://127.0.0.1:8000/docs` pour tester l'API directement depuis votre navigateur.

