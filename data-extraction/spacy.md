# Notes for Using Spacy

<ul>
    <li> include "import spacy" in file
    <li> run the following commands in bash
        
        $ python -m venv .env
        $ .env\Scripts\activate
        $ pip install -U pip setuptools wheel
        $ pip install -U spacy
        $ python -m spacy download en_core_web_trf

<li> import the pretrained model using <code> nlp = spacy.load("en_core_web_trf")</code> where <code>nlp</code> is the name of your spacy model
<li> create a spacy doc using your model

        doc = nlp("{text to parse}")
        
</ul>