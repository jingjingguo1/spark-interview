JingjingGuo-spark-interview
==============================

Spark Interview for Data Scientist Position at Deloitte HUX 2019

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── bash               <- vagrant virtual machine provision bash files      
    │   └── vagrant_spark_env.sh
    │
    ├── data
    │   ├── samples        <- Sample data provided by Deloitte.
    │   ├── assmbled       <- Assembled data from assembling 3 sample files.
    │   └── featurized     <- Encoded and scaled data.
    │
    ├── models             <- Trained models.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to assemble provided data files.
    │   │   ├── assemble_data.py
    │   │   └── Samples.py <- Sample class.
    │   │
    │   ├── features       <- Scripts to turn assembled data into features for modeling
    │   │   ├── featurize_data.py
    │   │   └── Features.py<- Features class
    │   │
    │   └── models         <- Scripts to train and save models
    │       └── model_fitting.py
    │
    └── vagrantfile        <- vagrantfile to spin up Centos 7 virtual machine and provision Spark and python environment.

Execution Instructions
------------
> ### Step 1 - Environment setup
>
>     make install
> ### Step 2 - Log in to CentOS 7
>     make ssh
>
> ### Step 3 - Navigate to sync folder
>     cd spark-model
>
> ### Step 4 - Assemble Data
>     make assemble
>
> ### Step 5 - Model Fitting
>     make classifier
>
> ### Step 6 - Exit and Cleanup
>     ctrl+D
>     make clean
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
