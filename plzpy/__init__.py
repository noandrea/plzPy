import pkg_resources
import logging


# initialize logging
logging.basicConfig(level=logging.ERROR)


def _version():
    try:
        return pkg_resources.get_distribution('plz').version
    except pkg_resources.DistributionNotFound:
        return 'snapshot'
