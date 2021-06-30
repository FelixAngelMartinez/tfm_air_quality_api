# tfm_air_quality_api
Project API REST

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Pandas)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/FelixAngelMartinez/tfm_air_quality_api)
![GitHub last commit](https://img.shields.io/github/last-commit/FelixAngelMartinez/tfm_air_quality_api)
![GitHub all releases](https://img.shields.io/github/downloads/FelixAngelMartinez/test_1/tfm_air_quality_api)
![GitHub issues](https://img.shields.io/github/issues-raw/FelixAngelMartinez/tfm_air_quality_api)
![GitHub contributors](https://img.shields.io/github/contributors/FelixAngelMartinez/tfm_air_quality_api)
![GitHub followers](https://img.shields.io/github/followers/FelixAngelMartinez?style=social)

## Description
Repository belonging to the development of the Master Thesis entitled "Intelligent system for monitoring indoor air quality and fight against COVID-19", which develops a system to monitor air quality in enclosed spaces using IoT devices and Machine Learning algorithms. All this developed with a Cloud approach.

This Master's Thesis has been developed within the framework of the "Master in Computer Engineering" of the University of Castilla la Mancha.

## Repository elements
In this respository there is 1 directory:
* **app/**: python code that contains the REST API coded with the FAST API library

## Requirements
This repository has the code ready to deploy as a container and inside of it a requirements.txt file to automatically install it.

## Commands
There are a few command that are importat to manage a container:
```console
  $docker build -t api:v1 .
  $docker run -d --name api_container -p 80:80 api:v1
  docker logs -f api_container
  docker exec -it api_container bash
```
### Exit
```console
  Control + p + q
```
## Master's thesis
The report of the project will be published in the university repository.
[UCLM Repository](https://ruidera.uclm.es/)

## License:
Project under license [LICENSE](LICENSE)

---
_Project carried out by:_
* **Félix Ángel Martínez Muela** - [Félix Ángel Martínez](https://github.com/FelixAngelMartinez)