# AutoGluon Test Case on Titanic Dataset with Kaggle

This repo is designed to show the basic function of AutoGluon and Kaggle API for your Machine Learning and Data Science Practices with the Titanic dataset.

## Step 1: Create a new python development environment and install packages

```bash
conda create -n AutoGluon python=3.8 pip

# brew install libomp # MacOS user
pip install -U pip
pip install -U "mxnet<2.0.0"
pip install -U setuptools wheel
pip install autogluon

```

## Step 2: Register Kaggle and Install Kaggle API

To use the Kaggle API, sign up for a Kaggle account at https://www.kaggle.com.

Then go to the `Account` tab of your user profile (https://www.kaggle.com/<username>/account) and select `Create API Token`.

This will trigger the download of kaggle.json, a file containing your API credentials.

Place this file in the location `~/.kaggle/kaggle.json` (on Windows in the location `C:\Users\<Windows-username>\.kaggle\kaggle.json` - you can check the exact location, sans drive, with `echo %HOMEPATH%`).

You can define a shell environment variable `KAGGLE_CONFIG_DIR` to change this location to `$KAGGLE_CONFIG_DIR/kaggle.json` (on Windows it will be `%KAGGLE_CONFIG_DIR%\kaggle.json`).

For your security, ensure that other users of your computer do not have read access to your credentials. On Unix-based systems you can do this with the following command:

```bash
chmod 600 ~/.kaggle/kaggle.json
```

## 3. Download the data and Run the model

Download and unzip the data.

```bash
kaggle competitions download -c titanic
unzip -o titanic.zip
```

Run the model:

```bash
python run.py
```

You will generate the model and other files at the `model` folder.
File structure in the folder:

```bash
(AutoGluon) ➜  autogluon-casestudy git:(master) tree model
    model
    ├── learner.pkl
    ├── models
    │   ├── CatBoost
    │   │   └── model.pkl
    │   ├── ExtraTreesEntr
    │   │   └── model.pkl
    │   ├── ExtraTreesGini
    │   │   └── model.pkl
    │   ├── KNeighborsDist
    │   │   └── model.pkl
    │   ├── KNeighborsUnif
    │   │   └── model.pkl
    │   ├── LightGBM
    │   │   └── model.pkl
    │   ├── LightGBMLarge
    │   │   └── model.pkl
    │   ├── LightGBMXT
    │   │   └── model.pkl
    │   ├── NeuralNetFastAI
    │   │   ├── model-internals.pkl
    │   │   └── model.pkl
    │   ├── NeuralNetMXNet
    │   │   ├── model.pkl
    │   │   └── net.params
    │   ├── RandomForestEntr
    │   │   └── model.pkl
    │   ├── RandomForestGini
    │   │   └── model.pkl
    │   ├── WeightedEnsemble_L2
    │   │   ├── model.pkl
    │   │   └── utils
    │   │       ├── model_template.pkl
    │   │       └── oof.pkl
    │   ├── XGBoost
    │   │   └── model.pkl
    │   └── trainer.pkl
    ├── predictor.pkl
    └── utils
        └── data
            ├── X.pkl
            ├── X_val.pkl
            ├── y.pkl
            └── y_val.pkl

18 directories, 25 files
```

And also create the `submission.csv` for Kaggle.

```bash
(AutoGluon) ➜  autogluon-casestudy git:(master) tree -L 1
.
├── ReadMe.md
├── gender_submission.csv
├── model
├── run.py
├── submission.csv <------ This is the file to be submitted to Kaggel.
├── test.csv
├── titanic.zip
└── train.csv
```

You can submit your prediction by:

```bash
kaggle competitions submit -c titanic -f submission.csv -m "msg"
```

and then visit the Kaggle website to see your ranking: https://www.kaggle.com/c/titanic/leaderboard#score.

## Reference

1. [AutoGluon: AutoML for Text, Image, and Tabular Data](https://auto.gluon.ai/stable/index.html)

2. [AWS Lab AutoGluon](https://github.com/awslabs/autogluon)

3. [动手学深度学习](https://zh-v2.d2l.ai/index.html)

4. [Dive into Deep Learning](https://d2l.ai/)

5. [Kaggle](https://www.kaggle.com/)

6. [Kaggle Python API](https://github.com/Kaggle/kaggle-api)
