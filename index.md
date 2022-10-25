<title>Project Portfolio</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

/* Create two equal columns that floats next to each other */
.column {
  float: left;
  width: 50%;
  padding: 0px 15px 0px 0px;
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
<div id="cis731project">
<h2>Satellite Image Feature Extraction & Classification Using PySpark</h2>
Term Project for CIS 731: Programming Techniques for Data Science and Analytics
<br><br>
<div class="row">
<p align="center">
    <a href="pdf/cis731_paper.pdf">Paper</a> | <a href="pdf/cis731_presentation.pdf">Presentation Slides</a> | <a href="/code/cis731">Python Code</a>
    </p>  
  </div>   
<div class="row">
  <div class="column">
    <ul style="list-style-position: outside; padding-left: 15px">
    <li>Entirely using the Apache Spark/PySpark distributed computing framework in Python, evaluated methods of feature extraction and compared performance of classification algorithms with a gigabyte-scale data set of 500,000 labeled satellite images, with the goal of developing a model to accurately predict land classes (forested, grassland, barren, other)</li>
     <br>
    <li>Utilized a weighted F1 score (the harmonic mean of precision and recall) for evaluation, which helped to account for class imbalance in the model training data</li>
    <br>
    <li>To validate evaluation results, created a custom implementation within PySpark of 10-fold cross validation with a paired t-test</li>
    <br>
    <li>Joined original image data with the transformed image data and classification results and exported for visualization with Matplotlib</li>
    <br>
    <li>Deployed a Spark cluster on Amazon Web Services EMR to test real-world functionality and evaluate the processing time reduction from applied distributed computing; utilized a Google Cloud Platform virtual machine with a 16-core vCPU and 64 GB RAM for development and evaluation (to save on costs of running a real Spark cluster)</li>
    <br>
      <li><b>Result</b>: Improved weighted-F1 score from baseline of 81% to 93% by transforming images into a greyscale histogram and utilizing the logistic regression classifier algorithm</li>
    <br>
    <li>Technologies used:  <code>PySpark, Python, MLlib, OpenCV, Numpy, AWS EMR, GCP</code></li>
    </ul>
  </div>
  <div class="column">
    <p align="center">
    <img src="images/3_pyspark_classification_project.png?raw=true" width="350"/>
    </p>
  </div>
</div>
</div>
---
<div id="cis730project">
<h2>Training a Proximal Policy Optimization (PPO) Deep Reinforcement Learning Model to Play Mario Bros</h2>

Term Project for CIS 730: Principles of Artificial Intelligence
<br>
<div class="row">
<p align="center">
    <a href="pdf/cis730_paper.pdf">Paper</a> | <a href="pdf/cis730_presentation.pdf">Presentation Slides</a> | <a href="/code/cis730">Python Code</a>
    </p>
  </div>
<div class="row">
  <div class="column">
    <ul style="list-style-position: outside; padding-left: 15px">
    <li>Trained a deep reinforcement learning model to play the game Mario Bros, using OpenAI's Gym framework in Python, and evaluated methods of improving the trained Proximal Policy Optimization (PPO) model with modifications to the state-space, the action-space, and the reward function</li>
    <br>
    <li>Developed and trained utilizing a Google Cloud Platform virtual machine with a 8-core vCPU and a Tesla T4 GPU</li>
    <br>
    <li><b>Result</b>: Developed a model that was able to efficiently complete the first level of Mario Bros after training to 20m timesteps</li>
    <br>
    <li>Technologies used:  <code>Python, OpenAI Gym Retro, OpenAI Baselines, TensorFlow, GCP</code></li>
    </ul>
  </div>
  <div class="column">
    <p align="center">
    <img src="images/4_reinforcement_learning_project.gif?raw=true" width="350"/>
    </p>
  </div>
</div>
</div>
---
<div id="cis732project">
<h2>Comparison of Deep Learning Text Generation Models Trained with Song Lyrics</h2>

Term Project for CIS 732: Machine Learning and Pattern Recognition
<br><br>
<div class="row">
 <p align="center">
    <a href="pdf/cis732_paper.pdf">Paper</a> | <a href="pdf/cis732_presentation.pdf">Presentation Slides</a> | <a href="/code/cis732">Python Code</a>
    </p>
  </div>
<div class="row">
  <div class="column">
    <ul style="list-style-position: outside; padding-left: 15px">
    <li>Trained unconditional text generation language models from a text corpus of song lyrics, utilizing recurrent neural networks (RNNs) and generative adversarial networks (GANs) in Python with the PyTorch deep learning framework, and evaluated text output by utilizing a combination of human scoring and a computed bilingual evaluation understudy (BLEU) score</li>
    <br>
    <li>Developed and evaluated utilizing a free Google Colab instance with a GPU</li>
    <br>
    <li><b>Result</b>: the trained SeqGAN model was evaluated the highest; however, the overall text generation seemed to generally lack quality and coherence compared to genuine song lyrics, indicating that significant future work could be undertaken to improve model output</li>
    <br>
    <li>Technologies used:  <code>PyTorch, Python, TextBox module (GAN algorithms)</code></li>
    </ul>
  </div>
  <div class="column">
    <p align="center">
    <img src="images/6_deep_text_generation_project.png?raw=true" width="350"/>
    </p>
  </div>
</div>
</div>                                                                     
---
<div id="stat705project">
<h2>Statistical Analysis of Home Pricing with Linear Modeling in R</h2>

Term Project for STAT 705: Regression and Analysis of Variance
<br><br>
<div class="row")
 <p align="center">
    <a href="pdf/stat705_paper.pdf">Paper</a> | <a href="pdf/stat705_presentation.pdf">Presentation Slides</a> | <a href="/code/stat705/stat705_code.html">R Code</a>
    </p>
