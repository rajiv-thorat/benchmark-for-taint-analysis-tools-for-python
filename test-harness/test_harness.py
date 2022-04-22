import snyk_harness
import logging
import utils


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)
logging.info("Starting the benchmark.")
logging.debug(f"The realworld projects are at {utils.DIRECTORY_PATH_FOR_REALWORLD_PROJECTS}")
# The synthetic tests directory may contain subdirectories.
# The subdirectories will contain roots for individual projects (tests)

logging.debug(f"The synthetic tests are are at {utils.DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA}")
logging.debug(f"All the tests are at {utils.DIRECTORY_PATH_FOR_TESTS}")

logging.info("Running Snyk Code on the benchmark.")
# snyk_harness.run_benchmark_on_snyk(DIRECTORY_PATH_FOR_REALWORLD_PROJECTS, DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA, DIRECTORY_PATH_FOR_TESTS)
logging.info("Finished running the benchmark using Snyk code.")

snyk_harness.read_results_and_compare()
logging.info("Finished reading snyk results ")
