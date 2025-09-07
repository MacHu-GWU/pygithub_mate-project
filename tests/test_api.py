# -*- coding: utf-8 -*-

from pygithub_mate import api


def test():
    _ = api


if __name__ == "__main__":
    from pygithub_mate.tests import run_cov_test

    run_cov_test(
        __file__,
        "pygithub_mate.api",
        preview=False,
    )
