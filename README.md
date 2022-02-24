[![CI](https://github.com/ekimdev/hangman-multiplayer-game/actions/workflows/github-ci.yml/badge.svg)](https://github.com/ekimdev/hangman-multiplayer-game/actions/workflows/github-ci.yml)
![black](https://img.shields.io/badge/code%20style-black-black)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

<br />
<div align="center">
  <a href="https://gitlab.com/rodrigoacosta444/hangman-multiplayer-game">
  </a>
  <h3 align="center">Hangman Multiplayer Game</h3>
  <p align="center">
    <br />
    <a href="https://github.com/centaurialpha/hangman-multiplayer-game/edit/readme/README.md#installation"><strong>Getting started »</strong></a>
    <br />
    ·
    <a href="https://gitlab.com/rodrigoacosta444/hangman-multiplayer-game/issues">Report Bug</a>
    ·
    <a href="https://gitlab.com/rodrigoacosta444/hangman-multiplayer-game/issues">Request Feature</a>
  </p>
</div>

A simple hangman game built with Python 🐍

**HMG** is my first project I do in Python using sockets, so if you find some error I would appreciate if you let me know through issues tracker.

### Demo

![hmg-demo](https://user-images.githubusercontent.com/5894606/161370923-3c08ddf4-df0f-43bf-9c2a-f9a656399307.gif)

### Installation

```
$ pip install hmg
```

This installs two execuables. The `hmg-server` and the `hmg-client`. You can check the cli help for more options:

```
$ hmg-server --help
usage: hmg-server [-h] [-H HOST] [-p PORT] [-w WORD]

options:
  -h, --help            show this help message and exit
  -H HOST, --host HOST
  -p PORT, --port PORT
  -w WORD, --word WORD  Word to use instead of internet (usefull for testing)

$ hmg-client --help
usage: hmg-client [-h] [-H HOST] [-p PORT] [-c BOARD_CHAR]

options:
  -h, --help            show this help message and exit
  -H HOST, --host HOST
  -p PORT, --port PORT
  -c BOARD_CHAR, --board-char BOARD_CHAR
                        Char used for fill board
```

### Running
First run server. Also you can run server on another host, for example in my Raspberry Pi:

```
$ hmg-server --host 0.0.0.0
```

Now start the players in different terminals or computers:

For server executed without `--host` argument, just:
```
$ hmg-client
```

For server executed with `--host` argument:
```
$ hmg-client --host 192.168.1.15
```

The `192.168.1.15` is the RPi IP.

Enjoy 🎮 🎉 !

## Developers
Run `pip install -e ".[dev]"` to install all dependencies used by the development environment.

Check the `make` command for useful tasks such as tests and lint.

```
$ make
flake8           Execute flake8
tests            Execute unit tests
format           Execute black formater
format-check     Execute black formater without modify files
```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [rich](https://github.com/Textualize/rich): an awesome Python library for text and formatting in the terminal ❤️.
* [API Palabras Aleatorias](https://palabras-aleatorias-public-api.herokuapp.com/): for the words used in game 🙂.
