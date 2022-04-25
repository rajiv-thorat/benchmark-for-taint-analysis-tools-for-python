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

force_snyk_execution = False
logging.info("Running Snyk Code on the benchmark.")
logging.info(f"Force execution set to {force_snyk_execution}")
snyk_harness.run_snyk_on_benchmark(utils.DIRECTORY_PATH_FOR_REALWORLD_PROJECTS, force_snyk_execution)
logging.info("Finished running Snyk Code on the real world tests.")
snyk_harness.run_snyk_on_benchmark(utils.DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA, force_snyk_execution)
logging.info("Finished running Snyk Code on the synthetic tests.")

snyk_harness.read_results_and_compare()
logging.info("Finished reading snyk results ")
