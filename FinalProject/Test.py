from IBManalysis import toneAnalyzer
from WikiData import get_cleaned_text

team = "Minnesota_Timberwolves"
text = get_cleaned_text(team)
toneAnalyzer(text)
