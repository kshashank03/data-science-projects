# Overview
This project is an expansion to a neural network I built to differentiate cats and dogs from one another. My girlfriend has a rabbit so I decided to take a whack at training a neural network to recognize rabbits as well. 

# Process

### Data Cleaning
Through a course in Data Science by the team at SUper Data Science, I already had access to 5000 images of cats and dogs each. The first challenge was finding images of rabbits to train my network on. I had only found out about the Google Open Images API after I had gathered my images otherwise I would have used that. Not knowing better I set out to scrape the images off of Google Images. Modifying a script I found to scrape Google Images using Selenium and Chrome, i was able to pull all 5000 images I needed. For more details click here: https://github.com/kshashank03/data-science-projects/blob/master/neural_networks/dog_cat_rabbit_classifier/rabbit_image_scraper.ipynb 

### Data Modeling
The original goal was to use Google Colab to leverage their GPUs/TPUs to train my neural network. Unfortunately I was not able to get this to work and resorted to using my personal laptop to train the model. After 4 major iterations I settled on a model with: 
* Three hidden layers, 32 -> 64 -> 128 filters, ReLU activation, Dropout 0.25 on the last hidden layer. 
* One fully connected output layer, Stochastic Gradient Descent optimizer, categorical crossentropy loss, accuracy metric.

### Evaluation
The model took about 24 hours to train over 50 epochs and had:
* Overall accuracy 0.9394
* Overall loss 0.1643
* Validation accuracy 0.7940
* Validation loss 0.6860

Anecdotally, the would accurately classify my friend's pets provided I cropped out any backgrounds. 

Two improvements I could see myself adding to this project would be to train it to automatically recognize and cut out backgrounds, and train it for longer to see if we could achieve a better validation accuracy. It hadn't converged by the 50th epoch but I couldn't wait another 24 hours to see if it performed any better. 


https://www.superdatascience.com/pages/deep-learning
