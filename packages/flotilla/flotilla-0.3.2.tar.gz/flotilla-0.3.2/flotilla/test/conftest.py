"""
This file will be auto-imported for every testing session, so you can use
these objects and functions across test files.
"""

from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

from collections import defaultdict
import os

import matplotlib as mpl
import numpy as np
from pytest import fixture, mark
import pandas as pd
from scipy import stats
import seaborn as sns


@fixture(scope='module')
def data_dir():
    return os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        'example_data')


@fixture(scope='module')
def RANDOM_STATE():
    """Consistent random state"""
    return 0


#######################################################
# samples
########

@fixture(scope='module')
def n_samples():
    """Number of samples to create example data from"""
    return 50


@fixture(scope='module')
def samples(n_samples):
    """Sample ids"""
    return ['sample_{}'.format(i + 1) for i in np.arange(n_samples)]


@fixture(scope='module')
def technical_outliers(n_samples, samples):
    """If request.param is True, return randomly chosen samples as technical
    outliers, otherwise None"""
    return np.random.choice(samples,
                            size=np.random.randint(1, int(n_samples / 10.)),
                            replace=False)


@fixture(scope='module')
def pooled(request, n_samples, samples):
    """If request.param is True, return randomly chosen samples as pooled,
    otherwise None"""
    return np.random.choice(samples,
                            size=np.random.randint(1, int(n_samples / 10.)),
                            replace=False)


@fixture(scope='module')
def outliers(request, n_samples, samples):
    """If request.param is True, return randomly chosen samples as outliers,
    otherwise None"""
    return np.random.choice(samples,
                            size=np.random.randint(1, int(n_samples / 10.)),
                            replace=False)


#######################################################
# groups
########

@fixture(scope='module')
def n_groups():
    """Number of phenotype groups."""
    return 2


@fixture(scope='module')
def groups(n_groups):
    """Phenotype group names"""
    # return ['group{}'.format(i + 1) for i in np.arange(n_groups)]
    return [(b'group' + str(i+1).encode()).decode()
            for i in np.arange(n_groups)]


@fixture(scope='module')
def group_order(groups):
    """so-called 'logical' order of groups for plotting.
    To test if the user gave a specific order of the phenotypes, e.g.
    by differentiation time"""
    return np.random.permutation(groups)


@fixture(scope='module')
def colors(n_groups):
    """Colors to use for the samples"""
    return [mpl.colors.rgb2hex(rgb)
            for rgb in sns.color_palette('husl', n_colors=n_groups)]


@fixture(scope='module')
def group_to_color(group_order, colors):
    """Mapping of groups to colors"""
    return dict(zip(group_order, colors))


@fixture(scope='module')
def color_ordered(group_order, group_to_color):
    """Colors in the order created by the groups"""
    return [group_to_color[g] for g in group_order]


@fixture(scope='module')
def group_transitions(group_order):
    """List of pairwise transitions between phenotypes, for NMF"""
    return zip(group_order[:-1], group_order[1:])


# TODO commented out fixture, what for
######################################
# @fixture(scope='module')
# def n_groups_fixed():
#     """Fixed number of phenotype groups (3)"""
#     return 3
#
# @fixture(scope='module')
# def groups_fixed(n_groups_fixed):
#     """Phenotype group names"""
#     return ['group{}'.format(i + 1) for i in np.arange(n_groups_fixed)]
#
# @fixture(scope='module')
# def group_order_fixed(groups_fixed):
#     """so-called 'logical' order of groups for plotting.
#
#     To test if the user gave a specific order of the phenotypes, e.g.
#     by differentiation time
#     """
#     return np.random.permutation(groups_fixed)
#
# @fixture(scope='module')
# def colors_fixed(n_groups_fixed):
#     """Colors to use for the samples"""
#     return [mpl.colors.rgb2hex(rgb)
#         for rgb in sns.color_palette('husl', n_colors=n_groups_fixed)]
#
# @fixture(scope='module')
# def group_to_color_fixed(group_order_fixed, colors_fixed):
#     """Mapping of groups to colors"""
#     return dict(zip(group_order_fixed, colors_fixed))
#
# @fixture(scope='module')
# def color_ordered_fixed(group_order_fixed, group_to_color_fixed):
#     """Colors in the order created by the groups"""
#     return [group_to_color_fixed[g] for g in group_order_fixed]
#
# @fixture(scope='module')
# def group_transitions_fixed(group_order_fixed):
#     """List of pairwise transitions between phenotypes, for NMF"""
#     return zip(group_order_fixed[:-1], group_order_fixed[1:])


@fixture(scope='module')
def group_to_marker(request):
    """Mapping of groups to plotting markers"""
    marker_iter = iter(list('ov^<>8sp*hHDd'))
    return defaultdict(lambda: marker_iter.next())


