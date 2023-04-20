import pytest

import numpy as np

from baskerville import dna

def test_delete():
  seq_dna = 'GATTACA'
  seq_1hot = dna.dna_1hot(seq_dna)
  dna.hot1_delete(seq_1hot, 3, 2)
  seq_dna_del = dna.hot1_dna(seq_1hot)
  assert('GATCANN' == seq_dna_del)


def test_insert():
  seq_dna = 'GATTACA'
  seq_1hot = dna.dna_1hot(seseq_dnaq)
  dna.hot1_insert(seq_1hot, 3, 'AG')
  seq_dna_ins = dna.hot1_dna(seq_1hot)
  assert('GATAGTA' == seq_dna_ins)


def test_rc():
  #########################################
  # construct sequences
  seq1 = 'GATTACA'
  seq1_1hot = dna.dna_1hot(seq1)

  seq2 = 'TAGATAC'
  seq2_1hot = dna.dna_1hot(seq2)

  seqs_1hot = np.array([seq1_1hot, seq2_1hot])

  #########################################
  # reverse complement
  seqs_1hot_rc = dna.hot1_rc(seqs_1hot)

  seq1_rc = dna.hot1_dna(seqs_1hot_rc[0])
  seq2_rc = dna.hot1_dna(seqs_1hot_rc[1])

  #########################################
  # compare
  assert('TGTAATC' == seq1_rc)
  assert('GTATCTA' == seq2_rc)

  #########################################
  # reverse complement again
  seqs_1hot_rcrc = dna.hot1_rc(seqs_1hot_rc)

  seq1_rcrc = dna.hot1_dna(seqs_1hot_rcrc[0])
  seq2_rcrc = dna.hot1_dna(seqs_1hot_rcrc[1])

  #########################################
  # compare
  assert(seq1 == seq1_rcrc)
  assert(seq2 == seq2_rcrc)


def test_augment():
  seq = 'GATTACA'
  seq1 = dna.dna_1hot(seq)
  seqs1 = np.array([seq1])

  # forward, shift 0
  aseqs1_fwd0 = dna.hot1_augment(seqs1, True, 0)
  aseq_fwd0 = dna.hot1_dna(aseqs1_fwd0)[0]
  assert('GATTACA' == aseq_fwd0)

  # reverse, shift 0
  aseqs1_rc0 = dna.hot1_augment(seqs1, False, 0)
  aseq_rc0 = dna.hot1_dna(aseqs1_rc0)[0]
  assert('TGTAATC' == aseq_rc0)

  # forward, shift 1
  aseqs1_fwd1 = dna.hot1_augment(seqs1, True, 1)
  aseq_fwd1 = dna.hot1_dna(aseqs1_fwd1)[0]
  assert('NGATTAC' == aseq_fwd1)

  # reverse, shift 1
  aseqs1_rc1 = dna.hot1_augment(seqs1, False, 1)
  aseq_rc1 = dna.hot1_dna(aseqs1_rc1)[0]
  assert('GTAATCN' == aseq_rc1)

  # forward, shift 1
  aseqs1_fwd_m1 = dna.hot1_augment(seqs1, True, -1)
  aseq_fwd_m1 = dna.hot1_dna(aseqs1_fwd_m1)[0]
  assert('ATTACAN' == aseq_fwd_m1)

  # reverse, shift 1
  aseqs1_rc_m1 = dna.hot1_augment(seqs1, False, -1)
  aseq_rc_m1 = dna.hot1_dna(aseqs1_rc_m1)[0]
  assert('NTGTAAT' == aseq_rc_m1)