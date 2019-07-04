# Extractive-summarizer
Summary of News 

# To run The .ipynb file:
Need to install JupyterNotebook From Anaconda.

# Imports:

conda install OS
conda install string
conda install NLTK
conda install sklearn
conda install networks

# install <glove> Predefine word Embeding library.
    f = open(r'Location', encoding='utf-8')
    Location= put the location address for the glove:
    
# Load data
## directory = 'dataset/stories_text_summarization_dataset_test'
Write path location of train data/ test data to read given data.


# Result:
   It will give the highlights of the story.
   
   Beacuse our method is rank based Extraction IT will give user define number of sentences in headlines.
   
     sn = 2
     summ = ''
     #Generate summary
     for o in range(sn):
         summ = summ + ' @highlight ' + str(ranked_sentences[o][1])
         #summ = summ + str(ranked_sentences[o][1]) + '. ' 
         #stories[j]['summary'] = summ
     print('*****', j+1, '*****')
     
 # the value of sn is user define you can increase or decrease to get more highlights per stroy(News)


# TO RUN .py FILE:

same import as we mention above needed.
YOU can run easly by following above mention techniques, Suitable for both.

Inisted of JUPYTER NOTEBOOK, You need Spyder by anconda for one time run.

