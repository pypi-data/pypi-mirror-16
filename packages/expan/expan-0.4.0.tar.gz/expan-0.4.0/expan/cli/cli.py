#!/usr/bin/python

import argparse
import ast
import logging
import pickle

import pandas as pd

from expan.core.experiment import Experiment
from expan.core.experimentdata import ExperimentData


class UsageError(Exception):
	def __init__(self, msg):
		self.msg = msg

	def __str__(self):
		return 'Usage Error: {}'.format(self.msg)


def parse_metadata(filename):
	metadata_file = open(filename)
	metadata_s = metadata_file.read()
	return ast.literal_eval(metadata_s)


def run_analysis(features_file, kpis_file, metadata_file):
	kpis = pd.read_csv(kpis_file)
	if features_file:
		features = pd.read_csv(features_file)
	else:
		features = 'default'
	print(features)
	metadata = parse_metadata(metadata_file)

	exp_data = ExperimentData(metrics=kpis,
							  metadata=metadata,
							  features=features)
	exp = Experiment(baseline_variant=metadata['baseline_variant'],
					 metrics_or_kpis=kpis,
					 metadata=metadata,
					 features=features)

	return (exp.delta(), exp.sga())


def run_expan(xxx_todo_changeme):
	(features_file, kpis_file, metadata_file, output_file) = xxx_todo_changeme
	(delta_result, sga_result) = run_analysis(features_file, kpis_file, metadata_file)
	print_results(delta_result, sga_result, output_file)


def print_results(delta, sga, output_file):
	delta_s = pickle.dumps(delta)
	sga_s = pickle.dumps(sga)
	if output_file:
		output = open(output_file, 'w')
		output.write(delta_s)
		output.write(sga_s)
	else:
		print(delta_s)
		print(sga_s)


def check_input_data(args):
	print(args)
	if not args.kpis:
		raise UsageError('Kpis file shall be provided (-k cli parameter)')
	if not args.metadata:
		raise UsageError('Metadata file shall be provided (-m cli parameter)')


def prepare_cli_parameters(args):
	check_input_data(args)
	features_file = args.features
	kpis_file = args.kpis
	metadata_file = args.metadata
	output_file = args.output

	return features_file, kpis_file, metadata_file, output_file


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--features', help='Path to file with feature data')
	parser.add_argument('-k', '--kpis', help='Path to file with kpis data')
	parser.add_argument('-m', '--metadata', help='Path to file with metadata')
	parser.add_argument('-o', '--output', help='Path to output file')

	args = parser.parse_args()

	try:
		run_expan(prepare_cli_parameters(args))
	except UsageError as e:
		logging.error(e)


if __name__ == '__main__':
	main()
