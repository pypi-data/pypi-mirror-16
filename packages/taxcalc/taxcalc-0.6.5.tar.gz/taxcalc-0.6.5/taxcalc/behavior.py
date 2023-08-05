"""
Tax-Calculator elasticity-based behavioral-response Behavior class.
"""
# CODING-STYLE CHECKS:
# pep8 --ignore=E402 behavior.py
# pylint --disable=locally-disabled --extension-pkg-whitelist=numpy behavior.py
# (when importing numpy, add "--extension-pkg-whitelist=numpy" pylint option)

import copy
import numpy as np
from .policy import Policy
from .parameters import ParametersBase


class Behavior(ParametersBase):
    """
    Constructor for elasticity-based behavioral-response class.

    Parameters
    ----------
    behavior_dict: dictionary of PARAM:DESCRIPTION pairs
        dictionary of behavioral-response elasticities; if None, default
        elasticities are read from the behavior.json file.

    start_year: integer
        first calendar year for behavioral-response elasticities.

    num_years: integer
        number of calendar years for which to specify elasticity
        values beginning with start_year.

    Raises
    ------
    ValueError:
        if behavior_dict is neither None nor a dictionary.
        if num_years is less than one.

    Returns
    -------
    class instance: Behavior
    """

    JSON_START_YEAR = Policy.JSON_START_YEAR
    DEFAULTS_FILENAME = 'behavior.json'
    DEFAULT_NUM_YEARS = Policy.DEFAULT_NUM_YEARS

    def __init__(self, behavior_dict=None,
                 start_year=JSON_START_YEAR,
                 num_years=DEFAULT_NUM_YEARS):
        super(Behavior, self).__init__()
        if behavior_dict is None:
            self._vals = self._params_dict_from_json_file()
        elif isinstance(behavior_dict, dict):
            self._vals = behavior_dict
        else:
            raise ValueError('behavior_dict is not None or a dictionary')
        if num_years < 1:
            raise ValueError('num_years < 1 in Behavior ctor')
        self.initialize(start_year, num_years)
        self._validate_elasticity_values()

    def update_behavior(self, revisions):
        """
        Update behavior for given revisions, a dictionary consisting
        of one or more year:modification dictionaries.
        For example: {2014: {'_BE_sub': [0.4, 0.3]}}
        Also checks for valid elasticity values in revisions dictionary.
        NOTE: this method uses the specified revisions to update the
              DEFAULT elasticity values, so use this method just once
              rather than calling it sequentially in an attempt to update
              elasticities in several steps.
        """
        precall_current_year = self.current_year
        self.set_default_vals()
        revision_years = sorted(list(revisions.keys()))
        for year in revision_years:
            self.set_year(year)
            self._update({year: revisions[year]})
        self.set_year(precall_current_year)
        self._validate_elasticity_values()

    def has_response(self):
        """
        Returns true if any behavioral-response elasticity is non-zero for
        the current_year; returns false if all elasticities are zero.
        """
        # pylint: disable=no-member
        if self.BE_sub != 0.0 or self.BE_inc != 0.0 or self.BE_cg != 0.0:
            return True
        else:
            return False

    @staticmethod
    def response(calc_x, calc_y):
        """
        Modify calc_y records to account for behavioral responses that arise
          from the policy reform that involves moving from calc_x.policy to
          calc_y.policy.
        Returns new Calculator object --- a deepcopy of calc_y --- that
          incorporates behavioral responses to the reform.
        Note: the use here of a dollar-change income elasticity (rather than
          a proportional-change elasticity) is consistent with Feldstein and
          Feenberg, "The Taxation of Two Earner Families", NBER Working Paper
          No. 5155 (June 1995).  A proportional-change elasticity was used by
          Gruber and Saez, "The elasticity of taxable income: evidence and
          implications", Journal of Public Economics 84:1-32 (2002) [see
          equation 2 on page 10].
        """
        # pylint: disable=too-many-locals
        assert calc_x.records.dim == calc_y.records.dim
        # Calculate marginal tax rates and the corresponding
        # proportional changes (pch) in marginal net-of-tax rates
        if calc_y.behavior.BE_sub != 0.0:
            # e00200p is taxpayer's wages+salary
            wage_mtr_x, wage_mtr_y = Behavior._mtr_xy(calc_x, calc_y,
                                                      mtr_of='e00200p',
                                                      tax_type='combined')
            wage_pch = ((1. - wage_mtr_y) / (1. - wage_mtr_x)) - 1.
        if calc_y.behavior.BE_cg != 0.0:
            # p23250 is filing unit's long-term capital gains
            ltcg_mtr_x, ltcg_mtr_y = Behavior._mtr_xy(calc_x, calc_y,
                                                      mtr_of='p23250',
                                                      tax_type='iitax')
            ltcg_pch = ((1. - ltcg_mtr_y) / (1. - ltcg_mtr_x)) - 1.
        # Calculate dollar change (dch) in after-tax income, ati
        if calc_y.behavior.BE_inc != 0.0:
            # _combined is filing unit's income+payroll tax liability
            # pylint: disable=protected-access
            ati_dch = calc_x.records._combined - calc_y.records._combined
        # Calculate magnitude of substitution and income effects and their sum
        #   c04800 is filing unit's taxable income
        if calc_y.behavior.BE_sub == 0.0:
            sub = np.zeros(calc_x.records.dim)
        else:
            sub = calc_y.behavior.BE_sub * wage_pch * calc_x.records.c04800
        if calc_y.behavior.BE_inc == 0.0:
            inc = np.zeros(calc_x.records.dim)
        else:
            inc = calc_y.behavior.BE_inc * ati_dch
        taxinc_chg = sub + inc
        # Calculate magnitude of behavioral response in long-term capital gains
        if calc_y.behavior.BE_cg == 0.0:
            ltcg_chg = np.zeros(calc_x.records.dim)
        else:
            ltcg_chg = calc_y.behavior.BE_cg * ltcg_pch * calc_x.records.p23250
        # Add behavioral-response changes to income sources
        calc_y_behv = copy.deepcopy(calc_y)
        calc_y_behv = Behavior._update_ordinary_income(taxinc_chg, calc_y_behv)
        calc_y_behv = Behavior._update_cap_gain_income(ltcg_chg, calc_y_behv)
        # Recalculate post-reform taxes incorporating behavioral responses
        calc_y_behv.calc_all()
        return calc_y_behv

    # ----- begin private methods of Behavior class -----

    def _validate_elasticity_values(self):
        """
        Check that behavioral-response elasticities have valid values.
        """
        msg = '{} elasticity cannot be {} in year {}; value is {}'
        pos = 'positive'
        neg = 'negative'
        for elast in self._vals:
            values = getattr(self, elast)
            for year in values:
                val = values[year]
                if elast == '_BE_inc':
                    if val > 0.0:
                        raise ValueError(msg.format(elast, pos, year, val))
                elif elast == '_BE_sub':
                    if val < 0.0:
                        raise ValueError(msg.format(elast, neg, year, val))
                elif elast == '_BE_cg':
                    if val < 0.0:
                        raise ValueError(msg.format(elast, neg, year, val))
                else:
                    raise ValueError('illegal elasticity {}'.format(elast))

    @staticmethod
    def _update_ordinary_income(taxinc_change, calc):
        """
        Implement total taxable income change induced by behavioral response.
        """
        # assume no behv response for filing units with no, or negative, AGI
        agi = calc.records.c00100
        delta_income = np.where(agi > 0., taxinc_change, 0.)
        # compute AGI minus itemized deductions, agi_m_ided
        # pylint: disable=protected-access
        ided = np.where(calc.records.c04470 < calc.records._standard,
                        0.,
                        calc.records.c04470)
        agi_m_ided = agi - ided
        # allocate delta_income into three parts
        delta_wage = np.where(agi_m_ided > 0.,
                              delta_income * calc.records.e00200 / agi_m_ided,
                              0.)
        other_income = agi - calc.records.e00200
        delta_oinc = np.where(agi_m_ided > 0.,
                              delta_income * other_income / agi_m_ided,
                              0.)
        delta_ided = np.where(agi_m_ided > 0.,
                              delta_income * ided / agi_m_ided,
                              0.)
        # confirm that the three parts add up to delta_income
        assert np.allclose(delta_income, delta_wage + delta_oinc + delta_ided)
        # add the three parts to different calc.records variables
        calc.records.e00200 = calc.records.e00200 + delta_wage
        calc.records.e00200p = calc.records.e00200p + delta_wage
        calc.records.e00300 = calc.records.e00300 + delta_oinc
        calc.records.e19200 = calc.records.e19200 + delta_ided
        return calc

    @staticmethod
    def _update_cap_gain_income(cap_gain_change, calc):
        """
        Implement capital gain change induced by behavioral responses.
        """
        calc.records.p23250 = calc.records.p23250 + cap_gain_change
        return calc

    @staticmethod
    def _mtr_xy(calc_x, calc_y, mtr_of='e00200p', tax_type='combined'):
        """
        Computes marginal tax rates for Calculator objects calc_x and calc_y
        for specified mtr_of income type and specified tax_type.
        """
        _, iitax_x, combined_x = calc_x.mtr(mtr_of)
        _, iitax_y, combined_y = calc_y.mtr(mtr_of)
        if tax_type == 'combined':
            return (combined_x, combined_y)
        elif tax_type == 'iitax':
            return (iitax_x, iitax_y)
        else:
            raise ValueError('tax_type must be "combined" or "iitax"')

# end Behavior class
