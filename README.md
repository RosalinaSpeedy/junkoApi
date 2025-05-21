This is the Flask API portion of the of the S.E.E.K application to communicate with the Junko AI model that's trained on a custom dataset; but is rather a tuned version of the Llama 2-7b open source model from Meta. The bulk of the application code can be found here:

https://github.com/RosalinaSpeedy/S.E.E.K

This Flask API is run via Google Colab on the A100 GPU with high RAM - and is authenticated via HuggingFace - this is because the React Native framework used for S.E.E.K's development cannot run or communicate with the AI model directly.
The ipynb files in this repository document the training and exporting process underwent to allow Junko to be loaded in by the Flask API code.

The model was tuned using a JSON file of question/answer pairs where the addiction name, triggers and severity are used as the question and the answer is the same as the question but extended with warning signs and coping strategies for the given addiction type.

![image](https://github.com/user-attachments/assets/feb77f19-0609-42a1-8793-a2a6fe1dcbe5) ![image](https://github.com/user-attachments/assets/a961fd48-d429-4dd0-af54-f7aceb1c76d4)


The quiz within the S.E.E.K application formats the input data into a string that acts as a prompt

The code focuses on the below route:

/submit-prompt/:prompt where the prompt is the given input for the quiz - and the prompt is then fed into the loaded model, and the output returned as a JSON object.

Known issues:

o	Issue: the most egregious bug in the system – you can put empty values in the quiz when making a call to the Junko API – this causes null values to be saved in the plan – thus breaking the route to the plan page and crashing the app.

  >	Potential fix: ensure that empty values cannot be submitted on the quiz page using similar checks to the journal and forum.
  
o	The model has a clear bias - and tends to repeat itself. 

  >	Potential fix: reduction of overfitting - regularise the dataset and add more, varied data - as the tuning was performed on an albeit augmented - but limited dataset.
  
