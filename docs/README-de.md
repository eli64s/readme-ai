<div align="center">
    <h1 align="center">
        <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="80" />
        <img src="https://img.icons8.com/?size=512&id=kTuxVYRKeKEY&format=png" width="80" />
        <br>README-AI
    </h1>
    <h3>◦ Erstellen Sie schöne und informative <i>README</i>-Dateien</h3>
    <h3>◦ Entwickelt mit den GPT-Sprachmodell-APIs von OpenAI</h3>
    <br>
    <p align="center">
        <img src="https://img.shields.io/badge/Markdown-000000.svg?&logo=Markdown&logoColor=white" alt="Markdown" />
        <img src="https://img.shields.io/badge/OpenAI-412991.svg?&logo=OpenAI&logoColor=white" alt="OpenAI" />
        <img src="https://img.shields.io/badge/Python-3776AB.svg?&logo=Python&logoColor=white" alt="Python" />
        <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?&logo=Pytest&logoColor=white" alt="pytest" />
        <img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />
        <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="actions" />
    </p>
    <a href="https://pypi.org/project/readmeai/">
        <img src="https://img.shields.io/pypi/v/readmeai?color=5D6D7E&logo=pypi" alt="pypi-version" />
    </a>
    <a href="https://pypi.org/project/readmeai/">
        <img src="https://img.shields.io/pypi/pyversions/readmeai?color=5D6D7E&logo=python" alt="pypi-python-version" />
    </a>
    <img src="https://img.shields.io/github/commit-activity/m/eli64s/readme-ai.svg?color=5D6D7E" alt="commits-month" />
    <img src="https://img.shields.io/github/license/eli64s/readme-ai?color=5D6D7E" alt="license" />
    <br>
</div>

---

## 📖 Inhaltsverzeichnis

