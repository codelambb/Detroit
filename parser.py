from .model import RPS

class RockPaperScissorPaser:

	def _init_(self, choice):
		choice = choice.lower()

		if choice == RPS.ROCK:
			self.choice = RPS.ROCK
		elif choice == RPS.PAPER:
			self.choice = RPS.PAPER
		elif choice == RPS.SCISSOR:
			self.choice = RPS.SCISSOR
		else:
			raise