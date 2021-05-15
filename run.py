from autogluon.tabular import TabularDataset, TabularPredictor
# Train
train_data = TabularDataset('train.csv')
id, label = 'PassengerId', 'Survived'
save_path = 'model'
predictor = TabularPredictor(label=label,
                             path=save_path).fit(train_data.drop(columns=[id]))
# Test
import pandas as pd

test_data = TabularDataset('test.csv')

predictor = TabularPredictor.load(
    save_path
)  # unnecessary, just demonstrates how to load previously-trained predictor from file

preds = predictor.predict(test_data.drop(columns=[id]))
submission = pd.DataFrame({id: test_data[id], label: preds})
submission.to_csv('submission.csv', index=False)