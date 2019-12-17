import unittest
from GameOracle import *

class TestGameOracle(unittest.TestCase):
	def testGetState(self):
		game = GameOracle(
				p0_hidden_hand='6s0 6s1 7s0 7s2',
				p0_discarded='1s3 9s4',
				p0_built_sets='OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3)',
				p1_hidden_hand='1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 7z1 *9s3',
				p1_discarded='2z0 4z3',
				mountain='2z1 2z3 2z2',
				next_step='P1Discard')
				
		state_p0 = game.getState(role='p0')
		self.assertEquals(state_p0['p0_hidden_hand'], '6s0 6s1 7s0 7s2')
		self.assertEquals(state_p0['p0_discarded'], '1s3 9s4')
		self.assertEquals(state_p0['p0_built_sets'], 'OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3)')
		self.assertEquals(state_p0['p1_hidden_hand'], '??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? *???')
		self.assertEquals(state_p0['p1_discarded'], '2z0 4z3')
		self.assertEquals(state_p0['p1_built_sets'], '')
		self.assertEquals(state_p0['mountain'], '??? ??? ???')
		self.assertEquals(state_p0['next_step'], 'P1Discard')

		state_p1 = game.getState(role='p1')
		self.assertEquals(state_p1['p0_hidden_hand'], '??? ??? ??? ???')
		self.assertEquals(state_p1['p0_discarded'], '1s3 9s4')
		self.assertEquals(state_p1['p0_built_sets'], 'OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3)')
		self.assertEquals(state_p1['p1_hidden_hand'], '1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 7z1 *9s3')
		self.assertEquals(state_p1['p1_discarded'], '2z0 4z3')
		self.assertEquals(state_p1['p1_built_sets'], '')
		self.assertEquals(state_p1['mountain'], '??? ??? ???')
		self.assertEquals(state_p1['next_step'], 'P1Discard')

		state_ob = game.getState(role='ob')
		self.assertEquals(state_ob['p0_hidden_hand'], '6s0 6s1 7s0 7s2')
		self.assertEquals(state_ob['p0_discarded'], '1s3 9s4')
		self.assertEquals(state_ob['p0_built_sets'], 'OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3)')
		self.assertEquals(state_ob['p1_hidden_hand'], '1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 7z1 *9s3')
		self.assertEquals(state_ob['p1_discarded'], '2z0 4z3')
		self.assertEquals(state_ob['p1_built_sets'], '')
		self.assertEquals(state_ob['mountain'], '2z1 2z3 2z2')
		self.assertEquals(state_ob['next_step'], 'P1Discard')
	
	def testGetStateAfterFinished(self):
		game = GameOracle(
				p0_hidden_hand='6s0 6s1 7s0 7s2',
				p0_discarded='1s3 9s4',
				p0_built_sets='OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3)',
				p1_hidden_hand='1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 9s3 *8s3',
				p1_discarded='2z0 4z3',
				mountain='2z1 2z3 2z2',
				next_step='',
				p1_winning_type='DrawAndWin',
				p1_winning_patterns='AllConcealed NineGates',
				p1_winning_hand='ClosedTriplet(1s0,1s1,1s2) ClosedSeq(2s0,3s1,4s2) ClosedSeq(5s3,6s2,7s1) ClosedTriplet(9s1,9s2,9s3) Pair(8s0,8s3)')

		state_p0 = game.getState(role='p0')
		self.assertEquals(state_p0['p0_hidden_hand'], '6s0 6s1 7s0 7s2')
		self.assertEquals(state_p0['p0_discarded'], '1s3 9s4')
		self.assertEquals(state_p0['p0_built_sets'], 'OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3)')
		self.assertEquals(state_p0['p1_hidden_hand'], '??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? *???')
		self.assertEquals(state_p0['p1_discarded'], '2z0 4z3')
		self.assertEquals(state_p0['p1_built_sets'], '')
		self.assertEquals(state_p0['mountain'], '??? ??? ???')
		self.assertEquals(state_p0['next_step'], '')
		self.assertEquals(state_p0['p1_winning_type'], 'DrawAndWin')
		self.assertEquals(state_p0['p1_winning_hand'], 'ClosedTriplet(1s0,1s1,1s2) ClosedSeq(2s0,3s1,4s2) ClosedSeq(5s3,6s2,7s1) ClosedTriplet(9s1,9s2,9s3) Pair(8s0,8s3)')
		self.assertEquals(state_p0['p1_winning_patterns'], 'AllConcealed NineGates')

		state_p1 = game.getState(role='p1')
		self.assertEquals(state_p1['p0_hidden_hand'], '??? ??? ??? ???')
		self.assertEquals(state_p1['p0_discarded'], '1s3 9s4')
		self.assertEquals(state_p1['p0_built_sets'], 'OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3)')
		self.assertEquals(state_p1['p1_hidden_hand'], '1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 7z1 *9s3')
		self.assertEquals(state_p1['p1_discarded'], '2z0 4z3')
		self.assertEquals(state_p1['p1_built_sets'], '')
		self.assertEquals(state_p1['mountain'], '??? ??? ???')
		self.assertEquals(state_p1['next_step'], '')
		self.assertEquals(state_p1['p1_winning_type'], 'DrawAndWin')
		self.assertEquals(state_p1['p1_winning_hand'], 'ClosedTriplet(1s0,1s1,1s2) ClosedSeq(2s0,3s1,4s2) ClosedSeq(5s3,6s2,7s1) ClosedTriplet(9s1,9s2,9s3) Pair(8s0,8s3)')
		self.assertEquals(state_p1['p1_winning_patterns'], 'AllConcealed NineGates')

		state_ob = game.getState(role='ob')
		self.assertEquals(state_ob['p0_hidden_hand'], '6s0 6s1 7s0 7s2')
		self.assertEquals(state_ob['p0_discarded'], '1s3 9s4')
		self.assertEquals(state_ob['p0_built_sets'], 'OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3)')
		self.assertEquals(state_ob['p1_hidden_hand'], '1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 7z1 *9s3')
		self.assertEquals(state_ob['p1_discarded'], '2z0 4z3')
		self.assertEquals(state_ob['p1_built_sets'], '')
		self.assertEquals(state_ob['mountain'], '2z1 2z3 2z2')
		self.assertEquals(state_ob['next_step'], '')
		self.assertEquals(state_ob['p1_winning_type'], 'DrawAndWin')
		self.assertEquals(state_ob['p1_winning_hand'], 'ClosedTriplet(1s0,1s1,1s2) ClosedSeq(2s0,3s1,4s2) ClosedSeq(5s3,6s2,7s1) ClosedTriplet(9s1,9s2,9s3) Pair(8s0,8s3)')
		self.assertEquals(state_ob['p1_winning_patterns'], 'AllConcealed NineGates')
			
	def testPerformActionDiscard(self):
		game = GameOracle(
				p0_hidden_hand='6s0 6s1 7s0 7s2',
				p0_discarded='1s3 9s4',
				p0_built_sets='OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3)',
				p1_hidden_hand='1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 9s3 *7z1',
				p1_discarded='2z0 4z3',
				mountain='2z1 2z3 2z2',
				next_step='P1Discard')
		role = 1
		action = 'Discard(7z1)'
		accepted = game.performAction(role, action)
		self.assertTrue(accepted)
		
		newState = game.getState(role='ob')
		self.assertEquals(newState['p0_hidden_hand'], '6s0 6s1 7s0 7s2')
		self.assertEquals(newState['p0_discarded'], '1s3 9s4')
		self.assertEquals(newState['p0_built_sets'], 'OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3)')
		self.assertEquals(newState['p1_hidden_hand'], '1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 9s3')
		self.assertEquals(newState['p1_discarded'], '2z0 4z3')
		self.assertEquals(newState['p1_built_sets'], '')
		self.assertEquals(newState['mountain'], '2z1 2z3 2z2')
		self.assertEquals(newState['next_step'], 'P2ReactToDiscardingFromP1')
		
	def testPerformActionDiscardBadTiming(self):
		game = GameOracle(
				p0_hidden_hand='6s0 6s1 7s0 7s2',
				p0_discarded='1s3 9s4',
				p0_built_sets='OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3)',
				p1_hidden_hand='1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 9s3 *7z1',
				p1_discarded='2z0 4z3',
				next_step='P1Discard')
		role = 0
		action = 'Discard(6s0)'
		accepted = game.performAction(role, action)
		self.assertTrue(accepted)
		
	def testPerformActionDiscardNonexisting(self):
		game = GameOracle(
				p0_hidden_hand='6s0 6s1 7s0 7s2',
				p0_discarded='1s3 9s4',
				p0_built_sets='OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3)',
				p1_hidden_hand='1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 9s3 *7z1',
				p1_discarded='2z0 4z3',
				next_step='P1Discard')
		role = 1
		action = 'Discard(2z0)'
		accepted = game.performAction(role, action)
		self.assertTrue(accepted)
	
	def testPerformActionPon(self):
		game = GameOracle(
				p0_hidden_hand='6s0 6s1 7s0 7s2',
				p0_discarded='1s3 9s4',
				p0_built_sets='OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3)',
				p1_hidden_hand='1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 8s0 9s1 9s2 9s3 7z1',
				p1_discarded='2z0 4z3 7s1',
				mountain='2z1 2z3 2z2',
				next_step='P0ReactToDiscardingFromP1')
		role = 0
		action = 'Pon(7s0,7s2,7s1)'
		accepted = game.performAction(role, action)
		self.assertTrue(accepted)
		
		newState = game.getState(role='ob')
		self.assertEquals(newState['p0_hidden_hand'], '6s0 6s1')
		self.assertEquals(newState['p0_discarded'], '1s3 9s4')
		self.assertEquals(newState['p0_built_sets'], 'OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3) OpenTriplet(7s0,*7s1,7s2)')
		self.assertEquals(newState['p1_hidden_hand'], '1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 9s3')
		self.assertEquals(newState['p1_discarded'], '2z0 4z3')
		self.assertEquals(newState['p1_built_sets'], '')
		self.assertEquals(newState['mountain'], '2z1 2z3 2z2')
		self.assertEquals(newState['next_step'], 'P0Discard')

	def testPerformActionSkip(self):
		game = GameOracle(
				p0_hidden_hand='6s0 6s1 7s0 7s2',
				p0_discarded='1s3 9s4',
				p0_built_sets='OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3)',
				p1_hidden_hand='1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 8s0 9s1 9s2 9s3 7z1',
				p1_discarded='2z0 4z3 7s1',
				mountain='2z1 2z3 2z2',
				next_step='P0ReactToDiscardingFromP1')
		role = 0
		action = 'Skip()'
		accepted = game.performAction(role, action)
		self.assertTrue(accepted)
		
		newState = game.getState(role='ob')
		self.assertEquals(newState['p0_hidden_hand'], '6s0 6s1 7s0 7s2 *2z1')
		self.assertEquals(newState['p0_discarded'], '1s3 9s4')
		self.assertEquals(newState['p0_built_sets'], 'OpenSeq(*1s3,2s1,3s0) Quad0(1z0,1z1,1z2,1z3) Quad1(3z0,3z1,*3z2,3z3) OpenTriplet(7s0,*7s1,7s2)')
		self.assertEquals(newState['p1_hidden_hand'], '1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 9s3')
		self.assertEquals(newState['p1_discarded'], '2z0 4z3')
		self.assertEquals(newState['p1_built_sets'], '')
		self.assertEquals(newState['mountain'], '2z3 2z2')
		self.assertEquals(newState['next_step'], 'P0Discard')

	def testPerformActionWin(self):
		game = GameOracle(
				p0_hidden_hand='6s0 6s1 6s2 7s0 7s2 8s0 8s1 8s3 5z0 5z1',
				p0_discarded='1s3 9s4',
				p0_built_sets='OpenTriplet(3z0,3z1,*3z2)',
				p1_hidden_hand='1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 8s0 9s1 9s2 9s3 7z1',
				p1_discarded='2z0 4z3 7s1',
				mountain='2z1 2z3 2z2',
				next_step='P0ReactToDiscardingFromP1')
		role = 0
		action = 'Win(OpenTriplet(3z0,3z1,*3z2),ClosedTriplet(6s0,6s1,6s2),OpenTriplet(7s0,*7s1,7s2),ClosedTriplet(8s0,8s1,8s3),Pair(5z0,5z1))'
		accepted = game.performAction(role, action)
		self.assertTrue(accepted)
		
		newState = game.getState(role='ob')
		self.assertEquals(newState['p0_hidden_hand'], '6s0 6s1 6s2 7s0 7s2 8s0 8s1 8s3 5z0 5z1')
		self.assertEquals(newState['p0_discarded'], '1s3 9s4')
		self.assertEquals(newState['p0_built_sets'], 'OpenTriplet(3z0,3z1,*3z2)')
		self.assertEquals(newState['p1_hidden_hand'], '1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 9s3')
		self.assertEquals(newState['p1_discarded'], '2z0 4z3 7s1')
		self.assertEquals(newState['p1_built_sets'], '')
		self.assertEquals(newState['mountain'], '2z1 2z3 2z2')
		self.assertEquals(newState['next_step'], '')
		self.assertEquals(newState['p0_winning_type'], 'Ron(P1)')
		self.assertEquals(newState['p0_winning_hand'], 'OpenTriplet(3z0,3z1,*3z2),ClosedTriplet(6s0,6s1,6s2),OpenTriplet(7s0,*7s1,7s2),ClosedTriplet(8s0,8s1,8s3),Pair(5z0,5z1)')
		self.assertEquals(newState['p0_winning_patterns'], 'AllTriplets')
		
	def testPerformActionWinWithAlternativePattern(self):
		game = GameOracle(
				p0_hidden_hand='6s0 6s1 6s2 7s0 7s2 8s0 8s1 8s3 5z0 5z1',
				p0_discarded='1s3 9s4',
				p0_built_sets='OpenTriplet(3z0,3z1,*3z2)',
				p1_hidden_hand='1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 8s0 9s1 9s2 9s3 7z1',
				p1_discarded='2z0 4z3 7s1',
				mountain='2z1 2z3 2z2',
				next_step='P0ReactToDiscardingFromP1')
		role = 0
		action = 'Win(OpenTriplet(3z0,3z1,*3z2),ClosedSeq(6s0,7s0,8s0),ClosedSeq(6s1,7s2,8s1),OpenSeq(6s2,*7s1,8s3),Pair(5z0,5z1))'
		accepted = game.performAction(role, action)
		self.assertTrue(accepted)
		
		newState = game.getState(role='ob')
		self.assertEquals(newState['p0_hidden_hand'], '6s0 6s1 6s2 7s0 7s2 8s0 8s1 8s3 5z0 5z1')
		self.assertEquals(newState['p0_discarded'], '1s3 9s4')
		self.assertEquals(newState['p0_built_sets'], 'OpenTriplet(3z0,3z1,*3z2)')
		self.assertEquals(newState['p1_hidden_hand'], '1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 9s3')
		self.assertEquals(newState['p1_discarded'], '2z0 4z3 7s1')
		self.assertEquals(newState['p1_built_sets'], '')
		self.assertEquals(newState['mountain'], '2z1 2z3 2z2')
		self.assertEquals(newState['next_step'], '')
		self.assertEquals(newState['p0_winning_type'], 'Ron(P1)')
		self.assertEquals(newState['p0_winning_hand'], 'OpenTriplet(3z0,3z1,*3z2),ClosedSeq(6s0,7s0,8s0),ClosedSeq(6s1,7s2,8s1),OpenSeq(6s2,*7s1,8s3),Pair(5z0,5z1)')
		self.assertEquals(newState['p0_winning_patterns'], 'IdenticalSequences IdenticalSequences IdenticalSequences')
		
	def testPerformActionChi(self):
		game = GameOracle(
				p0_hidden_hand='6s0 6s1 6s2 7s0 7s2 8s0 8s1 8s3 5z0 5z1',
				p0_discarded='1s3 9s4',
				p0_built_sets='OpenTriplet(3z0,3z1,*3z2)',
				p1_hidden_hand='1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s3 8s0 9s1 9s2 9s3 7z1',
				p1_discarded='2z0 4z3 7s1',
				mountain='2z1 2z3 2z2',
				next_step='P0ReactToDiscardingFromP1')
		role = 0
		action = 'Chi(6s0,7s1,8s0)'
		accepted = game.performAction(role, action)
		self.assertTrue(accepted)
		
		newState = game.getState(role='ob')
		self.assertEquals(newState['p0_hidden_hand'], '6s1 6s2 7s0 7s2 8s1 8s3 5z0 5z1')
		self.assertEquals(newState['p0_discarded'], '1s3 9s4')
		self.assertEquals(newState['p0_built_sets'], 'OpenTriplet(3z0,3z1,*3z2),OpenSeq(6s0,*7s1,8s0)')
		self.assertEquals(newState['p1_hidden_hand'], '1s0 1s1 1s2 2s0 3s1 4s2 5s3 6s2 7s1 8s0 9s1 9s2 9s3')
		self.assertEquals(newState['p1_discarded'], '2z0 4z3')
		self.assertEquals(newState['p1_built_sets'], '')
		self.assertEquals(newState['mountain'], '2z1 2z3 2z2')
		self.assertEquals(newState['next_step'], 'P0Discard')
