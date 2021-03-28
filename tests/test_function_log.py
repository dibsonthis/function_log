import pandas as pd
import pytest

from function_log import log_this


# helper functions to test the decorator's behavior with its new arguments.
@log_this(False)
def fakefunction_argflagfalse(df):
    return df


@log_this
def fakefunction_argflagtrue(df):
    return df


@log_this(True)
def fakefunction_argflagtrueexplicit(df):
    return df


# %%

def test_log_this_dataframe_arg_with_logfuncargumentsisfalse_passes():
    df = pd.DataFrame([1, 2, 3])
    fakefunction_argflagfalse(df=df)


def test_log_this_dataframe_arg_with_logfuncargumentsistrue_raisestypeerror():
    df = pd.DataFrame([1, 2, 3])
    with pytest.raises(TypeError):
        fakefunction_argflagtrue(df=df)


def test_log_this_dataframe_arg_with_logfuncargumentsistrueexplicit_raisestypeerror():
    df = pd.DataFrame([1, 2, 3])
    with pytest.raises(TypeError):
        fakefunction_argflagtrueexplicit(df=df)

# %%
