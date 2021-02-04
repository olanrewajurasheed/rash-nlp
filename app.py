#import Viz packages 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
matplotlib.use('Agg')

#set seaborn as style
sns.set_style('darkgrid')

#import streamlit
import streamlit as st
#ignore warning 
st.set_option('deprecation.showPyplotGlobalUse', False) 

#import necessary NLP libraries
import nltk
import textblob
import goslate
from textblob import TextBlob
from nltk import ngrams 
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

#setting background image from local host  
import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

#restyling the CSS and HTML tags.  
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    color: white;
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-color: white;
    -webkit-tap-highlight-color: red;
    -webkit-highlight-color: red;
    
    }
    .st-ci {
    color: blue;
    
    }
    .st-br {
    background-color:#C0C0C0;  
       }
    .st-cd {
    color: black;
	}
    .st-dd {
    color: white;
    }
    .st-de {
    color: white;
	}
    .css-145kmo2 {
    color: white;
    }
    .css-3xqji8 {
    color: white;
    }
    #head {
	 -webkit-border-radius: 10px;
    -moz-border-radius: 10px;
 	 border-radius: 10px;
 	 -webkit-box-shadow: 0px 0px 100px #0000A0;
	  -moz-box-shadow: 0px 0px 100px #0000A0;
 	 box-shadow: 0px 0px 100px #0000A0;
	}
	#para {
    font-family: "IBM Plex Sans", sans-serif;
	}
	#Mname {
    font-family: "IBM Plex Sans", sans-serif;
     
     color:#C0C0C0;    
	}
	.css-2trqyj {
    color: red;
    }

	.css-1v4eu6x a {
	color: #013220;
	text-decoration: none;
	-webkit-border-radius: 10px;
    -moz-border-radius: 10px;
 	 border-radius: 10px;
 	padding:5px;
 	 
	} 
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

#file name
set_png_as_page_bg('ai_bkgrd.jpg')


html_temp = """
<div style="background-color:{};height:{};width:{};">
</div>
<div id="head" style="background-color:{};padding:10px;">
<h1 style="color:{};text-align:center;">Natural Language Processing WebApp </h1>
</div>
"""
st.markdown(html_temp.format('red','5px', '100%','#cccccc','#0000A0'),unsafe_allow_html=True)

html_temp2 = """
<hr>

<p id="para" style="font-size:{};color:{};text-align:left;">
<b> Description </b> <br/>
This is a mini Natural Language Processing (NLP) web-app built with streamlit. It performs 
various NLP activities like tokenization, sentiment-analysis, translation and summarization. \
It uses packages like textblob, nltk, gensim, goslate, pandas and seaborn.<br/>
More features like NER will be added later.
 </p>
"""
 
st.markdown(html_temp2.format('17px', '#ffffff' ),unsafe_allow_html=True)

st.subheader("""
	Start NLProcessing Here...
	""")