</div>  
<div class="row">
  <div class="column">
    <ul style="list-style-position: outside; padding-left: 15px">
    <li>Created a linear model in R to conduct statistical analysis of home pricing in Kansas City, MO, and evaluated the linear model compared to a more-complex generalized additive model (GAM) for predictive performance</li>
    <br>
    <li><b>Result</b>: the simple linear model outperformed for short and medium-term price predictions (≤28 months), and the GAM performed better for longer-term price predictions (>28 months and ≤36 months)</li>
    <br>
    <li>Technologies used:  <code>R, ggplot2</code></li>
    </ul>
  </div>
  <div class="column">
    <p align="center">
    <img src="images/8_statistics_linear_model_project.png?raw=true" width="350"/>
    </p>
  </div>
</div>
</div>
---
<div id="genba890project">
<h2>Business Capstone Data Visualization Project</h2>

Term Project for GENBA 890: Business Capstone
<br><br>
<div class="row">
 <p align="center">
    <a href="pdf/genba890_presentation.pdf">Presentation Slides</a>
    </p>
  </div> 
<div class="row">
  <div class="column">
    <ul style="list-style-position: outside; padding-left: 15px">
    <li>Coordinated student team in consulting with a client company to provide research findings into data visualization methods, and developed visualization dashboard implementations that provide greater insight into the status of their nationwide supply chain, utilizing both Python and PowerBI</li>
    <br>
    <li>I can't share the deliverables due to confidential data used in this project; however, the presentation slides linked below are a summary that was presented at the K-State College of Business Graduate School Advisory Council Meeting on May 4th, 2022, which includes randomized data used in the examples of recommended visualizations</li>
    <br>
    <li>Technologies used:  <code>Python, Plotly, PowerBI</code></li>
    </ul>
  </div>
  <div class="column">
    <p align="center">
    <img src="images/7_capstone_visualization_project.png?raw=true" width="350"/>
    </p>
  </div>
</div>
</div>
---
<div id="mis670project">
<h2>Web Scraping News & Twitter Sentiment Analysis of Bitcoin</h2>

Term Project for MIS 670: Social Media Analytics and Web Mining
<br><br>
<div class="row">
<p align="center">
    <a href="https://github.com/zstrathe/zstrathe.github.io/blob/master/code/mis670/mis670_notebook.ipynb">Python Notebook</a>
    </p>
  </div>
<div class="row">
  <div class="column">
    <ul style="list-style-position: outside; padding-left: 15px">
    <li>Utilized web scraping with Python to collect news articles and historical price information about Bitcoin, and performed sentiment analysis on news articles to calculate the average aggregate sentiment per year to compare with annual Bitcoin price changes. Also utilized the Twitter API to collect and process tweets about Bitcoin to perform further sentiment analysis and network analytics</li>
    <br>
    <li><b>Result</b>: by comparing graphs of the annual Bitcoin price changes and the annual aggregate news sentiment about Bitcoin, there appeared to be some correlation between the two, though with sentiment lagging behind price changes by about a year</li>
    <br>
    <li>Technologies used:  <code>Python, Natural Language Toolkit (NLTK), Pandas, Matplotlib</code></li>
    </ul>
  </div>
  <div class="column">
    <p align="center">
    <img src="images/1_bitcoin_webscraping_sentiment_analysis_project.png?raw=true" width="350"/> 
    </p>
  </div>
</div>
</div>
---
<div id="mangt830project">
<h2>Real Estate Data Visualization with Tableau</h2>

Term Project for MANGT 830: Information Technology Strategy and Application
<br><br>
<div class="row">
<p align="center">
    <a href="pdf/mangt830_paper.pdf">Paper</a>
    </p>
  </div> 
<div class="row">
  <div class="column">
    <ul style="list-style-position: outside; padding-left: 15px">
    <li>Analyzed residential real estate in Seattle, WA with a combination of visualizations developed in Tableau, utilizing a data set containing property prices and additional feature details for 21,000 properties</li>
    <br>
    <li>Technologies used:  <code>Tableau</code></li>
    </ul> 
  </div>
  <div class="column">
    <p align="center">
    <img src="images/5_data_visualiztion_project.png?raw=true" width="350"/>
    </p>
  </div>
</div>
</div>
---
<p style="font-size:11px">Page template forked from <a href="https://github.com/evanca/quick-portfolio">evanca</a></p>
<!-- Remove above link if you don't want to attibute -->
