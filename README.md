<div align="center">
<img style="" src="https://github.com/Jinkogule/Multi-Analyst/blob/main/static/img/logo.png" width="250px;" alt=""/>
<br>

[![Release](https://img.shields.io/github/v/release/Jinkogule/multi-Analyst?style=for-the-badge)](https://github.com/Jinkogule/PokeApp/releases)
[![License](https://img.shields.io/github/license/Jinkogule/multi-Analyst?style=for-the-badge)](LICENSE)<br>
![Status](https://img.shields.io/badge/STATUS-Em%20Desenvolvimento-brightyellow?style=for-the-badge)
</div>
<p align="center">
 <a href="#-sobre-o-projeto">Sobre</a> •
 <a href="#-documentação">Documentação</a> • 
 <a href="#-desenvolvimento">Desenvolvimento</a> • 
 <a href="#-tecnologias">Tecnologias</a> •  
 <a href="#-autor">Autor</a> • 
 <a href="#-licença">Licença</a>
</p>

---

## 💻 Sobre o projeto

O **Multi Analyst** é uma ferramenta de análise de dados com uma usabilidade simples e acessível, que utiliza inteligência artificial para interpretar os resultados das análises realizadas, retornando *insights* úteis aos usuários.

## 📋 Documentação

-   **[Wiki](https://github.com/Jinkogule/Multi-Analyst/wiki)**

## 🧑🏻‍💻 Desenvolvimento

-   **[Código-fonte](https://github.com/Jinkogule/Multi-Analyst)**
-   **[Issue Tracking](https://github.com/Jinkogule/Multi-Analyst/issues)**

## 🛠 Tecnologias

#### **Website**  ([Python](https://www.python.org/)  +  [Django](https://www.djangoproject.com/))

-   **[Python 3.12.4](https://www.python.org/)**
-   **[Django 4.2.14](https://www.djangoproject.com/)**

#### **Serviços**

-   **[OpenAI API](https://platform.openai.com/docs/overview)**

## ⚙ Executar o projeto localmente

#### **Pré-Requisitos**

Antes de começar, certifique-se de:

- Instalar o **[Git](https://git-scm.com/)**.
- Instalar o **[MySQL Server 8.0.3](https://dev.mysql.com/downloads/mysql/)** (ou versão compatível).
- Executar o **[script de banco de dados](https://github.com/Jinkogule/Spring-Boot-CRUD/blob/main/src/main/resources/documents/trabalhodac.sql)** para criar o schema e as tabelas necessárias.
- Instalar o **[JDK 17](https://www.oracle.com/br/java/technologies/downloads/#java17)** (ou versão compatível) e configurar a variável `JAVA_HOME` com o caminho correto do JDK.

#### **Rodando o Back-End (servidor)**

```bash
# Clone este repositório
$ git clone https://github.com/Jinkogule/Spring-Boot-CRUD

# Acesse a pasta do projeto no terminal/cmd
$ cd Spring-Boot-CRUD

# Instale as dependências e execute a aplicação usando o Maven Wrapper
# No Linux/macOS ou PowerShell
$ ./mvnw install
$ ./mvnw spring-boot:run

# No Windows
$ mvnw.cmd install
$ mvnw.cmd spring-boot:run
```

## 🎨 Layout

### Telas da aplicação
<table>
  <tr>
    <td align="center">
      <img src="/src/screenshots/pokedex-desktop.png" alt="Pokédex (Desktop)" title="Pokédex (Desktop)">
      <br>
      <em>Pokédex (Desktop)</em>
    </td>
    <td align="center">
      <img src="/src/screenshots/pokedex-cel.png" alt="Pokédex (Mobile)" title="Pokédex (Mobile)">
      <br>
      <em>Pokédex (Mobile)</em>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="/src/screenshots/pokemon-details-desktop.png" alt="Pokémon Details - Venusaur (Desktop)" title="Pokémon Details - Venusaur (Desktop)">
      <br>
      <em>Pokémon Details - Venusaur (Desktop)</em>
    </td>
    <td align="center">
      <img src="/src/screenshots/pokemon-details-cel.png" alt="Pokémon Details - Venusaur (Mobile)" title="Pokémon Details - Venusaur (Mobile)">
      <br>
      <em>Pokémon Details - Venusaur (Mobile)</em>
    </td>
  </tr>
</table>

## ✒ Autor

<table>
  <tr>
    <td align="center">
      Lucas Pimenta
      <br>
      <a href="https://github.com/Jinkogule">
        <img src="https://avatars.githubusercontent.com/u/52849575?v=4" width="100px;" alt="Lucas Pimenta"/>
      </a>
      <br>
      <a href="https://github.com/Jinkogule">
        <img src="https://img.shields.io/badge/-Github-black?style=flat-square&logo=Github&logoColor=white">
      </a>
    </td>
  </tr>
</table>

## 📝 Licença

Este projeto é licenciado sob a [GNU Affero General Public License v3.0 (AGPLv3)](./LICENSE).