from subprocess import Popen, PIPE


def test_app_requirements_safety():
    with Popen(
        ["safety", "check", "-r", "requirements/development.txt"],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
    ) as p:
        output, _ = p.communicate()
        rc_development = (
            p.returncode
        )  # If 0 has no vulnerable packages, if 255, it has.

        assert rc_development != 255, f"\n==== Development:\n{output.decode()}"