#The main script body
def main():
	word = st.text_area('Enter text ', height = 120)
	text  = TextBlob(word)
	
	st.markdown("""
		Check the boxes below  :point_down:  """)	

	#Tokenization  
	if st.checkbox("Tokenize"):
		box = st.selectbox("Select",("Sentences", "Words", "Noun Phrases"))
		
		if box == "Sentences": 
			token_sen = text.sentences
			st.write(f"YOUR TEXT HAS {len(token_sen)} SENTENCE(S).\n")
			st.write(f"The sentences are : \n")
			for w in token_sen:
				st.write(w)

		if box == "Words":
			box_word = text.words
			#removing stop words from wordList 
			stops = set(stopwords.words('english'))
			no_stop = [word for word in box_word if word not in stops]
			st.write("YOUR TEXT HAS {} WORD(S).\n".format(len(box_word)))
			st.write("YOUR TEXT HAS {} WORD(S), EXCLUDING STOPWORDS.\n".format(len(no_stop)))
			st.write("\nThe WordList (excluding stopwords) are : \n")
			for word in no_stop:
				st.write(word)

		if box == "Noun Phrases":
			noun_ph = text.noun_phrases
			st.write("YOUR TEXT HAS {} NOUN PHRASES(S).\n".format(len(noun_ph)))
			st.write("The noun phrases are :")
			for phrase in noun_ph:
				st.write(phrase)


	if st.checkbox("POS Tagging"):
		box = st.selectbox("Select", ("Singular Verb","Proper Noun","Adjective"))
		p_word = text.words
		stops = set(stopwords.words('english'))
		no_stop = [word for word in p_word if word not in stops]
		tagged = nltk.pos_tag(no_stop)
		
		if box == "Singular Verb":			
			st.write('SINGULAR VERBS EXTRACTED :\n')
			for word, tag in tagged:
				if tag == 'VBZ':
					st.write(word)

		if box == "Proper Noun":
			st.write('PROPER NOUNS EXTRACTED :\n')
			for word, tag in tagged:
				if tag == 'NNP':
					st.write(word)

		if box == "Adjective":
			st.write('ADJECTIVES EXTRACTED :\n')
			for word, tag in tagged:
				if tag == 'JJ':
					st.write(word)
    
		
	lang_dict = {'French':'fr','Afrikaans':'af', 'Irish':'ga','Albanian':'sq','Italian':'it','Arabic':'ar','Japanese':'ja',
	             'Azerbaijani':'az','Basque':'eu','Korean':'ko','Bengali':'bn','Latin':'la','Belarusian':'be',
	             'Latvian':'lv','Bulgarian':'bg','Lithuanian':'lt','Catalan':'ca','Macedonian':'mk',
	             'Chinese Simplified':'zh-CN','Malay':'ms','Chinese Traditional':'zh-TW','Maltese':'mt','Croatian':'hr',
	             'Norwegian':'no','Czech':'cs','Persian':'fa','Danish':'da','Polish':'pl','Dutch':'nl','Portuguese':'pt',
	             'Romanian':'ro','Esperanto':'eo','Russian':'ru','Estonian':'et','Serbian':'sr','Filipino':'tl',
	             'Slovak':'sk','Finnish':'fi','Slovenian':'sl','Spanish':'es','Galician':'gl',
	             'Swahili':'sw','Georgian':'ka','Swedish':'sv','German':'de','Tamil':'ta','Greek':'el','Telugu':'te',
	             'Gujarati':'gu','Thai':'th','Haitian Creole':'ht','Turkish':'tr','Hebrew':'iw','Ukrainian':'uk',
	             'Hindi':'hi','Urdu':'ur','Hungarian':'hu','Vietnamese':'vi','Icelandic':'is','Welsh':'cy','Indonesian':'id',
	             'Yiddish':'yi'}

	#word translation using google translate             
	if st.checkbox('Translate'):
		try:
			lang = list(lang_dict.keys())
			activity = st.selectbox("Language", lang)
			gs = goslate.Goslate()
			st.write(gs.translate(str(text), lang_dict[activity]))
		except:
			st.markdown('*Error, check your text!*')
			

	#sentiment analysis using SentimentIntensityAnalyzer
	if st.checkbox("Sentiment Analysis"):
		try:
			sia = SentimentIntensityAnalyzer()
			sent_claf =  sia.polarity_scores(str(text))			
			if sent_claf['pos'] > 0.5:
				st.write(f"Positive Review: {round(sent_claf['pos']*100)}%")
			elif sent_claf['neg'] > 0.5:
				st.write(f"Negative Review: {round(sent_claf['neg']*100)}%")
			else:
				st.write('Neutral Review')
		except:
			st.markdown('*Error, check your text!*')		

	#summarization using Summa & Gensim 
	if st.checkbox("Summarise"):					
		try:
			if st.button('Gensim'):
				from gensim.summarization import summarize
				st.write(f"The summary using gensim:\n\n {summarize(str(text))}")
			if st.button('Summa'):
				from summa.summarizer import summarize
				st.write(f"The summary using summa:\n\n {summarize(str(text))}\n")
				st.markdown("**No major difference between Gensim and Summa!**")
		except:
			st.markdown('*Input must be more than one sentence!*')
			

	#n-grams using nltk
	if st.checkbox('Display n-grams'):
		try:
			sentence = text.words
			n_gram = st.number_input('Enter the number of grams: ', 2, )
			grams = ngrams(sentence, n_gram)
			for gram in grams:
				st.write(gram)
		except:
			st.markdown('*Error, check your text!*')

	
	try:
		if st.checkbox('Specific Word Count'):
			word = st.text_input("Enter the word you'll like to count from your text.").lower()
			occur = text.word_counts[word]
			st.write('The word " {} " appears {} time(s) in the text .'.format((word),(occur)))

		if st.checkbox("Word Frequency Visualization"):		
			input_no = st.number_input("Enter no of words:", 3,20)
			items = text.word_counts.items()
			stops = set(stopwords.words('english')) 		
			items = [item for item in items if item[0] not in stops]	
			from operator import itemgetter
			sorted_items = sorted(items, key=itemgetter(1), reverse=True)
			top = sorted_items[0:int(round(input_no, 0))]
			st.subheader(f"Top {str(input_no)} Words ")
			df = pd.DataFrame(top, columns=['Text', 'Count'])
			st.dataframe(df)
			#display the visualized word frequency
			if st.button("Display"):
				df.plot.bar(x='Text', y='Count', legend=True)
				plt.title("Word Frequency Visualization")			
				st.pyplot()

	except:
		st.markdown('*Oops, check your text!*')



	format_temp = """
<br><br><br>

Developed by: <span><a href="https://www.linkedin.com/in/olanrewajurasheed/"><b><button>Olanrewaju Rasheed</button></b></a>
</span>

"""

	st.markdown(format_temp, unsafe_allow_html = True)		
if __name__ == '__main__':
	main()		