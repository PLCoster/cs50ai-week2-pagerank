from pagerank import transition_model

corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}

damping = 0.85

page = "1.html"

print(transition_model(corpus, page, damping))