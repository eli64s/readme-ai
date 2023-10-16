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
- [🔭 Aperçu](#-aperçu)
- [🤖 Démos](#-démos)
- [💫 Fonctionnalités](#-fonctionnalités)
- [👩‍💻 Utilisation](#-utilisation)
  - [📦 Installation](#-installation)
  - [⚙️ Configuration](#️-configuration)
  - [Arguments de Ligne de Commande](#arguments-de-ligne-de-commande)
  - [Paramètres Personnalisés](#paramètres-personnalisés)
  - [🚀 Exécution de *README-AI*](#-exécution-de-readme-ai)
  - [🧪 Tests](#-tests)
  - [🛠 Feuille de Route](#-feuille-de-route)
- [📒 Journal des Modifications](#-journal-des-modifications)
- [🤝 Contribuer](#-contribuer)
- [📄 Licence](#-licence)
- [👏 Remerciements](#-remerciements)

---

## 🔭 Aperçu

<div align="center">
  <img src="https://github.com/eli64s/readme-ai/blob/main/examples/imgs/dalle-readmeai.png?raw=true" height="500" />
</div>

<table>
    <tr>
        <td>
            <strong>👋 À Propos</strong>
            <br><br>
            <em>README-AI</em> est un outil en ligne de commande qui génère des fichiers README.md robustes pour vos projets logiciels et de données. En fournissant simplement une URL de dépôt distant ou un chemin vers votre base de code, cet outil génère automatiquement la documentation pour l'ensemble de votre projet, en exploitant les capacités des APIs du modèle linguistique GPT d'OpenAI.
            <br><br>
            <strong>🎯 Motivations</strong>
            <br><br>
            Simplifie le processus de rédaction et de maintenance d'une documentation de projet de haute qualité, améliorant ainsi la productivité et le flux de travail des développeurs. L'objectif ultime de <em>readme-ai</em> est d'améliorer l'adoption et l'utilisabilité des logiciels open source, permettant à tous les niveaux de compétence de mieux comprendre les bases de code complexes et d'utiliser facilement les outils open source.
            <br><br>
            <strong>⚠️ Avertissement</strong>
            <br><br>
            Ce projet est actuellement en cours de développement et dispose d'une configuration orientée. Bien que <em>readme-ai</em> offre un excellent point de départ pour la documentation, il est important de réviser tout le texte généré par l'API OpenAI pour s'assurer qu'il représente avec précision votre base de code.
        </td>
    </tr>
</table>

---

## 🤖 Démos

***Interface en Ligne de Commande***

‣ Exécutez <i>readme-ai</i> dans votre terminal via PyPI, Docker, et plus encore !

[cli-demo](https://github.com/eli64s/readme-ai/assets/43382407/645c2336-6ea7-444c-a927-5450930c5255)

<br>

***Streamlit Community Cloud***

‣ Utilisez *readme-ai* directement dans votre navigateur ! Aucune installation, aucun code !

[streamlit-demo](https://github.com/eli64s/readme-ai/assets/43382407/e8260e78-b684-4e72-941c-b3046b90c452)

---

## 💫 Fonctionnalités

<div>
<details>
    <summary style="display: flex; align-items: center;">
        <span style="font-size: 2.0em;"> ❶ Badges Shieldsio</span>
    </summary>
    <table>
        <tr>
            <td>
                <h4><i>Slogan du Projet et Badges</i></h4>
                <p>
                    ‣ Un slogan pour mettre en valeur votre projet est généré en <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L56">interrogeant</a> le moteur GPT d'OpenAI.
                    </p>
                <p>
                    ‣ Les dépendances et métadonnées de la base de code sont visualisées à l'aide de badges <a href="https://shields.io/">Shields.io</a>.
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/badges.png" alt="badges" />
            </td>
        </tr>
    </table>
    <table>
        <p>
            ‣ Utilisez l'option CLI <code>--badges</code> pour sélectionner le style de badges pour votre README ! 3 styles sont actuellement pris en charge :
        </p>
        <tr>
            <td>
                <h4 style="text-align:left;">1. Style de badge Shieldsio par défaut</h4>
                <p style="text-align:left;">Commande : aucune car c'est le style par défaut pour <em>readme-ai</em></p>
                <div style="text-align:center;">
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/badges-shieldsio-default.png" alt="badges-shieldsio-default" />
                </div>
            </td>
        </tr>
        <tr>
            <td>
                <h4 style="text-align:left;">2. Style Shieldsio <em>for-the-badge</em></h4>
                <p style="text-align:left;">Commande : <code>--badges shields</code></p>
                <div style="text-align:center;">
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/badges-shieldsio-flat.png" alt="badges-shieldsio-flat" />
                </div>
            </td>
        </tr>
        <tr>
            <td>
                <h4 style="text-align:left;">3. Badges de style carré <em>iOS</em></h4>
                <p style="text-align:left;">Commande : <code>--badges square</code></p>
                <div style="text-align:center;">
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/badges-square.png" alt="badges-square" />
                </div>
            </td>
        </tr>
    </table>
</details>
</div>
<br>
<div>
    <details>
        <summary style="display: flex; align-items: center;">
            <span style="font-size: 2.0em;"> ❷ Documentation de la Base de Code</span>
        </summary>
        <table>
            <tr>
                <td colspan="2">
                    <h4><i>Arborescence des Répertoires et Résumés des Fichiers</i></h4>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <p>‣ La structure de répertoire de votre projet est visualisée à l'aide d'une fonction d'arborescence personnalisée.</p>
                    <p>‣ Chaque fichier de la base de code est résumé par le modèle <i>GPT</i> d'OpenAI.</p>
                </td>
            </tr>
            <tr>
                <td align="center">
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/repository-tree.png" alt="repository-tree" />
                </td>
                <td align="center">
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/code-summaries.png" alt="code-summaries" />
                </td>
            </tr>
        </table>
    </details>
</div>
<br>
<div>
    <details>
        <summary style="display: flex; align-items: center;">
            <span style="font-size: 2.0em;"> ❸ Aperçu et Tableau des Fonctionnalités</span>
        </summary>
        <table>
            <tr>
                <td>
                    <h4><i>Génération de Texte sur Demande</i></h4>
                    <p>
                        ‣ Un paragraphe d'aperçu et un tableau de fonctionnalités sont générés en utilisant des <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L31">demandes détaillées</a>, intégrées avec les métadonnées du projet.
                    </p>
                </td>
            </tr>
            <tr>
                <td>
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/feature-table.png" alt="feature-table" />
                </td>
            </tr>
        </table>
    </details>
</div>
<br>
<div>
    <details>
        <summary style="display: flex; align-items: center;">
            <span style="font-size: 2.0em;"> ❹ Instructions d'Utilisation Dynamiques</span><br>
        </summary>
        <table>
            <tr>
                <td>
                    <h4><i>Installation, Exécution, et Test</i></h4>
                    <p>
                        ‣ Génère des instructions pour installer, exécuter, et tester votre projet. Les instructions sont créées en identifiant le langage principal de la base de code et en se référant à notre fichier de configuration <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/language_setup.toml">language_setup.toml</a>.
                    </p>
                </td>
            </tr>
            <tr>
                <td>
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/usage-instructions.png" alt="usage-instructions" />
                </td>
            </tr>
        </table>
    </details>
</div>
<br>
<div>
    <details>
        <summary style="display: flex; align-items: center;">
            <span style="font-size: 2.0em;"> ❺ Directives de Contribution et plus encore !</span><br>
        </summary>
        <table>
            <tr>
                <td>
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/roadmap.png" alt="roadmap" />
                </td>
            </tr>
            <br>
            <tr>
                <td>
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/license.png" alt="license" />
                </td>
            </tr>
        </table>
    </details>
</div>
<br>
<div>
<details>
    <summary style="display: flex; align-items: center;">
        <span style="font-size: 2.0em;">❻ Modèles à Venir</span><br>
    </summary>
    <table>
        <tr>
            <td>
                <p>‣ Développement d'une option CLI permettant aux utilisateurs de sélectionner parmi une variété de styles de README</p>
                <p>‣ Modèles pour des cas d'utilisation tels que les données, l'apprentissage automatique, le développement web, et plus encore !</p>
            </td>
        </tr>
        <tr>
            <td>
                <h3>Concept de Modèle de README pour IA et ML</h3>
                <ul>
                    <li><strong><a href="#overview">Aperçu</a></strong> : Résumé des objectifs, de la portée et des résultats attendus du projet.</li>
                    <li><strong><a href="#project-structure">Structure du Projet</a></strong> : Aperçu de l'organisation du projet et de ses principaux composants.</li>
                    <li><strong><a href="#data-collection-and-preprocessing">Collecte et Prétraitement des Données</a></strong> : Sources de données, méthodes de collecte, et types de données.</li>
                    <li><strong><a href="#feature-engineering">Ingénierie des Caractéristiques</a></strong> : Importance de l'ingénierie des caractéristiques et son impact sur les performances du modèle.</li>
                    <li><strong><a href="#model-architecture-and-development">Architecture et Développement du Modèle</a></strong> : Choix du modèle, stratégies de développement et algorithmes de mise en œuvre.</li>
                    <li><strong><a href="#training-and-validation">Entraînement et Validation</a></strong> : Informations sur le processus d'entraînement du modèle, l'ajustement des hyperparamètres et les stratégies de validation.</li>
                    <li><strong><a href="#testing-and-evaluation">Test et Évaluation</a></strong> : Résultats des tests du modèle, analyse des performances, et comparaison avec des benchmarks.</li>
                    <li><strong><a href="#deployment-and-integration">Déploiement et Intégration</a></strong> : Intégration avec d'autres systèmes, API et interfaces utilisateur.</li>
                    <li><strong><a href="#usage-and-maintenance">Utilisation et Maintenance</a></strong> : Guide de l'utilisateur sur la façon d'utiliser le modèle et l'interface déployés.</li>
                    <li><strong><a href="#results-and-discussion">Résultats et Discussion</a></strong> : Impact, limites, et travaux futurs.</li>
                    <li><strong><a href="#ethical-considerations">Considérations Éthiques</a></strong> : Considérations éthiques, confidentialité des données, et équité dans les prédictions du modèle.</li>
                    <li><strong><a href="#contributing">Contribuer</a></strong> : Processus pour soumettre des contributions, signaler des problèmes, et suggérer des améliorations.</li>
                    <li><strong><a href="#acknowledgements">Remerciements</a></strong> : Références aux ressources, bibliothèques, et frameworks utilisés.</li>
                    <li><strong><a href="#license">Licence</a></strong> : Explication des droits d'utilisation, restrictions et exigences en matière d'attribution.</li>
                </ul>
            </td>
        </tr>
    </table>
</details>
</div>
<br>
<div>
    <details>
        <summary style="display: flex; align-items: center;">
            <span style="font-size: 2.0em;"> ❼ Exemples de fichiers README</span><br>
        </summary>
        <table>
            <thead>
                <tr>
                    <th></th>
                    <th>Fichier de sortie</th>
                    <th>Référentiel</th>
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
</div>
<br>

<p align="right">
    <a href="#top"><b>🔝 Retour</b></a>
</p>

---

## 👩‍💻 Utilisation

***Dépendances***

Assurez-vous d'avoir installé les dépendances suivantes sur votre système :

- *Python version 3.9 ou supérieure*
- *Gestionnaire de paquets (i.e. pip, conda, poetry) ou Docker*
- *Compte payant OpenAI API et clé API*

<br>

***Dépôt***

Un URL de dépôt distant ou un chemin de répertoire local vers votre projet est nécessaire pour utiliser *readme-ai*. Les plateformes suivantes sont actuellement prises en charge :
- *GitHub*
- *GitLab*
- *Bitbucket*
- *Système de fichiers*

<br>

***OpenAI API***

Un compte OpenAI API et une clé API sont nécessaires pour utiliser *readme-ai*. Les étapes ci-dessous décrivent ce processus :

<details closed><summary>🔐 OpenAI API - Instructions de configuration</summary>

1. Rendez-vous sur le [site OpenAI](https://platform.openai.com/).
2. Cliquez sur le bouton "Sign up for free".
3. Remplissez le formulaire d'inscription avec vos informations et acceptez les conditions d'utilisation.
4. Une fois connecté, cliquez sur l'onglet "API".
5. Suivez les instructions pour créer une nouvelle clé API.
6. Copiez la clé API et conservez-la dans un endroit sûr.

</details>

<details closed><summary>⚠️ OpenAI API - Directives de prudence</summary>

1. **Réviser les informations sensibles** : Avant d'exécuter l'application, assurez-vous que tout le contenu de votre dépôt est exempt d'informations sensibles. Notez que *readme-ai* ne filtre pas les données sensibles du fichier README et ne modifie aucun fichier dans votre dépôt.

2. **Coûts d'utilisation de l'API** : L'API OpenAI n'est pas gratuite, et chaque requête effectuée vous sera facturée. Les coûts peuvent s'accumuler rapidement, il est donc essentiel d'être conscient de votre utilisation. Vous pouvez surveiller votre utilisation de l'API et les coûts associés en visitant le [Tableau de bord d'utilisation de l'API OpenAI](https://platform.openai.com/account/usage).

3. **Compte payant recommandé** : Il est fortement recommandé de configurer un compte payant avec OpenAI pour éviter d'éventuels problèmes. Sans méthode de paiement enregistrée, votre utilisation de l'API sera limitée aux modèles de base GPT-3. Cette limitation peut entraîner une génération de fichiers README moins précise et peut conduire à des erreurs d'API en raison de limites de requêtes.

4. **Considérations sur le temps d'exécution** : La génération du fichier README prend généralement moins d'une minute. Si le processus dépasse quelques minutes (par exemple, 3 minutes), il est conseillé de terminer *readme-ai* pour éviter des temps de traitement prolongés.

</details>

---

### 📦 Installation

***Utilisation de Pip***

Pip est la méthode d'installation recommandée pour la plupart des utilisateurs.

```sh
pip install readmeai
```
<br>

***Utilisation de Docker***

Docker est recommandé pour les utilisateurs souhaitant exécuter l'application dans un environnement conteneurisé.

```sh
docker pull zeroxeli/readme-ai:latest
```

<br>

***Manuellement***

1️⃣ Clonez le dépôt readme-ai.
```sh
git clone https://github.com/eli64s/readme-ai
```

2️⃣ Naviguez vers le répertoire readme-ai.

```sh
cd readme-ai
```

3️⃣ Installez les dépendances en utilisant une méthode ci-dessous.

***Utilisation de Bash***
```sh
bash setup/setup.sh
```

***Utilisation de Conda***
```sh
conda create -n readmeai python=3.9 -y && \
conda activate readmeai && \
pip install -r requirements.txt
```

***Utilisation de Poetry***
```sh
poetry shell && \
poetry install
```

---

### ⚙️ Configuration

<br>

### Arguments de Ligne de Commande

Pour générer un fichier *README.md*, utilisez la commande `readmeai` dans votre terminal, accompagnée des arguments ci-dessous.

| Argument Court | Argument Long | Description                                         | Statut       |
|----------------|---------------|-----------------------------------------------------|--------------|
| `-k`           | `--api-key`   | Votre clé secrète d'API pour le modèle de langage.  | Optionnel    |
| `-b`           | `--badges`    | Choisissez 'shields' ou 'square' pour changer le style des badges. | Optionnel    |
| `-f`           | `--offline-mode`| Exécutez en mode hors ligne sans appeler l'API OpenAI. | Optionnel    |
| `-m`           | `--model`     | Moteur de grand modèle de langage (gpt-3.5-turbo).  | Optionnel    |
| `-o`           | `--output`    | Le chemin de sortie pour votre fichier README.md.   | Optionnel    |
| `-r`           | `--repository`| L'URL ou le chemin vers votre dépôt de code.        | Requis       |
| `-t`           | `--temperature`| La "température" (aléatoire) du modèle.            | Optionnel    |
| `-l`           | `--language`  | La langue dans laquelle rédiger le README.         | Bientôt disponible ! |
| `-s`           | `--style`     | Le style du modèle README à construire.            | Bientôt disponible ! |

<br>

### Paramètres Personnalisés

Pour personnaliser le processus de génération du fichier README, vous pouvez modifier le [fichier de configuration](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml) du projet :

- [*api*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L2) - Paramètres de configuration de l'API du modèle de langage OpenAI.
- [*git*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L12) - Paramètres du dépôt git par défaut utilisés si aucun dépôt n'est fourni.
- [*paths*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L17) - Chemins des répertoires et fichiers utilisés par l'application *readme-ai*.
- [*prompts*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L26) - Invitations du grand modèle de langage utilisées pour générer le fichier README.
- [*md*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L59) - Modèles de code de section Markdown dynamiques utilisés pour construire le fichier README.

---

### 🚀 Exécution de *README-AI*

***Utilisation avec Pip***

```sh
# Option 1 : Exécutez la commande readmeai avec tous les arguments requis.
readmeai --api-key "VOTRE_CLÉ_API" --output readme-ai.md --repository https://github.com/eli64s/readme-ai
```
```sh
# Option 2 : Exécutez la commande readmeai avec la clé API OpenAI définie comme variable d'environnement.
export OPENAI_API_KEY="VOTRE_CLÉ_API"
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai -b shields
```

<br>

***Utilisation avec Docker***

```sh
# Option 1 : Exécutez le conteneur Docker avec tous les arguments requis.
docker run -it \
-e OPENAI_API_KEY="VOTRE_CLÉ_API" \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai
```
```sh
# Option 2 : Exécutez le conteneur Docker avec la clé API OpenAI définie comme variable d'environnement.
export OPENAI_API_KEY="VOTRE_CLÉ_API"
docker run -it \
-e OPENAI_API_KEY=$OPENAI_API_KEY \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<br>

***Utilisation avec Conda***
```sh
conda activate readmeai
export OPENAI_API_KEY="VOTRE_CLÉ_API"
python3 -m readmeai.cli.commands -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<br>

***Utilisation avec Poetry***
```sh
poetry shell
export OPENAI_API_KEY="VOTRE_CLÉ_API"
poetry run python3 -m readmeai.cli.commands -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<br>

***Utilisation avec Streamlit***

Utilisez l'application directement dans votre navigateur via Streamlit Community Cloud.

- [🛸 Emmenez-moi vers *readme-ai* sur Streamlit !](https://readmeai.streamlit.app/)

---

### 🧪 Tests

Exécutez la suite de tests en utilisant la commande ci-dessous.

```sh
bash scripts/test.sh
```

---

### 🛠 Feuille de Route

- [X] Publier le projet en tant que bibliothèque Python via PyPI pour faciliter l'installation.
  - [*PyPI - readmeai*](https://pypi.org/project/readmeai/)
- [X] Rendre le projet disponible en tant qu'image Docker sur Docker Hub.
  - [*Docker Hub - readme-ai*](https://hub.docker.com/repository/docker/zeroxeli/readme-ai/general)
- [X] Intégrer et déployer l'application avec Streamlit pour la rendre plus largement accessible.
  - [*Streamlit Community Cloud - readmeai*](https://readmeai.streamlit.app/)
- [ ] Remanier notre moteur de grand modèle de langage pour permettre une génération de README plus robuste.
  - [ ] Explorer [LangChain 🦜️🔗](https://python.langchain.com/docs/get_started/introduction) comme alternative à l'utilisation directe de l'API OpenAI.
  - [ ] Explorer le framework [LlamaIndex 🦙](https://gpt-index.readthedocs.io/en/stable/index.html) et le paradigme de génération augmentée par récupération (RAG).
- [ ] Ajouter le support pour générer des fichiers README dans toutes les langues (par ex. CN, ES, FR, JA, KO, RU).
- [ ] Concevoir des modèles de sortie README pour une variété de cas d'utilisation (par ex. données, développement web, minimal, etc.)
- [ ] Développer un script GitHub Actions pour mettre à jour automatiquement le fichier README lorsqu'un nouveau code est poussé.

---

## 📒 Journal des Modifications

[Journal des Modifications](https://github.com/eli64s/readme-ai/blob/main/CHANGELOG.md)

---

## 🤝 Contribuer

Vous souhaitez contribuer à *readme-ai* ? Voici ce que vous pouvez faire pour aider :

- 🐍 Recherchez des opportunités pour rendre le code plus efficace et lisible.
- 🤖 La gestion des exceptions et les corrections de bugs sont toujours les bienvenues !
- 📝 Améliorez la documentation et ajoutez plus d'exemples au README.
- 🔡 Ajoutez le support pour générer des fichiers README dans toutes les langues (par exemple CN, ES, FR, JA, KO, RU).
- 🎨 Créez de nouveaux modèles pour différents cas d'utilisation (c'est-à-dire données, développement web, minimal, etc.).
  - Le README est construit en sections, définies dans le fichier [config.toml].
  - Suivez le format existant pour commencer.

[Directives pour Contribuer](https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md)

---

## 📄 Licence

[MIT](https://github.com/eli64s/readme-ai/blob/main/LICENSE)

---

## 👏 Remerciements

*Icones de Badges*
  - [Shields.io](https://shields.io/)
  - [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)
  - [Ileriayo/Markdown-Badges](https://github.com/Ileriayo/markdown-badges)
  - [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons)


<p align="right">
  <a href="#top"><b>🔝 Retour </b></a>
</p>

---