- [📖 Inhaltsverzeichnis](#-inhaltsverzeichnis)
- [🔭 Übersicht](#-übersicht)
- [🤖 Demos](#-demos)
- [💫 Funktionen](#-funktionen)
- [👩‍💻 Nutzung](#-nutzung)
  - [📦 Installation](#-installation)
  - [⚙️ Konfiguration](#️-konfiguration)
  - [🚀 Ausführen von *README-AI*](#-ausführen-von-readme-ai)
  - [🧪 Tests](#-tests)
- [🛠 Roadmap](#-roadmap)
- [📒 Changelog](#-changelog)
- [🤝 Mitwirken](#-mitwirken)
- [📄 Lizenz](#-lizenz)
- [👏 Danksagungen](#-danksagungen)

---

## 🔭 Übersicht

<table>
    <tr>
        <td>
            <strong>👋 Über</strong>
            <br><br>
            <em>README-AI</em> ist ein Befehlszeilen-Tool, das robuste README.md-Dateien für Ihre Software- und Datenprojekte generiert. Indem Sie einfach eine Remote-Repository-URL oder einen Pfad zu Ihrer Codebasis angeben, generiert dieses Tool automatisch Dokumentation für Ihr gesamtes Projekt, indem es die Fähigkeiten der GPT-Sprachmodell-APIs von OpenAI nutzt.
            <br><br>
            <strong>🎯 Motivationen</strong>
            <br><br>
            Vereinfacht den Prozess des Schreibens und Wartens von hochwertiger Projektdokumentation, verbessert die Produktivität und den Arbeitsablauf von Entwicklern. Das ultimative Ziel von <em>readme-ai</em> ist es, die Adoption und Benutzerfreundlichkeit von Open-Source-Software zu verbessern, sodass alle Kompetenzniveaus komplexe Codebasen besser verstehen und Open-Source-Tools einfach nutzen können.
            <br><br>
            <strong>⚠️ Haftungsausschluss</strong>
            <br><br>
            Dieses Projekt befindet sich derzeit in der Entwicklung und hat eine meinungsbildende Konfiguration. Während <em>readme-ai</em> einen hervorragenden Ausgangspunkt für Dokumentationen bietet, ist es wichtig, alle vom OpenAI API generierten Texte zu überprüfen, um sicherzustellen, dass sie Ihre Codebasis genau darstellen.
        </td>
        <td>
            <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/dalle-readmeai" width="2500" />
        </td>
    </tr>
</table>

---

## 🤖 Demos

***Befehlszeilen-Interface***

‣ Führen Sie <i>readme-ai</i> in Ihrem Terminal über PyPI, Docker und mehr aus!

[cli-demo](https://github.com/eli64s/readme-ai/assets/43382407/645c2336-6ea7-444c-a927-5450930c5255)

<br>

***Streamlit Community Cloud***

‣ Nutzen Sie *readme-ai* direkt in Ihrem Browser! Keine Installation, kein Code!

[streamlit-demo](https://github.com/eli64s/readme-ai/assets/43382407/e8260e78-b684-4e72-941c-b3046b90c452)

---

## 💫 Funktionen

<br>
<div>
<details>
    <summary style="display: flex; align-items: center;">
        <span style="font-size: 2.0em;"> ❶ Shieldsio Abzeichen</span>
    </summary>
    <table>
        <tr>
            <td>
                <h4><i>Projekt-Slogan und Abzeichen</i></h4>
                <p>
                    ‣ Ein Slogan, um Ihr Projekt hervorzuheben, wird durch das <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L56">Prompting</a> der OpenAI GPT-Engine generiert.
                    </p>
                <p>
                    ‣ Codebase-Abhängigkeiten und Metadaten werden mit <a href="https://shields.io/">Shields.io</a>-Abzeichen visualisiert.
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
            ‣ Verwenden Sie die CLI-Option <code>--badges</code>, um den Stil der Abzeichen für Ihre README zu wählen! Aktuell werden 3 Stile unterstützt:
        </p>
        <tr>
            <td>
                <h4 style="text-align:left;">1. Standard Shieldsio-Abzeichenstil</h4>
                <p style="text-align:left;">Befehl: keiner, da es der Standardstil für <em>readme-ai</em> ist</p>
                <div style="text-align:center;">
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/badges-shieldsio-default.png" alt="badges-shieldsio-default" />
                </div>
            </td>
        </tr>
        <tr>
            <td>
                <h4 style="text-align:left;">2. Shieldsio <em>for-the-badge</em>-Stil</h4>
                <p style="text-align:left;">Befehl: <code>--badges shields</code></p>
                <div style="text-align:center;">
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/badges-shieldsio-flat.png" alt="badges-shieldsio-flat" />
                </div>
            </td>
        </tr>
        <tr>
            <td>
                <h4 style="text-align:left;">3. Quadratische <em>iOS-Stil</em>-Abzeichen</h4>
                <p style="text-align:left;">Befehl: <code>--badges square</code></p>
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
            <span style="font-size: 2.0em;"> ❷ Codebase Dokumentation</span>
        </summary>
        <table>
            <tr>
                <td colspan="2">
                    <h4><i>Verzeichnisbaum und Dateizusammenfassungen</i></h4>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <p>‣ Die Verzeichnisstruktur Ihres Projekts wird mit einer benutzerdefinierten Baumfunktion visualisiert.</p>
                    <p>‣ Jede Datei in der Codebase wird vom <i>GPT</i>-Modell von OpenAI zusammengefasst.</p>
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
            <span style="font-size: 2.0em;"> ❸ Übersicht und Feature-Tabelle</span>
        </summary>
        <table>
            <tr>
                <td colspan="2">
                    <h4><i>Ein strukturierter Überblick</i></h4>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <p>‣ <i>readme-ai</i> bietet Ihnen eine strukturierte Übersicht über die Hauptfunktionen Ihres Projekts, basierend auf Ihrem Code und den von Ihnen zur Verfügung gestellten Beschreibungen.</p>
                </td>
            </tr>
            <tr>
                <td align="center">
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/overview.png" alt="overview" />
                </td>
                <td align="center">
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/features-table.png" alt="features-table" />
                </td>
            </tr>
        </table>
    </details>
</div>
<br>
<div>
    <details>
        <summary style="display: flex; align-items: center;">
            <span style="font-size: 2.0em;"> ❸ Übersicht und Eigenschaften Tabelle</span>
        </summary>
        <table>
            <tr>
                <td>
                    <h4><i>Gesteuerte Texterstellung</i></h4>
                    <p>
                        ‣ Ein Überblicksabsatz und eine Eigenschaften-Tabelle werden mit <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L31">detaillierten Aufforderungen</a>, eingebettet mit Projekt-Metadaten, erstellt.
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
            <span style="font-size: 2.0em;"> ❹ Dynamische Nutzungsanweisungen</span><br>
        </summary>
        <table>
            <tr>
                <td>
                    <h4><i>Installation, Ausführung und Test</i></h4>
                    <p>
                        ‣ Erstellt Anweisungen für die Installation, Ausführung und das Testen Ihres Projekts. Die Anweisungen werden erstellt, indem die Hauptprogrammiersprache des Codebasis identifiziert und auf unsere <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/language_setup.toml">language_setup.toml</a> Konfigurationsdatei verwiesen wird.
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
            <span style="font-size: 2.0em;"> ❺ Beitragsrichtlinien und mehr!</span><br>
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
        <span style="font-size: 2.0em;">❻ Vorlagen kommen bald</span><br>
    </summary>
    <table>
        <tr>
            <td>
                <p>‣ Entwicklung einer CLI-Option, die es den Benutzern ermöglicht, aus einer Vielzahl von README-Stilen auszuwählen</p>
                <p>‣ Vorlagen für Anwendungsfälle wie Daten, maschinelles Lernen, Webentwicklung und mehr!</p>
            </td>
        </tr>
        <tr>
            <td>
                <h3>KI und ML README Vorlagenkonzept</h3>
                <ul>
                    <li><strong><a href="#overview">Übersicht</a></strong>: Zusammenfassung der Projektziele, des Umfangs und der erwarteten Ergebnisse.</li>
                    <li><strong><a href="#project-structure">Projektstruktur</a></strong>: Überblick über die Organisation der Projekte und ihre Hauptkomponenten.</li>
                    <li><strong><a href="#data-collection-and-preprocessing">Datenverarbeitung</a></strong>: Datenquellen, Sammlungsmethoden und Datentypen</li>
                    <li><strong><a href="#feature-engineering">Merkmalsentwicklung</a></strong>: Bedeutung der Merkmalsentwicklung und ihre Auswirkungen auf die Modellleistung.</li>
                    <li><strong><a href="#model-architecture-and-development">Modellarchitektur und -entwicklung</a></strong>: Modellauswahl, Entwicklungsstrategien und implementierte Algorithmen.</li>
                    <li><strong><a href="#training-and-validation">Training und Validierung</a></strong>: Infos zu Modelltrainingsverfahren, Hyperparameter-Tuning und Validierungsstrategien.</li>
                    <li><strong><a href="#testing-and-evaluation">Testen und Evaluierung</a></strong>: Modelltestergebnisse, Leistungsanalyse und Vergleich mit Benchmarks.</li>
                    <li><strong><a href="#deployment-and-integration">Deployment und Integration</a></strong>: Integration mit anderen Systemen, APIs und Benutzerschnittstellen</li>
                    <li><strong><a href="#usage-and-maintenance">Nutzung und Wartung</a></strong>: Benutzerhandbuch zur Nutzung der bereitgestellten Modelle und Schnittstellen.</li>
                    <li><strong><a href="#results-and-discussion">Ergebnisse und Diskussion</a></strong>: Implikationen, Einschränkungen und zukünftige Arbeit.</li>
                    <li><strong><a href="#ethical-considerations">Ethische Überlegungen</a></strong>: Ethische Aspekte, Datenschutz und Fairness in Modellvorhersagen.</li>
                    <li><strong><a href="#contributing">Mitwirken</a></strong>: Verfahren zur Einreichung von Beiträgen, Meldung von Problemen und Vorschlagen von Verbesserungen.</li>
                    <li><strong><a href="#acknowledgements">Danksagungen</a></strong>: Verweise auf genutzte Ressourcen, Bibliotheken und Frameworks.</li>
                    <li><strong><a href="#license">Lizenz</a></strong>: Erläuterung der Nutzungsrechte, Einschränkungen und Anforderungen an die Zuschreibung.</li>
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
            <span style="font-size: 2.0em;"> ❼ Beispiel README-Dateien</span><br>
        </summary>
        <table>
            <thead>
                <tr>
                    <th></th>
                    <th>Ausgabedatei</th>
                    <th>Repository</th>
                    <th>Sprachen</th>
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
    <a href="#top"><b>🔝 Zurück</b></a>
</p>

---

## 👩‍💻 Nutzung

***Abhängigkeiten***

Bitte stellen Sie sicher, dass die folgenden Abhängigkeiten auf Ihrem System installiert sind:

- *Python-Version 3.9 oder höher*
- *Paket-Manager (z.B. pip, conda, poetry) oder Docker*
- *OpenAI API bezahlter Account und API-Schlüssel*

<br>

***Repository***

Eine Remote-Repository-URL oder ein lokaler Verzeichnispfad zu Ihrem Projekt ist erforderlich, um *readme-ai* zu verwenden. Die folgenden Plattformen werden derzeit unterstützt:
- *GitHub*
- *GitLab*
- *Bitbucket*
- *Dateisystem*

<br>

***OpenAI API***

Ein OpenAI-API-Konto und ein API-Schlüssel werden benötigt, um *readme-ai* zu verwenden. Die unten stehenden Schritte beschreiben diesen Prozess:

<details closed><summary>🔐 OpenAI API - Einrichtungsanweisungen</summary>

1. Besuchen Sie die [OpenAI-Website](https://platform.openai.com/).
2. Klicken Sie auf den Button "Sign up for free".
3. Füllen Sie das Registrierungsformular mit Ihren Informationen aus und stimmen Sie den Nutzungsbedingungen zu.
4. Nach dem Einloggen klicken Sie auf den "API"-Tab.
5. Befolgen Sie die Anweisungen zur Erstellung eines neuen API-Schlüssels.
6. Kopieren Sie den API-Schlüssel und bewahren Sie ihn an einem sicheren Ort auf.

</details>

<details closed><summary>⚠️ OpenAI API - Vorsichtsrichtlinien</summary>

1. **Überprüfung sensitiver Informationen**: Stellen Sie vor dem Ausführen der Anwendung sicher, dass alle Inhalte in Ihrem Repository frei von sensiblen Informationen sind. Beachten Sie, dass *readme-ai* keine sensiblen Daten aus der README-Datei filtert und keine Dateien in Ihrem Repository ändert.

2. **API-Nutzungskosten**: Die OpenAI API ist nicht kostenlos, und für jede gestellte Anfrage fallen Gebühren an. Die Kosten können sich schnell summieren, daher ist es wichtig, sich Ihrer Nutzung bewusst zu sein. Sie können Ihre API-Nutzung und die damit verbundenen Kosten überprüfen, indem Sie das [OpenAI API-Nutzungs-Dashboard](https://platform.openai.com/account/usage) besuchen.

3. **Bezahlter Account empfohlen**: Es wird dringend empfohlen, ein bezahltes Konto bei OpenAI einzurichten, um mögliche Probleme zu vermeiden. Ohne hinterlegte Zahlungsmethode wird Ihre API-Nutzung auf die Grundmodelle von GPT-3 beschränkt. Diese Einschränkung kann zu einer weniger genauen README-Dateierstellung führen und aufgrund von Anfragebeschränkungen zu API-Fehlern führen.

4. **Laufzeitüberlegungen**: Die Erstellung einer README-Datei dauert in der Regel weniger als eine Minute. Wenn der Prozess ein paar Minuten (z.B., 3 Minuten) überschreitet, ist es ratsam, *readme-ai* zu beenden, um längere Verarbeitungszeiten zu vermeiden.

</details>

---

### 📦 Installation

***Mit Pip***

Pip ist die empfohlene Installationsmethode für die meisten Nutzer.

```sh
pip install readmeai
```
<br>

***Mit Docker***

Docker wird für Benutzer empfohlen, die die Anwendung in einer containerisierten Umgebung ausführen möchten.

```sh
docker pull zeroxeli/readme-ai:latest
```

<br>

***Manuell***

1️⃣ Klone das readme-ai Repository.
```sh
git clone https://github.com/eli64s/readme-ai
```

2️⃣ Navigiere zum readme-ai Verzeichnis.

```sh
cd readme-ai
```

3️⃣ Installiere die Abhängigkeiten mit einer der unten stehenden Methoden.

***Mit Bash***
```sh
bash setup/setup.sh
```

***Mit Conda***
```sh
conda create -n readmeai python=3.9 -y && \
conda activate readmeai && \
pip install -r requirements.txt
```

***Mit Poetry***
```sh
poetry shell && \
poetry install
```

</details>

---

### ⚙️ Konfiguration

<br>

***Befehlszeilenargumente***

Um eine *README.md* Datei zu generieren, verwenden Sie den Befehl `readmeai` in Ihrem Terminal zusammen mit den unten aufgeführten Argumenten.

| Kurzflag | Langflag       | Beschreibung                                        | Status       |
|----------|----------------|-----------------------------------------------------|--------------|
| `-k`     | `--api-key`    | Ihr API-Geheim-Schlüssel für das Sprachmodell.      | Optional     |
| `-b`     | `--badges`     | Wählen Sie 'shields' oder 'square', um den Badge-Stil zu ändern. | Optional     |
| `-f`     | `--offline-mode`| Laufen Sie offline, ohne die OpenAI API aufzurufen. | Optional     |
| `-m`     | `--model`      | Großes Sprachmodell-Motor (gpt-3.5-turbo)            | Optional     |
| `-o`     | `--output`     | Der Ausgabepfad für Ihre README.md-Datei.            | Optional     |
| `-r`     | `--repository` | Die URL oder der Pfad zu Ihrem Code-Repository.      | Erforderlich |
| `-t`     | `--temperature`| Die Temperatur (Zufälligkeit) des Modells.           | Optional     |
| `-l`     | `--language`   | Die Sprache, in der die README geschrieben werden soll. | In Kürze verfügbar! |
| `-s`     | `--style`      | Der zu erstellende README-Template-Stil.             | In Kürze verfügbar! |

<br>

***Benutzerdefinierte Einstellungen***

Um den README-Dateierstellungsprozess anzupassen, können Sie die [Konfigurationsdatei](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml) des Projekts modifizieren:

- [*api*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L2) - OpenAI Sprachmodell API Konfigurationseinstellungen.
- [*git*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L12) - Standard Git Repository-Einstellungen, die verwendet werden, wenn kein Repository bereitgestellt wird.
- [*paths*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L17) - Verzeichnispfade und Dateien, die von der *readme-ai* Anwendung genutzt werden.
- [*prompts*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L26) - Aufforderungen des großen Sprachmodells, die zur Erstellung der README-Datei verwendet werden.
- [*md*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L59) - Dynamische Markdown-Sektion Code-Templates, die zum Erstellen der README-Datei verwendet werden.

---

### 🚀 Ausführen von *README-AI*

***Mit Pip***

```sh
# Option 1: Führe den readmeai Befehl mit allen erforderlichen Befehlszeilenargumenten aus.
readmeai --api-key "YOUR_API_KEY" --output readme-ai.md --repository https://github.com/eli64s/readme-ai
```
```sh
# Option 2: Führe den readmeai Befehl mit OpenAI API Schlüssel als Umgebungsvariable aus.
export OPENAI_API_KEY="YOUR_API_KEY"
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai -b shields
```

<br>

***Mit Docker***

```sh
# Option 1: Führe Docker-Container mit allen erforderlichen Befehlszeilenargumenten aus.
docker run -it \
-e OPENAI_API_KEY="YOUR_API_KEY" \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai
```
```sh
# Option 2: Führe Docker-Container mit OpenAI API Schlüssel als Umgebungsvariable aus.
export OPENAI_API_KEY="YOUR_API_KEY"
docker run -it \
-e OPENAI_API_KEY=$OPENAI_API_KEY \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<!--
<br>

<details><summary><b><i>Manuell ausführen</i></b></summary>
-->
<br>

***Mit Conda***
```sh
conda activate readmeai
export OPENAI_API_KEY="YOUR_API_KEY"
python3 -m readmeai.cli.commands -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<br>

***Mit Poetry***
```sh
poetry shell
export OPENAI_API_KEY="YOUR_API_KEY"
poetry run python3 -m readmeai.cli.commands -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<br>

***Mit Streamlit***

Verwenden Sie die App direkt in Ihrem Browser über Streamlit Community Cloud.

- [🛸 Bring mich zu *readme-ai* auf Streamlit!](https://readmeai.streamlit.app/)

</details>

---

### 🧪 Tests

Führen Sie die Testsuite mit dem unten stehenden Befehl aus.

```sh
bash scripts/test.sh
```

---

## 🛠 Roadmap

- [X] Projekt als Python-Bibliothek über PyPI für eine einfache Installation veröffentlichen.
  - [*PyPI - readmeai*](https://pypi.org/project/readmeai/)
- [X] Projekt als Docker-Image auf Docker Hub verfügbar machen.
  - [*Docker Hub - readme-ai*](https://hub.docker.com/repository/docker/zeroxeli/readme-ai/general)
- [X] App mit Streamlit integrieren und bereitstellen, um das Tool breiter zugänglich zu machen.
  - [*Streamlit Community Cloud - readmeai*](https://readmeai.streamlit.app/)
- [ ] Unsere große Sprachmodell-Engine überarbeiten, um eine robustere README-Erzeugung zu ermöglichen.
  - [ ] Erkunden von [LangChain 🦜️🔗](https://python.langchain.com/docs/get_started/introduction) als Alternative zur direkten Verwendung der OpenAI API.
  - [ ] Erkunden des [LlamaIndex 🦙](https://gpt-index.readthedocs.io/en/stable/index.html) Frameworks und des Retrieval augmented generation (RAG) Paradigmas.
- [ ] Unterstützung für die Erstellung von README-Dateien in jeder Sprache hinzufügen (d.h. CN, ES, FR, JA, KO, RU).
- [ ] README-Ausgabevorlagen für eine Vielzahl von Anwendungsfällen entwerfen (d.h. Daten, Web-Entwicklung, minimal, etc.)
- [ ] Ein GitHub Actions Skript entwickeln, um die README-Datei automatisch zu aktualisieren, wenn neuer Code gepusht wird.

---

## 📒 Changelog

[Änderungsprotokoll](https://github.com/eli64s/readme-ai/blob/main/CHANGELOG.md)

---

## 🤝 Mitwirken

Möchten Sie zu *readme-ai* beitragen? Hier finden Sie, wie Sie helfen können:

- 🐍 Suchen Sie nach Möglichkeiten, den Code effizienter und lesbarer zu machen.
- 🤖 Ausnahmehandhabung und Fehlerbehebungen sind immer willkommen!
- 📝 Verbessern Sie die Dokumentation und fügen Sie dem README mehr Beispiele hinzu.
- 🔡 Fügen Sie Unterstützung für die Erstellung von README-Dateien in jeder Sprache hinzu (d.h. CN, ES, FR, JA, KO, RU).
- 🎨 Erstellen Sie neue Vorlagen für verschiedene Anwendungsfälle (d.h. Daten, Web-Entwicklung, minimal, etc.).
  - Das README wird in Abschnitten erstellt, die in der [config.toml]-Datei definiert sind.
  - Folgen Sie dem vorhandenen Format, um zu beginnen.

[Beitrags

richtlinien](https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md)

---

## 📄 Lizenz

[MIT](https://github.com/eli64s/readme-ai/blob/main/LICENSE)

---

## 👏 Danksagungen

*Abzeichen Icons*
  - [Shields.io](https://shields.io/)
  - [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)
  - [Ileriayo/Markdown-Badges](https://github.com/Ileriayo/markdown-badges)
  - [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons)


<p align="right">
  <a href="#top"><b>🔝 Zurück </b></a>
</p>

---
