Python code for scraping lyrics from web:
	[Python Notebook](/Data Collection Code/WebScraping_SongLyrics.ipynb)

Python Language Model Training Code:
	- Baseline RNN:
		- [Python Notebook](/Model Training Code/Baseline_RNN.ipynb)
	
	- RNN with tuned hyperparameters:
		- [Python Notebook](/Model Training Code/RNN.ipynb)
	
	- GAN Models (using TextBox library)
	  Trained SeqGAN, TextGAN, and LeakGAN
          'Model Training Code/Modified TextBox files' folder contains 
	  files from the TextBox library that were modified:
		- [Python Notebook](/Model Training Code/GANs_with_Textbox_lib.ipynb)

Python evaluation code:
	- Calculate BLEU scores for generated text:
		-Text Sampling and Evaluation Code/bleu_evaluation.ipynb
	- Randomly sample generated text and save 10 examples from each model
	  to a .csv file 
          & calculate human evaluation score by displaying 
          a random selection from sampled text and prompting for score, 
          then calculates the average for each model:
		- Text Sampling and Evaluation Code/select_and_evaluate.py
	 

