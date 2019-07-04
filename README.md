# Extractive-summarizer


# To run The .ipynb file
Need to install JupyterNotebook From Anaconda.

# Imports
```
conda install OS
conda install string
conda install NLTK
conda install sklearn
conda install networks
```
## install glove Predefine word Embeding library.
    f = open(r'Location', encoding='utf-8')
    Location= put the location address for the glove:
    
# Load data
###### directory = 'dataset/stories_text_summarization_dataset_test'
Write path location of train data/ test data to read given data.


# User Input
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
     
 ###### the value of sn is user define you can increase or decrease to get more highlights per stroy(News)


# TO RUN .py FILE

same import as we mention above needed.
YOU can run easly by following above mention techniques, Suitable for both.

Inisted of JUPYTER NOTEBOOK, You need Spyder by anconda for one time run.
# PROCEDURE
I use Page Ranking algorithm, is an extractive and unsupervised text summarization technique
## Split story in to Sentences.
## Text Preprocessing
remove punctuations, numbers and special characters and make alphabets lowercase
## Get rid of the stopwords
```
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
```
## Vector representation of Sentences With help of golve word vector

## Similarity Matrix
I use the cosine similarity approach for this challenge.
## Applying PageRank Algorithm
 I applied the PageRank algorithm to arrive at the sentence rankings.

 ```
 import networkx as nx

nx_graph = nx.from_numpy_array(sim_mat)
scores = nx.pagerank(nx_graph)
```
## Summary Extraction.
 
# RESULTS
```
***** 1 *****
 @highlight win sunday would perfect way former mcilroy prepare british open starts next week royal liverpool last two majors 
 @highlight mcilroy shot course record royal aberdeen thursday actually second player better old mark swedens kristoffer broberg earlier fired
***** 2 ***** 
 @highlight anyone doubts potential influence movies public opinion need look two films causing uproar even opened nationwide present hot button issues manage fire people left right 
 @highlight movie actually convince support torture movie really persuade fracking process used drill natural gas danger environment movie truly cause view certain minority groups negative light
***** 3 *****
 @highlight math may scary pi evidenced widespread revelry pi day one might even say gasp cool like pi days even house representatives supported designation march national pi day 
 @highlight pi day began small gathering mostly museum staff public pi extravaganza featuring pi procession whose attendees get number line order pis digits get idea
***** 4 *****
 @highlight unsuccessfully demanding meeting malaysian ambassador hotel eight hours angry relatives pushed past police officers tried stop making midnight march across chinese capital destination malaysian embassy 
 @highlight weeks distraught next kin requested facetoface meetings malaysian officials demanding briefing details last moments flight believed disappeared indian ocean absence information malaysian authorities many relatives continue believe missing loved ones still alive
***** 5 *****
 @highlight un security council approved resolution monday send peacekeepers abyei sudan part recent agreement sudan southern sudan @highlight resolution establish six months united nations interim security force abyei unisfa comprising maximum military personnel police personnel appropriate civilian support resolution states
***** 6 *****
 @highlight nfls current policy sends terrible message players fans americans even committing horrific act violence quickly back field senators wrote
 @highlight bipartisan group women senators waded ongoing drama nfl ray rice domestic violence
***** 7 *****
 @highlight white house wednesday said puzzled former spokesmans memoir accuses bush administration mired propaganda political spin times playing loose truth 
 @highlight excerpts book released monday scott mcclellan writes war iraq bush advisers confused propaganda campaign high level candor honesty fundamentally needed build sustain public support time war
***** 8 *****
 @highlight third think twitter tech company media company part larger environment little correct failure diversity year year studies one last week directors guild america well reports makes news womens media center status women media document exactly distorted mainstream media ownership management production remain online situation improving even difference largely gains womenoriented pinkcollar content 
 @highlight bryan goldbergs september launch bustle womens centric website world news politics alongside beauty tips blunt force case point announcing site tonedeaf post goldberg widely mocked personal failure grasp among things ridiculous claim starting first site kind women real issue isnt goldbergs cluelessness institutional biases enabled raise million far able knowledgeable experienced women cant
***** 9 *****
 @highlight queens day never trouw newspaper said netherlands always proud nonsense royal family comes queen cycles bike also mixes people without obvious security measurements still possible royal family target attack 
 @highlight man whose name released seriously injured crash thursday town apeldoorn miles east amsterdam police said died early friday police said
***** 10 *****
 @highlight late mao would stand tiananmen rostrum launch cultural revolution rallied hundreds thousands young chinese radical red guards lionized like demigod rebel justified proclaimed rebelled everything wreaked havoc everywhere ten years china condemned political turmoil economic malaise perhaps factor kept country total collapse peoples incomparable resilience ability chi ku eat bitterness bear hardship 
 @highlight tiananmen rostrum chairman mao formally proclaimed founding peoples republic chinese people stood declared shrill hunanese accent decades whole nation followed mao loyally emphasized political mobilization common man especially peasantry maos ideology chinese people found hope new china wherein citizens would always bowl rice eat clothes wear
```
