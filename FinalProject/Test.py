from IBManalysis import toneAnalyzer
from WikiData import get_cleaned_text

team = "San_Antonio_Spurs"
text = get_cleaned_text(team)
toneAnalyzer(text, team)
