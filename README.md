# israel-theory-dataset-parser
Script that parses the Israel theory (Te`oria) data set into a json file that's easy to work with

## Setup
```
pip install -r requirements.txt
```

## Execution
### From the project's root directory:
```
python parse.py
```

## Results
You should see a new file named `questions.json` that contains a list of questions with the following structure:
```
{
    "question": "Question title(?)",
    "answers": [
      {
        "answer": "Answer 1",
        "correct": false
      },
      {
        "answer": "Answer 2",
        "correct": false
      },
      {
        "answer": "Answer 3",
        "correct": false
      },
      {
        "answer": "Answer 4",
        "correct": true
      }
    ],
    "extra_content": [
      "<img src=\"http://tqpic.mot.gov.il/<some_photo_id>.jpg\" style=\"width: 100%; padding: 0pt; border: 0pt none; outline: 0pt none;\" alt=\"<some_photo_id>\" title=\"<some_photo_id>\" />"
    ]
  }
```

## Notes
`extra_content` can be empty if the question doesn't have any photos in it.

`answers` will always have the 3 wrong answers at first and the correct one in the end.

If you wish to shuffle them, you'll have to do it yourself.

The url in `parse.py` for the data set may not be up to date.

Get the latest dataset from: https://data.gov.il/dataset/tqhe (XML file)
