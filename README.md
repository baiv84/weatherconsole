# Description

`Weatherconsole` is the script tool to show weather conditions as a console output. 

    In this version only 3 cities - Cherepovets, Sheremetievo and London are used to be just example places to show program features. 


# Prerequisites

Firstly, you have to install package `python3-venv` to work with python virual environment.

Update packages on your system `!(it depends on your operating system)`

in this document I use Ubuntu as my operating system. So run update:
```console
$ sudo apt update
```

and run command:
```console
$ sudo apt install -y python3-venv
```

Then jump to project folder:
```console
$ cd weatherconsole
```

and create new python environment to run the code:
```console
$ python3 -m venv venv
```

Activate new virtual environment:
```console
$ source venv/bin/activate
```

As a result, you will see command line prompt like this:
```console
(venv) weatherconsole $ 
```

# Install dependencies

In the virtual environment run command:

```console
(venv) weatherconsole $  pip install -r requirements.txt
```

This command install `requests` library in `venv` virtual environment.

# Run program 

    (venv) weatherconsole $ python weather.py

# Control results

If program running successfully, you will see result like this:

![Alt text](img/london.png?raw=true "London")

![Alt text](img/sheremetievo.png?raw=true "Sheremetievo")

![Alt text](img/cherepovets.png?raw=true "Cherepovets")


# Final steps

Deactivate virtual environment:

```console
(venv) weatherconsole $ deactivate
```

Close console:
```console
$ exit
```

