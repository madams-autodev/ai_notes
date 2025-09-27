# PyTorch

Think of PyTorch like a set of building blocks (like Lego).

* It gives you raw tools (bricks, wheels, doors).
* You can use them to build anything: cars, castles, spaceships.
* But you need skill and time to design and build your structure.

In AI terms:

* PyTorch lets you build neural networks from scratch.
* Super flexible → great for researchers, custom models, and experiments.
* Key feature: dynamic computation graph = you can change your “Lego structure” mid-build without breaking everything.



# Hugging Face

Now, think of Hugging Face like a Lego shop where people share their pre-built Lego models.

* Instead of building a car from scratch, you can just download one and start driving.
* Want to tweak it? You still can, but most of the heavy lifting is already done.

In AI terms:

* Hugging Face is a platform + library with thousands of pre-trained models (BERT, GPT, T5, etc.).
* Focuses on NLP (text tasks) like:
  * Sentiment analysis (“is this review positive or negative?”)
  * Text summarization (“make this article shorter”)
  * Question answering (“what is the capital of France?” → “Paris”).
* Huge community hub → people share models & datasets, kind of like the GitHub of AI.



#  How They Work Together

* PyTorch = the engine (raw power, flexibility).
* Hugging Face = the car built on top of that engine (ready to drive, but still customizable).

Example:
If you want to build a translation app (English → French):

* With PyTorch → you’d have to design and train the entire translation model from scratch (very time-consuming).
* With Hugging Face → you just grab a pre-trained translation model (like T5), fine-tune it on your data if needed, and you’re good to go.



# When to use what?

* PyTorch only → when you’re doing research, custom AI projects, or new model architectures.
* Hugging Face + PyTorch → when you want to quickly use state-of-the-art models for NLP with less coding effort.
