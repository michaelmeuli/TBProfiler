import setuptools


setuptools.setup(

	name="tbprofiler",
	version="2.4.2",
	packages=["tbprofiler",],
	license="MIT",
	long_description="TBProfiler command line tool",
	# install_requires=['numpy','pyvcf','tqdm','ete3','biopython','colour','matplotlib','pysam'],
	scripts= [
		'tb-profiler',
		'scripts/tbprofiler_performance.py',
		'scripts/tbprofiler_variant_matrix.py',
		'scripts/tbprofiler_library_summary.py',
		'scripts/tbprofiler_get_mutation.py',
		'scripts/tbprofiler_utils.py',
		'scripts/tbprofiler_get_dr_freq.py',
		'scripts/tbprofiler_get_library_freq.py',
		'scripts/tbprofiler_get_heteroresistant_calls.py',
		'scripts/tbprofiler_odds_ratios.py',
		'scripts/tbprofiler_generate_haplotypes.py',
		],
	data_files=[('share/tbprofiler',["db/tbdb.ann.txt","db/tbdb.barcode.bed","db/tbdb.bed","db/tbdb.dr.json","db/tbdb.fasta","db/tbdb.gff","example_data/tbprofiler.test.fq.gz"])]
)
