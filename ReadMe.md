# AutoGluon Test Case on Titanic Dataset

This repo is designed to show the basic function of AutoGluon and Kaggle for your Machine Learning and Data Science Practices.

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

You will genearate the model and other files at the `model` folder.

And also create the `submission.csv` for Kaggle.

You can submit your prediction by:

```bash
kaggle competitions submit -c titanic -f submission.csv -m "msg"
```

and visit the Kaggle website to see your ranking: https://www.kaggle.com/c/titanic/leaderboard#score.

## Reference

1. [AutoGluon: AutoML for Text, Image, and Tabular Data](https://auto.gluon.ai/stable/index.html)

2. [AWS Lab AutoGluon](https://github.com/awslabs/autogluon)

3. [动手学深度学习](https://zh-v2.d2l.ai/index.html)

4. [Dive into Deep Learning](https://d2l.ai/)

5. [Kaggle](https://www.kaggle.com/)

6. [Kaggle Python API](https://github.com/Kaggle/kaggle-api)
