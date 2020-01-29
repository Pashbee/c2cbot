# c2cbot

Train stats for you. Work in Progress project to collect stats using the Real Time Trains API and then output to CSV for future analytic work.

## Pre-requisites

- Python >= 3.5.x
- Pip3

## Install

Easy as:-

```
git clone https://github.com/Pashbee/c2cbot.git 
make setup
```
&& then:-

```
c2cbot --help
Usage: c2cbot [OPTIONS] COMMAND [ARGS]...

  c2cbot_cli - cli tool to search and print stats.

Options:
  --version               Show the version and exit.
  --rttapi-username TEXT
  --rttapi-password TEXT
  --rttapi-url TEXT
  --help                  Show this message and exit.

Commands:
  service  Search sub-command to run a service search.

```

## Maturity

Not stable, Under heavy development.

## Develop and Contribute

To install in develop mode:-

```
git clone https://github.com/Pashbee/c2cbot.git 
cd c2cbot/
make setup-dev
```

To contribute please follow these pointers:-

* Create an issue describing the feature/bug you would like to work on.
* Clone the repository via git: `git clone https://github.com/Pashbee/c2cbot.git`
* Make your changes, ensure `make test` passes, commit and push your changes in a new branch.
* Create a pull request referencing your created issue.

Note: Please ensure you follow [these git commit conventions.](https://www.conventionalcommits.org/en/v1.0.0-beta.2/)