# TODO commented out fixture, what for
# @fixture(scope='module', params=['phenotype', 'group'])
# def metadata_phenotype_col(request):
#     """Which column in the metadata specifies the phenotype"""
#     return request.param


@fixture(scope='module')
def groupby(groups, samples):
    return dict((sample, np.random.choice(groups)) for sample in samples)


@fixture(scope='module')
def metadata_data(groupby, samples, n_samples):
    df = pd.DataFrame(index=samples)
    df['phenotype'] = df.index.map(lambda x: groupby[x])
    df['subset1'] = np.random.choice([True, False], size=n_samples)
    return df


# TODO commented out fixture, what for
# @fixture(scope='module')
# def metadata_data_groups_fixed(groupby_fixed, outliers, pooled, samples,
#                                n_samples,
#                                metadata_phenotype_col):
#     df = pd.DataFrame(index=samples)
#     if outliers is not None:
#         df['outlier'] = df.index.isin(outliers)
#     if pooled is not None:
#         df['pooled'] = df.index.isin(pooled)
#     df[metadata_phenotype_col] = df.index.map(lambda x: groupby_fixed[x])
#     df['subset1'] = np.random.choice([True, False], size=n_samples)
#     return df


@fixture(scope='module')
def metadata_kws(group_order, group_to_color,
                 group_to_marker):
    kws = {}
    # if metadata_phenotype_col != 'phenotype':
    #     kws['phenotype_col'] = metadata_phenotype_col
    kws['phenotype_order'] = group_order
    kws['phenotype_to_color'] = group_to_color
    kws['phenotype_to_marker'] = group_to_marker
    return kws


# TODO commented out fixture, what for
# @fixture(scope='module')
# def metadata_kws_fixed(metadata_phenotype_col, group_order_fixed,
#                        group_to_color_fixed):
#     kws = {}
#     if metadata_phenotype_col != 'phenotype':
#         kws['phenotype_col'] = metadata_phenotype_col
#     kws['phenotype_order'] = group_order_fixed
#     kws['phenotype_to_color'] = group_to_color_fixed
#     kws['phenotype_to_marker'] = defaultdict(lambda: 'o')
#     return kws


@fixture(scope='module')
def mapping_stats_number_mapped_col():
    return 'mapped_reads'


@fixture(scope='module')
def mapping_stats_min_reads_default():
    return 5e5


@fixture(scope='module')
def mapping_stats_kws(mapping_stats_number_mapped_col):
    kws = {'number_mapped_col': mapping_stats_number_mapped_col}
    # if request.param is not None:
    # kws['min_reads'] = 1e6
    return kws


@fixture(scope='module')
def mapping_stats_data(samples, technical_outliers,
                       mapping_stats_min_reads_default,
                       mapping_stats_number_mapped_col):
    df = pd.DataFrame(index=samples)
    df[mapping_stats_number_mapped_col] = 2 * mapping_stats_min_reads_default
    if technical_outliers is not None:
        df.ix[technical_outliers, mapping_stats_number_mapped_col] = \
            .5 * mapping_stats_min_reads_default
    return df


#######################################################
# genes
########

@fixture(scope='module')
def n_genes():
    return 50


@fixture(scope='module')
def genes(n_genes):
    # TODO make 'gene_n' unicode
    # return [b'gene_{}'.format(i + 1) for i in np.arange(n_genes)]
    # return [b'gene_' + bytes(bytearray([i+1])) for i in np.arange(n_genes)]
    # return [b'gene_' + str(i+1).encode() for i in np.arange(n_genes)]
    return [(b'gene_' + str(i+1).encode()).decode()
            for i in np.arange(n_genes)]


#######################################################
# events
########

@fixture(scope='module')
def n_events():
    return 100


@fixture(scope='module')
def events(n_events):
    # TODO make 'event_n' unicode
    # return [b'event_{}'.format(i + 1) for i in np.arange(n_events)]
    # return [b'event_' + bytes(bytearray([i+1])) for i in np.arange(n_events)]
    # return [b'event_' + str(i+1).encode() for i in np.arange(n_events)]
    return [(b'event_' + str(i+1).encode()).decode()
            for i in np.arange(n_events)]


@fixture(scope='module')
def modality_models():
    parameter = 20.
    rv_psi1 = stats.beta(parameter, 1)
    rv_psi0 = stats.beta(1, parameter)
    rv_middle = stats.beta(parameter, parameter)
    rv_ambiguous = stats.uniform(0, 1)
    rv_bimodal = stats.beta(1. / parameter, 1. / parameter)

    models = {'Psi~1': rv_psi1,
              'Psi~0': rv_psi0,
              'middle': rv_middle,
              'ambiguous': rv_ambiguous,
              'bimodal': rv_bimodal}
    return models


