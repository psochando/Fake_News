# Fake News


## Context
Having access to the internet provides us with nearly limitless information, or at least much more than we can absorb. This is largely due to the collaborative nature of the online community, where all of us can act as consumers and producers of content. This dynamic has the potential to elevate collective knowledge to unprecedented levels, although the possibility for anyone to contribute information on any topic also presents significant challenges.
Partial or biased information that circulates through social media and takes root in people's beliefs, generative artificial intelligence software capable of creating highly realistic audiovisual material about events that never actually happened, and so on, are examples of often overlooked side effects of the technological revolution we are experiencing. It's clear that we live in the information era but, ironically, it's also the era of misinformation. Thus, we believe it's crucial to be highly critical of the information we consume and share with the broader community.

## Goal
This project focuses on the distinction between truth and falsehood in the realm of Natural Language Processing. This immensely complex and even philosophical issue is currently one of the primary areas of research in this field. Our humble objective has been to explore the necessary methods and techniques for tackling this type of challenge and to provide an approximate solution, within certain constraints, to the problem of distinguishing actual news from the fake ones.

## The Algorithm
The data for this project was collected using web scraping techniques from four well-known Spanish newspapers: El País, El Mundo, Hay Noticia, and El Mundo Today. The news collected from the first two constitute the set of true news, while those from the latter two are fake. After analyzing and cleaning the data, we ended up with around 5000 news articles (balanced between true and false) that were used to train the model.
The chosen model for the final implementation is ALBERT-tiny, a pre-trained Spanish version of a deep neural network with Transformer architecture. Among all the evaluated models, including other LLM and Deep Learning models, ALBERT-tiny proved to be the most efficient during the fine-tuning phase with our data. The term "fine-tuning" refers to the final supervised training, in which the model internalizes specific patterns from the actual news set (El País, El Mundo) and contrasts them with the characteristic patterns of fake news (Hay Noticia, El Mundo Today). This process equips the model to classify new news articles as true or false, preferably from among these four newspapers.

## How to Use It
- Click on the following link to access the interface: https://fakenews-bnq6oagfvzpvamg6hxmzxt.streamlit.app/

- Go to the website of any of the mentioned four newspapers (you can choose either one depending on whether you want a real news article or a fake one). Carefully copy and paste the ENTIRE BODY of any news article (Make sure you can read it in full. Complete access to some articles is reserved for premium users) and paste ONLY THE BODY of the news into the text box on the interface.

- Click on "Comprobar veracidad" and... that's it! You'll see what our algorithm thinks about the chosen news article. Did it get it right?

Important: Remember that there is no magic involved in this, and the model can make mistakes. However, its performance will be optimum if we provide it with right data. Include only the complete body of the news article, from beginning to end, and nothing more. No headlines, footnotes, or anything other than the body. While the model will still provide a prediction even if we don't strictly follow these guidelines, its performance simply won't be as good.

