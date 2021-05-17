<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/mateokingler/ez-a">
    <img src="https://raw.githubusercontent.com/mateokingler/ez-a/main/eza.ico" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center">EZ Accessibility</h3>

  <p align="center">
    EZ Accessibility helps course developers by compiling inaccessible<br />.pptx figures into a neat tabular .docx report.
    <br />
    <br />
    <a href="https://www.youtube.com/watch?v=jupwazddS4M"><strong>View Demo »</strong></a>
    <br />
    <a href="https://github.com/mateokingler/ez-a/issues">Report Bug</a>
    ·
    <a href="https://github.com/mateokingler/ez-a/issues">Request Feature</a>
  </p>
</p>



### Built With

* [Python 3.8](https://www.python.org/downloads/release/python-385/)
* [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html)



<!-- GETTING STARTED -->
## Quick Start

You can download the latest stable build for Windows [here](https://github.com/mateokingler/ez-a/releases).

## Development setup

Follow the instructions below to run EZ-A from source, on your own fork.

### Prerequisites
Use the Python package manager pip to install the prerequisites.
* python-pptx
  ```sh
  pip install python-pptx
  ```
* python-docx
  ```sh
  pip install python-docx
  ```
* pyinstaller
  ```sh
  pip install pyinstaller
  ```
* PyQt5
  ```sh
  pip install PyQt5
  ```

### Compiling

In the projects root directory, package the executable using the SPEC file
   ```sh
   pyinstaller ezagui.spec
   ```
