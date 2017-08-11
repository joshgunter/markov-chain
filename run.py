from markov_python.cc_markov import MarkovChain
import fetch_data

mc = MarkovChain()
html = fetch_data.poem_output

mc.add_string(html)

output = mc.generate_text()
output2 = mc.generate_text()

print " ".join(output)
print " ".join(output2)
