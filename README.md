# sumbook

Small command-line tool that totals a file of amounts (one per line, `#` comments).

    python3 -m sumbook.cli amounts.txt

Health: `python3 -m unittest discover -s tests` must pass. CI's last log is in `logs/ci-last.txt`.

Layout: `sumbook/` the package, `tests/` its tests, `deploy/` production configuration
(owned by operations), `logs/` copies of CI and scanner output.
