from markov_python.cc_markov import MarkovChain
import fetch_data

mc = MarkovChain()
html = fetch_data.html

mc.add_string(html)
print mc.generate_text()
