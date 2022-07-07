<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

/* Create two equal columns that floats next to each other */
.column {
  float: left;
  width: 50%;
  padding: 10px;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Responsive layout - makes the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 600px) {
  .column {
    width: 100%;
  }
}
</style>

# Project Portfolio
---

<h2>Satellite Image Feature Selection & Classification Using PySpark</h2>

Term Project for CIS 731: Programming Techniques for Data Science and Analytics

* Entirely using the Apache PySpark distributed computing framework in Python, evaluated methods of feature selection and compared performance of classification algorithms with a data set of 500,000 labeled satellite images, and implemented 10-fold cross validation with a paired t-test to validate evaluation results

* Deployed a Spark cluster on Amazon Web Services Elastic MapReduce to test functionality; utilized a Google Cloud Platform virtual machine with a 16-core vCPU and 64 GB RAM for development and evaluation (to save on costs of running a real Spark cluster)

* Technologies used:  ```PySpark, Python, MLlib, OpenCV, Numpy, AWS EMR, GCP```

<a href="pdf/cis731_paper.pdf">Paper</a>
<br>
<a href="pdf/cis731_presentation.pdf">Presentation</a>
<br>
[Python Code](/code/cis731)

<p align="center">
    <img src="images/3_pyspark_classification_project.png?raw=true" width="350"/>
</p>

---

<h2>Training a Proximal Policy Optimization (PPO) Reinforcement Learning Model to Play Mario Bros</h2>

Term Project for CIS 730: Principles of Artificial Intelligence

* Trained a deep reinforcement learning model to play the game Mario Bros, using OpenAI's Gym framework in Python, and evaluated methods of improving the trained Proximal Policy Optimization (PPO) model with modifications to the state-space, the action-space, and the reward function

* Developed and trained utilizing a Google Cloud Platform virtual machine with a 8-core vCPU and a Tesla T4 GPU

* Technologies used:  ```Python, OpenAI Gym Retro, OpenAI Baselines, TensorFlow, GCP```

<a href="pdf/cis730_paper.pdf">Paper</a>
<br>
<a href="pdf/cis730_presentation.pdf">Presentation</a>
<br>
[Python Code](/code/cis730)

<p align="center">
  <img src="images/4_reinforcement_learning_project.gif?raw=true" width="350"/>
</p>

---

<h2>Comparison of Deep Learning Text Generation Models Trained with Song Lyrics</h2>

Term Project for CIS 732: Machine Learning and Pattern Recognition

* Trained unconditional text generation language models from a text corpus of song lyrics, utilizing recurrent neural networks (RNNs) and generative adversarial networks (GANs) in Python with the PyTorch deep learning framework, and evaluated text output by utilizing a combination of human scoring and a computed bilingual evaluation understudy (BLEU) score

* Developed and evaluated utilizing a free Google Colab instance with a GPU

* Technologies used: ```PyTorch, Python, TextBox module (GAN algorithms)```

<a href="pdf/cis732_paper.pdf">Paper</a>
<br>
<a href="pdf/cis732_presentation.pdf">Presentation</a>
<br>
[Python Code](/code/cis732)

<p align="center">
  <img src="images/6_deep_text_generation_project.png?raw=true" width="350"/>
</p>                                                                          

---

<h2>Statistical Analysis of Home Pricing with Linear Modeling in R</h2>

Term Project for STAT 705: Regression and Analysis of Variance

<div class="row">
  <div class="column">
    <ul style="margin-left: -10px">
    <li>
    Created a linear model in R to conduct statistical analysis of home pricing in Kansas City, MO, and evaluated the linear model compared to a more-complex generalized additive model (GAM) for predictive performance
    </li>
    <li>
    Technologies used:  <code>R, ggplot2</code>
    </li>
    <a href="pdf/stat705_paper.pdf">Paper</a>
    <br>
    <a href="pdf/stat705_presentation.pdf">Presentation</a>
    <br>
    <a href="/code/stat705/stat705_code.html">R Code</a>
  </div>
  <div class="column">
    <p align="center">
    <img src="images/8_statistics_linear_model_project.png?raw=true" width="350"/>
    </p>
  </div>
</div>

---

<h2>Business Capstone Data Visualization Project</h2>

Term Project for GENBA 890: Business Capstone

<div class="row">
  <div class="column">
    <ul style="margin-left: -10px">
    <li>Coordinated student team in consulting with a client company to provide research findings into data visualization methods, and developed visualization dashboard implementations that provide greater insight into the status of their nationwide supply chain, utilizing both Python and PowerBI</li>
    <br>
    <li>I can't share the deliverables due to confidential data used in this project; however, the presentation linked below is a summary that was presented at the K-State College of Business Graduate School Advisory Council Meeting on May 4th, 2022, which includes randomized data used in the examples of recommended visualizations</li>
    <br>
    <li>Technologies used:  <code>Python, Plotly, PowerBI</code></li>
    <br>
    <li><a href="pdf/genba890_presentation.pdf">Presentation</a></li>
    </ul>
  </div>
  <div class="column">
    <p align="center">
    <img src="images/7_capstone_visualization_project.png?raw=true" width="350"/>
    </p>
  </div>
</div>

---

<h2>Web Scraping News & Twitter Sentiment Analysis of Bitcoin</h2>

Term Project for MIS 670: Social Media Analytics and Web Mining

<div class="row">
  <div class="column">
    <ul style="margin-left: -10px">
    <li>Utilized web scraping with Python to collect news articles and historical price information about Bitcoin, and performed sentiment analysis on news articles to calculate the average aggregate sentiment per year to compare with annual Bitcoin price changes. Also utilized the Twitter API to collect and process tweets about Bitcoin to perform further sentiment analysis and network analytics</li>
    <br>
    <li>Technologies used:  <code>Python, Natural Language Toolkit (NLTK), Pandas, Matplotlib</code></li>
    <br>
    <li><a href="https://github.com/zstrathe/zstrathe.github.io/blob/master/code/mis670/mis670_notebook.ipynb">Python Notebook</a></li>
    </ul>
  </div>
  <div class="column">
    <p align="center">
    <img src="images/1_bitcoin_webscraping_sentiment_analysis_project.png?raw=true" width="350"/> 
    </p>
  </div>
</div>

---

<h2>Real Estate Data Visualization with Tableau</h2>

Term Project for MANGT 830: Information Technology Strategy and Application

<div class="row">
  <div class="column">
    <ul style="margin-left: -10px">
    <li>Analyzed residential real estate in Seattle, WA with a combination of visualizations developed in Tableau, utilizing a data set containing property prices and additional feature details for 21,000 properties</li>
    <br>
    <li>Technologies used:  <code>Tableau</code></li>
    <br>
    <li><a href="pdf/mangt830_paper.pdf">Paper</a></li>
    </ul>
  </div>
  <div class="column">
    <p align="center">
    <img src="images/5_data_visualiztion_project.png?raw=true" width="350"/>
    </p>
  </div>
</div>

---
<p style="font-size:11px">Page template forked from <a href="https://github.com/evanca/quick-portfolio">evanca</a></p>
<!-- Remove above link if you don't want to attibute -->