@fixture(scope='module',
         params=[0., 0.5],
         ids=['na_thresh0', 'na_thresh5'])
# @fixture(scope='module',
#          params=[0.],
#          ids=['na_thresh0'])
def na_thresh(request):
    return request.param


@fixture(scope='module')
def feature_rename_col():
    return 'gene_name'


@fixture(scope='module')
def gene_categories():
    return list('ABCDE')


@fixture(scope='module')
def boolean_gene_categories():
    return list('WXYZ')


# TODO commented out fixture, what for
# @fixture(scope='module', params=[False, True])
# def pooled(request):
# return request.param
#
#
# TODO commented out fixture, what for
# @fixture(scope='module', params=[False, True])
# def outlier(request):
# return request.param


@fixture(scope='module',
         params=[False, True],
         ids=['renamedno', 'renamedyes'])
# @fixture(scope='module',
#          params=[False],
#          ids=['renamedno'])
def renamed(request):
    return request.param

# ############################################################333
# expression
# ############


# TODO D.R.Y. only difference are under-above-ligned
@fixture(scope='module')
def expression_data(samples, genes, groupby,

                    #########
                    na_thresh
                    #########

                    ):
    df = pd.DataFrame(index=samples, columns=genes)

    def dataframe_maker(df):
        data = np.vstack([
            np.random.lognormal(np.random.uniform(0, 5),
                                np.random.uniform(0, 2),
                                df.shape[0]) for _ in df.columns]).T
        return pd.DataFrame(data, index=df.index, columns=df.columns)

    df = pd.concat([dataframe_maker(d) for name, d in
                    df.groupby(groupby)], axis=0).sort_index()

    ###########################
    if na_thresh > 0:
        df = df.apply(lambda x: x.map(
            lambda i: i
            if np.random.uniform() > np.random.uniform(0, na_thresh)
            else np.nan), axis=1)
    ############################

    return df


@fixture(scope='module')
def expression_data_no_na(samples, genes, groupby):
    df = pd.DataFrame(index=samples, columns=genes)

    def dataframe_maker(df):
        data = np.vstack([
            np.random.lognormal(np.random.uniform(0, 5),
                                np.random.uniform(0, 2),
                                df.shape[0]) for _ in df.columns]).T
        return pd.DataFrame(data, index=df.index, columns=df.columns)

    df = pd.concat([dataframe_maker(d) for name, d in
                    df.groupby(groupby)], axis=0).sort_index()
    return df


@fixture(scope='module')
def expression_feature_data(genes, gene_categories,
                            boolean_gene_categories, renamed):
    df = pd.DataFrame(index=genes)
    if renamed:
        df['renamed'] = df.index.map(lambda x: x.replace(u'gene', u'renamed'))
    df['gene_category'] = df.index.map(lambda x:
                                       np.random.choice(gene_categories))
    for category in boolean_gene_categories:
        p = np.random.uniform()
        df[category] = np.random.choice([True, False], size=df.shape[0],
                                        p=[p, 1 - p])
    return df


@fixture(scope='module')
def expression_feature_rename_col(renamed):
    if renamed:
        return 'renamed'
    else:
        return None


@fixture(scope='module')
def expression_log_base():
    return 2


@fixture(scope='module')
def expression_plus_one():
    return True


@fixture(scope='module')
def expression_thresh(request):
    return 2


@fixture(scope='module')
def expression_kws(expression_feature_data, expression_feature_rename_col,
                   expression_log_base,
                   expression_plus_one,
                   expression_thresh):
    kws = {}
    kws['feature_data'] = expression_feature_data
    kws['feature_rename_col'] = expression_feature_rename_col
    kws['log_base'] = expression_log_base
    kws['plus_one'] = expression_plus_one
    kws['thresh'] = expression_thresh
    return kws


@fixture(scope='module')
def true_modalities(events, modality_models, groups):
    data = {evt: {grp: (np.random.choice(list(modality_models.keys())))
                  for grp in groups
                  }
            for evt in events
            }
    return pd.DataFrame(data)


