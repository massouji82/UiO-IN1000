# a) Implementer en klasse Student. En student har et navn, en total quiz score og et antall quizer studenten har deltatt på.

class Student():
	def __init__(self, navn, total_quiz_score, antall_quiz):
		self._navn = navn
		self._total_quiz_score = total_quiz_score
		self._antall_quiz = antall_quiz

# b) Lag metoden leggTilQuizScore i klassen. Den skal ta inn en verdi som står for en ny quiz-score, og samtidig skal den øke antall quizer studenten har deltatt på med 1.

	def leggTilQuizScore(self, verdi):
		self._total_quiz_score += verdi
		self._antall_quiz += 1

# c) Lag metoden gjennomsnittligScore som returnerer gjennomsnittlig score per quiz studenten har tatt.

	def gjennomsnittligScore(self):
		return self._total_quiz_score / self._antall_quiz

# d) Lag en metode som skriver ut all informasjon fra instansvariablene i et objekt på én linje.

	def skrivUt(self):
		print(f'{self._navn} fikk {self._total_quiz_score} poeng totalt, etter {self._antall_quiz} quizzer.')

# e) Lag tre nye Student-objekter, ved navn "Joakim", "Kristin" og "Dag".

joachim = Student('Joachim', 30, 10)
kristin = Student('Kristin', 45, 10)
dag = Student('Dag', 5, 10)

# f) Kall så metoden leggTilQuizScore på alle studentene minst to ganger hver.

joachim.leggTilQuizScore(5)
kristin.leggTilQuizScore(10)
dag.leggTilQuizScore(0)
joachim.leggTilQuizScore(20)
kristin.leggTilQuizScore(15)
dag.leggTilQuizScore(5)
	
# g) Print ut alle studentene sin totale score og gjennomsnittelige score.
 
joachim.skrivUt()
print(f'Gjennomsnittsscore: {joachim.gjennomsnittligScore()}\n')
kristin.skrivUt()
print(f'Gjennomsnittsscore: {kristin.gjennomsnittligScore()}\n')
dag.skrivUt()
print(f'Gjennomsnittsscore: {dag.gjennomsnittligScore()}\n')




