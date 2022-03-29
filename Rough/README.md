
# Rules

1. Code for steering the leg
2. Follow PEP (can ignore E501 warning). You can take help of the Flake8 Python Library to do this. Command: ```flake8 leg.py --ignore=E501```
3. Use a lot of comments to explain your code.
4. Every function and method should start with a docstring.

# Note

1. Read the help.ipynb file to understand how to:
   a. write and use docstrings
   b. use PyFirmata (Please use only those functions of the module for read and write to keep it uniform)

# Convensions

1. {Aritra} For the steering motors, positive rotation is anticlockwise and negative rotation is clockwise. So, we define the terminals of the motor positive and negative according to that. **i.e.:** if we keep the positive terminal at higher potensial and negative terminal at lower potenial, then the motor will rotate in anticlockwise direction. If we keep the negative terminal at higher potenial and positive terminal at lower potenial, then the motor will rotate in clockwise direction. All these are done keeping the terminal side of the motor upwards and the shaft side downwards.

2. {Mahesh} Define more convensions here if you need, for example the naming of the variables for the pins in Step 2.
    Pin convention format: (<Component>_<Row>_<Column>_<Sign>). Note that potentiometer labels have only 3 parts as <Sign> is not required. 
        Abbreviations:
            Component:  sm-steering motor, dm-driving motor, pr-potentiometer
            Row:        f-Front, m-middle , b-back
            Column:     l-left, r-right
            Sign:       p-positive (plus), n-negative (minus)    
    Eg: sm_f_l_p stands for steering motor front left positive
        pr_f_r stands for potentiometer front right

# Roles

* ```settings.py``` - **Mahesh** (You need to complete this before others can start their parts)
* ```motors.py``` - **Girija**
* ```rover.py``` - **Samyak** + **Mahesh** (As Mahesh has completed the ```settings.py``` he is free to help Samyak on this)
* ```main.py``` - **Suman**

# GitHub steps

* You can fork the project and start working on it, create a pull request when think your changes are ready to be mreged.
* Fork the repository
* Work on your individual parts as mentioned in Roles.
* Because you are working on the same file, @Samyak will fork my repository and @Mahesh will fork the Samyaks repository to collaborate efficiently.
* Finally you will raise **pull requests** once your parts are done.
* @Girija, @Samyak, and @Suman you won't fork the repo straight away. Fork it only after @Mahesh completed the ```settings.py``` file. This way it would be easier.