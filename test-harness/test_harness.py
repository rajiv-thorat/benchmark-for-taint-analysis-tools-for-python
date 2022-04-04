from posixpath import abspath
import snyk_harness

DIRECTORY_PATH_FOR_REALWORLD_PROJECTS = abspath("../tests/real-world-projects/")
# The synthetic tests directory may contain subdirectories.
# The subdirectories will contain roots for individual projects (tests)
DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA = abspath(
    "../tests/synthetic-taint-data/src/compound-statements/")

snyk_harness.run_benchmark_on_snyk(DIRECTORY_PATH_FOR_REALWORLD_PROJECTS, DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA)


