# Testing Report

## Objectives
- Verify correct area and perimeter calculations for the circle and square helpers.
- Keep automated checks ready for future CI runs.

## Product Overview
- Library `geometric_lib` with `area` and `perimeter` functions in `circle.py` and `square.py`.

## Test Scope
- Circle area and perimeter with integer and fractional radii.
- Square area and perimeter with integer and fractional side lengths.

## Test Strategy
- Functional unit tests with `unittest`; value checks via `assertEqual` / `assertAlmostEqual`.

## Acceptance Criteria
- All tests pass with `python3 -m unittest` without errors.
- Results match the reference formulas in `docs/README.md`.

## Expected Outcomes
- Test run reports with statuses.
- Presence of the test file `test_geometry.py` in the public repository (e.g., GitHub).

## Current Test Results
- Command `python3 -m unittest` executed: 5 tests passed (covering circle.area/perimeter and square.area/perimeter).
