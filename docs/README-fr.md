<div align="center">
    <h1 align="center">
        <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="80" />
        <img src="https://img.icons8.com/?size=512&id=kTuxVYRKeKEY&format=png" width="80" />
        <br>README-AI
    </h1>
    <h3>◦ Générez de beaux et informatifs fichiers <i>README</i></h3>
    <h3>◦ Développé avec les APIs du modèle linguistique GPT d'OpenAI</h3>
    <br>
    <p align="center">
        <img src="https://img.shields.io/badge/Markdown-000000.svg?stylee&logo=Markdown&logoColor=white" alt="Markdown" />
        <img src="https://img.shields.io/badge/OpenAI-412991.svg?stylee&logo=OpenAI&logoColor=white" alt="OpenAI" />
        <img src="https://img.shields.io/badge/Python-3776AB.svg?stylee&logo=Python&logoColor=white" alt="Python" />
        <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?stylee&logo=Pytest&logoColor=white" alt="pytest" />
        <img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />
        <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="actions" />
    </p>
    <a href="https://pypi.org/project/readmeai/">
        <img src="https://img.shields.io/pypi/v/readmeai?color=5D6D7E&logo=pypi" alt="version-pypi" />
    </a>
    <a href="https://pypi.org/project/readmeai/">
        <img src="https://img.shields.io/pypi/pyversions/readmeai?color=5D6D7E&logo=python" alt="version-python-pypi" />
    </a>
    <a href="https://pypi.org/project/readmeai/">
        <img src="https://img.shields.io/pypi/dm/readmeai?color=5D6D7E" alt="téléchargements-pypi" />
    </a>
    <img src="https://img.shields.io/github/license/eli64s/readme-ai?color=5D6D7E" alt="licence-github" />
</div>

---

## 📖 Sommaire

