#### Python code for scraping lyrics from web: 
- <a href="/Data Collection Code/WebScraping_SongLyrics.ipynb">Python Notebook</a>


#### Python Language Model Training Code:
- Baseline RNN: <a href="/Model Training Code/Baseline_RNN.ipynb">Python Notebook</a>
	
- RNN with tuned hyperparameters: <a href="/Model Training Code/RNN.ipynb">Python Notebook</a>
	
- GAN Models (using TextBox library): <a href="/Model Training Code/GANs_with_Textbox_lib.ipynb">Python Notebook</a>
 	
	- 'Model Training Code/Modified TextBox files' folder (<a href="https://github.com/zstrathe/zstrathe.github.io/tree/master/code/cis732/Python%20Code/Model%20Training%20Code/Modified%20TextBox%20files)">link</a>) contains files from the TextBox library that were modified for training the SeqGAN, TextGAN, and LeakGAN models: 


#### Python evaluation code:
- Calculate BLEU scores for generated text: <a href="/Text Sampling and Evaluation Code/bleu_evaluation.ipynb">Python Notebook</a>

- Random sample and calculate human score: <a href="/Text Sampling and Evaluation Code/select_and_evaluate.ipynb">Python Notebook</a>
	- Randomly sample generated text and save 10 examples from each model to a .csv file & calculate human evaluation score by displaying a random selection from sampled text and prompting for score, then calculates the average for each model:
	 

