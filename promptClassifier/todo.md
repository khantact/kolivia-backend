ask how to train a pretrained model
Traceback (most recent call last):
File "/Users/Kkhhh/Documents/College/Junior/Sem1/NLP/kolivia-backend/bert.py", line 164, in <module>
results = task*evaluator.compute(
^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/homebrew/lib/python3.11/site-packages/evaluate/evaluator/text_classification.py", line 148, in compute
metric_results = self.compute_metric(
^^^^^^^^^^^^^^^^^^^^
File "/opt/homebrew/lib/python3.11/site-packages/evaluate/evaluator/base.py", line 527, in compute_metric
result = metric.compute(**metric_inputs, **self.METRIC_KWARGS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/homebrew/lib/python3.11/site-packages/evaluate/module.py", line 974, in compute
results.append(evaluation_module.compute(**batch))
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/homebrew/lib/python3.11/site-packages/evaluate/module.py", line 462, in compute
output = self.\_compute(**inputs, **compute_kwargs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Users/Kkhhh/.cache/huggingface/modules/evaluate_modules/metrics/evaluate-metric--recall/e40e6e98d18ff3f210f4d0b26fa721bfaa80704b1fdf890fa551cfabf94fc185/recall.py", line 126, in \_compute
score = recall_score(
^^^^^^^^^^^^^
File "/opt/homebrew/lib/python3.11/site-packages/sklearn/utils/\_param_validation.py", line 214, in wrapper
return func(\*args, **kwargs)
^^^^^^^^^^^^^^^^^^^^^
File "/opt/homebrew/lib/python3.11/site-packages/sklearn/metrics/\_classification.py", line 2304, in recall_score
*, r, _, _ = precision_recall_fscore_support(
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/homebrew/lib/python3.11/site-packages/sklearn/utils/\_param_validation.py", line 187, in wrapper
return func(\*args, \*\*kwargs)
^^^^^^^^^^^^^^^^^^^^^
File "/opt/homebrew/lib/python3.11/site-packages/sklearn/metrics/\_classification.py", line 1724, in precision_recall_fscore_support
labels = \_check_set_wise_labels(y_true, y_pred, average, labels, pos_label)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/homebrew/lib/python3.11/site-packages/sklearn/metrics/\_classification.py", line 1518, in \_check_set_wise_labels
raise ValueError(
ValueError: Target is multiclass but average='binary'. Please choose another average setting, one of [None, 'micro', 'macro', 'weighted'].

What is this error ^ @evaluate