- [📖 Sommaire](#-sommaire)
- [📍 Aperçu](#-aperçu)
- [🎈 Démonstrations](#-démonstrations)
- [🤖 Fonctionnalités](#-fonctionnalités)
- [👩‍💻 Utilisation](#-utilisation)
  - [🛠 Installation](#-installation)
  - [⚙️ Configuration](#️-configuration)
  - [🚀 Exécution de *README-AI*](#-exécution-de-readme-ai)
  - [🧪 Tests](#-tests)
- [🛣 Feuille de route](#-feuille-de-route)
- [📒 Changelog](#-changelog)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Aperçu

*README-AI* est un puissant outil en ligne de commande qui génère des fichiers README.md robustes pour vos projets logiciels et de données. En fournissant simplement une URL de dépôt distant ou un chemin vers votre base de code, cet outil génère automatiquement la documentation pour l'ensemble de votre projet, en exploitant les capacités des APIs du modèle linguistique GPT d'OpenAI.

**🎯 Motivation**

Simplifie le processus de rédaction et de maintenance d'une documentation de projet de haute qualité, améliorant ainsi la productivité et le flux de travail des développeurs. L'objectif ultime de *readme-ai* est d'améliorer l'adoption et l'utilisabilité des logiciels open-source, permettant à tous les niveaux de compétence de mieux comprendre les bases de code complexes et d'utiliser facilement les outils open-source.

**⚠️ Avertissement**

Ce projet est actuellement en développement et a une configuration opinâtre. Bien que *readme-ai* offre un excellent point de départ pour la documentation, il est important de réviser tout le texte généré par l'API OpenAI pour s'assurer qu'il représente précisément votre base de code.

---

## 🎈 Démonstrations

***Interface en Ligne de Commande***

‣ Exécutez <i>readme-ai</i> dans votre terminal via PyPI, Docker, et plus encore !

[cli-demo](https://github.com/eli64s/readme-ai/assets/43382407/645c2336-6ea7-444c-a927-5450930c5255)

<br>

***Streamlit Community Cloud***

‣ Utilisez *readme-ai* directement dans votre navigateur ! Zéro installation, zéro code !

[streamlit-demo](https://github.com/eli64s/readme-ai/assets/43382407/e8260e78-b684-4e72-941c-b3046b90c452)

---

## 🤖 Fonctionnalités

<details>
    <summary>
        <h2 style="margin-top: 1em;">❶ Badges de Projet</h2>
    </summary>
    <table>
        <tr>
            <td>
                <h4><i>Slogan du Projet et Badges</i></h4>
                <p>
                    ‣ Un slogan pour mettre en valeur votre projet est généré en <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L56">interrogeant</a> le moteur GPT d'OpenAI.
                </p>
                <p>
                    ‣ Les dépendances et les métadonnées du code source sont visualisées à l'aide des badges <a href="https://shields.io/">Shields.io</a>.
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/badges.png" alt="badges" />
            </td>
        </tr>
    </table>
</details>
<details>
    <summary>
        <h2 style="margin-top: 1em;">❷ Documentation du Code Source</h2>
    </summary>
    <table>
        <tr>
            <h4><i>Arborescence des Dossiers et Résumés des Fichiers</i></h4>
            <p>
                ‣ La structure de répertoire de votre projet est visualisée à l'aide d'une fonction d'arborescence personnalisée.
            </p>
            <p>
                ‣ Chaque fichier dans le code source est résumé par le modèle <i>GPT</i> d'OpenAI.
            </p>
        </tr>
        <tr>
            <td align="center">
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/repository-tree.png" alt="arborescence-du-répertoire" />
            </td>
            <td align="center">
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/code-summaries.png" alt="résumés-du-code" />
            </td>
        </tr>
    </table>
</details>
<details>
    <summary>
        <h2 style="margin-top: 1em;">❸ Tableau de Présentation et Fonctionnalités</h2>
    </summary>
    <table>
        <tr>
            <td>
                <h4><i>Génération de Texte Guidée</i></h4>
                <p>
                    ‣ Un paragraphe de présentation et un tableau de fonctionnalités sont générés en utilisant des <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L31">invitations détaillées</a>, intégrant des métadonnées de projet.
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/feature-table.png" alt="tableau-des-fonctionnalités" />
            </td>
        </tr>
    </table>
</details>
<details>
    <summary>
        <h2 style="margin-top: 1em;">❹ Instructions d'Utilisation Dynamiques</h2>
    </summary>
    <table>
        <tr>
            <td>
                <h4><i>Installation, Exécution, et Test</i></h4>
                <p>
                    ‣ Génère des instructions pour installer, exécuter, et tester votre projet. Les instructions sont créées en identifiant le langage principal du code source et en se référant à notre fichier de configuration <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/language_setup.toml">language_setup.toml</a>.
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/usage-instructions.png" alt="instructions-d'utilisation" />
            </td>
        </tr>
    </table>
</details>
<details>
    <summary>
        <h2 style="margin-top: 1em;">❺ Guide de Contribution et plus encore !</h2>
    </summary>
    <table>
        <tr>
            <td>
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/roadmap.png" alt="feuille-de-route" />
            </td>
        </tr>
        <br>
        <tr>
            <td>
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/license.png" alt="licence" />
            </td>
        </tr>
    </table>
</details>
<details>
    <summary>
        <h2 style="margin-top: 1em;">❻ Modèles Personnalisés - bientôt disponibles !</h2>
    </summary>
    <p>‣ Développement d'une option CLI permettant aux utilisateurs de choisir parmi une variété de styles de README</p>
    <p>‣ Modèles pour des cas d'utilisation tels que les données, l'apprentissage machine, le développement web, et plus encore !</p>
</details>
<details>
    <summary>
        <h2 style="margin-top: 1em;">❼ Exemples de Fichiers README</h2>
    </summary>
    <table>
        <thead>
            <tr>
                <th></th>
                <th>Fichier de Sortie</th>
                <th>Répertoire</th>
                <th>Langages</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-python.md">readme-python.md</a></td>
                <td><a href="https://github.com/eli64s/readme-ai">readme-ai</a></td>
                <td>Python</td>
            </tr>
            <tr>
                <td>2️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-typescript.md">readme-typescript.md</a></td>
                <td><a href="https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript">chatgpt-app-react-typescript</a></td>
                <td>TypeScript, React</td>
            </tr>
            <tr>
                <td>3️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-javascript.md">readme-javascript.md</a></td>
                <td><a href="https://github.com/idosal/assistant-chat-gpt-javascript">assistant-chat-gpt-javascript</a></td>
                <td>JavaScript, React</td>
            </tr>
            <tr>
                <td>4️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-kotlin.md">readme-kotlin.md</a></td>
                <td><a href="https://github.com/rumaan/file.io-Android-Client">file.io-android-client</a></td>
                <td>Kotlin, Java, Android</td>
            </tr>
            <tr>
                <td>5️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-rust-c.md">readme-rust-c.md</a></td>
                <td><a href="https://github.com/DownWithUp/CallMon">rust-c-app</a></td>
                <td>C, Rust</td>
            </tr>
            <tr>
                <td>6️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-go.md">readme-go.md</a></td>
                <td><a href="https://github.com/olliefr/docker-gs-ping">go-docker-app</a></td>
                <td>Go</td>
            </tr>
            <tr>
                <td>7️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-java.md">readme-java.md</a></td>
                <td><a href="https://github.com/avjinder/Minimal-Todo">java-minimal-todo</a></td>
                <td>Java</td>
            </tr>
            <tr>
                <td>8️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-fastapi-redis.md">readme-fastapi-redis.md</a></td>
                <td><a href="https://github.com/FerrariDG/async-ml-inference">async-ml-inference</a></td>
                <td>Python, FastAPI, Redis</td>
            </tr>
            <tr>
                <td>9️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-mlops.md">readme-mlops.md</a></td>
                <td><a href="https://github.com/GokuMohandas/mlops-course">mlops-course</a></td>
                <td>Python, Jupyter</td>
            </tr>
            <tr>
                <td>🔟</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-pyflink.md">readme-pyflink.md</a></td>
                <td><a href="https://github.com/eli64s/flink-flow">flink-flow</a></td>
                <td>PyFlink</td>
            </tr>
        </tbody>
    </table>
</details>

<p align="right">
    <a href="#top"><b>🔝 Retour</b></a>
</p>

---

## 👩‍💻 Utilisation

***Dépendances***

Veuillez vous assurer que les dépendances suivantes sont installées sur votre système :

- *Version de Python 3.9 ou supérieure*
- *Gestionnaire de paquets (ex. pip, conda, poetry) ou Docker*
- *Compte OpenAI API payant et clé API*

<br>

***Référentiel***

Une URL de référentiel distant ou un chemin vers le répertoire de votre projet local est nécessaire pour utiliser *readme-ai*. Les types de référentiels suivants sont actuellement pris en charge :
- *GitHub*
- *GitLab*
- *Système de fichiers*

<br>

***OpenAI API***

Un compte OpenAI API et une clé API sont nécessaires pour utiliser *readme-ai*. Les étapes ci-dessous décrivent ce processus :

<details closed><summary>🔐 OpenAI API - Instructions de configuration</summary>

1. Allez sur le [site OpenAI](https://platform.openai.com/).
2. Cliquez sur le bouton "S'inscrire gratuitement".
3. Remplissez le formulaire d'inscription avec vos informations et acceptez les conditions d'utilisation.
4. Une fois connecté, cliquez sur l'onglet "API".
5. Suivez les instructions pour créer une nouvelle clé API.
6. Copiez la clé API et conservez-la en lieu sûr.

</details>

<details closed><summary>⚠️ OpenAI API - Directives de prudence</summary>

1. **Révision des informations sensibles** : Avant de lancer l'application, assurez-vous que tout le contenu de votre référentiel est exempt d'informations sensibles. Notez que *readme-ai* ne filtre pas les données sensibles du fichier README et ne modifie aucun fichier dans votre référentiel.

2. **Coûts d'utilisation de l'API** : L'API OpenAI n'est pas gratuite, et chaque requête est facturée. Les coûts peuvent s'accumuler rapidement, il est donc essentiel d'être conscient de votre utilisation. Vous pouvez surveiller votre utilisation de l'API et les coûts associés en visitant le [Tableau de bord d'utilisation de l'API OpenAI](https://platform.openai.com/account/usage).

3. **Compte payant recommandé** : Il est fortement recommandé de configurer un compte payant avec OpenAI pour éviter d'éventuels problèmes. Sans méthode de paiement enregistrée, votre utilisation de l'API sera limitée aux modèles de base GPT-3. Cette limitation peut entraîner une génération de fichier README moins précise et peut conduire à des erreurs d'API en raison des limites de requêtes.

4. **Considérations sur le temps d'exécution** : La génération du fichier README prend généralement moins d'une minute. Si le processus dépasse quelques minutes (par exemple, 3 minutes), il est conseillé d'arrêter *readme-ai* pour éviter des temps de traitement prolongés.

</details>

---

### 🛠 Installation

***En utilisant Pip***

Pip est la méthode d'installation recommandée pour la plupart des utilisateurs.

```sh
pip install --upgrade readmeai
```
<br>

***En utilisant Docker***

Docker est recommandé pour les utilisateurs souhaitant exécuter l'application dans un environnement conteneurisé.

```sh
docker pull zeroxeli/readme-ai:latest
```

<br>

<details><summary><b><i>Installation manuelle</i></b></summary>

<br>

1️⃣ Clonez le référentiel readme-ai.
```sh
git clone https://github.com/eli64s/readme-ai
```

2️⃣ Naviguez vers le répertoire readme-ai.

```sh
cd readme-ai
```

3️⃣ Installez les dépendances en utilisant une méthode ci-dessous.

***En utilisant Bash***
```sh
bash setup/setup.sh
```

***En utilisant Conda***
```sh
conda create -n readmeai python=3.9 -y && \
conda activate readmeai && \
pip install -r requirements.txt
```

***En utilisant Poetry***
```sh
poetry install
```

</details>

---

### ⚙️ Configuration

<br>

***Arguments de Ligne de Commande***

Pour générer un fichier *README.md*, utilisez la commande `readmeai` dans votre terminal, accompagnée des arguments ci-dessous.

| Drapeau Court | Drapeau Long    | Description                                       | Statut       |
|---------------|-----------------|---------------------------------------------------|--------------|
| `-k`          | `--api-key`     | Votre clé secrète de l'API OpenAI.                | Facultatif   |
| `-c`          | `--encoding`    | Les encodages spécifient comment le texte est converti en tokens.| Facultatif   |
| `-e`          | `--engine`      | Moteur du modèle linguistique OpenAI GPT (gpt-3.5-turbo) | Facultatif   |
| `-f`          | `--offline-mode`| Exécutez hors ligne sans appeler l'API OpenAI.     | Facultatif   |
| `-o`          | `--output`      | Le chemin de sortie pour votre fichier README.md.  | Facultatif   |
| `-r`          | `--repository`  | L'URL ou le chemin vers votre dépôt de code.      | Obligatoire  |
| `-t`          | `--temperature` | La température (aléatoire) du modèle              | Facultatif   |
| `-l`          | `--language`    | La langue du texte écrit dans le fichier README.  | Bientôt disponible! |
| `-s`          | `--style`       | Le format du modèle de README à utiliser. (bientôt disponible!) | Bientôt disponible! |

<br>

***Paramètres Personnalisés***

Pour personnaliser le processus de génération du fichier README, vous pouvez modifier les sections suivantes du [fichier de configuration:](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml)

- [*api*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L2) - Paramètres de configuration de l'API du modèle linguistique OpenAI.
- [*git*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L12) - Paramètres du dépôt git par défaut utilisés si aucun dépôt n'est fourni.
- [*paths*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L17) - Chemins de répertoire et fichiers utilisés par l'application *readme-ai*.
- [*prompts*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L26) - Prompts du grand modèle linguistique utilisés pour générer le fichier README.
- [*md*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L59) - Modèles de code de section Markdown dynamiques utilisés pour construire le fichier README.

---

### 🚀 Exécution de *README-AI*

<br>

***Utilisation de Streamlit***

Utilisez l'application directement dans votre navigateur via Streamlit Community Cloud.

- [🛸 Emmenez-moi vers *readme-ai* sur Streamlit!](https://readmeai.streamlit.app/)

<br>

***Utilisation de Pip***

```sh
# Option 1 : Exécutez la commande readmeai avec tous les arguments de ligne de commande requis.
readmeai --api-key "YOUR_API_KEY" --output readme-ai.md --repository https://github.com/eli64s/readme-ai
```
```sh
# Option 2 : Exécutez la commande readmeai avec la clé API OpenAI définie comme variable d'environnement.
export OPENAI_API_KEY="YOUR_API_KEY"
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<br>

***Utilisation de Docker***

```sh
# Option 1 : Exécutez le conteneur Docker avec tous les arguments de ligne de commande requis.
docker run -it \
-e OPENAI_API_KEY="YOUR_API_KEY" \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai
```
```sh
# Option 2 : Exécutez le conteneur Docker avec la clé API OpenAI définie comme variable d'environnement.
export OPENAI_API_KEY="YOUR_API_KEY"
docker run -it \
-e OPENAI_API_KEY=$OPENAI_API_KEY \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<br>

<details><summary><b><i>Exécution Manuelle</i></b></summary>

<br>

***Utilisation de Conda***
```sh
conda activate readmeai
export OPENAI_API_KEY="YOUR_API_KEY"
python readmeai/main.py -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<br>

***Utilisation de Poetry***
```sh
poetry shell
export OPENAI_API_KEY="YOUR_API_KEY"
poetry run python readmeai/main.py -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

</details>

---

### 🧪 Tests

Exécutez la suite de tests en utilisant la commande ci-dessous.

```sh
bash scripts/test.sh
```

---

## 🛣 Feuille de route

- [X] Publier le projet en tant que bibliothèque Python via PyPI et une image Docker sur Docker Hub.
  - [*PyPI - readmeai*](https://pypi.org/project/readmeai/)
  - [*Docker Hub - readme-ai*](https://hub.docker.com/repository/docker/zeroxeli/readme-ai/general)
- [X] Intégrer et déployer l'application avec Streamlit pour fournir une interface utilisateur simple pour utiliser l'outil.
  - [*Streamlit Community Cloud - readmeai*](https://readmeai.streamlit.app/)
- [ ] Développer un script GitHub Actions pour mettre à jour automatiquement le fichier README lorsque du nouveau code est poussé.
- [ ] Concevoir des modèles de sortie README pour une variété de cas d'utilisation (i.e. data, web-dev, minimal, etc.)
- [ ] Ajouter la prise en charge pour générer des fichiers README dans n'importe quelle langue (i.e. CN, ES, FR, JA, KO, RU).

---

## 📒 Changelog

[Changelog](https://github.com/eli64s/readme-ai/blob/main/CHANGELOG.md)

---

## 🤝 Contributing

[Contributing Guidelines](https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md)

---

## 📄 License

[MIT](https://github.com/eli64s/readme-ai/blob/main/LICENSE)

---

## 👏 Acknowledgments

*Badges*
  - [Shields.io](https://shields.io/)
  - [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)
  - [Ileriayo/Markdown-Badges](https://github.com/Ileriayo/markdown-badges)

<p align="right">
  <a href="#top"><b>🔝 Return </b></a>
</p>

---