@fixture(scope='module')
def splicing_data(samples, events, true_modalities, modality_models, groupby):
    df = pd.DataFrame(index=samples, columns=events)

    def dataframe_maker(group, true_modalities, modality_models, df):
        data = np.vstack([modality_models[modality].rvs(df.shape[0])
                          for modality in true_modalities.ix[group]]).T
        return pd.DataFrame(data, index=df.index, columns=df.columns)

    df = pd.concat([dataframe_maker(group, true_modalities, modality_models,
                                    d)
                    for group, d in df.groupby(groupby)], axis=0)
    # randomly add NA since all splicing data has NAs
    na_thresh = 0.2
    df = df.apply(lambda x: x.map(
        lambda i: i if np.random.uniform() > np.random.uniform(0, na_thresh)
        else np.nan), axis=1)

    def randomly_add_na(x, na_thresh):
        if np.random.uniform() > np.random.uniform(0, na_thresh / 10):
            return x
        else:
            return pd.Series(np.nan, index=x.index)

    df = pd.concat([d.apply(randomly_add_na, na_thresh=na_thresh,
                            axis=1)
                    for group, d in
                    df.groupby(groupby)], axis=0)
    return df.sort_index()


@fixture(scope='module')
def splicing_feature_data(
        events, genes, feature_rename_col,
        expression_feature_data,
        splicing_feature_common_id):
    df = pd.DataFrame(index=events)
    df[feature_rename_col] = df.index.map(lambda x: np.random.choice(genes))
    df = df.join(expression_feature_data, on=splicing_feature_common_id)
    return df


@fixture(scope='module')
def splicing_feature_common_id(feature_rename_col):
    return feature_rename_col


@fixture(scope='module')
def splicing_kws(splicing_feature_data, splicing_feature_common_id,
                 feature_rename_col):
    return {'feature_data': splicing_feature_data,
            'feature_rename_col': feature_rename_col,
            'feature_expression_id_col': splicing_feature_common_id}


@fixture(scope='module')
def genelist_path(data_dir):
    return '{}/example_gene_list.txt'.format(data_dir)


@fixture(scope='module')
def genelist_dropbox_link():
    return 'https://www.dropbox.com/s/652y6hb8zonxe4c/example_gene_list.txt' \
           '?dl=0'


@fixture(params=['local', 'dropbox'])
def genelist_link(request, genelist_path, genelist_dropbox_link):
    if request.param == 'local':
        return genelist_path
    elif request.param == 'dropbox':
        return genelist_dropbox_link


@fixture(scope='module')
def x_norm():
    """Normally distributed numpy array"""
    n_samples = 20
    n_features = 50
    x = np.random.randn(n_samples * n_features)
    x = x.reshape(n_samples, n_features)
    return x


@fixture(scope='module')
def df_norm(x_norm):
    """Normally distributed pandas dataframe"""
    nrow, ncol = x_norm.shape
    index = ['sample_{0:02d}'.format(i) for i in range(nrow)]
    columns = ['feature_{0:04d}'.format(i) for i in range(ncol)]
    df = pd.DataFrame(x_norm, index=index, columns=columns)
    return df


@fixture(scope='module')
def df_nonneg(df_norm):
    """Non-negative data for testing NMF"""
    return df_norm.abs()


@fixture(scope='module', params=[0, 5])
def metadata_minimum_samples(request):
    return request.param


@fixture(params=[True, False])
def featurewise(request):
    return request.param


@fixture(scope='module')
def base_data(expression_data):
    from flotilla.data_model.base import BaseData

    return BaseData(expression_data)


@fixture(params=[None, 'half', 'all'], scope='module')
def sample_ids(request, base_data):
    if request.param is None:
        return request.param
    elif request.param == 'some':
        half = base_data.data.shape[0] / 2
        return base_data.data.index[:half]
    elif request.param == 'all':
        return base_data.data.index


@fixture(params=[None, 'half', 'all'], scope='module')
def feature_ids(request, base_data):
    if request.param is None:
        return request.param
    elif request.param == 'some':
        half = base_data.data.shape[1] / 2
        return base_data.data.columns[:half]
    elif request.param == 'all':
        return base_data.data.columns


@fixture(params=[True, False], scope='module')
def standardize(request):
    return request.param


@fixture(
    params=['subset1', None, 'phenotype: group1', '~subset1', 'ids'],
    scope='module')
def sample_subset(request, samples):
    if request.param == 'ids':
        return samples[:10]
    else:
        return request.param


@fixture(
    params=[None, 'all', 'gene_category: A', 'W', mark.xfail('asdf')],
    ids=['none', 'all_features', 'categorical_gene_category',
         'boolean_gene_category', 'nonexistent_gene_category'],
    scope='module')
def feature_subset(request):
    return request.param


@fixture(scope='module')
def splicing(splicing_data):
    from flotilla.data_model.splicing import SplicingData
    return SplicingData(splicing_data)


@fixture(scope='module')
def gene_ontology_data_path(data_dir):
    return '{}/human_grch38_chr22_gene_ontology.txt'.format(data_dir)


@fixture(scope='module')
def gene_ontology_data(gene_ontology_data_path):
    return pd.read_table(gene_ontology_data_path)
